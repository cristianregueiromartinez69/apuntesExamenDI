import gi

from listbox.datosListBox import DatosListBox

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Listbox ejemplo")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)
        self.cajaHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 6)

        self.cajaVerticalEtiquetas = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)


        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.cajaVertical.pack_start(self.listbox, True, True, 0)

        self.fila = Gtk.ListBoxRow()
        self.listbox.add(self.fila)
        self.fila.add(self.cajaVerticalEtiquetas)

        self.labelNombre = Gtk.Label(label = "pedrito")
        self.labelApellido = Gtk.Label(label = "de los santos")
        self.labelEdad = Gtk.Label(label = "20")

        self.cajaHorizontal.pack_start(self.labelNombre, True, True, 0)
        self.cajaHorizontal.pack_start(self.labelApellido, True, True, 0)
        self.cajaHorizontal.pack_start(self.labelEdad, True, True, 0)

        self.cajaVerticalEtiquetas.add(self.cajaHorizontal)

        #segundo listBox
        self.listBox2 = Gtk.ListBox()
        self.listBox2.set_sort_func(self.funcion_ordenacion)
        self.listBox2.set_filter_func(self.funcion_filtracion)
        self.fila2 = Gtk.ListBoxRow()

        self.nombres = [
            "Pedro", "Juana", "Veronica", "José", "Dimitri", "Juanito",
            "Alejandro", "Sodayo", "luka", "Liko"
        ]
        for nombre in self.nombres:
            self.listBox2.add(DatosListBox(nombre))



        self.cajaVertical.pack_start(self.listBox2, True, True, 0)
        #conexiones
        self.listBox2.connect("row-activated", self.on_list_activated)



        self.add(self.cajaVertical)
        self.show_all()


    def on_list_activated(self, listbox, fila):
        print(fila.dato)

    def funcion_ordenacion(self, fila1, fila2):
        return fila1.dato.lower() > fila2.dato.lower()

    def funcion_filtracion(self, fila):
        return False if fila.dato == "Sodayo" else True

if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()




'''


        # Primera fila dentro del ListBox
        self.fila = Gtk.ListBoxRow()  # Creamos una fila
        self.cajaHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)  # Caja para organizar elementos en horizontal
        self.fila.add(self.cajaHorizontal)  # Agregamos la caja a la fila

        # Caja vertical para colocar dos etiquetas
        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.cajaHorizontal.pack_start(self.cajaVertical, True, True, 0)  # Agregamos la caja vertical dentro de la caja horizontal

        # Creamos dos etiquetas dentro de la caja vertical
        self.lblEtiqueta1 = Gtk.Label(label="Fecha y hora automáticas")
        self.lblEtiqueta2 = Gtk.Label(label="Acceso a internet")
        self.cajaVertical.pack_start(self.lblEtiqueta1, True, True, 0)
        self.cajaVertical.pack_start(self.lblEtiqueta2, True, True, 0)

        # Creamos un interruptor (switch) y lo alineamos verticalmente en el centro
        self.switch = Gtk.Switch()
        self.switch.props.valign = Gtk.Align.CENTER

        # Agregamos el switch a la caja horizontal
        self.cajaHorizontal.pack_start(self.switch, False, False, 0)

        # Agregamos la fila completa al ListBox
        self.listBox.add(self.fila)

        # Segunda fila dentro del ListBox
        self.fila2 = Gtk.ListBoxRow()
        self.cajaHFila2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)  # Caja horizontal
        self.fila2.add(self.cajaHFila2)  # Agregamos la caja a la fila

        # Creamos una etiqueta y un CheckButton
        self.lblEtiqueta3 = Gtk.Label(label="Permite actualización automática", xalign=0)
        self.check = Gtk.CheckButton()
        self.cajaHFila2.pack_start(self.lblEtiqueta3, True, True, 0)  # Agregamos la etiqueta
        self.cajaHFila2.pack_start(self.check, False, False, 0)  # Agregamos el botón de verificación

        # Agregamos la segunda fila al ListBox
        self.listBox.add(self.fila2)

        # Segundo ListBox con elementos desordenados
        self.listBox2 = Gtk.ListBox()
        self.listBox2.set_sort_func(self.funcion_ordenacion)  # Establecemos función de ordenación
        self.listBox2.set_filter_func(self.funcion_filtracion)  # Establecemos función de filtrado

        # Lista de palabras que se añadirán al ListBox
        elementos = "Esta es una lista con elementos desordenada".split()
        for elemento in elementos:
            self.listBox2.add(ListBoxConDatos(elemento))  # Agregamos cada palabra como una fila personalizada

        # Conectamos la señal para detectar cuando se activa una fila
        self.listBox2.connect("row-activated", self.on_row_activated)

        # Agregamos el segundo ListBox a la caja principal
        self.cajaPrincipal.pack_start(self.listBox2, True, True, 0)

        # Mostramos todos los elementos del segundo ListBox
        self.listBox2.show_all()

        # Agregamos la caja principal a la ventana y mostramos todos los elementos
        self.add(self.cajaPrincipal)
        self.show_all()

    # Evento que se dispara cuando se hace clic en una fila del ListBox2
    def on_row_activated(self, listBox, fila):
        """
        Se activa cuando se hace clic en una fila de listBox2.
        Imprime en consola el texto de la fila seleccionada.
        """
        print(fila.dato)

    # Función que ordena las filas del ListBox2 alfabéticamente
    def funcion_ordenacion(self, fila1, fila2):
        """
        Función de ordenación que compara dos filas y decide su orden en la lista.
        Devuelve True si fila1 debe ir antes que fila2, según orden alfabético.
        """
        return fila1.dato.lower() < fila2.dato.lower()

    # Función de filtrado para excluir elementos no deseados
    def funcion_filtracion(self, fila):
        """
        Función de filtrado que excluye de la lista la palabra "lista".
        Si el dato de la fila es "lista", devuelve False (lo oculta).
        En caso contrario, devuelve True (se mantiene visible).
        """
        return False if fila.dato == "lista" else True

'''