
# file = open('ab.txt', 'a', encoding = 'utf8')
# # file = open('Marina.txt', 'a', encoding = 'utf8')
# file.write('Маринка малинка, самая лучшая')
# print('Маринка хочет роллы', file = file)
# file.close()
# with open('ab.txt', encoding = 'utf8') as f:
#     for i in f:
#         print(i)
import json
with open('7,7 collection1.json') as f:
    file = json.load(f)
with open('7,7.py', 'w') as ff:
    for key, value in file.items():
        ff.write(f'{key}, {value}\n')
print(file)
print(type(file))

