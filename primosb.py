a=int(input("ingrese numero a"))
div=0
i=0


while i<a:
    i=i+1
    if a%i==0:
        div=div+1
if div>2:
    print("no es primo")
else:
    print("es primo")
