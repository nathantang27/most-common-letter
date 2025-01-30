def most_common_letters(words):
    letter_count = {}
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    max_frequency = max(letter_count.values())

    most_common = {letter for letter, count in letter_count.items() if count ==max_frequency}
    return most_common

words = ["tends","ricks","kales","yauld","heder","batch","smite","zouks","hence","himbo","ixias"]
result = most_common_letters(words)
print("The most common letter is", result)