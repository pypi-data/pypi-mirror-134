import ctypes
import inspect
import threading


class Thread:
    def __init__(self, run, args=()):
        self.factory = threading.Thread(target=run, args=args, daemon=True)

    def is_alive(self):
        return self.factory.is_alive()

    def start(self):
        self.factory.start()

    def stop(self):
        while self.is_alive():
            tid = ctypes.c_long(self.factory.ident)
            exctype = SystemExit
            if not inspect.isclass(exctype):
                exctype = type(exctype)
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
            if res == 0:
                break
            elif res != 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
                break
