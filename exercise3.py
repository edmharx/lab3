

def vowelsToUpper(sentence):
    vowels = 'aeiou'
    transformed = [char.upper() if char in vowels else char for char in sentence]
    return transformed

vowelsToUpper("hi hello word mah homie")