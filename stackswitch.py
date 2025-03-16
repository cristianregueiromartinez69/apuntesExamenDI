import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ventanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("StackSwitch")
        self.set_resizable(False)
        self.set_size_request(400, 400)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        #creamos el stackLayout
        self.stackLayout = Gtk.Stack()

        #defines el tipo de transicición entre los elementos
        self.stackLayout.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

        #duracion de la transicion
        self.stackLayout.set_transition_duration(1000)

        self.chkBoton = Gtk.CheckButton(label="Púlsame perra")
        self.stackLayout.add_titled(self.chkBoton, "chk", "boton para pulsar")

        self.labelSwith = Gtk.Label()
        self.labelSwith.set_markup("<big>Hala madrid</big>")
        self.stackLayout.add_titled(self.labelSwith, "label", "label del switch")

        self.cajaVerticalFormulario = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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

        self.cajaVerticalFormulario.pack_start(self.gridFormulario, True, True, 0)

        self.stackLayout.add_titled(self.cajaVerticalFormulario, "form", "formulario de registro")

        self.giradorSwitcher = Gtk.StackSwitcher()
        self.giradorSwitcher.set_stack(self.stackLayout)

        self.cajaVertical.pack_start(self.giradorSwitcher, True, True, 0)
        self.cajaVertical.pack_start(self.stackLayout, True, True, 0)



        self.add(self.cajaVertical)
        self.show_all()

if __name__ == '__main__':
    # Creamos una instancia de la ventana principal
    win = ventanaPrincipal()


    win.connect("destroy", Gtk.main_quit)

    # Iniciamos el bucle principal de la aplicación Gtk
    Gtk.main()



'''

Aquí tienes el código explicado con comentarios detallados, incluyendo la funcionalidad del StackSwitcher y Stack:

# Importamos el módulo de PyGObject para poder usar Gtk
import gi

# Establecemos la versión de Gtk que queremos usar (en este caso, la 3.0)
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # Importamos Gtk desde la librería de GI

# Definimos una clase que representa la ventana principal de la aplicación
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        # Llamamos al constructor de la clase padre (Gtk.Window)
        super().__init__()

        # Configuración básica de la ventana
        self.set_title("Ejemplo con StackSwitch")  # Título de la ventana
        self.set_size_request(400, 400)  # Definimos el tamaño de la ventana en píxeles (ancho x alto)
        self.set_resizable(False)  # Evita que el usuario pueda redimensionar la ventana

        # Creamos una caja vertical que servirá como contenedor de los widgets
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Creamos un Stack, que es un contenedor que nos permite cambiar entre diferentes widgets
        stackLayout = Gtk.Stack()

        # Definimos el tipo de transición cuando cambiemos entre los elementos del stack
        stackLayout.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)  # Transición deslizante izquierda-derecha

        # Definimos la duración de la animación en milisegundos (1 segundo en este caso)
        stackLayout.set_transition_duration(1000)

        # Creamos un botón de tipo CheckButton (casilla de verificación)
        chkPulsame = Gtk.CheckButton(label="Púlsame")

        # Agregamos el CheckButton al Stack, asignándole un nombre interno ("chk") y un título visible en el switcher
        stackLayout.add_titled(chkPulsame, "chk", "Check para pulsar")

        # Creamos una etiqueta con texto formateado en HTML (marcado como "big" para hacer el texto más grande)
        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<big> Una etiqueta </big>")

        # Agregamos la etiqueta al Stack, con un nombre interno ("lbl") y un título visible en el switcher
        stackLayout.add_titled(lblEtiqueta, "lbl", "Etiqueta elegante")

        # Creamos un StackSwitcher, que será el widget que permitirá cambiar entre los elementos del Stack
        stack_switcher = Gtk.StackSwitcher()

        # Asociamos el StackSwitcher con el Stack para que pueda controlar sus elementos
        stack_switcher.set_stack(stackLayout)

        # Agregamos el StackSwitcher a la caja vertical (se coloca en la parte superior)
        cajaV.pack_start(stack_switcher, True, True, 0)

        # Agregamos el Stack al contenedor (se coloca debajo del StackSwitcher)
        cajaV.pack_start(stackLayout, True, True, 0)

        # Agregamos la caja vertical a la ventana principal
        self.add(cajaV)

        # Mostramos todos los elementos de la ventana
        self.show_all()

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Creamos una instancia de la ventana principal
    win = FiestraPrincipal()

    # Conectamos el evento "destroy" de la ventana con la función Gtk.main_quit()
    # Esto permite que al cerrar la ventana, se cierre la aplicación
    win.connect("destroy", Gtk.main_quit)

    # Iniciamos el bucle principal de la aplicación Gtk
    Gtk.main()

¿Qué es y para qué sirve el StackSwitcher en PyGObject?

📌 StackSwitcher es un widget que permite cambiar entre los elementos de un Gtk.Stack.
Funciona como un sistema de pestañas o botones que permiten alternar entre distintos elementos gráficos dentro de un Stack.

    En este código, el StackSwitcher permite alternar entre:
        Un CheckButton con el texto "Púlsame".
        Una Etiqueta con el texto "Una etiqueta elegante".

💡 ¿Dónde se usa en el mundo real?

    En aplicaciones de escritorio con varias vistas (por ejemplo, configuraciones, menús de navegación).
    En herramientas de administración donde se quiera mostrar diferentes opciones en la misma ventana sin necesidad de abrir nuevas.
    En interfaces de usuario interactivas, como asistentes paso a paso o formularios dinámicos.

🔹 Ejemplo común: En el menú de configuración de muchas aplicaciones, puedes ver cómo cambian las opciones al seleccionar diferentes pestañas. Ese comportamiento se puede lograr con StackSwitcher y Stack.

Si quieres más detalles o ejemplos prácticos, dime y te ayudo. 🚀


'''