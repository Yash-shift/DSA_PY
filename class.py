
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
  
def selection_sort(num):
    l=len(num)
    for i in range(0,l):
        min_idx=i
        for j in range(i+1,l):
            if num[j]>num[min_idx] :
                
                min_idx=j
        num[i],num[min_idx]=num[min_idx],num[i]
        
    print(num)    
 
a=[7,3,2,9,4]
selection_sort(a)   
    
        
        



    