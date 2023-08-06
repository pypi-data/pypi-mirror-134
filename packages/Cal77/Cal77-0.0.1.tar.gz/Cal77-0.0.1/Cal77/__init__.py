def calculate(*args):
    while True:
        try:
            i = input(*args)
            print(eval(i))
        except:
            print('invalid')
            exit()

