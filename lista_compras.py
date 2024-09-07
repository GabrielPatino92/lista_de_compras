lista_compras = []

while True:
    print("Bienvenido, a continuación se mostrará nuestro menú de opciones:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

    option = input("Por favor, ingrese una opción correcta entre el 1 y el 4: ")

    if option == "1":
        item = input("Por favor, ingrese el nombre del artículo: ")
        lista_compras.append(item)
        print(f"El artículo {item} ha sido agregado exitosamente")

    elif option == "2":
        print(lista_compras)
        indice = int(input("Por favor, digite el índice del artículo a eliminar: "))
        del lista_compras[indice]
        
    elif option == "3":
        print(lista_compras)

    elif option == "4":
        print("Gracias por usar nuestros servicios, hasta la próxima")

    else:
        print("Digite una opción correcta, por favor")