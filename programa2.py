frase_usuario=input("Ingrese una frase: ")
print("Evaluando...")
a,e,i,o,u=0,0,0,0,0

for j in frase_usuario:
    if j=='a'or j=='A'or j=='á':
        a+=1
    elif j=='e'or j=='E'or j=='é':
        e+=1
    elif j=='i'or j=='I'or j=='í':
        i+=1
    elif j=='o'or j=='O'or j=='ó':
        o+=1
    elif j=='u'or j=='U'or j=='ú':
        u+=1

print("Vocales A:",a)
print("Vocales E:",e)
print("Vocales I:",i)
print("Vocales O:",o)
print("Vocales U:",u)
print(f"Total de vocales: {(a+e+i+o+u)}")