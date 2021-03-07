import json
import urllib.request
import itertools  
import statistics
import pandas as pd
from nltk.tokenize import word_tokenize



stack=[]
name = input('What is your problem dude  ? ')
query=word_tokenize(name)
x = "+".join(query)


myTuple = ("https://clinicaltrials.gov/api/query/full_studies?expr=",x,"&min_rnk=1&max_rnk=100&fmt=json")
#url="https://clinicaltrials.gov/api/query/full_studies?expr=heart+attack&min_rnk=1&max_rnk=100&fmt=json"
y ="".join(myTuple)
url=y

list1=[]
list2=[]
list3=[]
with urllib.request.urlopen(url) as url:
    s = url.read()
    data = json.loads(s) #data is dictonart datatype
    data= data.get('FullStudiesResponse').get('FullStudies')




j=0
while j<100:
     for i in data[j].get('Study').get('DerivedSection').get('ConditionBrowseModule').get('ConditionMeshList').get('ConditionMesh'):
        list1.append(i.get('ConditionMeshTerm'))
        #print(i.get('ConditionMeshTerm'))
        j=j+1

j=0
while j<100:
     for i in data[j].get('Study').get('DerivedSection').get('ConditionBrowseModule').get('ConditionAncestorList').get('ConditionAncestor'):
        list2.append(i.get('ConditionAncestorTerm'))
        #print(i.get('ConditionMeshTerm'))
        j=j+1
j=0
while j<100:
     for i in data[j].get('Study').get('DerivedSection').get('ConditionBrowseModule').get('ConditionBrowseLeafList').get('ConditionBrowseLeaf'):
        list3.append(i.get('ConditionBrowseLeafName'))
        #print(i.get('ConditionMeshTerm'))
        j=j+1



#print(list1,list2,list3)
list1.extend(list2)
list1.extend(list3)

s = []
for i in list1:
   if i not in s:
     s.append(i)

print(s)
print("end")

