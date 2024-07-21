texto = input("texto: ")
columnes = int(input("columnes: "))
salida = ""
for i in range(0, columnes):
  for j in range(i, len(texto)-i, columnes):
    print(texto[j])
