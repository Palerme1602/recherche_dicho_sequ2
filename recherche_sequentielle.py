tableau=[1,5,9,8,7,5,3,21]
element_n=int(input("entrer la valeur recherchee:"))
trouve = False
i=0
while i < len(tableau):
    if tableau[i] == element_n:
        trouve= True
        print("la valeur recherchee est a la position,",i)
        break
    i += 1
else:
    print("la valeur",element_n," est introuvable dans le tableau")



    