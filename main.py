
from ctypes.wintypes import HLOCAL
import math

class Restaurant:
    def __init__(self, menu):
        self.menu = menu

    def pedir (self, delivery):
        print("Menú del restaurante.")
        print("")
        for i in self.menu:
            print(i + ". " + self.menu[i][0]+"   ---    $"+ str (self.menu[i][1]))
        num = str(input("digite el número de producto que desea pedir."))
        print("")
        print("Ha seleccionado el plato " + self.menu[num][0] + "que tiene un precio de $"+ str(self.menu[num][1]))
        self.descrip_plato(num)
        self.confirmation(num, delivery)
        self.agregar(num)
        
        

    def cobro_total (self, plato):

        a= self.menu[plato][1]
        print("El pago es igual a "+str(a))
    
    def descrip_plato (self, plato):
        print("El " + str(self.menu[plato][0])+ " trae: " + str(self.menu[plato][2]))
    
    def confirmation (self, plato, delivery):

        option = input("Digite 1 si quiere confirmar el pedido, 2 si quiere volver al menú anterior")
        if (option == "2"):
            self.pedir()
        else:
            print("El pago es igual a "+str(self.menu[plato][1] + delivery))
    
    def agregar (self, plato):
        option = input("Digite 1 si quiere agregar otro plato, 2 si quiere ver el total de pago")
        if (option == "2"):
            self.pedir()
        else:
            print("El pago es igual a "+str(self.menu[plato][1]))


class User:
    def __init__(self, name) -> None:
        self.name= name

    def login(self):
        name = input("ingrese su nombre")
        direccion = input("ingrese su dirección de residencia.")
        juntar = [name, direccion]
        return juntar


class Delivery: 

    def __init__(self) -> None:
        pass

    def hallar_dist (self,lat1,lon1,lat2,lon2):
        rad = math.pi/180
        self.dta_lat = lat2-lat1
        self.dta_lon = lon2-lon1
        radio = 6373.795477596
        in_raiz = (math.sin(self.dta_lat*rad/2)**2 + math.cos(lat1*rad)*math.cos(lat2*rad)*math.sin(self.dta_lon*rad/2)**2)
        dist = 2*radio*math.asin(math.sqrt(in_raiz))
        if (dist < 1.0): 
            precio_dom = 3000
        else:
            if(dist > 1.0 or math.dist < 3.0):
                precio_dom = 5000
            else:
                if(dist > 3.0):
                    precio_dom = 8000
        return precio_dom
