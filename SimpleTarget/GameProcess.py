import subprocess

class ProcessMethod:

    def __init__(self, file):
        self.proc = subprocess.Popen(file , stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf8')

    def __del__(self):
        self.proc.terminate()

    def __call__(self, inp:str):
        self.proc.stdin.write(inp)
        self.proc.stdin.flush()
    
        line = self.proc.stdout.readline()   #Single line
        self.proc.stdin.flush()

        return line
    