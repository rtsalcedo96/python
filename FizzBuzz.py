#FizzBuzz Code Exercise
for num1 in range(0,101):
    if num1 %3 == 0 and num1 %5 == 0:
        print('FizzBuzz')
    elif num1 %3 == 0:
        print('Fizz')
    elif num1 %5 == 0:
        print('Buzz')
    else:
        print(num1)
