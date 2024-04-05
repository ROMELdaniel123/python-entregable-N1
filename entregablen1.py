a = int(input("ingrese un numero"))
b = int(input("ingrese un numero"))
c = int(input("ingrese un numero"))
if a>b>c: 
    print("el numero mayor es",a) 
    print("el numero menor es",c)
if b>a>c:
    print("el numero mayor es",b) 
    print("el numero menor es",c)
if a>c>b:
    print("el numero mayor es",a) 
    print("el numero menor es",b)
if c>a>b:
    print("el numero mayor es",c) 
    print("el numero menor es",b)
if c>b>a:
    print("el numero mayor es",c) 
    print("el numero menor es",a)
if b>c>a: 
    print("el numero mayor es",b) 
    print("el numero menor es",a)