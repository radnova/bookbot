alphabet = {'a': 10, 'b': 30, 'c': 15}
alph_list = []
for key in alphabet:
    if key.isalpha():
        new_dict = {key: alphabet[key]}
        alph_list.append(new_dict)
print(alph_list)

alph_list.sort(key=alph)
print(alph_list)

for key in alphabet:
    if key.isalpha():
        print(key,alphabet[key])
