numbers = "12,22,34,45,66"

for i in range(1,len(numbers)):
    if numbers[i] in '0123456789':
        print(i,end='')

print('\n---------')

for n in numbers:
    if n in '0123456789':
        print(n,end='')