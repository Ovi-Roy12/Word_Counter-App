input_file = open("input.txt",'r')
input_read_file = input_file.read()

search_words = ['Python','C','OOP','Hello','Java','C++']

word_count = {word: 0 for word in search_words} #dict

input_words = input_read_file.split()

for word in input_words:
    if word in word_count:
        word_count[word] += 1

for word, count in word_count.items():
    print(f"'{word}' -> {count}")

