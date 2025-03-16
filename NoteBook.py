import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_title("Ventana de NoteBook")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.cajaNoteBook = Gtk.Notebook()

        self.pagina1NoteBook = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.pagina1NoteBook.set_border_width(10)

        self.gridFormulario = Gtk.Grid()

        self.gridFormulario.set_column_spacing(15)
        self.gridFormulario.set_row_spacing(15)

        self.labelNonbre = Gtk.Label(label="Nombre")
        self.txtNombre = Gtk.Entry()

        self.labelapellido = Gtk.Label(label="Apellido")
        self.txtApellido = Gtk.Entry()

        self.labelDNI = Gtk.Label(label="DNI")
        self.txtDNI = Gtk.Entry()

        self.gridFormulario.attach(self.labelNonbre, 0, 0, 1, 1)
        self.gridFormulario.attach_next_to(self.txtNombre, self.labelNonbre, Gtk.PositionType.RIGHT, 1, 1)
        self.gridFormulario.attach_next_to(self.labelapellido, self.labelNonbre, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridFormulario.attach_next_to(self.txtApellido, self.labelapellido, Gtk.PositionType.RIGHT, 1, 1)
        self.gridFormulario.attach_next_to(self.labelDNI, self.labelapellido, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridFormulario.attach_next_to(self.txtDNI, self.labelDNI, Gtk.PositionType.RIGHT, 1, 1)

        self.pagina1NoteBook.pack_start(self.gridFormulario, True, True, 0)


        self.pagina2NoteBook = Gtk.Box()
        self.pagina2NoteBook.set_spacing(10)
        self.pagina2NoteBook.set_border_width(10)
        self.pagina2NoteBook.add(Gtk.Label(label = "Pagina 2"))

        self.cajaNoteBook.append_page(self.pagina1NoteBook, Gtk.Label(label = "Formulario"))
        self.cajaNoteBook.append_page(self.pagina2NoteBook, Gtk.Image.new_from_icon_name("help_about", Gtk.IconSize.MENU))

        self.add(self.cajaNoteBook)
        self.show_all()


if __name__ == '__main__':
    win = VentanaPrincipal()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()






'''

Aquí te explico el código paso a paso, con comentarios detallados para que entiendas cómo funciona el Gtk.Notebook y qué hace cada parte del código:

# Importamos los módulos necesarios para trabajar con GTK+ a través de PyGObject
import gi

# Establecemos la versión de GTK que queremos usar (en este caso, la 3.0)
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # Importamos el módulo Gtk desde la librería GI

# Definimos la clase que representará nuestra ventana principal
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        # Llamamos al constructor de la clase padre (Gtk.Window) para inicializar la ventana
        super().__init__()

        # Configuración básica de la ventana
        self.set_title("Ejemplo con NoteBook")  # Título de la ventana
        self.set_size_request(400, 400)  # Establecemos un tamaño fijo de la ventana (ancho x alto en píxeles)
        self.set_resizable(False)  # Evitamos que el usuario pueda cambiar el tamaño de la ventana

        # Creamos un objeto Gtk.Notebook. Este widget nos permite manejar múltiples "páginas" dentro de una misma ventana
        cajaNotebook = Gtk.Notebook()

        # Creamos la primera página del notebook. Usamos un contenedor Box, que es el que contiene los widgets
        pagina1Notebook = Gtk.Box()
        pagina1Notebook.set_border_width(10)  # Definimos un margen de 10 píxeles alrededor de la página
        pagina1Notebook.add(Gtk.Label(label="Pagina 1"))  # Añadimos una etiqueta que dice "Página 1" en esta página

        # Creamos la segunda página del notebook
        pagina2 = Gtk.Box()
        pagina2.set_spacing(10)  # Añadimos un espacio de 10 píxeles entre los widgets dentro de la página
        pagina2.set_border_width(10)  # Añadimos un margen de 10 píxeles alrededor de la página
        pagina2.add(Gtk.Label(label="Pagina 2"))  # Añadimos una etiqueta que dice "Página 2" en esta página

        # Añadimos las páginas al notebook utilizando el método append_page()
        # El primer parámetro es el widget (la página) y el segundo es el "tab" o la etiqueta que aparece en la parte superior del notebook
        cajaNotebook.append_page(pagina1Notebook, Gtk.Label("Pagina 1"))  # La primera página tiene la etiqueta "Pagina 1"
        cajaNotebook.append_page(pagina2, Gtk.Image.new_from_icon_name("help_about", Gtk.IconSize.MENU))  # La segunda página tiene un icono de ayuda como tab

        # Finalmente, agregamos el notebook a la ventana principal
        self.add(cajaNotebook)

        # Mostramos todos los elementos de la ventana, haciendo visible el notebook con sus páginas
        self.show_all()

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Creamos una instancia de la ventana principal
    win = FiestraPrincipal()

    # Conectamos el evento "destroy" de la ventana para que cuando se cierre, se termine la aplicación
    win.connect("destroy", Gtk.main_quit)

    # Iniciamos el bucle principal de GTK
    Gtk.main()

¿Qué es Gtk.Notebook?

El Gtk.Notebook es un widget contenedor que permite crear interfaces con varias páginas, donde cada página tiene su propio contenido. Es útil para aplicaciones que necesitan mostrar diferentes tipos de información sin ocupar demasiada área en la interfaz. Cada "página" es esencialmente un contenedor donde puedes poner widgets como etiquetas, botones, cajas, entre otros. La característica destacada es que el Gtk.Notebook proporciona una interfaz de pestañas o tabs para navegar entre las páginas.
Función del Gtk.Notebook en este ejemplo:

    Creación de Páginas:
        El Gtk.Notebook en este código tiene dos páginas: Página 1 y Página 2.
        En la Página 1 se muestra una etiqueta con el texto "Pagina 1".
        En la Página 2 se muestra otra etiqueta con el texto "Pagina 2".
    Tabs:
        Cada página tiene un "tab" que aparece en la parte superior del Gtk.Notebook, lo que le permite al usuario cambiar entre las diferentes páginas.
        La Página 1 tiene un tab con la etiqueta "Pagina 1".
        La Página 2 tiene un tab con un icono de ayuda ("help_about").

Detalles del código:

    Gtk.Notebook:
        Es el contenedor principal que contiene las "páginas".
        Las páginas se añaden usando el método append_page(pagina, tab_label), donde el primer argumento es el widget (página) y el segundo es el tab que aparece para esa página.

    Gtk.Box:
        Es un contenedor flexible que puede organizar widgets de manera horizontal o vertical. Aquí se usa para crear las páginas dentro del Gtk.Notebook.

    Gtk.Label:
        Es un widget simple que se usa para mostrar texto. En este caso, se usa para mostrar las etiquetas "Pagina 1" y "Pagina 2" dentro de las páginas.

    Gtk.Image.new_from_icon_name():
        Crea una imagen a partir del nombre de un icono. En este caso, se usa para agregar un icono de ayuda al tab de la Página 2.

¿Dónde usarías Gtk.Notebook en el mundo real?

    Aplicaciones de configuración:
        Cuando tienes diferentes secciones de configuración, por ejemplo, "General", "Avanzada", "Red", y quieres que el usuario cambie fácilmente entre ellas sin sobrecargar la interfaz.
    Aplicaciones con múltiples secciones:
        Cualquier aplicación que necesite mostrar diferentes tipos de contenido en la misma ventana, como un cliente de correo electrónico con pestañas para "Bandeja de entrada", "Enviados", "Borradores", etc.
    Aplicaciones de edición de documentos:
        Para organizar diferentes secciones de un documento o varios documentos dentro de la misma ventana, similar a las pestañas de un editor de texto o navegador.

Si necesitas más detalles sobre algún aspecto o tienes alguna duda, no dudes en preguntar. ¡Estoy aquí para ayudarte!

'''