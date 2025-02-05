#Working with strings
#list [start:end:step]
s="Aditya"
# print(s[1:]) o/p:- ditya (as it indexes from the first, as python starts from 0)
# print(s[1:-1]) o/p:- dity (as it indexes from first to last)
# s=s.split(" ")
# try:
#     s=[x for x in s]
#     print(s)
#     print("Rev:",''.join(s[::-1]))
# except IndexError as e:
#     print(f"No index found sorry!")

nums=[1,2,3,4,5,6,7,8]
# list comprehension for n times n in nums
# my=[n for n in nums]
# print (my)
#for n*n in nums.

# nums=[n*n for n in nums]
# print(nums)

# nums=[n for n in nums if n%2==0]
# print(nums)
#lambda and map
# my=map(lambda n:n*n , nums)
# print(list(my))

#need letter num pair (abcd)(0123)

# nums=[(letter,num) for letter in 'abcd' for num in range(4)]
# print(nums)

#Dictionary comprehension

names=['Bruce','Peter','Logan','Tony','Steve']
heroes=['Batman','Spiderman','Wolverine','Ironman','Captain America']

#One way print (dict(zip(names,heroes)))
# myDict={name:hero for name, hero in zip(names,heroes) if name !='Peter'}
# print(myDict)

#For set use {} for generators use ()