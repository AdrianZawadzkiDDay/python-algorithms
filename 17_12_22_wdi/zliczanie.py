import re
from string import whitespace
from collections import Counter

SENTENCES = re.compile(r'([A-Z].*?\.)(?=(\s[A-Z]|\Z))', re.DOTALL)
STATS_TEMPLATE = ('Podana przez ciebie treść zawiera {} znakow,'
                  '{} wyrazów, {} zdań')

def stats(string):
    words = string.split()
    sentences = SENTENCES.findall(string)
    print(STATS_TEMPLATE.format(len(string), len(words), len(sentences)))
    chars_stats = Counter(string).most_common()
    chars_stats = ', '.join(
        '{}: {}'.format(char, count)
        for char, count in chars_stats
        if char not in whitespace
    )
    print('Statystyki znaków:\n{}'.format(chars_stats))

if __name__ == '__main__':
    content = input("Wprowadź treść: ")
    stats(content)