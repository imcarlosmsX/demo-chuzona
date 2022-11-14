
import math, json
from numpy import double

#Clase encargada de realizar diferentes funciones dependiendo de la manipulación del diccionario que almacena el menú.
class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.plata = 0
        self.contador = 0
        self.lista = ""

#Esta funcion se encarga de recibir el numero del plato que va consumir el cliente.
    def pedir (self, delivery, name, lugar):
        print("Menú del restaurante.")
        print("")
        for i in self.menu:
            print(i + ". " + self.menu[i][0]+"   ---    $"+ str (self.menu[i][1]))
        print("")
        num = str(input("Digite el número de producto que desea pedir.      "))
        print("")
        self.plata += self.menu[num][1]
        self.descrip_plato(num)
        self.lista += self.menu[num][0] + " — "
        self.confirmation(num, delivery, name, lugar)
         
        
#Método encargado de que según el número que ingrese el cliente, se le suministre una breve descripción del plato seleccionado mediante
# el uso de diccionarios.
    def descrip_plato (self, plato):
        print("El plato " + str(self.menu[plato][0])+ " trae: " + str(self.menu[plato][2]))
    
#Método que le permite al usuario confirmar el pedido o regresar a las opciones anteriores sin guardar cambios.
    def confirmation (self, plato, delivery, name, lugar):

        print("")
        option = input("Digite 1 si quiere confirmar el pedido, 2 si quiere volver al menú anterior y cancelar todo el pedido:      ")
        if (option == "2"):
            self.plata = 0
            self.pedir(delivery, name, lugar)
        else:
            self.agregar(plato, delivery, name, lugar)
            

#Método que permite al usuario agregar otro plato a la cuenta o ver directamente su factura.
    def agregar (self, plato, delivery, name, lugar):
        print("")
        option = input("Digite 1 si quiere agregar otro plato, 2 si quiere ver el total de pago:     ")
        if (option == "1"):
            self.pedir(delivery, name, lugar)
            self.plata += self.menu[plato][1]
                    
        else:
            print("")
            print("El pago por el pedido es de: $"+ str(self.plata) + "\n Pago por domicilio: $" + str(delivery) + "\n Total: $", str(self.plata + delivery))

            comments = self.comments()
            file = open("info_clientes.txt", "a")
            file.write(name + ", " + str(self.lista) + ", " + str(self.plata + delivery) + ", " + lugar + ", " + comments)
            file.write("\n")
##Método que se usa para agregar comentarios extras al pedido y confirmarlo.
    def comments (self):
        print("")
        comentarios = input("Ingrese comentarios extras sobre su pedido y pulse ENTER para confirmarlo. (Ejem: Sin verdura, sin cebolla, etc.):        ")
        return comentarios


#Clase encargada de almacenar datos importantes de cada cliente, como su nombre y dirección para posteriormente ser enviados 
# a un archivo txt que contiene también el plato que seleccionó y el precio total de su pedido. 
class User:
    def __init__(self, name):
        self.name= name

    def login(self):
        name = input("Ingrese su nombre:     ")
        return name

#clase encargada de determinar la distancia entre el restaurante y la dirección ingresada por el usuario para poder determinar 
# un precio apropiado para el domicilio.
class Delivery: 

    def __init__(self) -> None:
        pass

#función encargada de determinar la distancia entre 2 coordenadas mediante el método de haversine.
    def hallar_dist (self, latitud, longitud):

        
        lat1= latitud
        lon1= longitud
        with open("settings.json") as settings:
            coords = json.load(settings)
            lat2= coords ["coords"][0]
            lon2= coords ["coords"][1]
        rad = math.pi/180
        self.dta_lat = lat2-lat1
        self.dta_lon = lon2-lon1
        radio = 6373.795477596
        in_raiz = (math.sin(self.dta_lat*rad/2)**2 + math.cos(lat1*rad)*math.cos(lat2*rad)*math.sin(self.dta_lon*rad/2)**2)
        dist = 2*radio*math.asin(math.sqrt(in_raiz))
        precio_dom = 0
        with open("settings.json") as settings:
            domis = json.load(settings)
            if (dist == 0):
                precio_dom = 0
            elif (dist <= 1.0): 
                precio_dom = domis ["domis"][0]
                
            elif( dist > 1 and dist < 5):
                precio_dom = domis ["domis"][1]
                    
            elif(dist >= 5.0 and dist <20):
                precio_dom = domis ["domis"][2]

            else:
                raise Exception("La distancia del pedido sobrepasa la capacidad de envío del restaurante.")

        return precio_dom
        
