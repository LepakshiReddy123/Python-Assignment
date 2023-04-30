Q2:
Description:write a program in python to print the number of unique letters in a string.Only new letters from the string 
    should be counted and not duplicates.
    
    input:string1="India"
    output:uniqueLetters=i,n,d,a
        
    input:string1="Dedication"
        output:uniqueLetters=d,e,i,c,a,t,o,n
		
		
------------------Code-------------------

str1=input("String1 = ")
str1=str1.lower()
str2=[]
for i in str1:
    if i not in str2:
        str2.append(i)
    str=','.join(str2)
    
print("Unique letters = ",str)

        
----------------OUTPUT------------------
String1 = Python Programming
Unique letters =  p,y,t,h,o,n, ,r,g,a,m,i
    