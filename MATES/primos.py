def get_divisible_minim_i_maxim(ronda):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for primo in primos:
        if ronda % primo == 0:
            return primo, ronda / primo
def get_divisibles_ronda(ronda):
    divisible_minim, divisible_maxim = get_divisible_minim_i_maxim(ronda)
    divisibles = [divisible_minim, divisible_maxim]
    divisor = divisible_minim
    while divisible_minim < divisible_maxim or divisible_minim != divisible_maxim:
        divisor += 1
        if ronda % divisor == 0:
            quocient = ronda / divisor
            divisibles.append(divisor)
            if quocient != divisor:
                divisibles.append(quocient)
            divisible_minim = divisor
            divisible_maxim = quocient
            
    return divisibles
    
    # divisibles = []
    # primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]    
    # if divident < 4:
    #     return divisibles
    # divisible_inicial = 1
    # divisible_final = divident
    # for primo in primos:
    #     if divident % primo == 0:
    #         divisible_inicial = primo
    #         divisible_final = divident / primo
    #         divisibles.extend(divisible_inicial, divisible_final)
    #         break
    
    # anterior_divisible = divisible_final
    # for divisor in range(divisible_inicial+1, divisible_final):
    #     quocient = divident / divisor
    #     if divisor not in divisibles and isinstance(quocient,int):
    #         divisibles.extend([divisor, quocient])
            
    
    
    # for i in range(len(primos)-1, -1, -1):
    #     primo = primos[i]
    #     if divident > primo and divident % primo == 0:
    #         print(primo)
    #         # multiple_primo = primo
    #         # factor = 1
    #         # while divident % multiple_primo == 0:
    #         #     divisibles.append(multiple_primo)
    #         #     factor += 1
    #         #     multiple_primo = primo * factor

print(get_divisibles_ronda(324))