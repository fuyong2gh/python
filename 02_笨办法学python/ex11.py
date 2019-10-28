# end='' means not end the line with a newline character and go to the next line
print("How old are you?",end='')
age = input()# This age is string
kage=int(age) #age has been changed to int format data
print("How tall are you?",end='')
height = input()
print("How much do you weigh?",end='')
weigh =input()

print(f"So,you're {age} old, {height} tall and {weigh} heavy and the kage={kage}.")
