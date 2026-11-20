import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()
    
    def POST(self):
        formulario = web.input(foto={})
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']
        
        archivo = formulario['foto']
        foto = archivo.filename
        
        ruta = os.path.join("static/fotos/", foto)
        
        with open(ruta, "wb") as file:
            file.write(formulario.foto.file.read())
        
        '''
        print(f"Nombre: {nombre}")
        print(f"Email: {email}")
        print(f"Telefono: {telefono}")
        '''
        
        contenido_bytes = archivo.file.read()
        
        model_contactos = ModelContactos()
        datos = model_contactos.insertarContacto(nombre,email,telefono,foto)
        
        html = """
        <h1>Contacto almacenado correctamente</h1>
        <a href="/contactos">Regresa</a>
        """
        return html