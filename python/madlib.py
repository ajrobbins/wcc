print('Welcome to the Mad Lib generator!')
adjective1 = raw_input('Type in an adjective:')
adjective2 = raw_input('Another adjective:')
adjective3 = raw_input('And another adjective:')
adjective4 = raw_input('One more adjective:')
plural_animal = raw_input('Plural animal (e.g., puppies):')
verb = raw_input('Now a verb:')
plural_noun = raw_input('Now a plural noun:')
musician = raw_input('The first name of a woman musician:')
beverage = raw_input('A beverage:')
body_part = raw_input("And finally, a plural body part:")

print('Excellent choices! Here\'s your story...')
print('---------------------------------')
print('There was once a ' + adjective1 + ' programmer named ' + musician)
print('who wanted to build a ' + adjective2 + 'mobile app to\nhelp ' + adjective3 + plural_animal +' find new homes.')
print(musician + 'stayed up all night, drinking lots of caffeinated' + beverage + 'as she worked and worked\ntrying to complete her ' + adjective4 + 'program.')
print('Whenever' + musician + 'hit a dead end, she would\nexclaim *' + plural_noun + '*!')
print('But she was not discouraged, and after a quick break\nto ' + verb + 'and clear her head, she got back to work.')
print('By morning, when the sun started to rise, she let out a\nbig yawn and stretched her ' + body_part + '.\nFinally, she was done.') 