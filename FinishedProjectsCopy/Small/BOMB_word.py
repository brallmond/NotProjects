alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l', \
'm','n','o','p','q','r','s','t','u','v','w','x','y','z']  

words = [
"about", "after", "again", "below", "could", \
"every", "first", "found", "great", "house", \
"large", "learn", "never", "other", "place", \
"plant", "point", "right", "small", "sound", \
"spell", "still", "study", "their", "there", \
"these", "thing", "think", "three", "water", \
"where", "which", "world", "would", "write"
]

def letter_positions(word):
  return [alphabet.index(word[i]) for i in range(len(word))]

def most_used(ar):
  m = max(ar)
  return [i for i in range(len(ar)) if ar[i] == m]

if __name__ == "__main__":
  allen = len(alphabet)
  pos_ar = [[0 for col in range(allen)] for row in range(5)]
  for i in range(len(words)):
    word_temp = letter_positions(words[i])
    for j in range(len(word_temp)):
      pos_ar[j][word_temp[j]] += 1

  print("chr: [" + ', '.join(alphabet) + "]")
  print("1st: " + str(pos_ar[0]))
  print("2nd: " + str(pos_ar[1]))
  print("3rd: " + str(pos_ar[2]))
  print("4th: " + str(pos_ar[3]))
  print("5th: " + str(pos_ar[4]))
  for j in range(5):
    most_letters = [alphabet[i] for i in most_used(pos_ar[j])]
    print("most often character in position " + str(j) + " : "+ str(most_letters))
