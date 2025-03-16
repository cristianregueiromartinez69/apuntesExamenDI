import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejemplo de flow box")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        self.flowBox = Gtk.FlowBox()
        self.flowBox.set_valign(Gtk.Align.START)
        self.flowBox.set_max_children_per_line(30)
        self.flowBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.crear_cosas_flowBox(self.flowBox)
        self.scroll.add(self.flowBox)
        self.add(self.scroll)

        self.show_all()

    def crear_cosas_flowBox(self, flowBox):
        for i in range(1001):
            boton = Gtk.Button(label=str(i))
            flowBox.add(boton)



if __name__ == '__main__':
    win = FiestraPrincipal()

    win.connect("destroy", Gtk.main_quit)

    Gtk.main()



'''
        # Creamos un widget Gtk.ScrolledWindow, que se utiliza para habilitar desplazamiento dentro de un área.
        self.scroll = Gtk.ScrolledWindow()
        # Definimos que no haya desplazamiento horizontal (NEVER) pero sí automático en vertical (AUTOMATIC)
        self.scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        # Creamos el FlowBox, que organiza los elementos de manera fluida, colocándolos uno tras otro
        # en filas y columnas de acuerdo a las restricciones que le definamos
        self.flowbox = Gtk.FlowBox()
        self.flowbox.set_valign(Gtk.Align.START)  # Indicamos que los elementos comienzan desde la parte superior del FlowBox
        self.flowbox.set_max_children_per_line(30)  # Definimos que el número máximo de botones por fila será 30
        self.flowbox.set_selection_mode(Gtk.SelectionMode.NONE)  # No permitimos seleccionar ningún elemento

        # Llamamos a la función create_flowbox para llenar el FlowBox con elementos
        self.create_flowbox(self.flowbox)

        # Añadimos el FlowBox al widget de desplazamiento
        self.scroll.add(self.flowbox)

        # Finalmente, agregamos el ScrolledWindow (que contiene el FlowBox) a la ventana principal
        self.add(self.scroll)

        # Mostramos todos los elementos de la ventana (esto hace que la ventana y su contenido sean visibles)
        self.show_all()

    # Función que llena el FlowBox con botones de colores
    def create_flowbox(self, flowbox):
        # Lista de colores para crear los botones
        colores = ["AliceBlue", "AntiqueWhite", "AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3", "AntiqueWhite4",
                   "aqua", "aquamarine", "aquamarine1", "aquamarine2", "aquamarine3", "aquamarine4", "azure", "azure1",
                   "azure2", "azure3", "azure4", "beige", "bisque", "bisque1", "bisque2", "bisque3", "bisque4", "black",
                   "BlanchedAlmond", "blue", "blue1", "blue2", "blue3", "blue4", "BlueViolet", "brown", "brown1", "brown2",
                   "brown3", "brown4", "burlywood", "burlywood1", "burlywood2", "burlywood3", "burlywood4", "CadetBlue",
                   "CadetBlue1", "CadetBlue2", "CadetBlue3", "CadetBlue4", "chartreuse", "chartreuse1", "chartreuse2",
                   "chartreuse3", "chartreuse4", "chocolate", "chocolate1", "chocolate2", "chocolate3", "chocolate4",
                   "coral", "coral1", "coral2", "coral3", "coral4"]

        # Iteramos sobre la lista de colores y creamos un botón para cada uno
        for color in colores:
            boton = self.crear_boton_color(color)  # Creamos un botón con el color correspondiente
            flowbox.add(boton)  # Añadimos el botón al FlowBox

    # Función para crear un botón con un color de fondo específico
    def crear_boton_color(self, color):
        # Creamos un objeto RGBA (que se usa para representar colores con valores de canal rojo, verde, azul y alfa/transparencia)
        rgba = Gdk.RGBA()
        rgba.parse(color)  # Parseamos el nombre del color para que el objeto RGBA tenga los valores adecuados

        # Creamos un botón en GTK
        boton = Gtk.Button()

        # Creamos un área de dibujo (DrawingArea) para poder dibujar un color personalizado en el botón
        area = Gtk.DrawingArea()
        area.set_size_request(50, 50)  # Definimos el tamaño del área de dibujo (50x50 píxeles)
        # Conectamos el evento "draw" del área de dibujo a nuestra función de dibujar el color
        area.connect("draw", self.on_draw, {"color": rgba})

        # Añadimos el área de dibujo al botón
        boton.add(area)
        return boton

    # Función que se llama cuando se dibuja el área (el color del botón)
    def on_draw(self, control, cr, dic):
        # Obtenemos el contexto de estilo del control (el área de dibujo)
        contexto = control.get_style_context()

        # Obtenemos el ancho y alto del área de dibujo
        ancho = control.get_allocated_width()
        alto = control.get_allocated_height()

        # Dibujamos el fondo del área
        Gtk.render_background(contexto, cr, 0, 0, ancho, alto)

        # Obtenemos los valores de color (rojo, verde, azul, alfa)
        r = dic["color"].red
        g = dic["color"].green
        b = dic["color"].blue
        a = dic["color"].alpha

        # Establecemos el color con los valores obtenidos y dibujamos un rectángulo de fondo con ese color
        cr.set_source_rgba(r, g, b, a)
        cr.rectangle(0, 0, ancho, alto)  # Establecemos el rectángulo del tamaño del área
        cr.fill()  # Lo rellenamos con el color

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Creamos una instancia de la ventana principal
    win = FiestraPrincipal()

    # Conectamos el evento "destroy" de la ventana para que cuando se cierre, se termine la aplicación
    win.connect("destroy", Gtk.main_quit)

    # Iniciamos el bucle principal de GTK
    Gtk.main()

Explicación detallada de los componentes clave:

    Gtk.FlowBox:
        Gtk.FlowBox es un widget contenedor que organiza los elementos de manera fluida. Los elementos se colocan en una cuadrícula fluida, es decir, se alinean automáticamente en filas, pero se ajustan a la ventana según el espacio disponible.
        En este caso, hemos configurado que el máximo número de elementos por fila sea 30 con set_max_children_per_line(30).

    Gtk.ScrolledWindow:
        Gtk.ScrolledWindow es un contenedor que permite agregar desplazamiento a cualquier otro widget que lo necesite.
        En este caso, el Gtk.FlowBox está dentro de un Gtk.ScrolledWindow, lo que permite que se muestren más de 30 botones si la ventana es más pequeña. El desplazamiento solo se habilita verticalmente.

    Gtk.Button y Gtk.DrawingArea:
        Cada botón que aparece en el FlowBox es un Gtk.Button con un área de dibujo (Gtk.DrawingArea) dentro, donde dibujamos un color específico.
        Cada botón tiene un color de fondo que se establece mediante el método on_draw donde se usa el color de tipo Gdk.RGBA.

    Colores:
        La lista de colores se utiliza para generar botones con diferentes colores de fondo, lo que le da a la aplicación un aspecto visualmente interesante. Cada botón tiene un color único que se dibuja en el área de dibujo.

¿Dónde usarías Gtk.FlowBox en el mundo real?

    Galerías de imágenes:
        En una aplicación que muestra miniaturas de imágenes. Los elementos pueden organizarse de manera fluida según el tamaño de la ventana.

    Lista de productos:
        En una tienda en línea, donde los productos (como botones, tarjetas, etc.) se organizan dinámicamente dependiendo del espacio disponible.

    Interfaz de usuario para seleccionar opciones:
        Si se tiene una gran cantidad de botones u opciones que pueden ir creciendo, y quieres que los usuarios naveguen a través de ellos sin que se vean apretados o forzados a usar barras de desplazamiento horizontales.

Si tienes más preguntas o necesitas más detalles, no dudes en preguntar. ¡Estoy aquí para ayudarte!

'''