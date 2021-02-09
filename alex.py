"""
Welcome to this GitHub practice exercise. I hope by the end of this you feel comfortable with branching! 
"""

# If you work for Grayce, add your name to this list

graycians = ['ELIZA IS COOL', '  Alice West  ', '  Roisin Wherry   ', '  peter busby  ', '  geoff smith   ', 'henry worrall']


# This function cleans a list of names and prints them
def print_clean_names(names):
    for name in names:
        name = name.strip()
        name = name.split(' ')
        clean_name = []
        for word in name:
            word = word.capitalize()
            clean_name.append(word)
        clean_name = ' '.join(clean_name)
        print(clean_name)

print_clean_names(graycians)
