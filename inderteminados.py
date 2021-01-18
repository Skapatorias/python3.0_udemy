

def infinito(*args):
    for args in args:
        print(args)

infinito("lalal", "juan", 22, {"sol":"minoli"})

def infi(**kwargs):
    for kwarg in kwargs:
        print (kwarg, "---->", kwargs[kwarg])

infi(a="hola", b=20, c=['Maria', 'Jose', 'Pedro'])