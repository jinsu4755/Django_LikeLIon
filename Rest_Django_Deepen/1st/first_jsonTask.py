import json

diary = {
    'id': 3,
    'title': 'I`m jinsu4755',
    'body': "hello hi hi",
}

print(diary)
print(type(diary))

diary_s = json.dumps(diary)
# dumps : dictionary -> json

print(diary_s)
print(type(diary_s))

diary_back = json.loads(diary_s)
# loads : json string type -> python data type

print(type(diary_back))

"""
출력 결과
--------------------
{'id': 3, 'title': 'I`m jinsu4755', 'body': 'hello hi hi'}
<class 'dict'>
기존 diary 는 dictionary type
{"id": 3, "title": "I`m jinsu4755", "body": "hello hi hi"}
<class 'str'>
dict -> json 변환시 string type 로 바뀜
<class 'dict'>
json 을 다시 변환하면 python 원래 data type 로 바뀐다(역변환)
"""
