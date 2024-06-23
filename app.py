# Etapa 3
import mysql.connector

class Catalogo:

    def __init__(self, host, user, password, database):

        self.conn = mysql.connector.connect(
          host=host,
          user=user,
          password=password,
          database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS destinos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255), 
            estadia VARCHAR (255)
            fecha VARCHAR (255))''')

        self.conn.commit()

    """Agregamos un nuevo paquete turístico a la base de datos, para ello necesitamos
      los parámetros que describen las características del paquete que agregamos."""
    def agregarPaqTuris(self, descripcion, cantidad, precio, imagen, estadia, fecha):
      sql = "INSERT INTO destinos (descripcion, cantidad, precio, imagen_url, estadia, fecha)VALUES (%s, %s, %s, %s, %s,%s)" 
      valores = (descripcion, cantidad, precio, imagen,estadia,fecha)
      self.cursor.execute(sql,valores) 
      self.conn.commit()
      return self.cursor.lastrowid
    
    # Consultamos un paquete t. a partir de su código.
    def consultarPaqTuris(self, codigo):
       self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
       return self.cursor.fetchone()
    
    # Actualizamos los datos de un paquete específico en la base de datos a partir de su código.
    def modificarPaqTuris(self, codigo, nuevaDescripcion, nuevaCantidad, 
    nuevoPrecio, nuevaImagen, nuevaEstadia, nuevaFecha):
      sql = "UPDATE destinos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, estadia = %s, fecha = %s WHERE codigo = %s"
      valores = (nuevaDescripcion, nuevaCantidad, nuevoPrecio, nuevaImagen, nuevaEstadia, nuevaFecha, codigo)
      self.cursor.execute(sql, valores)
      self.conn.commit()
      return self.cursor.rowcount > 0
    
    #Mostramos los datos de un paquete a partir de su código.
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
            print("Producto no encontrado.")

    #Mostramos todos los paquetes turísticos de la base de datos.
    def listarDestinos(self):
         self.cursor.execute("SELECT * FROM destinos")
         destinos = self.cursor.fetchall()
         return destinos
    
    # Eliminamos un paquete de la tabla a partir de su código.
    def eliminarPaqTuris(self, codigo):
        self.cursor.execute(f"DELETE FROM destinos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    
 # Programa principal

catalogo = Catalogo(host='localhost', user='root', password='', database='viajes')

# Agregamos paquetes turísticos a la tabla destinos
"""catalogo.agregarPaqTuris(1,"Córdoba,Argentina",40,450000,"Córdoba.png","5 noches","15/07/24 al 19/07/24")
   catalogo.agregarPaqTuris(2,"Mendoza,Argentina",30, 500000, "Mendoza.png","7 noches","15/07/24 al 21/07/24")
   catalogo.agregarPaqTuris(3,"Buenos Aires,Argentina",50, 450000, "Buenos Aires.png","5 noches","15/07/24 al 19/07/24")
   catalogo.agregarPaqTuris(4,"Bariloche,Argentina",60, 800000, "Bariloche.png","7 noches","15/07/24 al 21/07/24")
   catalogo.agregarPaqTuris(5,"Cataratas del Iguazú,Argentina",60,300000, "Cataratas del Iguazú.png","3 noches","15/07/24 al 17/07/24")"""

# Consultamos un paquete y lo mostramos
"""codPaqTuris = int(input("Ingrese el código del paquete turístico: "))
   paqTuris = catalogo.consultarPaqTuris(codPaqTuris)
    if paqTuris:
           print(f"Paquete turístico encontrado: {paqTuris['codigo']} - {paqTuris['descripcion']}")
    else:
          print(f'Paquete turístico {codPaqTuris} no encontrado.')"""

#Modificamos un paquete y lo mostramos
"""catalogo.mostrarPaqTuris(1)
   catalogo.modificarPaqTuris(1,"Córdoba,Argentina",40,5000000,"Córdoba.png","6 noches","15/07/24 al 20/07/24") # modificamos precio, estadia y fecha
   catalogo.mostrarPaqTuris(1)"""

#Listar paquetes turísticos (Todos)
#destinos = catalogo.listarDestinos()
#for paqTuris in destinos:
      #print (paqTuris)

# Eliminamos un paquete
#catalogo.eliminarPaqTuris(2)
#destinos = catalogo.listarDestinos()
#for paqTuris in destinos:
    #print (paqTuris)
#catalogo.listarDestinos()


















        


        
        

