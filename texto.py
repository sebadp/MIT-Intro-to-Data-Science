def run():
    result = []
    allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    not_allowed = []
    with open('textos.txt') as txt:
        lines = txt.readlines()
        for line in lines:
            words = line.split(' ')
            for word in words:
                for char in word:
                    if char not in allowed_chars:
                        not_allowed.append(char)
                for i in not_allowed:
                    word.replace(i, '')
            result.append(word)


    return print(result)

if __name__ == '__main__':
    run()