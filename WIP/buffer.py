import time as time
def word_buffer():
    words = 5*[' ']
    one = 'one'
    two = 'two'
    three = 'three'
    words[0] = one
    g = 0
    while g < 10:
        print('=====================')
        if g%2 == 0:
            words[3] = two
        else:
            words[3] = three
        for i in range(len(words)):
            print(words[i])
        time.sleep(0.5)
        print('\x1b[7A\x1b[J')
        g += 1

if __name__ == "__main__":
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('--phrase', '-p', required=True, action='store', help='Say something and I\'ll say it back!')
        word_buffer()
