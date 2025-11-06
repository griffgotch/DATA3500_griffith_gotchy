#3.4

for i in range(2):
    for j in range(7):
        print('@', end = '')
    print()

#3.9

num = int(input("Ente ar 7-10 digit number: "))

divisor = 10 ** (len(str(num))-1)

while divisor > 0:
    digit = num // divisor
    print(digit)
    num %= divisor
    divisor //= 10


#3.11

total_gallons = 0
total_miles = 0

gallons = float(input("Enter the gallons used (-1 to end): "))

while gallons != -1:
    miles = float(input("Enter the miles driven: "))
    mpg = miles / gallons
    print(f"The miles/gallon for this tank was ", mpg)
    
    total_gallons += gallons
    total_miles += miles
    
    gallons = float(input("Enter the gallons used (-1 to end): "))

if total_gallons != 0:
    overall_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was ", overall_mpg)
else:
    print("No gallons were entered.")


#3.12

nums = int(input("Enter a five digit number: "))

first = nums//10000

last = nums%10

if first == last:
    print("Palindrome!!!!")
else:
    print("not palindrome")

#3.14

pi = 0
sign = 1
denominator = 1

count_314 = 0
count_3141 = 0

iteration_314 = None
iteration_3141 = None

for i in range(1, 3001):  
    term = 4 / denominator
    pi += sign * term
    sign *= -1           
    denominator += 2     

    approx = round(pi, 3)

    if round(pi, 2) == 3.14:
        count_314 += 1
        if count_314 == 2 and iteration_314 is None:
            iteration_314 = i
    else:
        count_314 = 0

    if approx == 3.141:
        count_3141 += 1
        if count_3141 == 2 and iteration_3141 is None:
            iteration_3141 = i
    else:
        count_3141 = 0

print("First iteration reaching 3.14 twice:", iteration_314)
print("First iteration reaching 3.141 twice:", iteration_3141)
