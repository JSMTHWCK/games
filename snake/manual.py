def manual():
    a = input()
    while a not in ['w','a','s','d']:
        print('a not in ["w","a","s","d"]')
        a = input()
    return a