import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLoger()

class ModelContactos():
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
            self.SECRET_KEY = b"hola"
            
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR")
              

    def generarHash(self, id: int) -> str:
        try:
            mensaje = str(id).encode("utf-8")
            firma = hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexadiges
            
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR")
        
        
        
    def obtenerContactos(self):
        #SELECT * FROM contactos;
        try:
            response = self.supabase.table('contactos').select('*').execute()
            return response.data
        
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR")
            
            
            

    def buscarContacto(self, id_contacto:int):
        try:
            response = self.supabase.table('contactos').select('*').eq('id_contacto',id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR")




    def insertarContacto(self, nombre: str, email: str, telefono: str):
        
        try:
            data = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
            }
            response = self.supabase.table('contactos').insert(data).execute()
            return response.data
        
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR")
    
     
     
    def borrarContacto(self, id_contacto:int):
        
        try:
            response = self.supabase.table("contactos").delete(data).execute()
            return response.data
        
        except Exception as error:
            print(f"ERROR 100: {str(error)}")
            print(f"ERROR")
        
         
        
        
if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(1))
    print(model_contactos.insertarContacto(datos))
          
