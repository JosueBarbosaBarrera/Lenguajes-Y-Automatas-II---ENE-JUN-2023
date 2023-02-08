# def s0(char, estado_actual):
#     if char == "a" and (estado_actual==0 or estado_actual==1):
#         estado_actual = 1
#     # elif char == "a" and estado_actual==1:
#     #     estado_actual = 1
#     else:
#         #return "error en s0"
#         print("error en s0")
#     return estado_actual

# def s1(char, estado_actual):
#     if char == "b" and (estado_actual==1 or estado_actual==2):
#         estado_actual = 2   
#     # elif char == "a" and estado_actual==1:
#     #     estado_actual = 2
#     else:
#         #return "error en s1"
#         print("error en s1")
#     return estado_actual

# def s2(char, estado_actual):
#     if char == "c" and (estado_actual==2 or estado_actual==3):
#         estado_actual = 3
#     # elif char == "a" and estado_actual==1:
#     #     estado_actual = 2
#     else:
#         #return "error en s1"
#         print("error en s2")
#     return estado_actual

# def s3(char, estado_actual):
#     if char == "d" and (estado_actual==3 or estado_actual==4):
#         estado_actual = 4
#     # elif char == "a" and estado_actual==1:
#     #     estado_actual = 4
#     else:
#         print("error en s3")
#     return estado_actual

# def s4(char, estado_actual):
#     if char == "e" and (estado_actual==4 or estado_actual==5):
#         estado_actual = 5
#     # elif char == "e" and estado_actual==5:
#     #     estado_actual = 4
#     else:
#         print("error en s4")
#     return estado_actual



def estado(char, estado_actual):
    # INICIO y primer f1 "0" to A
    if char == "a" and (estado_actual==0 or estado_actual==1):
        estado_actual = 1
    # backward B to A and backward "2" C to A
    elif char == "a" and (estado_actual == 2 or estado_actual == 3):
            estado_actual = 1
    # f1 A to B
    elif char == "b" and (estado_actual==0 or estado_actual==1 or estado_actual==2):
        estado_actual = 2
    # backward C to B
    elif char == "b" and estado_actual == 3:
            estado_actual = 2
    # f1 B to C
    elif char == "c" and (estado_actual==0 or estado_actual==2 or estado_actual==3):
        estado_actual = 3
    # backward D to C
    elif char == "c" and estado_actual == 4:
            estado_actual = 3
    # f1 C to D and f2 B to D
    elif char == "d" and (estado_actual==0 or estado_actual==2 or estado_actual==3 or estado_actual==4):
        estado_actual = 4
    
    # backward E to D
    elif char == "d" and estado_actual == 5:
            estado_actual = 4
    # f1 D to E
    elif char == "e" and (estado_actual==0 or estado_actual==4 or estado_actual==5):
        estado_actual = 5
    else:
        estado_actual = "error, cadena no aceptada"
    return estado_actual

entrada = "abcde"
# entrada = "edcba"
# entrada = "abde"
# entrada = "abca"

estado_actual = 0
print("Estado - Dato de entrada")
for char in entrada:
    if char == "a":
        estado_actual = estado(char, estado_actual)
        print(estado_actual, "  -  " , char)
    elif char == "b":
        estado_actual = estado(char, estado_actual)
        print(estado_actual, "  -  " , char)
    elif char == "c":
        estado_actual = estado(char, estado_actual)
        print(estado_actual, "  -  " , char)
    elif char == "d":
        estado_actual = estado(char, estado_actual)
        print(estado_actual, "  -  " , char)
    elif char == "e":
        estado_actual = estado(char, estado_actual)
        print(estado_actual, "  -  " , char)
    else:
        print("cadena no aceptada")
        break
print("fin")