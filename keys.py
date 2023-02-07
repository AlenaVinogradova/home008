from random import randint

def key_gen():
    ki = True
    k = randint(100,1000)
    print(k)
    # return(k)
    with open('keys.txt', 'r') as file:
        for i in file:
            if str(k) in i:
                ki = False
                print('next')
                key_gen()
    if ki == True:
        with open('keys.txt', 'a') as file:
            file.write(f'{k}\n')
    return k
    
# key_gen()
# a = key_gen()
# print(a)
