odd=[1,3,5,7,9]
even=[2,4,6,8]
print(odd)
print(even)

odd[2]=even
print(odd)
odd=[1,3,*even,7,9]
print(odd)
odd.sort()
print(odd)

