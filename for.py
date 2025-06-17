#1. Print all numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#----------------------------------------------------------
#2.Print all even numbers between 1 and 20 using a for loop.
for i in range(1,21):
    if i%2==0:
        print(i)

#--------------------------------------------------------
#3.Print the square of numbers from 1 to 5.
for i in range(1,6):
    print(i**2) 

#--------------------------------------------------------\
#4.Calculate and print the sum of numbers from 1 to 10.
sum =0
for i in range(1,11):
   # print(sum+1)
    sum+=i
    print("sum: ",sum)

#-------------------------------------------------------
#5.Print the multiplication table of 5 (from 5×1 to 5×10).
n=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} × {i} = {n * i}")

#--------------------------------------------------------
#6.Print all odd numbers between 1 and 15.
print("The odd mubers are:")
for i in range(1,16,2):
    print(i)
#---------------------------------------------------------
#7.Print the cubes of numbers from 1 to 7
for i in range(1,8):
    print(f"the cube of {i} is {i**3}")
#-----------------------------------------------------
#8.Print numbers from 10 to 1 in reverse order.
for i in range(10,0,-1):
    print(i)
#-----------------------------------------------------
#9.Count how many numbers between 1 and 50 are divisible by 7.
count=0
for i in range(1,51):
    if i%7==0:
        count+=1
print(f"Total numbers divisble by 7 between 1 to 50: {count}")
#----------------------------------------------------
#10.Print the factorial of a number (e.g., 5!) using a for loop.
n=int(input("Enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f"The factorial of {n} is {factorial}")