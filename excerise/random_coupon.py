name = 'this is a test'

def what_happen():
    print(name)
    name = name + '!!!'
    print(name)
    global name

what_happen()

