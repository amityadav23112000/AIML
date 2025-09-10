#python lists
# list is group of homogenous and hetrogenous data type:
# index :forward and backward
# duplicates are allowed
#  declare by using []
# mutable : modifications are allowed

# l=[10,20,30,'amit']
# print(l)

# print(type(l))

# l=[]
# print(l)
# l=list()
# print(l)

# l=list("amit")
# print(l)

# op-
# [10, 20, 30, 'amit']
# <class 'list'>
# []
# []
# ['a', 'm', 'i', 't']

# id(), is ,is not ,== ,!=, in , not in all work for list


# l=[10,30,"amit"]
# a,b,c=l
# print(a,b,c)
# print(type(a))


# nested list
# l=[[10,20,],[20,30]] work like 2d array
# print(l[0])
# print(l[0][1])


# take input list from user
# i=5;
# l=list()
# while i:
#     a=int(input())
#     l.append(a)
#     i-=1
# print(l)

# l=[[10,20],["amit","anjali"]]
# for x,y in l:
#     print(x,y)
# op- 10 20
# amit anjali


# l=[ x for x in range(11)]
# print(l)


# concat
# l1=[10,20,30]
# l2=[30,40,50]
# l1=l1+l2
# print(l1)

# l=l1*3
# print(l)

# l=l1.copy()
# print(l)

# extend

# l1=[10,20,30]
# l2=[10,20,40]
# l2.extend(l1)
# print(l2)
# l2.append(300000) add at last
# print(l2)

# insert() function
# l=[10,20,30,40,50]
# # l.insert(3,1000) at 3rd index insert 10000
# print(l)

# list are mutable 
# l=[10,20,30,400]
# l.remove(20) remove 20
# print(l)

# l.pop() remove last element
# print(l)
# l.pop(2) remove index element present at 2 index
# print(l)

# l.clear()  remove all data
# print(l)

# l=[[10,20],["amit","anjali"],[30,40]]
# l1=list()
# l2=list()
# for x,y in l:
#     l1.append(x)
#     l2.append(y)
# print(l1)
# print(l2)

# SORTING-------
l=[10,320,300,4000,530]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

# l.reverse()
# print(l)
# print(len(l))

# print(max(l), min(l))








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


#                                      set   group of hetro and homo both
# duplicate not allowed
# inserstion order not preseerved
# no index
# set are mutable

# s={10,20,30}
# print3(s)
# print(type(s))
# s={}
# print(type(s))  it will dict data type

# s={10,"amit" ,(20,30)}
# print(s)

# mutable
# s={10,20,30,4}
# s.add(60)
# print(s)

# s.update([10,20,30]) used to add multiple values
# s1={10,20,30}
# s2=s1.copy()
# # s3=s1+s2  (+ ,* )operatiom not allowed ---concat and replicaton not allowed
# print(s3)

# s={"amit", 10,30,(10,30)}
# for x in s:
#     print(x)

#  id ,is ,is not ,==,!=,in ,not in all work

# s={(20,30),(429,"amit")}
# for x in s:
#     print(x[1]) 
# op-30
# amit

# set operations
# s=set("amitsingh")
# t=set("amitayadav")
# print(s-t)
# print(s|t)
# print(s&t)
# print(s^t)

# s={10,202,3040}
# s.remove(10)
# s.pop()
# print(s)
# s.discard(10)
# s.clear()

# l=[10,20320,2030,20302,10,10,30,30]
# s=set(l)
# l=list(s) to remove duplicates



# python tuple
# group of object hetro and homo
# duplicates. allowed
# list is mutable and tuple is immutable
# {}

# l=(10,20,30)
# print(type(l))
# print(l)
# l=(10)
# print(type(l)) int
# l=(10,)
# print(l)
# print(type(l))

# l=tuple("ratan")
# print(l)

# l=(10,20,30,40,50)
# print(l)
# print(l[-4:-2])

# t=((10,20),(3,40))
# for x,y, in t:
#     print(x,y)

# t=tuple(x for x in range(10))
# print(t)

# == id ,is , is not , in , in not ,!= all works forr string list ,tuple
 
# concatenation
# l1+l2
# l=l*30

# t=(10,20,30)
# l=list(t)
# l.append(200)
# t=tuple(l)
# print(t)

# t=(10,20,30,50,10,10)
# # a=t.count(10)
# # print(a)
# print(t.index(10))
# l=list(t)
# l.sort()
# t=tuple(l)
# print(t)
# print(min(t))
# print(max(t))


# l=(10,3453,52344523)
# l=sorted(l)
# print(l)