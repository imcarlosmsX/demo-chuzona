
import math, json
from numpy import double

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.plata = 0
        self.contador = 1

    def pedir (self, delivery):
        print("Menú del restaurante.")
        print("")
        for i in self.menu:
            print(i + ". " + self.menu[i][0]+"   ---    $"+ str (self.menu[i][1]))
        print("")
        num = str(input("Digite el número de producto que desea pedir.      "))
        print("")
        self.plata += self.menu[num][1]
        self.descrip_plato(num)
        x = self.confirmation(num, delivery)
        info = [self.menu[i][0], x + delivery]
        return info
        
        
    def descrip_plato (self, plato):
        print("El plato " + str(self.menu[plato][0])+ " trae: " + str(self.menu[plato][2]))
    
    def confirmation (self, plato, delivery):

        print("")
        option = input("Digite 1 si quiere confirmar el pedido, 2 si quiere volver al menú anterior y cancelar todo el pedido:      ")
        if (option == "2"):
            self.plata = 0
            self.pedir(delivery)
        else:
            x = self.agregar(plato, delivery)
            return x
    
    def agregar (self, plato, delivery):
        print("")
        option = input("Digite 1 si quiere agregar otro plato, 2 si quiere ver el total de pago:     ")
        if (option == "1"):
            self.pedir(delivery)
            self.plata += self.menu[plato][1]
            self.contador = self.contador + 1
            return self.plata
            
        else:
            print("")
            print("El pago por el pedido es de: $"+ str(self.plata) + "\n Pago por domicilio: $" + str(delivery) + "\n Total: $", str(self.plata + delivery))
            return self.plata

class User:
    def __init__(self, name):
        self.name= name

    def login(self):
        name = input("Ingrese su nombre:     ")
        return name


class Delivery: 

    def __init__(self) -> None:
        pass

    def hallar_dist (self, latitud, longitud):

        
        lat1= latitud
        lon1= longitud
        with open("settings.json") as settings:
            coords = json.load(settings)
            lat2= coords ["coords"][0]
            lon2= coords ["coords"][1]
        ## haversine - halla la distancia entre las dos coordenadas.

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
        
