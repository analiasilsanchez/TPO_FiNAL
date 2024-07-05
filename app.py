<<<<<<< HEAD
#ETAPA 4 PARTE II: DESARROLLAR UNA API PARA NUESTRO CRUD
#Instalar con pip install : Flask, flask-cors, mysql-connector-python, Werkseug
=======
#--------------------------------------------------------------------
# Instalar con pip install Flask
>>>>>>> a1a0689158f8446d45f03e817254a2611df447e5
from flask import Flask, request, jsonify, render_template
from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------



app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

<<<<<<< HEAD
# Primero, establecemos una conexión sin especificar la base de  datos
   self.conn = mysql.connector.connect(
      host=host,
      user=user,
      password=password
    )
   self.cursor = self.conn.cursor()
# Intentamos seleccionar la base de datos
   try:  
       self.cursor.execute(f"USE {database}")
   except mysql.connector.Error as err:
# Si la base de datos no existe, la creamos
    if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        self.cursor.execute(f"CREATE DATABASE {database}")
        self.conn.database = database
    else:
        raise err

# Una vez que la base de datos está establecida, creamos la tabla si no existe
   self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS destinos (
           codigo INT AUTO_INCREMENT PRIMARY KEY,
           descripcion VARCHAR(255) NOT NULL,
           cantidad INT NOT NULL,
           precio DECIMAL(10, 2) NOT NULL,
           imagen_url VARCHAR(255),
           estadia VARCHAR(255),
           fecha VARCHAR(255))''')
   self.conn.commit()
# Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
   self.cursor.close()
   self.cursor = self.conn.cursor(dictionary=True)

#-----------------------------------------------------------------------------------------------
 def agregarPaqTuris(self, descripcion, cantidad, precio, imagen, estadia, fecha):
               
        sql = "INSERT INTO destinos (descripcion, cantidad, precio, imagen_url, estadia, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (descripcion, cantidad, precio, imagen, estadia, fecha)

        self.cursor.execute(sql, valores)        
=======
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS destinos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255), 
            estadia VARCHAR (255),
            fecha VARCHAR (255))''')
>>>>>>> a1a0689158f8446d45f03e817254a2611df447e5
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    """Agregamos un nuevo paquete turístico a la base de datos, para ello necesitamos
    los parámetros que describen las características del paquete que agregamos."""
    def agregarPaqTuris(self, descripcion, cantidad, precio, imagen, estadia, fecha):
        sql = "INSERT INTO destinos (descripcion, cantidad, precio, imagen_url, estadia, fecha)VALUES (%s, %s, %s, %s, %s,%s)" 
        """Los valores se pasan como parámetros separados a la consulta,serán tratados como datos
        y no como parte del código SQL.Los marcadores de posición %s son reemplazados por los
        valores reales de los parámetros cuando se ejecuta la consulta."""

        valores = (descripcion, cantidad, precio, imagen, estadia, fecha)
        self.cursor.execute(sql,valores) 
        self.conn.commit() #Guardo
        return self.cursor.lastrowid # Nos da el valor de la clave primaria generada automáticamente por la 
    #base de datos para la fila recién insertada.

    #----------------------------------------------------------------
<<<<<<< HEAD
 def consultarPaqTuris(self, codigo):
        # Consultamos un paquete turístico a partir de su código, destinos es la tabla de la base de datos(turismo)
=======
    # Consultamos un paquete t. a partir de su código.
    def consultarPaqTuris(self, codigo):
>>>>>>> a1a0689158f8446d45f03e817254a2611df447e5
        self.cursor.execute(f"SELECT * FROM destinos WHERE codigo = {codigo}")
        return self.cursor.fetchone() # devuelve un solo registro

    #----------------------------------------------------------------
    # Actualizamos los datos de un paquete específico en la base de datos a partir de su código.
    def modificarPaqTuris(self, codigo, nuevaDescripcion, nuevaCantidad, 
    nuevoPrecio, nuevaImagen, nuevaEstadia, nuevaFecha):
        sql = "UPDATE destinos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, estadia = %s, fecha = %s WHERE codigo = %s"
        valores = (nuevaDescripcion, nuevaCantidad, nuevoPrecio, nuevaImagen, nuevaEstadia, nuevaFecha, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit() #Guardo
        return self.cursor.rowcount > 0
        """rowcount() se usa para comprobar si una operación SQL afectó a alguna fila en la base de datos.
        Es una comparación que verifica si este número es mayor que cero, indica que al menos una fila fue afectada."""

    #----------------------------------------------------------------
    #Mostramos todos los paquetes turísticos de la base de datos.
    def listarDestinos(self):
        self.cursor.execute("SELECT * FROM destinos")
        destinos = self.cursor.fetchall() # Devuelve todas las filas en una consulta SQL
        return destinos

    #----------------------------------------------------------------
    # Eliminamos un paquete de la tabla a partir de su código.
    def eliminarPaqTuris(self, codigo):
        self.cursor.execute(f"DELETE FROM destinos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    # Mostramos los datos de un paquete a partir de su código.
    def mostrarPaqTuris(self, codigo): 
        paqTuris = self.consultarPaqTuris(codigo)
        if paqTuris:
            print("-" * 40)
            print(f"Código.....: {paqTuris['codigo']}")
            print(f"Descripción: {paqTuris['descripcion']}")
            print(f"Cantidad...: {paqTuris['cantidad']}")
            print(f"Precio.....: {paqTuris['precio']}")
            print(f"Imagen.....: {paqTuris['imagen_url']}")
            print(f"Estadía....: {paqTuris['estadia']}")
            print(f"Fecha......: {paqTuris['fecha']}")
            print("-" * 40)
        else:
            print("Paquete turístico no encontrado.")


#--------------------------------------------------------------------
# Programa Principal
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
<<<<<<< HEAD
catalogo = Catalogo(host='localhost', user='root', password='root', database='viajes')
=======
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')
>>>>>>> a1a0689158f8446d45f03e817254a2611df447e5
#catalogo = Catalogo(host='USUARIO.mysql.pythonanywhere-services.com', user='USUARIO', password='CLAVE', database='USUARIO$miapp')


# Carpeta para guardar las imagenes.
RUTA_DESTINO = './static/imagenes/'

#Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
#RUTA_DESTINO = '/home/USUARIO/mysite/static/imagenes'



#--------------------------------------------------------------------
# Listar todos los paquetes turísticos
#--------------------------------------------------------------------
#La ruta Flask /destinos con el método HTTP GET está diseñada para proporcionar los detalles de todos los paquetes almacenados en la base de datos.
#El método devuelve una lista con todos los paquetes turísticos en formato JSON.
@app.route("/destinos", methods=["GET"])
def listarDestinos():
    destinos = catalogo.listarDestinos()
    return jsonify(destinos)


#--------------------------------------------------------------------
# Mostrar un sólo paquete turístico según su código
#--------------------------------------------------------------------
#La ruta Flask /destinos/<int:codigo> con el método HTTP GET está diseñada para proporcionar los detalles de un paquete específico basado en su código.
#El método busca en la base de datos el paquete con el código especificado y devuelve un JSON con los detalles del paquete si lo encuentra, o None si no lo encuentra.
@app.route("/destinos/<int:codigo>", methods=["GET"])
def mostrarPaqTuris(codigo):
    destino = catalogo.consultarPaqTuris(codigo)
    if destino:
        return jsonify(destino), 201
    else:
        return "Paquete turístico no encontrado.", 404


#--------------------------------------------------------------------
# Agregar un Paquete turístico
#--------------------------------------------------------------------
@app.route("/destinos", methods=["POST"])
#La ruta Flask `/destinos` con el método HTTP POST está diseñada para permitir la adición de un nuevo paquete a la base de datos.
#La función agregarPaqTuris se asocia con esta URL y es llamada cuando se hace una solicitud POST a /destinos.
def agregarPaqTuris():
    #Recojo los datos del form
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    precio = request.form['precio']
    imagen = request.files['imagen']
    estadia = request.form['estadia']
    fecha = request.form['fecha']  
    nombre_imagen=""

    
    # Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
    nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extensión.
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

    nuevo_codigo = catalogo.agregarPaqTuris(descripcion, cantidad, precio, nombre_imagen, estadia, fecha)
    if nuevo_codigo:    
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))

        #Si el paquete se agrega con éxito, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 201 (Creado).
        return jsonify({"mensaje": "Paquete turístico agregado correctamente.", "codigo": nuevo_codigo, "imagen": nombre_imagen}), 201
    else:
        #Si el paquete no se puede agregar, se devuelve una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Internal Server Error).
        return jsonify({"mensaje": "Error al agregar paquete turístico."}), 500
    

#--------------------------------------------------------------------
# Modificar un paquete turístico según su código
#--------------------------------------------------------------------
@app.route("/destinos/<int:codigo>", methods=["PUT"])
#La ruta Flask /destinos/<int:codigo> con el método HTTP PUT está diseñada para actualizar la información de un paquete existente en la base de datos, identificado por su código.
#La función modificarPaqTuris se asocia con esta URL y es invocada cuando se realiza una solicitud PUT a /destinos/ seguido de un número (el código del paquete).
def modificarPaqTuris(codigo):
    #Se recuperan los nuevos datos del formulario
    nuevaDescripcion = request.form.get("nuevaDescripcion")
    nuevaCantidad = request.form.get("nuevaCantidad")
    nuevoPrecio = request.form.get("nuevoPrecio")
    nuevaEstadia = request.form.get("nuevaEstadia")
    nuevaFecha = request.form.get("nuevaFecha")
    
    
    # Verifica si se proporcionó una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        # Procesamiento de la imagen
        nombre_imagen = secure_filename(imagen.filename) #Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de archivos
        nombre_base, extension = os.path.splitext(nombre_imagen) #Separa el nombre del archivo de su extensión.
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" #Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.

        # Guardar la imagen en el servidor
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        
        # Busco el paquete guardado
        destino = catalogo.consultarPaqTuris(codigo)
        if destino: # Si existe el paquete...
            imagen_vieja = destino["imagen_url"]
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

            # Y si existe la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    
    else:
        # Si no se proporciona una nueva imagen, simplemente usa la imagen existente del paquete
        destino = catalogo.consultarPaqTuris(codigo)
        if destino:
            nombre_imagen = destino["imagen_url"]


    # Se llama al método modificarPaqTuris pasando el codigo del paquete y los nuevos datos.
    if catalogo.modificarPaqTuris(codigo, nuevaDescripcion, nuevaCantidad, nuevoPrecio, nombre_imagen, nuevaEstadia, nuevaFecha):
        
        #Si la actualización es exitosa, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
        return jsonify({"mensaje": "Paquete turístico modificado"}), 200
    else:
        #Si el paquete no se encuentra (por ejemplo, si no hay ningún paquete con el código dado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Paquete turístico no encontrado"}), 403



#--------------------------------------------------------------------
# Eliminar un paquete turístico según su código
#--------------------------------------------------------------------
@app.route("/destinos/<int:codigo>", methods=["DELETE"])
#La ruta Flask /destinos/<int:codigo> con el método HTTP DELETE está diseñada para eliminar un paquete específico de la base de datos, utilizando su código como identificador.
#La función eliminarPaqTuris se asocia con esta URL y es llamada cuando se realiza una solicitud DELETE a /destinos/ seguido de un número (el código del paquete).
def eliminarPaqTuris(codigo):
    # Busco el paquete en la base de datos
    destino = catalogo.eliminarPaqTuris(codigo)
    if destino: # Si el paquete existe, verifica si hay una imagen asociada en el servidor.
        imagen_vieja = destino["imagen_url"]
        # Armo la ruta a la imagen
        ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)

        # Y si existe, la elimina del sistema de archivos.
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimina el paquete del catálogo
        if catalogo.eliminarPaqTuris(codigo):
            #Si el paquete se elimina correctamente, se devuelve una respuesta JSON con un mensaje de éxito y un código de estado HTTP 200 (OK).
            return jsonify({"mensaje": "Paquete turístico eliminado"}), 200
        else:
            #Si ocurre un error durante la eliminación (por ejemplo, si el paquete no se puede eliminar de la base de datos por alguna razón), se devuelve un mensaje de error con un código de estado HTTP 500 (Error Interno del Servidor).
            return jsonify({"mensaje": "Error al eliminar el paquete turístico"}), 500
    else:
        #Si el paquete no se encuentra (por ejemplo, si no existe un paquete con el codigo proporcionado), se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado). 
        return jsonify({"mensaje": "Paquete turísco no encontrado"}), 404

#--------------------------------------------------------------------
if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)

























=======
    app.run(debug=True)
>>>>>>> a1a0689158f8446d45f03e817254a2611df447e5
