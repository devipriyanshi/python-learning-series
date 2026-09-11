###numbers = [10,20,30,40,50]
## number in numbers:
    ##print(number)

#numbers = [10,20,30,40,50]
#sum = 0
#for number in numbers:
   # sum = sum + number
#print(f"Sum: {sum}")

numbers = [10,20,30,40,50]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"Max: {max}")
