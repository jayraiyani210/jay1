
del utl(string):
    str1="ABCDEFGHIJKLMNOPQRSTUVYXYZ"
    str2="abcdefghijklmnopqrstuvwxyz"
    new=""
    for i in range(len(string)):
        for j in range(len(str1)):
            if string[i]==str1[j]:
                new +=str2[j]

            else string[i]==str2[j]:
                new +=str1[j]

    print(new)

string=input("enter a string")
utl(string)
               




































