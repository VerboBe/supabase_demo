import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos():
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
            os.environ.get("SUPABASE_URL"),
            os.environ.get("SUPABASE_KEY")
        )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        #SELECT * FROM contactos;
        response = self.supabase.table('contactos').select('*').execute()
        return response.data

    def buscarContacto(self, id_contacto:int):
        response = self.supabase.table('contactos').select('*').eq('id_contacto',id_contacto)
        return response.data

    def insertarContacto(self, nombr:str, email:str, telefono:str):
        try:
            data = {
                "nombre":nombre,
                "email":email,
                "telefono":telefono
            }
            response = self.supabase.table("contactos").insert(data).execute()
            return response.data
        except Exception as error:
             print(f"ERROR 100: {error.args[0]}")
    
    
    def borrarContacto(self, id_contacto:int):

        try:
            response = self.supabase.table("contactos").delete(data).execute()
            return response.data
        
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")
        
        
if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(1))
    print(model_contactos.insertarContacto("Uri","uri2@gmail.com","12345"))

