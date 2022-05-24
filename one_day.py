import json

data="""
{
"student":  
       {
      "first name": "Uzuriha",
      "id":68942353,
      "last name ":"Akibi",
      "years": 20,
      "gender": "female"}
}
"""
data1=json.loads(data)
print(data1)
print(data1["student"]["gender"])
json_convert = json.dumps(data1,indent=2)

with open('my_json.json', 'w') as file:
    file.write(json.dumps(json_convert))

print(json_convert)




















