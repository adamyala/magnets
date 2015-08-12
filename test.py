import os
import re
import operator

def string_builder(genre):
    words = []
    for root, dirs, files in os.walk('./' + genre):
        for file in files:
            if file.endswith('.txt'):
                for line in open(os.path.join(root, file)):
                    words.extend(
                        [re.sub(r'[^a-zA-Z0-9_ ]', '', x).lower() for x in line.split()]
                    )
    list(set(words))
    word_counts = {}
    for word in words:
        word_counts[word] = words.count(word)

    removals = [
        'a', 'or', 'in', 'is', 'and',
        'the', 'at', 'my', 'on', 'be',
        'to', 'am', 'of', 'for', 'it',
        'our', 'can', 'as', 'that', 'was',
        'i', 'you', 'me', '', 'are', 'im',
        'your', 'but', 'so', 'dont', 'cant'
    ]
    for removal in removals:
        try:
            del word_counts[removal]
        except:
            print(removal)

    sorted_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_counts

print (string_builder('black_metal'))
print (string_builder('christian'))
