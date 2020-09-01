import fire
def add(a, b):
    return a + b

# if __name__ == '__main__':
#     fire.Fire()

# Running Command : - python fireTest.py add 10 22

# Fire : Exposing Multiple commands

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Varsion 1

# if __name__ == '__main__':
#     fire.Fire()

# Version 2
# if __name__ == '__main__':
#     fire.Fire({
#         'add': add, 'multiply' : multiply
#     })

# Version 3 worked on object

class calculator(object):
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    obj = calculator()
    fire.Fire(obj)

