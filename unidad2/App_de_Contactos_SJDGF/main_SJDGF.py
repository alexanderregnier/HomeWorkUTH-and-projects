'''
Práctica: App_de_contactos
Autor: Sadrach Juan Diego Garcia Flores
Grupo: TIDS2-2
Fecha: 12-Feb-2024
'''
from mis_funciones import *
from cls_archivo_JSON import *

def Main():
    # Declarar Objetos aquí
    datos = []
    archivo = ArchivoJSON("Contactos.json") 
    Cls()

    # Validar el archivo aquí
    if archivo.Existe():
        datos = archivo.TomarContenido()
        print(f"Hay {len(datos)} contactos en el archivo '{archivo.nombre}'.")
        len(datos)
        if len(datos) > 0: print("sus datos han sido cargados.")
        pausa()

    else:
        Respuesta = input(f"El archivo '{archivo.nombre}' no existe. ¿Desea crearlo? (S/N)")
        if Respuesta.upper()[0] == 'S':
            archivo.CrearNuevo()
            print(f"El archivo '{archivo.nombre}' ha sido creado")
        else:
            exit("\n El programa ha finalizado.")
            print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ")
            print("   /////////             //          ////      ////    //////////            ////////    //             //   //////////    //////     ")
            print(" ///                   //  //        //  //  //  //    //                  ///      ///   //          //     //           //    //    ")
            print(" ///                 //      //      //    //    //    ///////            ///        ///   //       //       ///////      //    //    ")
            print(" ///      ///       ////////////     //          //    //                 ///        ///    //     //        //           //////      ")
            print(" ////      ///    //           //    //          //    //                  ///     ///       //  //          //           //    //    ")
            print("  //////////     //             //   //          //    ///////////          ////////          ////           ///////////  //     //   ")
            print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ")

    # Ciclo para el menú aquí
    while True:
        Cls()
        print("——————— MENÚ DE OPCIONES ———————")
        print("1.- Mostrar lista de contactos.")
        print("2.- Buscar un contacto.")
        print("3.- Agregar un contacto.")
        print("4.- Eliminar un contacto.")
        print("5.- SALIR.")
        opcion = leer_entero("\nTeclee la opción deseada: ")
        match opcion:
            case 1:     # LISTA
                
                print("\n─────────────────── Lista de contactos ───────────────────")
                datos = archivo.TomarContenido()
                if datos == []:
                    print(f"En el archivo '{archivo.nombre}' no hay datos")
                    BeepError()
                else:
                    print("Nombre:              Telefono:    Email:")
                    print("──────────────────────────────────────────────────────────")
                    for reg in datos:
                        print(f"{reg['nombre']:<20} {reg['teléfono']:<12} {reg['email']}")
                    print("══════════════════════════════════════════════════════════")
                pausa()
            
            case 2:     # BÚSQUEDA
                Cls()
                print("\n──────────────────────── Busqueda ────────────────────────")
                nombre = input("introduce el nombre del contacto: ").strip()
                encontrado = False
                if nombre != "":
                    print("Nombre:              Telefono:    Email:")
                    print("──────────────────────────────────────────────────────────")
                    for reg in datos:
                        if str(reg['nombre']).__contains__(nombre):
                            print(f"{reg['nombre']:<20} {reg['teléfono']:<12} {reg['email']}")
                    print("══════════════════════════════════════════════════════════")
                    # if encontrado == False:
                    if not encontrado :
                        print(f"***No se ha encontrado coincidientes para {nombre}.***\n")
                    pausa()

            case 3:     # AGREGAR
                Cls()
                print("\n───── Agregar ─ Introduzca los datos del contacto ─────")
                nombre   = input("nombre: ").strip()
                teléfono = input("Telefono: ").strip()
                email    = input("email: ").strip()
                if nombre == "" or teléfono == "":
                    BeepError()
                    print("\n***El nombre y el telefono son obligatorios. El contacto no se agregó.***")
                else:
                    dicc = {'nombre': nombre,'teléfono': teléfono,'email': email}
                    datos.append(dicc)
                    archivo.ActualizarContenido(datos)
                    print(f"\n El nombre contacto {nombre} ha sido agregado.")
                pausa()
            
            case 4:     # ELIMINAR
                Cls()
                print("\n──────────────────────── Eliminar ────────────────────────")
                indice = []
                for reg in datos:
                    indice.append(reg['nombre'])

                nombre = input("Introduzca el nombre del contacto a eliminar: ").strip()
                if nombre in indice:
                    resp = input(f"estas seguro de que quieres hacerun game over al ocntacto{nombre}? (S/N): ")
                    if resp.upper()[0] == 'S':
                        del datos [indice.index(nombre)]
                        archivo.ActualizarContenido(datos)
                        print(f"El contacto '{nombre}' le has dado cuello")
                else:
                    BeepError()
                    print(f"\n El contacto {nombre} no se encuentra.")
                pausa()

            case 5:     # Salir
                print("\nEl programa ha finalizado.")
                break   # Terminar el while-True
            
            case _:     # Opción no válida
                BeepError()
                print("La opción no es válida.")
                pausa()

#-------------------------------------------------------
Main()