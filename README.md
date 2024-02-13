# Práctica 2 - TCP
## Introducción
En esta práctica se ha desarrollado en Python un módulo para la implementación de un login mediante mensajes TCP.  Los datos de los login se guardarán en documentos .txt así como los usuarios conectados. Todo el código del juego se encuentra dentro de la carpeta **Entregable**
## Explicación del login
1. **Funciones empleadas**
    - `register_user(username, password)`: Esta función verifica que el nombre de usuario con el que se está intentando registrar no está ya en uso. Si no está en uso se añade el usuario y la contraseña a la base de datos. Si existe se le indica al usuario.
    - `login_user(username, password)`: Esta función verifica que el conjunto de usuario y contraseña se encuentran en la base de datos. De ser así se considera el login como un éxito
    - `add_connection(username, client_address)` y `add_connection(username, client_address)`: son las funciones que nos ayudan a mantener un registro de los usuarios que están conectados (hay loggeados) en ese momento.

2. **Parte del Cliente (cliente.ipynb)**
   - **Inicialización y Configuración:** Se establecen el server_address que define una tupla que especifica la dirección del servidor al que se desea conectar.
   - **Interacciones:** El usuario una vez conectado encuentra por pantalla los comandos que puede ejecutar:
       + **Register** Permite al usuario crear un par de usuario contraseña que le permitirá hacer login.
       + **Login** Permite al usuario usar sus credenciales para hacer login.
       + **Testconnections** Permite al usuario verificar si sigue conectado con el servidor.
       + **Exit** Te desconecta del servidor.
   - **Desconexiones:** Por temas de seguridad si en algunas de las interacciones se observa alguna anomalía (login fallido, registro fallido...) se desconectará al usuario del servidor por precaución.
  
3. **Parte del Servidor**
    - **Recepción de Solicitudes del Cliente:** El servidor espera solicitudes de los clientes para interactuar con las distintas bases de datos.
    - **Manejo de las solicitudes:** El servidor recibe la solicitud del cliente, invoca a la función correspondiente para manejar la solicitud y envía la respuesta al cliente.
  
## Ejecución del código 
1. Abre una terminal o línea de comandos en tu sistema.

2. Clona el repositorio con el siguiente comando:

    ```
    git clone https://github.com/202006359/Practica-2-TCP.git
    ```

3. Inicializa el servidor Jupyter Notebook desde Anaconda.
<img width="249" alt="image" src="https://github.com/202006359/Practica-1-UDP/assets/113789409/8347b6ac-c6fb-42b4-8620-f8b7634689c4">

  
4. Esto abrirá una ventana del navegador web con el panel de control de Jupyter Notebook. Desde aquí, dirigite a la proyecto Practica-1-UDP y picha en la carpeta "Entregable". A continuación, abre el archivo "servidor.ipynb" y "cliente.ipynb".

5. Ejecuta el código del servidor en Jupyter Notebook ejecutando todas las celdas de código en "servidor.ipynb".

6. Ejecuta el código del cliente en Jupyter Notebook ejecutando todas las celdas de código en "cliente.ipynb".

Una vez que hayas ejecutado ambos códigos, podrás interactuar con el servicio de login. 

## Capturas de pantalla
¡Es fundamental tener en cuenta las mayúsculas y minúsculas a la hora de escribir los comandos!
![image](https://github.com/202006359/Practica-2-TCP/assets/52907821/a2cb1ba7-2994-4458-bad2-25c5de63fe56)

![image](https://github.com/202006359/Practica-2-TCP/assets/52907821/9991a2bb-b594-49ae-bb0d-b6d247523dd5)
![image](https://github.com/202006359/Practica-2-TCP/assets/52907821/90e89efa-4b00-4e78-b079-8e9d307e57fd)
![image](https://github.com/202006359/Practica-2-TCP/assets/52907821/03ab05fd-c0e8-47dd-8a78-ebdbd91776e2)







