users_file = "application_users.txt"
connections_file="current_connections.txt"
#DEFINICIONES DE LAS FUNCIONES
# Función para comprobar si un usuario ya existe
def user_exists(username): #Función que busca si un usuario ya está guardado.
    with open(users_file, 'r') as file:
        for line in file:
            if username == line.strip().split(':')[0]: #Se busca linea por linea si ecxiste alguna coincidencia
                return True # Si se encuentra una coincidencia se sale del bucle y se devuelve True
    return False #Si no se encuentra ninguna coincidencia se sale con un False

# Función para registrar un nuevo usuario
def register_user(username, password):
    if user_exists(username):#Se checkea paar que no haya nombres duplicados
        return False
    else:
        with open(users_file, 'a') as file:
            file.write(f'{username}:{password}\n') # Si no hay un duplicado se añade una nueva linea con username:password
        return True

# Función para validar el login de un usuario
def login_user(username, password):
    with open(users_file, 'r') as file:
        for line in file: 
            user, passw = line.strip().split(':')
            if username == user and password == passw:  # Para cada linea se compara si la combinacion de usuario 
                                                        # mas contraseña existe en alguna línea
                return True                             # si existe alguna coincidencia se hace login.
    return False                                        # si no existe alguna coincidencia no se hace login.

def add_connection(username, client_address):
    with open(connections_file, 'a') as file:
        file.write(f'{username}:{client_address}\n') # Si no hay un duplicado se añade una nueva linea con username:password
    return True
def remove_connection(username, client_address):
    with open(connections_file, 'r') as file:
        lines = file.readlines()  # Leer todas las líneas del archivo
    
    # Filtrar las líneas para eliminar la correspondiente a la conexión que queremos borrar
    with open(connections_file, 'w') as file:
        for line in lines:
            if line.strip() != f'{username}:{client_address}':
                file.write(line)
    return True