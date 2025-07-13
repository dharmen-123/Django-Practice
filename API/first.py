import json
d={'name':"Neeraj",'age':20}
Jsondata=json.dumps(d)
print(Jsondata)
print(type(Jsondata))


d1={'name':True,'age':False,'branch':None}
jdata=json.dumps(d1)
print(jdata)
print(type(jdata))
print("After Covert the json into python")
pdata=json.loads(jdata)
print(pdata)


print("json data into python")
jd='{"name": true, "age": false, "branch": null}'
pd=json.loads(jd)
print(pd)



