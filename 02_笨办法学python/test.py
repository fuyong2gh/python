for i in range(1,10):
    a= 1
    while a<=i:
        print("{0}*{1}={2:*>3}".format(a,i,a*i),end='\t')
        a+=1
    print()
