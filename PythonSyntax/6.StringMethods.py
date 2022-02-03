message = '  Hello There. My name is Senanur Korkmaz'

#Converts a string into upper case
print(message.upper())

#Converts a string into lower case
print(message.lower())

#Converts the first character of each word to upper case
print(message.title())

#Converts the first character to upper case
print(message.capitalize())

#Returns a trimmed version of the string
print(message.strip())

#Splits the string at the specified separator, and returns a list
splitMessage = message.split()
mergeMessage = ' '.join(splitMessage)
print(mergeMessage)
mergeMessage = '*'.join(splitMessage)
print(mergeMessage)
print(message.split())
print(message.split('.'))

#Searches the string for a specified value and returns the position of where it was found
index = message.find('Senanur')
print(index)


isFound = message.startswith('H')
print(isFound)

isFound = message.endswith('z')
print(isFound)

#Türkçe karakterleri kaldirdik
replaceMessage = message.replace('ö','o').replace('Ö','O')

#Returns a centered string
centerMessage = message.center(51,'*')
print(centerMessage)

