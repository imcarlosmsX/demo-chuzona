#%%
from classes import Restaurant, User, Delivery
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import json


name = User("carlos")

nombre = name.login()

direccion_destino = input("ingrese la direccion que desea:          ")

with open("settings.json") as settings:
    ciudad = json.load(settings)
    df = pd.DataFrame({'direcc':
    [direccion_destino + str(ciudad["ciudad"][0])]})

geolocartor = Nominatim(user_agent = "chuzona")
geocode = RateLimiter(geolocartor.geocode, min_delay_seconds = 1)

df["location"] = df["direcc"].apply(geocode)
df["coordenadas"] = df["location"].apply(lambda x: (x.latitude, x.longitude))

coord = df["coordenadas"]



precio_domi= Delivery()

domicilio = precio_domi.hallar_dist(coord[0][0], coord[0][1])


print("\nBienvenido a la Chuzona señor(a) " + nombre + "\n")
with open("menu.json") as menu_comida:
    listado_comida = json.load(menu_comida)
    comida = Restaurant(listado_comida)
    pedido = comida.pedir(domicilio, nombre, direccion_destino)
        



# %%
