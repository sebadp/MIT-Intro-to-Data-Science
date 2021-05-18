# def check_letter(guess, word, test_temp, errors):
#     if guess in word:
#         for i in word:
#             if i == guess:
#                 test_temp[word.index(i)] = guess
#     else:
#         errors += 1
#     return ()

def run():
    """
    Input Format
    Primero se recibe la palabra que se debe adivinar (en mayúsculas).
    Luego se recibe un número, la cantidad máxima de intentos errados.
    Por último se recibe cierta cantidad de letras en mayúsculas, una por línea, sin repetir.
    Constraints
    Output Format
    En caso de que se haya adivinado la palabra antes de superar el límite 
    , se imprime la cantidad de intentos que tardó en adivinar.
    En caso de que se haya superado el límite , se imprime el número
    Sample Input 0
    PYTHON
    3
    A
    B
    C
    P
    Y
    T
    H
    O
    N
    Sample Output 0
    9
    Explanation 0
    Si bien el jugador tuvo tres intentos erróneos ('A','B' y 'C'), 
    adivinó la palabra antes de equivocarse la cuarta vez y es por 
    ello que se cuenta como partida ganada. A su vez, notar que el 
    programa imprime la cantidad de turnos que se tardaron en adivinar 
    la palabra.
    """
    word = input()
    max_tries = int(input())
    done = False
    counter = 0
    errors = 0 
    test_temp = [ '-' for i in range(len(word))]
    temp = list(word)
    while done != True:
        guess = input()
        if len(guess)>1 or guess=="":
            print ('Tienes que adivinar una letra por vez.')
            pass
        counter += 1
        # check_letter(guess, word, test_temp, errors)
        if guess in word:
            # for i in word:
            #     print(i, "es i")
            #     if i == guess:
            #         test_temp.replace()
                    # for j in range(word.index(i)+1, len(word)):
                    #     print (j)
             word = word.replace(guess, "")      
        else:
            errors += 1
        if temp == test_temp:
            done = True
        if max_tries == errors:
            return print(counter)

        print(counter, word)
        print(guess)
        print(test_temp)
        print(word)

    return print(counter)

if __name__ == '__main__':
    run()
