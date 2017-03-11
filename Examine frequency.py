from collections import Counter

#Get the letter proportions for each letters
def get_proportions(word):
    frequencies = dict(Counter(word))
    for letter, value in frequencies.items():
        frequencies[letter] = float(value) / len(word)
    return frequencies

#compare respective proportions and input
def compare_to_dict(word, compare_to):
    props = get_proportions(word)
    comparison_scores = []
    for key in compare_to.keys():
        word_distance = sum(abs(props.get(letter, 0) - compare_to[key].get(letter, 0))
                            for letter in set(word + key))
        comparison_scores.append((key, word_distance))
    return sorted(comparison_scores, key=lambda x: x[1])

answer = input("Please enter your name")
comparison_dict = {}
for word in ['rincewind', 'adora belle', 'the patrician', 'vimes', 'cheery','drumknott','detritus','dorfl','nobb','teatime','death','moist von lipwick','gladys']:
    comparison_dict[word] = get_proportions(word)


#need for adding an step where only the word with the shorted distance is given not the distances themselves
result = compare_to_dict(answer, comparison_dict)

print (result[0][0])
