#  walking through lists and dictionaries.

#  LIST.
mylist =  ['rob', 'mike', 'rik', 'jimmy']

print('This is my list: ')
for element in mylist:
    print(element)

#  using the index and range method.
print('This is my list again: ')
for i in range(len(mylist)):
    print(mylist[i])


# DICTIONARY.
mydict = {'rtr':'good','swtch':'bad','vpn':'better'}

# # this prints only the keys, which is the default behaviour
# # when walking through a dictionary
print('\nThis is my dictionary by key: ')
for key in mydict:
    print(key)

# # this prints only the keys using the keys method on the dictionary.
print('\nThis is my dictionary by key (again): ')
for key in mydict.keys():
    print(key)

# # this prints only the values using the values method on the dictionary.
print('\nThis is my dictionary by value: ')
for value in mydict.values():
    print(value)

# # this prints each item which is a key:value pair using the items method on the dictionary.
print('\nThis is my dictionary by item (key:vlaue pair) ')
for item in mydict.items():
    print(item)

# this prints each item which is a key:value pair using the items method on the dictionary.
print('\nThis is my dictionary by item (key:vlaue pair) again:')
for a,b in mydict.items():
    print(a + ' : ' + b)