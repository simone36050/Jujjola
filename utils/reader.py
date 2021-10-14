
def read(filename: str):
    with open(filename, 'r') as f:
        return f.read()

def readWith(filename: str, **kargs):
    f = read(filename)
    for key, val in kargs.items():
        f = f.replace('{' + '{}'.format(key) + '}', str(val))
    return f
