a=int(input("ingrese numero a"))
div=0

for i in range (1,a+1):
    if a%i==0:
        div=div+1
if div>2:
    print("no es primo")
else:
    print("es primo")



