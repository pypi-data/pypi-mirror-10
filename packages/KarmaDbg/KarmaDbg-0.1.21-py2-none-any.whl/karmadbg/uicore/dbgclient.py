
from PySide.QtCore import *

from karmadbg.dbgcore.dbgengine import DbgEngine, LocalDebugServer
from karmadbg.uicore.async import AsyncOperation, async
from karmadbg.uicore.basewidgets import AutoQMutex

import sys
import time

class DebugAsyncCall(QRunnable):

    def __init__(self, dbgclient, *args, **kwargs):
        super(DebugAsyncCall,self).__init__()
        self.dbgclient = dbgclient
        self.asyncmgr = dbgclient.asyncMgr
        self.args = args
        self.kwargs = kwargs


    def doTaskAsync(self,async):

        class AsyncSignals(QObject):
            asyncDone = Signal(object)

        def onAsyncDone(res):
            try:
                asyncOp = async.send(res[0])
                asyncOp.doTaskAsync(async)
            except StopIteration:
                pass

        self.signals = AsyncSignals()
        self.signals.asyncDone.connect(onAsyncDone)
        self.asyncmgr.start(self)

    def run(self):
        res = self.task(*self.args, **self.kwargs)
        self.signals.asyncDone.emit((res,))

        if self.dbgclient.currentThreadChange:
            self.dbgclient.currentThreadChange = False
            self.dbgclient.uimanager.targetThreadChanged.emit()

        if self.dbgclient.currentFrameChanged:
            self.dbgclient.currentFrameChanged = False
            self.dbgclient.uimanager.targetFrameChanged.emit()

    def task(self, *args, **kwargs):
        pass

class InputWaiterSync(QObject):

    def __init__(self):
        self.inputMutex = QMutex()
        self.inputCompleted = QWaitCondition()
        self.inputBuffer = ""
        self.inputMutex.lock()

    def inputComplete(self,str):
        self.inputMutex.lock()
        self.inputBuffer = str
        self.inputCompleted.wakeAll()
        self.inputMutex.unlock()
            
    def wait(self):
        self.inputCompleted.wait(self.inputMutex)
        self.inputMutex.unlock()
        return self.inputBuffer

class AsyncProfiler:

    def __init__(self, dbgClient, str):
        self.dbgClient = dbgClient
        self.dbgClient.debugOutput.emit(str)

    def __enter__(self):
        self.startTime = time.time()*1000

    def __exit__(self, type, value, traceback):
        self.dbgClient.debugOutput.emit( "complete. took time = %dms" % ( time.time()*1000 - self.startTime ) )


class DebugClient(QObject):

    inputCompleted = Signal(str)
    inputAutoCompleted = Signal(str)
    debugOutput = Signal(str)

    def __init__(self, uimanager, dbgsettings):

        super(DebugClient,self).__init__()
        self.uimanager = uimanager

        self.activePythonDbg = False

        self.dbgServer = LocalDebugServer()
        self.dbgEngine = DbgEngine(self, self.dbgServer, dbgsettings)

        self.serverControl = self.dbgServer.getServerControl()
        self.serverInterrupt = self.dbgServer.getServerInterrupt()

        self.asyncMgr = QThreadPool()
        self.asyncMgr.setMaxThreadCount(1)

        self.waitPool = QThreadPool()

        self.inputCompleted.connect(self.inputComplete)
        self.inputAutoCompleted.connect(self.inputAutoComplete)

        self.currentFrameChanged = False
        self.currentThreadChange = False
        

        self.inputWaiter = None
        self.inputBuffer = ""

        self._stepSourceMode = False

        sys.stdout = self
        sys.stdin = self

    @async 
    def start(self):

        class InitScriptAsync(DebugAsyncCall):

            def task(self):
               self.dbgclient.serverControl.startup()

        self.dbgEngine.start()
       
        yield( InitScriptAsync(self) )

        self.uimanager.outputRequired.emit(">>>")
        self.uimanager.inputRequired.emit()

    def stop(self):
        self.dbgEngine.stop()
        self.asyncMgr.waitForDone()

    def inputComplete(self,str):
        if self.inputWaiter:
            self.inputWaiter.inputComplete(str)
            return
        self.callCommand(str)

    def inputAutoComplete(self,str):
        self.callCommand(str, autoComplete = True)

    @async
    def callCommand(self,str, echo=True, autoComplete = False):

        class CallCommandAsync(DebugAsyncCall):

            def task(self,cmdstr):
                with AsyncProfiler(self.dbgclient, "call command \"%s\"" %str ) as profiler:
                    return self.dbgclient.serverControl.debugCommand(cmdstr)

        if echo:
            self.uimanager.outputRequired.emit(str + "\n")

        self.uimanager.inputCompleted.emit()

        if str == "":
            str = "\n"

        if self.inputBuffer == "":
            self.inputBuffer = str
        else:
            self.inputBuffer += "\n" + str

        result = yield( CallCommandAsync(self, self.inputBuffer) )
           
        if result.IsQuit:
           self.uimanager.quit()

        if result.IsNeedMoreData:
            self.uimanager.outputRequired.emit("...")
        else:
            self.inputBuffer = ""
            if self.activePythonDbg:
                self.uimanager.outputRequired.emit("PY>")
            else:
                self.uimanager.outputRequired.emit(">>>")

        self.uimanager.inputRequired.emit()

    def write(self,str):
        self.output(str)

    def readline(self):
        return self.input()

    def output(self,str):
        self.uimanager.outputRequired.emit(str)

    def input(self):
        self.inputWaiter = InputWaiterSync()
        self.uimanager.inputRequired.emit()
        str = self.inputWaiter.wait()
        self.uimanager.inputCompleted.emit()
        self.uimanager.outputRequired.emit(str + "\n")
        self.inputWaiter = None
        return str

    def onTargetStateChanged(self,state):
        if state.IsRunning:
            self.uimanager.targetRunning.emit()
        elif state.IsStopped:
            self.uimanager.targetStopped.emit()
        elif state.IsNoTarget:
            self.uimanager.targetDetached.emit()

    def onTargetChangeCurrentThread(self):
        self.currentThreadChange = True

    def onTargetChangeCurrentFrame(self, frame):
        self.currentFrameChanged = True

    def onTargetChangeBreakpoints(self):
        self.uimanager.targetBreakpointsChanged.emit()

    def openProcess(self, processName):
        cmd = "startProcess(r\"" +  processName + "\")"
        self.callCommand(cmd)

    def attachKernel(self, commandLine):
        cmd = "attachKernel(r\"" + commandLine + "\")"
        self.callCommand(cmd)

    def openDump(self,dumpName):
        cmd="loadDump(r\"" + dumpName + "\")"
        self.callCommand(cmd)

    def go(self):
        self.callCommand("g")

    def step(self):
        self.callCommand("p")

    def stepout(self):
        self.callCommand('gu')

    def trace(self):
        self.callCommand("t")

    def breakin(self):
        self.serverInterrupt.breakin()

    def getSourceLineAsync(self):

        class SourceLineAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get source line") as profiler:
                    return self.dbgclient.serverControl.getSourceLine()

        return SourceLineAsync(self)


    def getDisasmAsync(self, relpos, linecount):

        class DisasmAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get disasm relpos = %d linecount = %d" % (relpos, lienpos) ) as profiler:
                    return self.dbgclient.serverControl.getDisasm(relpos, linecount)

        return DisasmAsync(self)


    def getRegistersAsync(self):

        class RegisterAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get register") as profiler:
                    return self.dbgclient.serverControl.getRegsiters()
    
        return RegisterAsync(self)

    def getStackTraceAsync(self):

        class StackTraceAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get stack") as profiler:
                    return self.dbgclient.serverControl.getStackTrace()

        return StackTraceAsync(self)

    def getPythonSourceLineAsync(self):

        class PythonSourceLineAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get python source line") as profiler:
                    return self.dbgclient.serverControl.getPythonSourceLine()

        return PythonSourceLineAsync(self)

    def getPythonStackTraceAsync(self):

        class PythonStackTraceAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get python stack trace") as profiler:
                    return self.dbgclient.serverControl.getPythonStackTrace()

        return PythonStackTraceAsync(self)

    def getPythonBreakpointListAsync(self):

        class PythonBreakpointListAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get python breakpoints") as profiler:
                    return self.dbgclient.serverControl.getPythonBreakpointList()

        return PythonBreakpointListAsync(self)

    def getPythonLocalsAsync(self, localsName):

        class PythonLocalsAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get python locals") as profiler:
                    return self.dbgclient.serverControl.getPythonLocals(localsName)

        return PythonLocalsAsync(self)


    def setCurrentFrameAsync(self, frameno):

        class CurrentFrameAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "set current frame no = %d" % frameno) as profiler:
                    return self.dbgclient.serverControl.setCurrentFrame(frameno)

        return CurrentFrameAsync(self)


    @async
    def setCurrentFrame(self, frameno):
        ret = yield( self.setCurrentFrameAsync(frameno))
        assert( ret == None)


    def getCurrentFrameAsync(self):

        class CurrentFrameAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get current frame") as profiler:
                    return self.dbgclient.serverControl.getCurrentFrame()

        return CurrentFrameAsync(self)


    def getExpressionAsync(self, expr):

        class ExpressionAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get expression \"%s\"" % expr) as profiler:
                    return self.dbgclient.serverControl.getExpr(expr)

        return ExpressionAsync(self)

    def getMemoryAsync(self,addr,length):

        class MemoryAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "read memory addr=%x len=%d" % (addr,length)) as profiler:
                    return self.dbgclient.serverControl.getMemoryRange(addr,length)

        return MemoryAsync(self)

    def pythonEvalAsync(self, expr):

        class PythonEvalAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "python eval \"%s\"" % expr ) as profiler:
                    return self.dbgclient.serverControl.pythonEval(expr)

        return PythonEvalAsync(self)

    def getAutoCompleteAsync(self, startCompleteStr):

        class AutoCompleteAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "get auto complete for \"%s\"" % startCompleteStr ) as profiler:
                    return self.dbgclient.serverControl.getAutoComplete(startCompleteStr)

        return AutoCompleteAsync(self)

    @async
    def addBreakpoint(self,filename,lineno):

        class AddBreakpointAsync(DebugAsyncCall):
            def task(self):
                with AsyncProfiler(self.dbgclient, "add breakpoint filename=%s lineno=%d" % (filename,lineno) ) as profiler:
                    return self.dbgclient.serverControl.addBreakpoint(filename,lineno)

        yield (AddBreakpointAsync(self))

    @async
    def removeBreakpoint(self,filename,lineno):

        class RemoveBreakpointAsync(DebugAsyncCall):
            def task(self):
                with AsyncProfiler(self.dbgclient, "remove breakpoint filename=%s lineno=%d" % (filename,lineno) ) as profiler:
                    return self.dbgclient.serverControl.removeBreakpoint(filename,lineno)

        yield (RemoveBreakpointAsync(self))


    def callServerAsync(self, func, *args, **kwargs):

        class CallServerAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "call server async: %s" % str(func) ) as profiler:
                    return self.dbgclient.serverControl.callFunction( func, *args, **kwargs)
    
        return CallServerAsync(self)

    @async
    def callFunction(self, *args, **kwargs):
        ret = yield( self.callServerAsync(*args, **kwargs))
        assert( ret == None)

    def onPythonStart(self, scriptPath):
        self.activePythonDbg = True
        self.uimanager.pythonStarted.emit(scriptPath)
        return True

    def onPythonStateChanged(self, state):
        if state.IsRunning:
            self.uimanager.pythonRunning.emit()
        elif state.IsStopped:
            self.uimanager.pythonStopped.emit()

    def onPythonQuit(self):
        self.uimanager.pythonExit.emit()
        self.activePythonDbg = False
        
    def onPythonBreakpointAdd(self, filename, lineno):
        self.uimanager.pythonBreakpointAdded.emit(filename, lineno)

    def onPythonBreakpointRemove(self, filename, lineno):
        self.uimanager.pythonBreakpointRemoved.emit(filename, lineno)

    @property
    def stepSourceMode(self):
        return self._stepSourceMode

    @stepSourceMode.setter
    @async
    def stepSourceMode(self, val):
        self._stepSourceMode = val == True

        class setStepSourceModeAsync(DebugAsyncCall):

            def task(self):
                with AsyncProfiler(self.dbgclient, "set source step mode" ) as profiler:
                    self.dbgclient.serverControl.setStepSourceMode(val)

        yield( setStepSourceModeAsync(self) )


    def lockMutexAsync(self,mutex):

        class LockMutexAsync(QRunnable):

            def __init__(self, dbgclient, mutex):
                super(LockMutexAsync,self).__init__()
                self.dbgclient = dbgclient
                self.mutex = mutex

            def doTaskAsync(self, async, ):

                class AsyncSignals(QObject):
                    asyncDone = Signal()

                def onAsyncDone():
                    try:
                        asyncOp = async.next()
                        asyncOp.doTaskAsync(async)
                    except StopIteration:
                        pass

                self.signals = AsyncSignals()
                self.signals.asyncDone.connect(onAsyncDone)
                self.dbgclient.waitPool.start(self)

            def run(self):
                self.mutex.lock()
                self.signals.asyncDone.emit()

        return LockMutexAsync(self, mutex)



    def callFunctionAsync(self, fn, *args, **kwargs):


        class CallFunctionAsync(object):

            def doTaskAsync(self, async, ):
                res = fn(*args, **kwargs)
                try:
                    asyncOp = async.send(res)
                    asyncOp.doTaskAsync(async)
                except StopIteration:
                    pass
   
        return CallFunctionAsync()

 
