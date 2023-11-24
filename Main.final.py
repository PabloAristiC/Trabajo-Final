import mysql.connector
import datetime
import json
import csv
from utilidadesfinal import *
cnx = mysql.connector.connect(user='root', password='bio123', host='127.0.0.1', database='info1')
cursor = cnx.cursor()
sql1 = '''CREATE TABLE IF NOT EXISTS Medicos(
    id int NOT NULL PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    apellido varchar(255) NOT NULL,
    especialidad varchar(255) NOT NULL,
    teléfono int,
    email varchar(255) NOT NULL
)'''
sql2 ='''CREATE TABLE IF NOT EXISTS Pacientes(
    id INT NOT NULL PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    nacimiento VARCHAR(255) NOT NULL,
    género VARCHAR(255) NOT NULL,
    sangre VARCHAR(255) NOT NULL,
    dirección VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    teléfono VARCHAR(255) NOT NULL
)'''
sql3 = '''CREATE TABLE IF NOT EXISTS citas(
    Fecha VARCHAR(255) NOT NULL PRIMARY KEY,
    Hora VARCHAR(255) NOT NULL,
    id_paciente INT NOT NULL,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    id_medico INT NOT NULL,
    Médico VARCHAR(255),
    Especialidad VARCHAR(255)
)'''
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cnx.commit()
cursor.close()
cnx.close()
from utilidadesfinal import *
usuarios='Administradores.json'
menu1 = ("""
        1. ingresar
        2. salir
        """)
menu2 = ("""
        1. Pacientes
        2. Medicos
        3. Gestion de citas
        4.salir
        """)
menu3 = ("""
        1. Ingresar un nuevo paciente
        2. Actualizar la información de un paciente
        3. Buscar un paciente
        4. Ver la información de todos los pacientes almacenados
        5. Eliminar un paciente
        6. salir
        """)
menu4 = ("""
        1. Ingresar un nuevo medico
        2. Actualizar la información de un medico
        3. Buscar un medico
        4. Ver la información de todos los medicos almacenados
        5. Eliminar un medico
        6. Salir
        """)
menu5 = ("""
        1. Programar cita
        2. Actualizar cita
        3. Cancelar cita
        4. Recordar cita
        5. salir
        """)
print('Bienvenido a el sistema de gestión de citas IPS Info1.')
while True :
    print('-'*50)
    print(menu1)
    print('-'*50)
    x = input("Ingrese 1 si desea ingresar ó 2 si quiere salir: \n")
    validar(x,int)
    if x == '1':
        a=user(usuarios)
        if a==True:
            while True:
                print('-'*50)
                print(menu2)
                print('-'*50)
                y = input("Ingrese una opción del menú: \n")
                validar(y,int)
                if y == '1':
                    while True:
                        print('-'*50)
                        print(menu3)
                        print('-'*50)
                        w = input("Ingrese una opción del menú\n")
                        validar(w,int)
                        if w == '1':
                            print('-'*50)
                            print('Ingrese la información del nuevo paciente')
                            print('-'*50)
                            documento=input('Ingrese el documento del nuevo paciente\n')
                            validar(documento,int)
                            Doc=longitud(documento,10)
                            print('-'*50)
                            nombre=input('Ingrese el nombre del nuevo paciente\n')
                            Nom=validar(nombre,str)
                            print('-'*50)
                            apellido=input('Ingrese el apellido del nuevo paciente\n')
                            Ap=validar(apellido,str)
                            print('-'*50)
                            nacimiento=input('Ingrese el nacimiento del paciente en formato dd/mm/yyyy\n')
                            Nacimiento=validar_fecha(nacimiento)
                            print('-'*50)
                            genero=input('Digite el género del paciente\n')
                            Gen=validar(genero,str)
                            print('-'*50)
                            sangre=input('Ingrese su tipo de sangre\n')
                            Sangre=validar_tipo_sanguineo(sangre)
                            print('-'*50)
                            direccion=input('Ingrese la dirección de vivienda\n')
                            print('-'*50)
                            email=input('Digite el email del paciente\n')
                            Email=validar_correo(email)
                            print('-'*50)
                            telefono=input('Agregue el teléfono del paciente\n')
                            Tel=validar(telefono,int)
                            print('-'*50)
                            data={'id':Doc, 
                                'Nombre':Nom,
                                'Apellido':Ap, 
                                'nacimiento':Nacimiento, 
                                'género':Gen, 
                                'sangre':Sangre, 
                                'dirección':direccion, 
                                'email':Email, 
                                'teléfono':Tel}
                            añadir_fila('pacientes',data)
                            pass                        
                        elif w == '2':
                            print('-'*50)
                            editar_pacientes()
                            print('-'*50)
                            pass                       
                        elif w == '3':
                            print('-'*50)
                            buscar_pacientes()
                            print('-'*50)
                            pass                       
                        elif w == '4':
                            cnx = mysql.connector.connect(user='root', password='bio123', host='127.0.0.1', database='info1')
                            cursor = cnx.cursor()
                            tabla = "SELECT * FROM pacientes"
                            cursor.execute(tabla)
                            result = cursor.fetchall()
                            pacientes=[]
                            for i in result:
                                print('-'*50)
                                print(f"""
                                    id: {i[0]}
                                    Nombre: {i[1]}
                                    Apellido: {i[2]} 
                                    nacimiento: {i[3]}
                                    Género: {i[4]} 
                                    Tipo De Sangre: {i[5]} 
                                    Dirección: {i[6]}
                                    Email: {i[7]}
                                    Teléfono: {i[8]}""")
                                pacientes.append(i)
                                print('-'*50)
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                            while True:
                                print('-'*50)
                                print('¿Quiere exportar la tabla de pacientes a un archivo CSV?\n1. Exportar a CSV\n2. Seguir')
                                print('-'*50)
                                menuCSV=input('Ingrese la opción a la que desea ingresar (1 ó 2)\n')
                                validar(menuCSV,int)
                                if menuCSV == '1':
                                    with open('Pacientes.csv','w') as z:
                                        writer=csv.writer(z, delimiter='\n')
                                        writer.writerow(pacientes)
                                        print('-'*50)
                                        z.close
                                        break
                                if menuCSV == '2':
                                    break
                                else:
                                    print('Ingrese un valor adecuado (1 ó 2)')
                                    pass                        
                        elif w == '5':
                            print('-'*50)
                            eliminar_paciente()
                            print('-'*50)
                            pass                                               
                        elif w == '6':
                            print('-'*50)
                            print("Gracias por entrar a la gestión de pacientes. Hasta luego.")
                            print('-'*50)
                            break                        
                        else:
                            print("Opcion incorrecta, ingrese una opcion válida del menú")
                            print('-'*50)    
                elif y == '2':
                    while True:
                        print('-'*50)
                        print(menu4)
                        print('-'*50)
                        z = input("Ingrese una opción del menú\n")
                        validar(z,int)
                        if z == '1':
                            print('-'*50)
                            print('Ingrese los datos del nuevo médico')
                            print('-'*50)
                            documento=input('Ingrese el documento del nuevo médico\n')
                            validar(documento,int)
                            Doc=longitud(documento,10)
                            print('-'*50)
                            nombre=input('Ingrese el nombre del nuevo médico\n')
                            Nom=validar(nombre,str)
                            print('-'*50)
                            apellido=input('Ingrese el apellido del médico\n')
                            Ap=validar(apellido,str)
                            print('-'*50)
                            especialidad=input('Ingrese la especialidad del médico\n')
                            Esp=validar(especialidad,str)
                            print('-'*50)
                            telefono=input('Ingrese el teléfono de contacto del médico\n')
                            TEL=validar(telefono,int)
                            print('-'*50)
                            email=input('Ingrese el email del médico\n')
                            Email=validar_correo(email)
                            print('-'*50)
                            datos={'id':Doc,
                                'nombre':Nom,
                                'apellido':Ap,
                                'especialidad':Esp,
                                'teléfono':TEL,
                                'email':Email}
                            añadir_fila('Medicos',datos)
                            pass                        
                        elif z == '2':
                            editar_medicos()
                            pass                        
                        elif z == '3':
                            buscar_medico()
                            pass                       
                        elif z == '4':
                            cnx = mysql.connector.connect(user='root', password='bio123', host='127.0.0.1', database='info1')
                            cursor = cnx.cursor()
                            tabla = "SELECT * FROM Medicos"
                            cursor.execute(tabla)
                            result = cursor.fetchall()
                            pacientes=[]
                            for i in result:
                                print('-'*50)
                                print(f"""
                                    id: {i[0]}
                                    nombre: {i[1]}
                                    apellido: {i[2]} 
                                    especialidad: {i[3]}
                                    teléfono: {i[4]}""")
                                pacientes.append(i)
                                print('-'*50)
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                            while True:
                                print('-'*50)
                                print('¿Quiere exportar la tabla de médicos a un archivo CSV?\n1. Exportar a CSV\n2. Seguir')
                                print('-'*50)
                                menuCSV=input('Ingrese la opción a la que desea ingresar (1 ó 2)\n')
                                validar(menuCSV,int)
                                if menuCSV == '1':
                                    with open('Medicos.csv','w') as z:
                                        writer=csv.writer(z, delimiter='\n')
                                        writer.writerow(pacientes)
                                        print('-'*50)
                                        z.close
                                        break
                                if menuCSV == '2':
                                    break
                                else:
                                    print('Ingrese un valor adecuado (1 ó 2)')
                                    pass
                            pass                        
                        elif z == '5':
                            eliminar_medico()
                            pass                        
                        elif z == '6':
                            print("Gracias por entrar. Hasta luego.")
                            print('-'*50)
                            break                       
                        else:
                            print("Opción incorrecta, ingrese una opción válida del menú")
                            print('-'*50)    
                elif y == '3':
                    while True:
                        print('-'*50)
                        print(menu5)
                        print('-'*50)
                        a = input("Ingrese una opción del menú: \n")
                        validar(a,int)
                        if a == '1':
                            programar_cita()
                            pass                                              
                        elif a == '2':
                            actualizar_cita()
                            pass                        
                        elif a == '3':
                            cancelar_cita()
                        elif a == '4':
                            recordar_citas_paciente_por_id()                            
                            pass                        
                        elif a == '5':
                            print("Gracias por entrar. Hasta luego.")
                            print('-'*50)
                            break                       
                        else:
                            print("Opción incorrecta, ingrese una opción valida del menú")
                            print('-'*50)    
                elif y == '4':
                    print("Gracias por entrar. Hasta luego.")
                    print('-'*50)
                    break                
                else:
                    print("Opción inválida, ingrese otra opción del menú")
                    print('-'*50)
    elif x == '2':
        print('-'*50)
        print('-'*50)
        print('-'*50)
        print("Gracias por contar con nosotros para sus gestiones de salud, vuelva pronto.")
        print('-'*50)
        print('-'*50)
        print('-'*50)
        break
    else:
        print("Opción inválida, ingrese 1 ó 2.")
        print('-'*50)