def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

while True:
    num = input("\nEnter The Number: ")
    print_factors(int(num))
