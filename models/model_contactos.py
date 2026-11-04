class ModelContactos:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
            os.environ.get("SUPABASE_URL"),
            os.environ.get("SUPABASE_KEY")
        )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        response = self.supabase.table("contactos").select("*").execite()
        return response.data

model_contactos = ModelContactos()
print(model_contactos.obtenerContactos())