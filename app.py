# Pasamos de funciones a OBJETOS
# ----------------------------------------------------------------
#Definimos una clase
#----------------------------------------------------------------

class Catalogo:

    #Definimos una lista para almacenar los paquetes turísticos.
    #Es una lista de paquetes turísticos(destinos)
    destinos = []
    #----------------------------------------------------------------------------------
    #Método para agregar un paquete turístico.
    #----------------------------------------------------------------------------------

    def agregarPaqTuris(self,codigo,descripcion,cantidad, precio, imagen,estadia,fecha):

                    """
                    Parámetros:
                    -código: int, código numérico del paquete turístico.
                    -descripción: str, descripción del destino.
                    -cantidad:int,cantidad de paquetes turísticos disponibles.
                    -precio: float, precio de venta.
                    -imagen: str, nombre de la imagen(destino).
                    -estadía: str, duración de estadía.
                    -fecha : str, fechas de ida y vuelta.

                    Retorna:
                    -bool: True si se agregó el paquete turístico,False si ya existe un destino con el mismo código.
                    """
                    #Verificamos si ya existe un paquete/ destino con el mismo código

                    if self.consultarPaqTuris(codigo):
                      print ("Paquete turístico existente.")
                      return False # ya existe un destino con el mismo código.
                    
                    else:
                        #Creamos un diccionario con los datos del destino

                     nuevoPaqTuris = {
                        "codigo": codigo,
                        "descripcion": descripcion,
                        "cantidad":cantidad,
                        "precio": precio,
                        "imagen": imagen,
                        "estadia": estadia,
                        "fecha": fecha
                    }
                    
                    #Agregamos el paquete turístico al array (destinos)
                    self.destinos.append(nuevoPaqTuris)
                    return True #El paquete se agregó exitosamente.

    #----------------------------------------------------------------------------------
    # Método para consultar si un paquete existe en el arreglo, a partir de su código
    #----------------------------------------------------------------------------------

    def consultarPaqTuris(self,codigo):
                      """
                     Consulta un paquete/destino a partir de su código y devuelve sus datos.
                     Parámetros:
                     -codigo: int, código numérico del producto.
                      Retorna:
                     -dict: datos del destino en forma del diccionario,o False si no se encontró el destino.
                    """
                 #recorremos la lista de destinos.

                      for paqTuris in self.destinos:
                            #Si el código existe
                            if paqTuris["codigo"] == codigo:
                             return paqTuris
                    #Si el bucle finaliza sin encontrar el paquete turístico
                      return False
                        
    #------------------------------------------------------------------------
    # Método para modificar datos de un paquete, a partir de su código
    #------------------------------------------------------------------------
    def modificarPaqTuris(self,codigo,nuevaDescripcion,nuevaCantidad,nuevoPrecio,
                                            nuevaImagen,nuevaEstadia,nuevaFecha):
                            
                    """
                    Modifica los datos de un destino a partir de su código:
                    Parámetros:
                    -código: int, código numérico del paquete turístico.
                    -nuevaDescripcion: str, nueva descripción del destino.
                    -nuevaCantidad:int, nueva cantidad de paquetes turísticos.
                    -nuevoPrecio: float,nuevo precio de venta.
                    -nuevaImagen: str,nueva imagen del paquete(destino).
                    -nuevaEstadia: str, nueva duración de estadía.
                    -nuevaFecha : str,nueva fecha (de ida y vuelta).
                    """ 
                    
                    #Recorremos la lista de destinos...
                    for paqTuris in self.destinos:
                        if paqTuris["codigo"] == codigo:
                         paqTuris["descripcion"] = nuevaDescripcion
                         paqTuris["cantidad"] = nuevaCantidad
                         paqTuris["precio"] = nuevoPrecio
                         paqTuris["imagen"] = nuevaImagen
                         paqTuris["estadia"] = nuevaEstadia
                         paqTuris["fecha"] = nuevaFecha

                         return True
                    #Si llegamos hasta aquí, el paquete turístico no existe
                    return False
    #-------------------------------------------------------------------
    # Método para obtener un listado de los paquetes en pantalla
    #-------------------------------------------------------------------

    def listarPaqTuris(self):
                    
    
    # Muestra en pantalla un listado de los destinos existentes.Recorremos la lista. 
                    
                    print("-"*50)
                    for paqTuris in self.destinos:
                    #Mostramos los datos de cada destino
                     print(f"Código..........:    {paqTuris["codigo"]}")
                     print(f"Descripción.....:    {paqTuris["descripcion"]}")
                     print(f"Cantidad........:    {paqTuris["cantidad"]}")
                     print(f"Precio..........:    {paqTuris["precio"]}")
                     print(f"Imagen..........:    {paqTuris["imagen"]}")
                     print(f"Estadía.........:    {paqTuris["estadia"]}")
                     print(f"Fecha...........:    {paqTuris["fecha"]}")
                     print("-"*50)

    #------------------------------------------------------------
    # Método para eliminar un paquete, a partir de su código.
    #------------------------------------------------------------
    def eliminarPaqTuris(self,codigo):
                        """
                    Elimina un paquete a partir de su código:
                    Parámetro:
                    -código: int, código numérico del paquete turístico.
                    """
                    #Recorremos la lista de destinos/paquetes

                        for paqTuris in self.destinos:
                            if paqTuris["codigo"] == codigo:
                             print (f"Paquete turístico {paqTuris["descripcion"]} eliminado.")
                             self.destinos.remove(paqTuris)
                        
                            return True
                        #Si llegamos hasta aquí, el paquete no existe
                        return False
                    
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                            EJEMPLOS DE USO DE MÉTODOS

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

"""catalogo = Catalogo()

                    
            # Agregamos paquetes turísticos a la lista
catalogo.agregarPaqTuris(1,"Salta,Argentina",40,450000,"Salta.png","5 noches","15/07/24 al 19/07/24")
catalogo.agregarPaqTuris(2,"San Rafael,Argentina",30, 500000, "San Rafael.png","7 noches","15/07/24 al 21/07/24")
catalogo.agregarPaqTuris(3,"Mar del Plata,Argentina",50, 450000, "Mar del Plata.png","5 noches","15/07/24 al 19/07/24")
catalogo.agregarPaqTuris(4,"Bariloche,Argentina",60, 800000, "Bariloche.png","7 noches","15/07/24 al 21/07/24")
catalogo.agregarPaqTuris(5,"Cataratas del Iguazú,Argentina",60,300000, "Cataratas del Iguazú.png","3 noches","15/07/24 al 17/07/24")
            
            #Consulta de paquetes turísticos
                
paqTuris = catalogo.consultarPaqTuris(1)
if paqTuris:
                    print(f"Paquete turístico encontrado:{paqTuris["descripcion"]}")
else:
                    print("Paquete turístico no encontrado.")

            #Modificación de un destino/paquete                 
catalogo.modificarPaqTuris(1,"Salta,Argentina",50,460000,"Salta.png","5 noches","15/07/24 al 19/07/24")

            #Listado de paquetes turísticos
catalogo.listarPaqTuris()

            #Eliminación de paquete turístico
print()
catalogo.eliminarPaqTuris(1)
print()
catalogo.listarPaqTuris()"""

















        


        
        

