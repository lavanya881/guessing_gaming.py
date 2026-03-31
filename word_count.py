# Word Count Program

with open("sample.txt", "r") as file:
    text = file.read().lower()
    words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word in sorted(word_count):
    print(word, ":", word_count[word])