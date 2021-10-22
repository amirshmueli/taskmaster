from io import TextIOWrapper
from typing import TextIO
import psutil


class taskmaster:
    def __init__(self):
        self.p = {}
        self.files = {}

    def GetProccess(self):
        for p in psutil.process_iter():
            __pid = p.pid
            __name = p.name()
            __args = 'None'
            
            
            self.p[__pid] = p

    def GetFiles(self):
        for proc in self.p.items():
            try:
                for handlers in proc[1].open_files():
                    key = list(handlers)[0]
                    self.files[key] = proc[1].name()
            except psutil.AccessDenied or PermissionError:
                print('.', end=' ')
            
                
    
    def IterProcs(self, toprint=False, args=False):
        for proc in self.p.items():
            proc : psutil.Process = proc[1]

            name = proc.name()
            id = proc.pid

            if toprint:
                print(f'{id} | {name}\n')
                if args:
                    try:
                        __args = ' '.join(proc.cmdline())
                    except:
                        continue
                    print(f'\t{__args}\n')
                    print('====================\n')
        
    def IterFiles(self, toprint=False):
        for path in self.files:
            print(path)
                

t = taskmaster()
t.GetProccess()
t.IterProcs(toprint=True)
t.GetFiles()
t.IterFiles(toprint=True)
