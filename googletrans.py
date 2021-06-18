# google translate on python
# intall pip intall googletrans

from googletrans import Translator

# create the translator
translator = Translator()

# You don't need to specify the Source Language
# The Target Language is by default English
print(translator.translate('Hola mundo'))

# You can also set your language pair (always a better option)
# src= Source Language
# dest= Target Language
print(translator.translate('Hola mundo', src='es', dest='fr'))

# You can also translate a list of words
vocab = ['besorgt', 'wütend', 'glücklich', 'gelangweilt', 'traurig']

translations = translator.translate(vocab, dest='pl')
for translation in translations:
	print(translation.origin, ' -> ', translation.text)

# You can detect the language of an input
translator = Translator()
print(translator.detect('Dobrý večer.')) # this will print out Detected(lang=cs, confidence=1)

# You can also insert your input as a string to better organize your code

text1 = " Qui ne meurt pas de n'être qu'un homme ne sera jamais qu'un homme. "

trl1 = translator.detect(text1)
print(trl1)


