def tienda(*frutas, **marcas):
    print("frutas: ")
    for fruta in frutas:
        print(fruta)
    
    print("marcas")
    for pos, marca in marcas.items():
        print(pos, marca)
        
tienda("manzana", "pera", m1="mercadona", m2="condis")