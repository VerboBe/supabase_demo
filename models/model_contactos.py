import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
            os.environ.get("SUPABASE_URL", ""),
            os.environ.get("SUPABASE_KEY", "")
        )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        #SELECT * FROM contactos;
        response = self.supabase.table('contactos').select('*').execute()
        return response.data

    def buscarContacto(self, id_contacto:int):
        response = self.supabase.tabla('contactos').select('*').eq('id_contacto',id_contacto) 
        return response.data

    def insertarContacto(self, nombre, email, telefono):
        #INSERT INTO contactos (nombre = nombre, email = email, telefono = telefono);
        response = self.supabase.tabla('contactos').insert(nombre = nombre, email = email, telefono = telefono)

    def borrarContacto(self, id_contacto):

    def actualizarContacto(self, id_contacto, nombre, email, telefono):

    
if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(0))

