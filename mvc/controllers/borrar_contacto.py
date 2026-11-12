import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:
    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contactos = model_contactos.buscarContacto(id_contacto)

        return render.ver_contacto(contactos)