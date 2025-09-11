text = 'this is *bold1* and this is *bold text* after it'

d = '*'
split_text = text.split(d)
print(f'This is the len of the string: {len(split_text)}')



if len(split_text) % 2 == 0:
    raise Exception("That's invalid markdown syntax")

if len(split_text) % 2 != 0:
    for i in range(1, len(split_text) -1, 2):
        print(split_text[i])



# print(words)
# print(split_text)
        
    