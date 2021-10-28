import psutil
import time


class taskmaster:
    def __init__(self):
        self.p = {}
        self.files = {}
        self.filetype = {}

    def GetProccess(self, toprint=False, args=False):
        if args:
            toprint = args

        for proc in psutil.process_iter():
            self.p[proc.pid] = proc
            name = proc.name()
            id = proc.pid

            if toprint:
                print('.' * 45)
                print(f'{str(id).ljust(5)} | {name}\n')
                if args:
                    try:
                        __args = ' '.join(proc.cmdline())
                    except:
                        continue
                    print(f'\targs: {__args}\n')
        print('\n>>> Proccess Scanned Successfully')

    def GetFiles(self, toprint=False, printaccess=True):
        l = len(self.p)
        i = 0
        for proc in self.p.values():
            if not toprint:
                i += 1
                print(f'Loading Files: {str(i / l * 100)[:5]}% \r', end='')

            try:
                if toprint:
                    print(f'[{str(proc.pid).ljust(5)} | {proc.name()}]',
                          end=' ')
                of = proc.open_files()

                if len(of) == 0:
                    continue

                if toprint:
                    print(f'| {len(of)} ->')
                for handlers in of:
                    self.files[list(handlers)[0]] = proc.pid
                    if toprint:
                        print(f'\t{handlers[0]}\n')
            except Exception:
                if toprint and printaccess:
                    print(f': Could Not Access')

        print('\n>>> Files Scanned Successfully')

    def UpdateFileType(self):
        for filename in self.files:
            type_ = filename.split('/')[-1].split('.')[-1]
            self.filetype[type_] = self.filetype.get(type_, 1) + 1

    def Taskill(self, id_):
        self.files.get(id_).kill()


if __name__ == '__main__':
    t = taskmaster()
    t.GetProccess(args=False)
    t.GetFiles(toprint=True, printaccess=True)
    t.UpdateFileType()