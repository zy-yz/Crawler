# encoding=utf-8

import json

json_str ='[{"username":"张三","age":18,"country":"china"}]'
persons = json.loads(json_str)
print(type(persons))
for person in persons:
    print(person)


# persons = [{
#     'username':"张三",
#     'age':18,
#     'country':'china'
# },
#     {
#     'username':"lisi",
#     'age':23,
#     'country':'china'
#     }
# ]
#
# json_str = json.dumps(persons)
# print(type(json_str))
# print(json_str)

with open('person.json','w',encoding='utf-8') as fp:
    json.dump(persons,fp,ensure_ascii=False)