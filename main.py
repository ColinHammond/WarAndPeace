import string
#WordFile.txt
file1 = open("WarandPeacetext.txt", 'r', encoding='UTF8')
all_lines = file1.readlines()
word_count = {"the":0}
for line in all_lines:
    words_in_line = line.split(" ")
    for word in words_in_line:
        word = word.replace(string.punctuation, '')
        word = word.strip()
        word = word.lower()
        if word_count.get(word):
            word_count[word]+= 1 #same as word_counts[word] = word_counts[word] +1
        else:
            word_count[word]=1
for word, count in word_count.items():
    print(f"{word}:\t {count}")