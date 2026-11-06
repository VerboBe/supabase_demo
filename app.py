import web
from mvc.controllers.index import Index
from mvc.controllers.contactos import Contactos

web.config.debug = False

url = (
    '/', 'Index', 
    '/', 'Contactos', 'mvc.controllers.contactos.Contactos',
)

app = web.application(url, globals())

if __name__ == "__main__":
    app.run()

'''
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