import web
import logging

from mvc.controllers.index import Index
from mvc.controllers.contactos import Contactos
from mvc.controllers.insertar_contacto import InsertarContacto
from mvc.controllers.ver_contacto import VerContacto
from mvc.controllers.actualizar_contacto import ActualizarContacto
from mvc.controllers.borrar_contacto import BorrarContacto



logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",  # Evita errores con tildes o caracteres especiales
)



web.config.debug = False

url = (
'/', 'Index',
'/contactos', 'Contactos',
'/insertar_contacto', "InsertarContacto",
'/ver_contacto/(.*)', 'VerContacto',
'/actualizar_contacto/(.*)', 'ActualizarContacto',
'/borrar_contacto/(.*)', 'BorrarContacto',
)

app = web.application(url, globals())

if __name__ == "__main__":
    app.run()

'''

github/salvadorhm

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

def obtenerContactos():
    response = supabase.table("contactos").select("*").execute()
    return response.data

    

print(obtenerContactos())
'''

