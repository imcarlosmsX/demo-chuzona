
from ctypes.wintypes import HLOCAL
import math

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.plata = 0

    def pedir (self, delivery):
        print("Menú del restaurante.")
        print("")
        for i in self.menu:
            print(i + ". " + self.menu[i][0]+"   ---    $"+ str (self.menu[i][1]))
        num = str(input("digite el número de producto que desea pedir."))
        print("")
        print("Ha seleccionado el plato " + self.menu[num][0] + "que tiene un precio de $"+ str(self.menu[num][1]))
        self.plata += self.menu[num][1]
        print (str(self.plata))
        self.descrip_plato(num)
        self.confirmation(num, delivery)
        
        
    def descrip_plato (self, plato):
        print("El plato" + str(self.menu[plato][0])+ " trae: " + str(self.menu[plato][2]))
    
    def confirmation (self, plato, delivery):

        option = input("Digite 1 si quiere confirmar el pedido, 2 si quiere volver al menú anterior y cancelar todo el pedido:      ")
        if (option == "2"):
            self.plata = 0
            self.pedir(delivery)
        else:
            self.agregar(plato, delivery)
    
    def agregar (self, plato, delivery):
        option = input("Digite 1 si quiere agregar otro plato, 2 si quiere ver el total de pago:     ")
        if (option == "1"):
            self.pedir(delivery)
            self.plata += self.menu[plato][1]
        else:
            print("El pago es igual a $"+ str(self.plata + delivery))


class User:
    def __init__(self, name):
        self.name= name

    def login(self):
        name = input("Ingrese su nombre:     ")
        direccion = input("Ingrese su dirección de residencia:      ")
        juntar = [name, direccion]
        return juntar


class Delivery: 

    def __init__(self, direcciones):
        self.direcciones = direcciones
    
    
    def hallar_dist (self, direc):

        lat1= self.direcciones[direc][0]
        lon1= self.direcciones[direc][1]
        lat2= self.direcciones["Unico"][0]
        lon2= self.direcciones["Unico"][1]

        ## haversine - halla la distancia entre las dos coordenadas.

        rad = math.pi/180
        self.dta_lat = lat2-lat1
        self.dta_lon = lon2-lon1
        radio = 6373.795477596
        in_raiz = (math.sin(self.dta_lat*rad/2)**2 + math.cos(lat1*rad)*math.cos(lat2*rad)*math.sin(self.dta_lon*rad/2)**2)
        dist = 2*radio*math.asin(math.sqrt(in_raiz))
        if (dist < 1.0): 
            precio_dom = 3000
        else:
            if( 1.0 > dist <  5.0):
                precio_dom = 6000
            else:
                if(dist > 5.0):
                    precio_dom = 8000
        return precio_dom
