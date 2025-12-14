import os

file_name = input("Please enter file name:")
file_path = os.path.join(os.path.dirname(__file__), file_name)
file = open(file_path, "r")

text = file.read()
file.close()

text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")

words = text.split()

# dictionary for word count frequency
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True) # taking word_count and sorting them by each words frequency

for word, count in sorted_words:
    print(word, ":", count)
