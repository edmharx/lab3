def vowelsToUpper(sentence):
    vowels = 'aeiou'
    transformed = ''.join([char.upper() if char in vowels else char for char in sentence])
    return transformed

print(vowelsToUpper("hi hello word mah homie"))