from pathlib import Path

asm_path = []

p = Path('c:/users/')



def printdat(dat):
    i = 0
    for pat in dat.iterdir():
        #asm_path.append(pat)
        try:
            if pat.is_dir():
                i = i + printdat(pat)
            else:
                i = i + 1
                #print(pat)
        except PermissionError:
            print('kann nicht lesen')
    return i


print(printdat(p))
