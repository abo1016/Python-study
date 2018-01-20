import hello
number = 23
guess = int(input('Enter an integer :'))

if guess == number:
    print('输入数字相等')
elif guess > number:
    print('输入数字大于等于')
else:
    print('输入数字小了')


print('Done')
