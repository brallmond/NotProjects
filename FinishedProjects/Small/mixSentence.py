import random as rand

inPhrase = raw_input("gimme a phrase and I'll change the order of the words: ")

# 4 lines
splitPhrase = inPhrase.split()
phraseRange = range(len(inPhrase.split()))
rand.shuffle(phraseRange)
print (" ".join([splitPhrase[i] for i in phraseRange]))
