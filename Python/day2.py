# data structures in python

# 1. List
l = [1, 2, 3, 4, 5]
print(l)
print(type(l))
l= [1,"amit", 2.5, 3, 4, 5]
print(l)
for x in l:
    print(x)
i=0
while(i < len(l)):
    print(l[i])
    i += 1
l.append(10)
print(l)

# print(l[2:4])
# l=l[::-1]
# print(l)
# l.sort()
# print(l)
# l.remove(1)
# print(l)
# l.pop(2) 
# print(l)
# l.reverse()
# print(l)
# l.insert(2, 100)
# print(l)
# l.count(2)
# print(l)


# multi D list

# l= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(l)
# print(type(l))
# print(l[0][0])
# print(l[1][0])
# print(l[2][0])
# l.append([10, 11, 12])
# print(l[0:5])



# l=[1,2,3,4,5]
# lst= [i**2 for i in l ]
# print(lst)
# lst = [ i for i in range(10) if i%2==0]
# print(lst)
# lst = [i*0 for i in range(10) if i%2==0]
# print(lst)
# lst = [[i for i in range(3)] for j in range(3)]
# print(lst)
# lst = [j for row in lst for j in row]
# print(lst)





# dictionary

# d = { "name": "amit", "age": 25, "address": "delhi", "phone": 1234567890 }
# print(d)
# for key in d:
#     print(key, " : ", d[key])
# print(d["name"])
# print(d["age"])
# print(d["address"])
# print(d["phone"])
# d["college"]="kiet"
# print(d)
# del d["college"]
# print(d)
# for x,y in d.items():
#     print(x,"  :  ",y)
# print(d.keys())
# print(d.values())
# print(d.items())
# print("name" in d)
# print("amit" in d)
# print("amit" not in d)
# print("amit" not in d.values())
# print(d.get("name"))


# d= { i:i**3 for i in range(5)}
# print(type(d))
# print(d)

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# d= { l1[i]:l2[i] for i in range(len(l1))}
# d=dict(zip(l1,l2))
# print(d)