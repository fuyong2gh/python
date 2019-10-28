#定义人种类
types_of_people = 10
#定义字符串x
x=f"There are {types_of_people} types of people."
#写单词
binary = 'binary'
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}." 
#打印出来
print (x)
print (y)

#熟悉f-string格式
print (f"I said : {x}.")
print (f"I also said: {y}.")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."

e = "a string with a right side"
#字符串的直接运算，再print显示出来
print (w+e)
