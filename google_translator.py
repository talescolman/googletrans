# google translate on python
# intall pip intall googletrans

# libraries
from googletrans import Translator

# create a translator object
trans = Translator()
t = trans.translate(
	'Bom dia') #the string is what we will translate

# source language
print(f'Source: {t.src}	') # google will identify the language
# detination 
print(f'Destination: {t.dest}') # the source is always english
# print the translated text
print(f'{t.origin} -> {t.text}')

# now if you want to translate to other languages
trans = Translator()
t = trans.translate(
	'Bom dia', #the string is what we will translate
	src= 'pt', #the source language
	dest= 'de') #the destination language

# source language
print(f'Source: {t.src}	') # google will identify the language
# detination 
print(f'Destination: {t.dest}') # the source is always english
# print the translated text
print(f'{t.origin} -> {t.text}')

# see all supported languages
from googletrans import languages

# iterate in the dictionary
for lang in LANGUAGES:
	print(f'{lang} - {LANGUAGES[lang]}') # will print the term and the description on the dictionary

# show the possible mistakes and translations

pm = t.extra_data['possible-mistakes']
pt = t.extra_data['possible-translations']

# show the results of possible mistakes and possible translations
print(f'Possible Mistakes: {pm}')
print(f'Possible Translations: {pt}')





