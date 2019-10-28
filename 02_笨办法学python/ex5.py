name = 'Fu Yong'
age = 30 #not a lie
height = 170 # cm
weight = 79.8 #Kg
eyes = 'black'
teeth = 'White'
hair = 'Black'

print (f"Let's talk about {name}.")

print ("Let's talk about {0}.".format(name))
print ("He's %d cm tall." % height)
print ("He's", height/100," m tall.")
print ("He's %d kg heavy.  After use round()" % round(weight))
print (f"He's {weight} kg heavy.show it with diffrent way")
print ("Actually that's not too heavy")
print("He's got %s eyes and %r hair." %(eyes,hair))
print("His teeth are usually %s depending on the coffee." % teeth)
# this line is tircky,try to get it exactly right
print("If I add %d, %d, and %d I get %d."%(age,height,weight,age+height+weight))
total=age+height+weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
