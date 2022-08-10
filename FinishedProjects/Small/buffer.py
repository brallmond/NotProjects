import time as time
def word_buffer(array_of_words):
    arrayLen = len(array_of_words)
    loop = 0
    while loop < 10:

        if loop%2 == 0:
          array_of_words[arrayLen-1] = "new word"
        else:
          array_of_words[arrayLen-1] = "newer WORD"

        for i in range(arrayLen):
            print(array_of_words[i])

        time.sleep(0.5)
        # \x1b is an escape code, [nA goes up n lines, [J clears to the bottom
        bufferControl = '\x1b'+'['+str(arrayLen)+'A'+'\x1b[J'
        print(bufferControl, end="") # end="" prevents \n (newline character) from being written
        loop += 1

if __name__ == "__main__":
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('--phrase', '-p', required=True, action='store', help='Say something and I\'ll say it back!')
        args = parser.parse_args()
        phrase = args.phrase
        phrase = phrase.strip()
        word_buffer(phrase.split(' '))
        print(phrase.split(' '))
