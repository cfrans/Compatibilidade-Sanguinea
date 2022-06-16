tipo_sanguineo = input("Informe seu tipo sanguíneo: ")

if tipo_sanguineo.lower() == 'a+':
    print("Você pode doar para A+ e AB+")
    print("Você pode receber de A+ A- O+ e O-")
elif tipo_sanguineo.lower() == 'a-':
    print("Você pode doar para A+ A- AB+ e AB- ")
    print("Você pode receber de A- e O-")
elif tipo_sanguineo.lower() == 'b+':
    print("Você pode doar para B+ e AB+ ")
    print("Você pode receber de B+ B- O+ e O-")
elif tipo_sanguineo.lower() == 'b-':
    print("Você pode doar para B+ B- AB+ e AB- ")
    print("Você pode receber de B- e O-")
elif tipo_sanguineo.lower() == 'ab+':
    print("Você pode doar para AB+ ")
    print("Você pode receber de todos os tipos")
elif tipo_sanguineo.lower() == 'ab-':
    print("Você pode doar para AB+ e AB- ")
    print("Você pode receber de A- B- AB- e O-")
elif tipo_sanguineo.lower() == 'o+':
    print("Você pode doar para A+ B+ AB+ e O+ ")
    print("Você pode receber de O+ e O-")
elif tipo_sanguineo.lower() == 'o-':
    print("Você pode doar para todos os tipos ")
    print("Você pode receber de O-")
else:
    print("Tipo sanguíneo não reconhecido.")



