print("main menu")
print("1.calculator")
print("2.area finder")
print("3.volume finder")
print("4.exit")
while True:
    opt=int(input("enter any one number which do you want"))
    if opt==1:
        print("1.add")
        print("2.multiply")
        print("3.divide")
        print("4.subtract")
        a=int(input("enter any one number which do you want"))
        if a==1:
            b=int(input("enter the first no. which you want to add"))
            c=int(input("enter the second no. which you want to add"))
            print(b+c)
        elif a==2:
            d=int(input("enter the first no. which you want to multiply"))
            e=int(input("enter the second no. which you want to multiply"))
            print(d*e)
        elif a==3:
            f=int(input("enter the first no. which you want to divide"))
            g=int(input("enter the second no. which you want to divide"))
            print(f/g)
        else:
            h=int(input("enter the first no. you want to subtract"))
            i=int(input("enter the second no. you want to subtract"))
            print(h-i)
     elif opt==2:
        print("1.square")
        print("2.rectangle")
        print("3.triangle")
        print("4.circle")
        j=int(input("enter the option which you want to do"))
        if j==1:
            k=int(input("enter your side"))
            print(k*k)
        elif j==2:
            l=int(input("enter your length"))
            m=int(input("enter your breadth"))
            print(l*m)
        elif j==3:
            n=int(input("enter base of triangle"))
            o=int(input("enter height of triangle"))
            print(12*n*o)
        else:
            p=int(input("enter the radius of the circle"))
            print(22/7*p*p))
     elif opt==3
        print("1.cyclinder")
        print("2.sphere")
        print("3.cone")
        q=int(input("enter the option which you want to do"))
