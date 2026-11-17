import os
from supabase import create_client, Client
from dotenv  import load_dotenv
import logging



load_dotenv()

logger = logging.getLogger(__name__)

class AuthUserts:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
            os.environ.get("SUPABASE_URL", ""),
            os.environ.get("SUPABASE_KEY", "")
                
            ) 
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")
            
    def iniciarSesion(self, email:str, password:str):
        try:
            response = self.supabase.auth.sign_in_with_password(
                {
                    "email":email,
                    "password":password,
                }
            )
            return response.session.acces_token
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")
            
if __name__ == "__main__":
    print("- - AUTENTICACION DE USUARIOS - -")
    objeto = AuthUserts()
    objeto.iniciarSesion("usuario@gmail.com", "123456")