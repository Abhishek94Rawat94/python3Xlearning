# Filter out the vowels in albhabets

letters = ['a', 'd', 'b', 'e', 'c', 'i', 'o', 'f', 'u', 'z']


def filter_vowel(letter):
    vowels = 'a', 'e', 'i', 'o', 'u'
    return letter in vowels


# result = filter_vowel('a')
# print(result)

vowel_word = filter(filter_vowel,letters)
print(list(vowel_word))
