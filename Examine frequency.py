from collections import Counter


def get_proportions(word):
    frequencies = dict(Counter(word))
    for letter, value in frequencies.items():
        frequencies[letter] = float(value) / len(word)
    return frequencies


def compare_to_dict(word, compare_to):
    props = get_proportions(word)
    comparison_scores = []
    for key in compare_to.keys():
        word_distance = sum(abs(props.get(letter, 0) - compare_to[key].get(letter, 0))
                            for letter in set(word + key))
        comparison_scores.append((key, word_distance))
    return sorted(comparison_scores, key=lambda x: x[1])


comparison_dict = {}
for word in ['pablo', 'rocky', 'rigo', 'nino']:
    comparison_dict[word] = get_proportions(word)

print(comparison_dict)

print(compare_to_dict('baobab', comparison_dict))
