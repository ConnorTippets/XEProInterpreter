import argparse as ap
import time

# Define arguments
parser = ap.ArgumentParser(description='An interpreter for XEPro')
parser.add_argument('-v', action='store_true')
parser.add_argument('-nc', action='store_true')
parser.add_argument('file', type=ap.FileType('r'))
args = parser.parse_args()

# Define command tokens
vie = '%' # vie = variable in echo
mws = '"' # mws = multi word string

# misc
version = '1.2.8'
code = ""

# read arguments
if args.v:
    print(f'[XEPro {version}] Initializing Interpreter...')

content = args.file.read()

# Interpreter Class
class XEPro_Interpreter:
    def __init__(self):
        if args.v:
            print(f'[XEPro {version}] Verbose Mode Enabled!')
    # function to make sense of and run the instructions given.
    def run(self, content):
        # read file
        if args.v:
            print(f'[XEPro {version}] Contents of file: \n{content}')
        content = content.split()
        if args.v:
            print(f'[XEPro {version}] Readable Data: {content}')
        # code to understand the stuff
        for x in range(len(content)):
            t = []
            #if content[x].startswith('.DefVar'):
            #    if args.v:
            #        print(f'[XEPro {version}] DefVar command found!')
            #    varName = content[x+2]
            #    varContents = content[x+1]
            #    varName.replace("'", "")
            #    with open('metadata.py', 'w') as f:
            #        f.write("# Generated by the XEPro Interpreter. \n# Do not touch! This is metadata to know what the variables are!\n\nvar = {}\nvarName = '{}'".format(varContents,varName))
                
            if content[x].startswith('.Echo'):
                import os
                x = content[x+1].replace('"', '')
                y = content[x+2].replace('"', '')
                if content[x+1].startswith(vie):
                    if content[x+2].endswith(vie):
                        print('{} {}'.format(x, y))
                else:
                    print('{}'.format(x))
                        #if os.path.exists('./metadata.py'):
                        #    if args.v:
                        #        print(f'[XEPro {version}] Metadata file found!')
                        #    import metadata
                        #    if metadata.varName in content[x+1]:
                        #        print(str(metadata.var))
                        #else:
                        #    if args.v:
                        #        print(f'[XEPro {version}] Metadata file does not exist! Won\'t be able to use variables unless one is generated!')
                
            if content[x].startswith('.NewLine'):
                print('\n')
            if content[x].startswith('.ReadFile'):
                if args.v:
                    print(f'[XEPro {version}] Found read file command, reading from {content[x+1]}')
                try:
                    with open(content[x+1], 'r') as f:
                        print(f.read())
                except FileNotFoundError:
                    if args.v:
                        print(f'[XEPro {version}] File not found')
            if content[x].startswith('.WriteFile'):
                with open(str(content[x+1]), 'w') as w:
                    if args.v:
                        print(f'[XEPro {version}] Found write file command, writing to {content[x+1]}')
                    w.write(content[x+2])
                    w.close()
            if content[x].startswith('.AppendFile'):
                with open(str(content[x+1]), 'a') as a:
                    if args.v:
                        print(f'[XEPro {version}] Found append file command, appending to {content[x+1]}')
                    a.write(content[x+2])
                    a.close()
            if content[x].startswith('.DeleteFile'):
                import os
                os.remove(f'./{content[x+1]}')
                if args.v:
                    print(f'[XEPro {version}] Found delete file command, deleting {content[x+1]}')
            if content[x].startswith('Wait'):
                print(f'*XEPro waited {content[x+1]}s here*')
                time.sleep(int(content[x+1]))
                if args.v:
                    print(f'[XEPro {version}] Found wait command, waiting {content[x+1]}s')
            if content[x].startswith('.listDir'):
                path = content[x+1]
                path = path.replace('\\', '/')
                import os
                print(str(os.listdir(str(path))))
                if args.v:
                    print(f'[XEPro {version}] Found list dir command, listing {path}')
            if content[x].startswith('.OpenProgram'):
                import os
                program = content[x+1]
                if args.v:
                    print(f'[XEPro {version}] Found open program command, opening {program}')
                    print(f'[XEPro {version}] Please close that window for program execution to continue')
                os.system(program)
            if content[x].startswith('.Math'):
                num1 = content[x+1]
                num2 = content[x+3]
                sym = content[x+2]
                if args.v:
                    print(f'[XEPro {version}] Found math command, calculating {num1} {sym} {num2}')
                print(str(eval(f'{num1} {sym} {num2}')))
            if content[x].startswith('.CreateFile'):
                fileName = str(content[x+1])
                try:
                    f = open(fileName, 'x')
                    f.close()
                    print(f'Created file named {fileName}')
                except FileExistsError:
                    print(f'Cannot create {fileName} because it already exists')
                    
            if content[x].startswith('.Mod'):
                num1 = int(content[x+1])
                num2 = int(content[x+2])
                print(num1 % num2)
            if content[x].startswith('.Power'):
                num1 = int(content[x+1])
                num2 = int(content[x+1])
                print(num1 ** num2)

    if not args.nc:
        print('Completed running code!')
interpreter = XEPro_Interpreter()
interpreter.run(content)
