# 1.Reverse a string without using slicing.
# 2.Count vowels in a string.
# 3.Check if a string is a palindrome.
# 4.Write a function to calculate factorial of a number.
# 5.Write a function to check if a number is prime.
# 6.Write a function to count words in a sentence.
# 7.Replace all spaces in a string with -.

#no-2
# str="my name is swapna"
# count=" "
# for str1 in str:
#   if(str1=="a" or str1=="e"or str1=="i" or str1=="o" or str1=="u"):
#     print(count(str1))


#no-3
# str1="hii its string2 and i trying to replace"
# str3=str1.replace(" "," - ")
# print(str3)

#no-4:factorial

# def calculatefact(num):
#   fact=1
#   # num=int(input("enter the number"))
#   for i in range(1,num+1):
#     fact=fact*i
#     i+=1 #unneccesry
#   print(fact)
# calculatefact(5)  


# string is palidrome

# def is_palidrome(s):
#   s=s.lower().replace(" ","")
#   return s==s[::-1]
# string="madam"
# if is_palidrome(string):
#   print("palindrome")
# else:
#   print("not pallidrome") 

#reversed string :1
# s="my name is swapna"
# reversedstring="".join(reversed(s))
# print(reversedstring)
#or
# s="my name is swapna"
# print(s[::-1])


# num=int(input("enter the number"))
# if num>1:
#   for i in range(2,num):
#     if num%i==0:
#       print("not prime")
#       break
#     else:
#       print("prime")
# else:
#   print("not prime")      


#.Write a function to count words in a sentence.
# def countwords(sen):
#   word=sen.split()
#   return len(word)
# text="my name is swapna and now i am studying at web_bocket"
# print(countwords(text))


# sen="my name is swapna"
# print(sen.split("-"))

# sen="my name is swapna"
# print(sen[::-1]) //inverse

# 8.Count the number of vowels in a string.
# 9.Remove spaces from the beginning and end of a string.
# 10.Find the sum of numbers from 1 to 100.


# str="abcd"
# # count=0
# for str3 in str:
#   if(str3=="a" or str3=="e" or str3=="i" or str3=="o" or str3=="u"):
#     count=count+1
# print(count)


# str="       my name is swapna    "
# print(str.strip()) #removing the spaces 


# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)    


# def is_pallidrom(num):
#   if(num==num[::-1]):
#     print('true')
#   else:
#     print('false')
# is_pallidrom('npn')  


# s=input('enter a sentence').lower()
# vowel='aeiou'
# words=s.split()

# print(len(words))

# count_vowel=0
# count_consonate=0

# for i in s:
#   if i.isalpha():
#     if i in vowel:
#       count_vowel +=1
#     else:
#       count_consonate +=1


# print("the total vowel are  :",count_vowel)   
# print("the total consonate are:",count_consonate)     


# list=[4,7,7,8,9,8,9,8,5,4,3,2,1,1,2,3,9,8,7,]
# convert=set(list)
# print(convert)


# def factorial(num):
#   fact=1
#   for i in  range(1,num+1):
#     fact=fact*i
#   print(fact)
# factorial(4)     
 

# list=[10,20,30,40,50]
# square=[]

# for i in list:
#   calcul=i*i
#   square.append(calcul)
# print(square)


# list=[10,89,67,0,98,56,45,34,23,14,24,65,8,7,4,6]
# list.sort()
# print(list)


#wrong
# target=98
# list=[10,89,67,0,98,56,45,34,23,14,24,65,8,7,4,6]
# for i in list:
#    if(i<target):
#      print(i)
    

# students={
#   "swapna":90,
#   "tunia":89,
#   "john":87,
#   "bob":78,
# }
# topper=max(students, key=students.get)
# print("topper",topper)
# print("mark",students[topper])

# class calculation:
#   def __init__(self,a,b):
#     self.a=a
#     self.b=b
#     print(a+b)
#   def mul(self) :
#     print(f'{self.a *self.b}')   
#   def sub(self)  :
#     print(f'{self.a -self.b}')
#   def divide(self):
#     print(f'{self.a // self.b}')  
# obj=calculation(2,4)
# obj.mul() 
# obj.sub()
# obj.divide()

# s="the sky is blue"
# s=s.strip()
# s=s.split()
# s.reverse()
# st=" " .join(s)
# print(st)



# 1. Write a program to create a list of prime numbers between 1 and 100.
# 2. Find common elemnts in two lists.
# 3. Find greatest common divisor(gcd) of two number(by using math module)
# 4. Find missing numbers in a list.[1,2,3,5,6,7,8]
# 5. Write a program to initialize object data.
# 6. Write a program to demostrate method overriding.
# 7. Write a program to handle division by zero error.
# 8. Write a program to handle multiple exception.
# 9. Write a program to create a user-defined exception.
# 10. Write a program to handle file also handle if the file is not found.
# 11. Write a program to write data line by line into a file.
# 12. Write a program to handle a file by both reading and writing using all the three a+, r+, and w+ method.
# 13. Write a program to add a key in a dictionary.

2.# list1=[1,2,3,4,5,6,7]
# list2=[1,54,7,6,8,7]
# for i in list1:
#    for j in list2:
#       if i==j:
#          print(i)


3.# import math
# a=24
# b=36
# gcd=math.gcd(a,b)
# print(gcd)


4.# list=[1,2,3,5,6,7,8]
# n=len(list)+1
# total=n*(n+1)//2
# missing=total-sum(list)
# print(missing)


5.# class student:
#   def __init__(self,name):
#     self.name=name
#     # print(name)
# obj1= student("swapna") 
# print(obj1.name)


#6.class student:
#   def __init__(self,name):
#     self.name="swapna"

#     print(f'my name is {name}')
#   def nickename(self,name)  :
#     self.name="tunia"
#     print(f'my nickname is  also {name}')
# obj=student("swapna")  
# obj.nickename("tunia")  


7.#try:
#   a=int(input("enter anything either number or a string"))
#   b=10/a
#   print(b)
# except ZeroDivisionError:
#   print("it can't divise by zero ")
  


8.# try:
#   a=(input("enter anything either number or a string"))
#   b=10/a
#   print(b)
# except ZeroDivisionError:
#   print("it can't divise by zero ")
# except ValueError:
#   print("it can't divide ")
# except TypeError:
#   print("it is type error")
# finally:
#   print("execute successful ")  



# try:
#   file=open("webs/exampllll.txt",'r')
#   content=file.read()
#   print(content)
# except FileNotFoundError:
#   print("first create a file in the right path ")  


13.# dict={
#   "name":"swapna",
#   "mark":89,
#   "[reg-no]":676666,

# }  
# dict.setdefault("collage ","nmiet")
# print(dict)

9.# try:
#   age=input("enter your age ")
#   if age<=18:
#     print("the people are eligible ")  
# except ValueError:
#   print("enter the valid age")

# except TypeError:
#   print("enter the valid input")

# 11. Write a program to write data line by line into a file.
# 12. Write a program to handle a file by both reading and writing using all the three a+, r+, and w+ method.

11.# file=open("webs/exampleset",'w')
# file.write('\n my name is swapna  \n my father name is karunakar panda')
# file.close()

12.# with open("webs/exampless.txt",'r+') as fl:
#   fl.write("hii its me \n  i am a student of btech cse")
#   fl.seek(0)
#   content=fl.read()
#   print(content)
#   print(fl.writable())
#   print(fl.readable())


# file=open("webs/example.txt",'w+')
# file.write("hii i am tunia")
# file.seek(0)
# content=file.read()
# print(content)

# file.close()

# with open("webs/example.txt",'a+') as e:
#   e.write("\n hii now i am continue my btech")
#   e.seek(0)
#   const=e.read()
#   print(const)


# list1=[1,2,3,4,5,6,7,88,7,7]
# list1=set(list1)
# list2=[1,2,7,98,78]
# list2=set(list2)
# list3=list1.intersection(list2)
# print(list3)


# primrnumber=[]
# for n in range(2,101):
#   for i in range(2,n):
#     if n%i==0:
#       break
#     else:
#       primrnumber.append(n)
# print(primrnumber) 

# l1=[1,2,3,4,6,7,2]
# l1.sort(reverse=True)

# Write a program to remove duplicates from a list.
# Write a program to create a dictionary and print keys and values.
# Write a program to check whether a key exists in a dictionary.
# Write a program to count word frequency in a string.
# Write a program to demonstrate method overriding.
# Write a program to add data into a file and display the content in the file.
# Write a program to check whether a file exists.
# Write a program to count lines in a file.
# Write a program to count digits in a number.
# Given a list of integers and a target, return indices of two numbers whose sum equals the target.
# Remove Duplicates from Sorted Array, Return length after removing duplicates.

# list1=[2,3,4,5,555,5,6,6,6,6,7,7,7,8,8,8,9,1,23,3,5,5,]
# list1.sort()
# print(set(list1))


# dict={
#   'name':"swapnarani panda",
#   'roll-no':2201288113,
#   'collage':'Nmiet',
#   'mark':85


# }
# for key,values in dict.items():
#   print(f'key:{key},values:{values}')



# def dictpreset(dict,key):
#   if key in dict:
#     print(f'{key} exist in dict')
#   else:
#     print(f"{key} don't exist in dict")  
# dictpreset(dict,'mark')    


# string="my name is swapna and my Qulification is btech and my nickname same as my new name ".lower()
# str=string.split()

# fre={}
# for word in str:
#   if word in fre:
#     fre[word]+=1
#   else:
#     fre[word] =1
# print(fre)  


# class student:
#   def show(self):
#     print("my name is swapna")
#   def show(self)  :
#     print("my name is tunia")
# obj=student() 
# obj.show()   


# try:
#   file=open("webs/exam",'w+')
#   file.write("it's a new file and \n it create  for pratice")
#   file.seek(0)
#   content=file.read()
#   print(content)
# except FileNotFoundError:
#   print("file not found are executed ") 
# finally:
#   print('it is execute anyway')


# import os
# if os.path.exists('webs/exam'):
#   print("file is exist")
# else:
#   print("file is not exists")  


# file=open('webs/exam','r+')
# content=file.readlines()
# print(len(content))

# last
# list=[1,2,3,4,5,5,6,6,7,7,7,7,8,88]
# n=len(list)
# j=0
# for i in range(1,n):
#   if list[j]!=list[i]:
#     j+=1
#     list[j]=list[i]
# print(list[j])


# n=12347845433232
# print(len(str(abs(n))))

#sorted array
# target=9
# nums=[2,7,11,15]
# def count(nums):
#   n=len(nums)
#   i,j=0,n-1
#   while(i>j) : 
#     current_sum=nums[i]+nums[j]
#     if current_sum>target:
#       j-=1
#     elif current_sum<target:
#       i+=1
#     else:
#       return [i+1,j+1]


# target=8
# nums=[1,7,4,5]
# n=len(nums)
# i,j=0,n-1
# while(i>j):
#   if nums[i]+nums[j]==target:
#     print(i,j)
#   else:
#     i=i+1
#     j=j-1  


# numbers=[1,2,3,43,4]
def targetsum(numbers,target):
  x={}
  for i,n in enumerate(numbers) :
    if target-n in x:
      return [x[target-n],i]
    x[n]=i

# print(targetsum(numbers,6))

#  x ={
#     1:0,
#     2:1,
#     6:2,
#     7:3,
#     4:4
# }


# def removedup(list):
#   uniq=[]
#   for i in list:
#     if i not in uniq:
#       uniq.append(i)
#   return uniq
# print(removedup([2,4,5,6,4,35,7,5,4])) 
# print(len(removedup([2,4,5,6,4,35,7,5,4])))

# def removeDuplicates(lst):
#     count = 0
#     for i in range(1, len(lst)):
#         if lst[i] != lst[count]:
#             count += 1
#             lst[count] = lst[i]
#     return count +1

# print(removeDuplicates(lst))

#spiral matrix
# n=len(matrix)
#         m=len(matrix[0])


#         col_start,col_end=0,m-1
#         row_start,row_end=0,n-1

#         ans=[]
#         while  len(ans) < n*m:
#             #row_start col_start->col_end
#             for i in range(col_start,col_end):
#                 ans.append(matrix[row_start][i])
#             row_start +=1

#             if len(ans) == n*m:
#                 break

#             #col_end row_start->row_end
#             for i in range(row_start,row_end) :
#                 ans.append(matrix[i][col_end]) 
#             col_end-=1

#             if len(ans) ==n*m:
#                 break

#             #row_end col_end->col_start
#             for i in range(col_end,col_start-1,-1) :
#                 ans.append(matrix[row_end][i])
#             row_end -=1

            
               

#             #col_start row_end,row_start:
#             for i in range(row_end,row_start-1,-1):
#                 ans.append(matrix[i][col_start])   
#             col_start+=1
#         return ans             











    
















  



































































 














 


   



























  

  
  
  



 

