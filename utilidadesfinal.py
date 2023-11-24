from datetime import datetime
import mysql.connector 
import json
import re
def validar_tipo_sanguineo(sanguineo):
    '''
    Función que valida el tipo de sangre añadido por un usuario.
    '''
    while True:
        tipos_sanguineos_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        sanguineo = sanguineo.upper()
        if sanguineo in tipos_sanguineos_validos:
            return sanguineo
        else:
            print('-'*50)
            print('Tipo de sngre no válido')
            print('-'*50)
            sanguineo=input('Ingrese el tipo de sangre nuevamente\n')
def validar_correo(correo):
    '''
    Toma como parámetro de entrada un correo ingresado por un usuario y valida que sea coherente
    '''
    while True:
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(patron, correo):
            return correo
        else:
            print('-'*50)
            print('Correo inválido')
            print('-'*50)
            correo=input('Ingrese su correo nuevamente\n')
def validar(valor,tipo):
    '''
    Esta función tiene dos entradas, la primera es el input el cual se va a validar y la segunda es el tipo de input esperado, ya sea str o int
    '''
    while True:
        try:
            if tipo==int:
                if valor.isdigit():
                    return valor
                else:
                    print('-'*50)
                    print('Error, debe ingresar un número entero')
                    print('-'*50)
                    valor=input('Ingresar el valor nuevamente\n')
                    print('-'*50)
            elif tipo==str:
                if valor.isalpha():
                    return valor
                else:
                    print('-'*50)
                    print('Error, debe ingresar solo texto')
                    print('-'*50)
                    valor=input('Ingresar el valor nuevamente\n')
                    print('-'*50)
            else:
                return valor
        except:
            print('-'*50)
            print('Error, no ingresó el valor solicitado tipo'+str(tipo))
            Valor=input('Ingresar el valor nuevamente\n')
            print('-'*50)
def longitud(valor,longitud):
    '''
    Esta función tiene dos entradas, una variaable a la cual se va a verificar su longitud y un número de logitud deseado
    '''
    while True:
        if len(valor)==longitud:
            return valor
        else:
            print('-'*50)
            print('No cumple con la longitud pedida')
            print('-'*50)
            valor=input('Ingresar el valor nuevamente\n')
            validar(valor,int)
            print('-'*50)
def validar_fecha(fecha):
    '''
    verifica que el usuario ingrese una fecha válida en el formato pedido
    '''
    while True:
        try:
            fecha_formato = datetime.strptime(fecha, '%d/%m/%Y')            
            print("La fecha ingresada es válida")
            print('-'*50)
            return fecha        
        except ValueError:
            print("El formato de la fecha ingresada no es válido. Debe ingresarse en formato dd/mm/yyyy")
            print('-'*50)
            fecha=input('Ingrese una fecha con el formato dd/mm/yyyy\n')
def validar_hora(hora):
    '''
    verifica que el usuario ingrese una hora válida en el formato pedido
    '''
    while True:
        try:
            fecha_formato = datetime.strptime(hora, "%H:%M").time()           
            if fecha_formato < datetime.strptime("08:00", "%H:%M").time() or fecha_formato > datetime.strptime("18:00", "%H:%M").time():
                print("Error: Las citas solo se dan de 08:00 a 18:00 ")
                print('-'*50)
                hora=input('Ingrese una hora con el formato HH:MM\n')
                continue
            else:
                print("La hora ingresada es válida")
                print('-'*50)
                return hora        
        except ValueError:
            print("El formato de la hora ingresada no es válido. Debe ingresarse en formato HH:MM:SS")
            print('-'*50)
            hora=input('Ingrese una hora con el formato HH:MM\n')
def añadir_fila(table_name, data):
    '''
    Toma de parámetro el nombre de la taabla (str) y un diccionario 
    con las columnas y los valores de las columnas (datos de la nueva fila)
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    column_names = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql_query = f"INSERT INTO {table_name} ({column_names}) VALUES ({values})"
    cursor.execute(sql_query, list(data.values()))
    cnx.commit()
    print('-'*50)
    print("Datos añadidos correctamente")
    print('-'*50)
    cursor.close()
    cnx.close()
def user(a):
    '''
    esta función toma de parámetro la ruta de un archivo json y verifica que un usuario esté archivado en el json
    '''
    with open(a,'r') as archivo:
        datos=json.load(archivo)
        while True:
            print('-'*50)
            user=str(input('Ingrese su usuario de 10 dígitos por favor\n'))
            validar(user,int)
            longitud(user,10)
            print('-'*50)
            if user in datos.keys():
                while True:
                    clave=input('Ingrese su contraseña de 4 dígitos respectiva al usuario por favor\n')
                    b=int(validar(clave,int))
                    if b==datos[user]["password"]:
                        print('-'*50)
                        print('Le damos la bienvenida a {}'.format(datos[user]["user"]))
                        print('-'*50)
                        return True
                    else:
                        print('Contraseña incorrecta')
                        print('-'*50)
                        continue
            else:
                print('Ingrese un usuario válido')
                print('-'*50)
                continue
def eliminar_paciente():
    '''
    Ayuda a eliminar un paciente de forma rápida
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    documento = input("Digite el documento del paciente que quiere eliminar\n")
    validar(documento,int)
    longitud(documento,10)
    print('-'*50)
    delete = f"SELECT * FROM pacientes WHERE id = '{int(documento)}'"
    cursor.execute(delete)
    result = cursor.fetchone()
    if result is not None:
        delete = f"DELETE FROM pacientes WHERE id = '{int(documento)}'"
        cursor.execute(delete)
        print("El paciente ha sido borrado.") 
        print('-'*50)  
    else:
        print("El paciente no está en nuestra base de datos")
        print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def eliminar_medico():
    '''
    Ayuda a eliminar un médico de forma rápida
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    documento = input("Digite el documento del médico que quiere eliminar\n")
    validar(documento,int)
    longitud(documento,10)
    print('-'*50)
    delete = f"SELECT * FROM Medicos WHERE id = '{int(documento)}'"
    cursor.execute(delete)
    result = cursor.fetchone()
    if result is not None:
        delete = f"DELETE FROM Medicos WHERE id = '{int(documento)}'"
        cursor.execute(delete)
        print("El Médico ha sido borrado.")
        print('-'*50)   
    else:
        print("El Médico no está en nuestra base de datos")
        print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def buscar_pacientes():
    '''
    Ayuda a buscar a un paciente por su id
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor() 
    print('-'*50)       
    documento = input("Digite el documento del paciente a buscar\n")
    validar(documento,int)
    longitud(documento,10)
    print('-'*50)
    paciente = f"SELECT * FROM pacientes where id = {int(documento)}"
    cursor.execute(paciente)
    result = cursor.fetchone()
    if result:
        print(f'El paciente buscado fue: {result}')
        print('-'*50)
    else:
        print("El documento ingresado no está en el sistema.")
        print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def buscar_medico():
    '''
    Ayuda a buscar a un médico por su id
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()   
    print('-'*50)     
    documento = input("Digite el documento del médico a buscar\n")
    validar(documento,int)
    longitud(documento,10)
    print('-'*50)
    medico = f"SELECT * FROM Medicos where id = {int(documento)}"
    cursor.execute(medico)
    result = cursor.fetchone()
    if result:
        print(f'El medico buscado fue: {result}')
        print('-'*50)
    else:
        print("El documento ingresado no está en el sistema.")
        print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def editar_pacientes():
    '''
    Esta función ayuda a actualizar los parámetros que consideramos, se podrían cambiar de un paciente
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    documento=input("Digite el documento del paciente que quiere modificar\n")
    validar(documento,int)
    longitud(documento,10)
    print('-'*50)
    busqueda = f"SELECT * FROM pacientes where id = {int(documento)}"
    cursor.execute(busqueda)
    results = cursor.fetchone()
    while True:
        column = input("""
        Escoja el área que quiere cambiar:
        1. Nombre
        2. Apellido
        3. Género
        4. Dirección
        5. Email
        6.Teléfono
        """)
        print('-'*50)
        validar(column,int)
        if column == '1':
            print('-'*50)
            Change =input("Ingrese el Nombre nuevo\n")
            change=validar(Change,str)
            print('-'*50)
            search = f"UPDATE pacientes SET nombre = '{change}' WHERE id = '{int(documento)}'"
        elif column == '2':
            print('-'*50)
            Change = input("Ingrese el Apellido nuevo\n")
            change=validar(Change,str)
            print('-'*50)
            search = f"UPDATE pacientes SET apellido ='{change}' WHERE id = '{int(documento)}'"
        elif column == '3':
            print('-'*50)
            Change = input("Digite la Género nuevo\n")
            change=validar(Change,str)
            print('-'*50)
            search = f"UPDATE pacientes SET género = '{change}' WHERE id = '{int(documento)}'"
        elif column == '4':
            print('-'*50)
            change = input("Digite la Direciión nueva\n")
            print('-'*50)
            search = f"UPDATE pacientes SET dirección = '{change}' WHERE id = '{int(documento)}'"
        elif column == '5':
            print('-'*50)
            Change = input("Digite el Email nuevo\n")
            change=validar_correo(Change)
            print('-'*50)
            search = f"UPDATE pacientes SET email = '{change}' WHERE id = '{int(documento)}'"
        elif column == '6':
            print('-'*50)
            Change = input("Digite el Teléfono nuevo\n")
            change=validar(Change,int)
            print('-'*50)
            search = f"UPDATE pacientes SET teléfono = '{change}' WHERE id = '{int(documento)}'"
        else:
            print("Error. Escoja una opción válida para modificar")
            print('-'*50)
            continue                   
        print("\n")
        print("Paciente actualizado correctamente")
        print('-'*50)
        break   
    cursor.execute(search)
    cnx.commit()
    cursor.close()
    cnx.close()
def editar_medicos():
    '''
    Esta función ayuda a actualizar los parámetros que consideramos, se podrían cambiar de un médico
    '''
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    documento=input("Digite el documento del médico que quiere modificar\n")
    validar(documento,int)
    longitud(documento,10)
    print('-'*50)
    busqueda = f"SELECT * FROM Medicos where id = {int(documento)}"
    cursor.execute(busqueda)
    results = cursor.fetchone()
    while True:
        column = input("""
        Escoja el área que quiere cambiar:
        1. Nombre
        2. Apellido
        3. Especialidad
        4. Teléfono
        5. Email
        """)
        print('-'*50)
        validar(column,int)
        if column == '1':
            Change =input("Ingrese el Nombre nuevo\n")
            change=validar(Change,str)
            print('-'*50)
            search = f"UPDATE Medicos SET nombre = '{change}' WHERE id = '{int(documento)}'"
        elif column == '2':
            Change = input("Ingrese el Apellido nuevo\n")
            change=validar(Change,str)
            print('-'*50)
            search = f"UPDATE Medicos SET apellido ='{change}' WHERE id = '{int(documento)}'"
        elif column == '3':
            Change = input("Digite la especialidad nueva\n")
            change=validar(Change,str)
            print('-'*50)
            search = f"UPDATE Medicos SET especialidad = '{change}' WHERE id = '{int(documento)}'"
        elif column == '4':
            Change = input("Digite el Teléfono nuevo\n")
            change=validar(Change,int)
            print('-'*50)
            search = f"UPDATE Medicos SET teléfono = '{change}' WHERE id = '{int(documento)}'"
        elif column == '5':
            Change = input("Digite el Email nuevo\n")
            change=validar_correo(Change)
            print('-'*50)
            search = f"UPDATE Medicos SET email = '{change}' WHERE id = '{int(documento)}'"
        else:
            print("Error. Escoja una opción válida para modificar")
            continue                   
        print("\n")
        print("Médico actualizado correctamente")
        print('-'*50)
        break   
    cursor.execute(search)
    cnx.commit()
    cursor.close()
    cnx.close()           
def consultar_citas_pendientes():
    """
    Permite al usuario consultar las citas pendientes para un paciente o médico.
    1. Solicita al usuario que ingrese el número de documento.
    2. Verifica si el número de documento pertenece a un paciente.
    3. Si es un paciente, muestra las citas pendientes para ese paciente.
    4. Si no es un paciente, verifica si el número de documento pertenece a un médico.
    5. Si es un médico, muestra las citas pendientes para ese médico.
    6. Si no es ni paciente ni médico, muestra un mensaje indicando que el número de documento
    no corresponde a ningún registro.
    """
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    numero_documento = input("Ingrese el número de documento del paciente o médico: ")
    validar(numero_documento,int)
    longitud(numero_documento,10)
    print('-'*50)
    consulta_paciente = """
        SELECT nombre, apellido FROM pacientes
        WHERE id = %s
    """
    cursor.execute(consulta_paciente, (numero_documento,))
    paciente = cursor.fetchone()
    if paciente:
        print('-'*50)
        print(f"\nCitas pendientes para el paciente {paciente[0]} {paciente[1]}:")
        consulta_citas_paciente = """
            SELECT id_cita, Fecha, Hora, id_medico, Médico, Especialidad
            FROM citas 
            WHERE id_paciente = %s
        """
        cursor.execute(consulta_citas_paciente, (numero_documento,))
        citas_paciente = cursor.fetchall()
        if not citas_paciente:
            print("No hay citas pendientes para este paciente.")
            print('-'*50)
        else:
            for cita in citas_paciente:
                print('-'*50)
                print(f"ID Cita: {cita[0]}, Fecha: {cita[1]}, Hora: {cita[2]}, ID Médico: {cita[3]}, Nombre Médico: {cita[4]}, Especialidad: {cita[5]}")
                print('-'*50)
    else:
        consulta_medico = """
            SELECT nombre, apellido FROM Medicos
            WHERE id = %s
        """
        cursor.execute(consulta_medico, (numero_documento,))
        medico = cursor.fetchone()
        if medico:
            print('-'*50)
            print(f"\nCitas pendientes para el médico {medico[0]} {medico[1]}:")
            consulta_citas_medico = """
                SELECT id_cita, Fecha, Hora, id_paciente, Nombre
                FROM citas 
                WHERE id_medico = %s)
            """
            cursor.execute(consulta_citas_medico, (numero_documento,))
            citas_medico = cursor.fetchall()
            if not citas_medico:
                print("No hay citas pendientes para este médico.")
                print('-'*50)
            else:
                for cita in citas_medico:
                    print(f"ID Cita: {cita[0]}, Fecha: {cita[1]}, Hora: {cita[2]}, ID Paciente: {cita[3]}, Nombre Paciente: {cita[4]}")
        else:
            print("El número de documento no corresponde a un paciente ni a un médico.")
            print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def programar_cita():
    """
    Permite al usuario programar una cita con un médico.
    1. Muestra la lista de médicos disponibles.
    2. Solicita al usuario que elija un médico mediante su ID.
    3. Pide al usuario que ingrese la fecha y hora de la cita en el formato adecuado.
    4. Verifica la disponibilidad de la fecha y hora para el médico seleccionado.
    5. Si la fecha y hora están disponibles, solicita el número de documento del paciente.
    6. Verifica que el paciente exista en la base de datos.
    7. Si todo es correcto, agenda la cita y la guarda en la base de datos.
    """
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    cursor.execute("SELECT id, nombre, apellido, especialidad FROM medicos")
    medicos_disponibles = cursor.fetchall()
    print("Médicos disponibles:")
    for medico in medicos_disponibles:
        print(f"{medico[0]}. {medico[1]} {medico[2]} / {medico[3]}")
    print('-'*50)
    id_medico = input("Seleccione el ID del médico para la cita\n")
    validar(id_medico,int)
    longitud(id_medico,10)
    consulta_medico=f"SELECT * FROM Medicos WHERE id = {int(id_medico)}"
    cursor.execute(consulta_medico)
    medico_existente=cursor.fetchone()
    if medico_existente:
        print('-'*50)
        fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa)\n")
        Fecha=validar_fecha(fecha)
        print('-'*50)
        Hora = input("Ingrese la hora de la cita (hh:mm)\n")
        hora=validar_hora(Hora)
        print('-'*50)
        consulta_disponibilidad = """
            SELECT * FROM citas 
            WHERE id_medico = %s AND Fecha = %s AND Hora = %s
        """
        cursor.execute(consulta_disponibilidad, (id_medico, Fecha, hora))
        cita_existente = cursor.fetchone()
        if cita_existente:
            print("Lo siento, esa fecha y hora ya están ocupadas por otra cita.")
        else:
            numero_documento_paciente = input("Ingrese el número de documento del paciente\n")
            validar(numero_documento_paciente,int)
            longitud(numero_documento_paciente,10)
            consulta_paciente = f"SELECT * FROM pacientes WHERE id = {int(numero_documento_paciente)}"
            cursor.execute(consulta_paciente)
            paciente_existente = cursor.fetchone()
            if paciente_existente:
                data={'Fecha':Fecha,
                'Hora':hora,
                'id_paciente':numero_documento_paciente,
                'Nombre':paciente_existente[1],
                'Apellido':paciente_existente[2],
                'id_medico':medico_existente[0],
                'Médico':medico_existente[1],
                'Especialidad':medico_existente[3]}
                column_names = ', '.join(data.keys())
                values = ', '.join(['%s'] * len(data))
                sql_query = f"INSERT INTO citas ({column_names}) VALUES ({values})"
                cursor.execute(sql_query, list(data.values()))
                cnx.commit()
                print("Cita agendada con éxito.")
                print('-'*50)
            else:
                print("El paciente no existe en la base de datos.")
                print('-'*50)
    else:
        print('ID de médico incorrecto')
        print('-'*50)
    cursor.close()
    cnx.close()
def actualizar_cita():
    """
    Permite al paciente actualizar la fecha y hora de una cita.
    1. Solicita el número de documento del paciente.
    2. Verifica que el paciente exista en la base de datos.
    3. Muestra las citas pendientes para el paciente.
    4. Solicita el ID de la cita que se desea actualizar.
    5. Verifica que el ID de la cita pertenezca a citas pendientes para este paciente.
    6. Pide la nueva fecha y hora.
    7. Verifica que la nueva fecha y hora estén disponibles para el mismo médico.
    8. Si todo es correcto, actualiza la cita en la base de datos.
    """
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    numero_documento_paciente = input("Ingrese el número de documento del paciente\n")
    validar(numero_documento_paciente,int)
    longitud(numero_documento_paciente,10)
    print('-'*50)
    consulta_paciente = "SELECT * FROM pacientes WHERE id = %s"
    cursor.execute(consulta_paciente, (numero_documento_paciente,))
    paciente_existente = cursor.fetchone()
    if paciente_existente:
        consulta_citas_pendientes = """
            SELECT Fecha, Hora, id_medico
            FROM citas
            WHERE id_paciente = %s
        """
        cursor.execute(consulta_citas_pendientes, (paciente_existente[0],))
        citas_pendientes = cursor.fetchall()
        if not citas_pendientes:
            print("No hay citas pendientes para este paciente.")
            return False
        else:
            print("Citas pendientes:")
            for cita in citas_pendientes:
                print(f"Fecha: {cita[0]}, Hora: {cita[1]}, ID Médico: {cita[2]}")
                print('-'*50)
        fecha = input("Ingrese la nueva fecha de la cita (dd/mm/aaaa)\n")
        validar_fecha(fecha)
        print('-'*50)
        hora = input("Ingrese la nueva hora de la cita (hh:mm)\n")
        validar_hora(hora)
        print('-'*50)
        if fecha and hora:
            consulta_disponibilidad = """
                SELECT * FROM citas
                WHERE id_medico = %s AND Fecha = %s AND Hora = %s 
            """
            cursor.execute(consulta_disponibilidad, (citas_pendientes[0][2], fecha, hora))
            cita_existente = cursor.fetchone()
            if cita_existente:
                print("Error: La nueva fecha y hora ya están ocupadas por otra cita.")
            else:
                consulta_actualizar_cita = """
                    UPDATE citas
                    SET Fecha = %s, Hora = %s
                    WHERE id_paciente = %s
                """
                cursor.execute(consulta_actualizar_cita, (fecha, hora, numero_documento_paciente))
                cnx.commit()
                print("Cita actualizada con éxito.")
        else:
            print("Error: La nueva fecha y hora no son válidas.")
            print('-'*50)
    else:
        print("El paciente no existe en la base de datos.")
        print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def recordar_citas_paciente_por_id():
    """
    Muestra las citas programadas para un paciente.
    Args:
    - id_paciente (int): ID del paciente.
    """
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    id_paciente = input("Ingrese el ID del paciente\n")
    validar(id_paciente,int)
    longitud(id_paciente,10)
    print('-'*50)
    consulta_citas_paciente = """
        SELECT Fecha, Hora, id_medico, Médico, Especialidad
        FROM citas
        WHERE id_paciente = %s
    """
    try:
        cursor.execute(consulta_citas_paciente, (id_paciente,))
        citas_paciente = cursor.fetchall()
        if not citas_paciente:
            print("No hay citas programadas para este paciente.")
        else:
            print("Citas programadas para el paciente:")
            for cita in citas_paciente:
                print(f"Fecha: {cita[0]} Hora: {cita[1]}, ID Médico: {cita[2]}, Nombre Médico: {cita[3]}, Especialidad: {cita[4]}")
    except Exception as e:
        print(f"Error al recuperar las citas del paciente: {e}")
        print('-'*50)
    cnx.commit()
    cursor.close()
    cnx.close()
def cancelar_cita():
    SERVER = 'localhost'
    USER = 'informatica1'
    PASSWD = 'bio123'
    DB = 'info1'    
    cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB )
    cursor = cnx.cursor()
    print('-'*50)
    id_paciente=input('Ingrese el documento del paciente\n')
    validar(id_paciente,int)
    Id=longitud(id_paciente,10)
    print('-'*50)
    try:
        consulta = "DELETE FROM citas WHERE id_paciente = %s"
        datos = (Id,)
        cursor.execute(consulta, datos)
        cnx.commit()
        if cursor.rowcount > 0:
            print(f"Citas canceladas para el paciente con ID {Id}")
        else:
            print(f"No hay citas para el paciente con ID {Id} o ya han sido canceladas")
    except Exception as e:
        print(f"Error al cancelar cita: {e}")
    cursor.close()
    cnx.close()