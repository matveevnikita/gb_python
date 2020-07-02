# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

n_lines = 0
n_words = list()

with open("ex2.txt") as f_obj:
    for line in f_obj:
        n_words.append(len(line.split(" ")))
        n_lines += 1

print('there are {} lines with {} words in each line'.format(n_lines, n_words))