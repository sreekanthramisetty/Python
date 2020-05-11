dict1={'A':[100,200],"B":(200,300),"C":{300,300,400}}
del dict1['B']
print(dict1.get('C',500))  
print(dict1.get("B"))
 