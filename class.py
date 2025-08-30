
# a=int(input("enter A"))
# b=int(input("enter B"))
# if a>=b :
#     print("true")
# else:
#     print("false")    
# n=59874
# num=n
# while num>0:
#     lastdigit=num%10
#     print(lastdigit)
#     num=num//10
# count=0
# while num>0:
#     count=count+1
#     num=num//10  
# print(count)

# check palindrome
# check palindrome
# n = 1234
# num = n
# result = 0

# while num > 0:
#     digit = num % 10
#     result = (result * 10) + digit
#     num = num // 10

# if result == n:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# n=153
# num=n
# total=0
# nod=len(str(n))
# while num>0:
#     ld=num%10
#     print(ld)
#     total=total+(ld**nod)
#     print(total)
#     num=num//10
#     print(num)
# print(total)

# if total==n:
#     print("Armstrong Number")
# else:
#      print("not")    
# def factors(n):
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i, end=" ")

# # Example usage
# num = int(input("Enter a number: "))
# print(f"Factors of {num}: ", end="")
# factors(num)

# def get_factors(n):
#     result = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             result.append(i)
#     return result

# # Example usage
# num = 12
# print(get_factors(num))  # [1, 2, 3, 4, 6, 12]


# def greet():
#     print("hello yash ")
#     greet()
    
# greet()    

# def func1(n,times):
#     while times>0:
#        print(n)
#        times-=1
       
# func1(5,3)       
# print 1-9 using recursion
# def func2(n):
#     if n==0:
#         return
#     else :
#         print(n) 
#         func2(n-1)

# func2(19)
# ṛeverse a array using recursion
# num=[5,2,4,8,1,9,0,8,2,4]
# l=0
# r=len(num)-1
# def reverse(num,l,r):
#     if l>=r:
#         return
#     else :
#         num[l],num[r]=num[r],num[l]
#         reverse(num,l+1,r-1)

# reverse(num,l,r)
# print(num)  

# check a string palindrome 
# def is_palindrome(s, l, r):
#     if l >= r:   # base case
#         return True
#     if s[l] != s[r]:
#         return False
#     return is_palindrome(s, l + 1, r - 1)

# print(is_palindrome("mom", 0, len("mom")-1))   # True
# print(is_palindrome("hello", 0, len("hello")-1))   # False

# cheeck fibonaaci

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# # Print first 10 terms
# for i in range(10):
#     print(fib(i), end=" ")

# selection sort

# def selection_sort(num):
#     l=len(num)
#     for i in range(0,l):
#         min_idx=i
#         for j in range(i+1,l):
#             if num[j]<num[min_idx] :
#                 print(num)
#                 min_idx=j
#         num[i],num[min_idx]=num[min_idx],num[i]
  
# def selection_sort(num):
#     l=len(num)
#     for i in range(0,l):
#         min_idx=i
#         for j in range(i+1,l):
#             if num[j]>num[min_idx] :
                
#                 min_idx=j
#         num[i],num[min_idx]=num[min_idx],num[i]
        
#     print(num)    
 
# a=[7,3,2,9,4]
# selection_sort(a)  

# insertion sort
# def insertion_sort(num):
#     n=len(num) 
#     for i in range (1,n):
#         key=num[i]
#         j=i-1
#         while j>=0 and num[j]>key:
#             num[j+1]=num[j]
#             j-=1
            
#         num[j+1] =key   
#     print(num)
# a=[2,3,,8,4,1]
# insertion_sort(a)    
        
# def largest_num(num):
#     l=len(num)
#     largest=num[0]
#     for i in range(0,l):
#         if largest>num[i]:
#             i=i+1
#         else :
#             largest=num[i]
#             i=i+1    
#     print(largest)    
# b=[3,4,5,6,7,78,8]
# largest_num(b)

# def second_largest(num):
#     if len(num) < 2:
#         print("List must have at least two elements")
#         return
    
#     largest = second = float('-inf')  # very small number
    
#     for x in num:
#         if x > largest:
#             second = largest
#             largest = x
#         elif x > second and x != largest:
#             second = x
    
#     if second == float('-inf'):
#         print("No second largest element (all elements are same)")
#     else:
#         print("Second largest:", second)

# b = [3, 4, 5, 6, 7, 8]
# second_largest(b)
   
# is array sorted
# def IsSorted(num):
#     for i in range(len(num) - 1):   # iterate using indexes
#         if num[i] > num[i+1]:       # check if current > next
#             return False
#     return True   # if no violation found, it's sorted

# b = [1, 9, 3, 4, 45, 99]
# print(IsSorted(b))  # ✅ True
    
    
#right rotate
# def rr(num):
#     n=len(num)
#     num=[num[-1]]+num[0:n-1]
#     print(num) 
    
    
# rr([1,2,3,4,5,6])
# move 0 to right 
# a=[1,0,2,3,4,0,0,7,9]
# def moveEnd(num):
#     n=len(num)
#     temp=[]
#     for i in range(0,n):
#         if num[i]!=0:
#             temp.append(num[i])
#     nz=len(temp)
#     for i in range (0,nz):
#         num[i]=temp[i]
#     for i in range(nz,n):
#         num[i]=0
#     print(num)              
    
# moveEnd(a)    
  
num1 = [1, 1, 2, 3, 4, 5, 7]
num2 = [1, 2, 3, 6, 7, 7, 8]

def merge(num1, num2):
    n = len(num1)
    m = len(num2)
    i, j = 0, 0
    result = []

    while i < n and j < m:
        if num1[i] <= num2[j]:
            if len(result) == 0 or result[-1] != num1[i]:
                result.append(num1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != num2[j]:
                result.append(num2[j])
            j += 1        

    while i < n:
        if len(result) == 0 or result[-1] != num1[i]:
            result.append(num1[i])
        i += 1

    while j < m:
        if len(result) == 0 or result[-1] != num2[j]:
            result.append(num2[j])
        j += 1

    return result

print(merge(num1, num2))
