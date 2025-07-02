
texto = "zzzrrzbr"

array = []
cont = 0

for i in range(0, len(texto)):
    print(i)
    if i < len(texto)-1:
        if texto[i] == texto[i+1]:
            cont +=1
        else:
            temp = [texto[i], cont+1]
            array.append(temp)
            cont = 0
    else:
        if texto[i] == texto[i-1]:
            cont += 1
            temp = [texto[i], cont+1]
            array.append(temp)
        else:
            temp = [texto[i], cont+1]
            array.append(temp)


print(array)

    
    