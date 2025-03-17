import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ConectaDB import ConexionBD

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Mas tree view")
        self.set_resizable(False)
        self.set_size_request(400,400)

        self.caja_vertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.modelo_datos = Gtk.ListStore(str, str, int, str, int)

        self.modelo_datos.set_sort_column_id(2, Gtk.SortType.ASCENDING)

        self.modelo_combo = Gtk.ListStore(str)
        self.base = ConexionBD("usuarios.db")

        self.lista_usuarios = self.base.consultaSenParametros("SELECT * FROM usuarios2")
        self.lista_generos = self.base.consultaSenParametros("SELECT DISTINCT genero FROM usuarios2")
        for genero in self.lista_generos:
            self.modelo_combo.append(genero)

        for dato in self.lista_usuarios:
            self.modelo_datos.append(dato)

        self.view = Gtk.TreeView(model = self.modelo_datos)

        self.objeto_seleccion = self.view.get_selection()
        self.objeto_seleccion.connect("changed", self.on_selection_changed)

        self.celda_nombre = Gtk.CellRendererText()
        self.columna_nombre = Gtk.TreeViewColumn("Nombre", self.celda_nombre, text=0)
        self.view.append_column(self.columna_nombre)

        self.celda_apellidos = Gtk.CellRendererText()
        self.columna_apellidos = Gtk.TreeViewColumn("Apellido", self.celda_apellidos, text=1)
        self.view.append_column(self.columna_apellidos)

        self.celda_progress_edad = Gtk.CellRendererProgress()
        self.columna_edad = Gtk.TreeViewColumn("Edad", self.celda_progress_edad, value=2)
        self.view.append_column(self.columna_edad)
        self.columna_edad.set_sort_column_id(2)


        self.renderer_combo = Gtk.CellRendererCombo()
        self.renderer_combo.set_property("editable", True)
        self.renderer_combo.set_property("model", self.modelo_combo)
        self.renderer_combo.set_property("text-column", 0)
        self.renderer_combo.set_property("has-entry", False)
        self.renderer_combo.connect("edited", self.combo_edited, self.modelo_datos)

        self.columna_combo = Gtk.TreeViewColumn("Genero", self.renderer_combo, text=3)
        self.view.append_column(self.columna_combo)

        self.celda_muerto = Gtk.CellRendererToggle()
        self.celda_muerto.set_property("activatable", True)
        self.columna_muerto = Gtk.TreeViewColumn("Muerto", self.celda_muerto, active=4)
        self.view.append_column(self.columna_muerto)

        self.celda_muerto.connect("toggled", self.on_change_muerto)


        self.caja_vertical.pack_start(self.view, True, True, 0)
        self.add(self.caja_vertical)
        self.show_all()

    def on_selection_changed(self, selecion):
        modelo, fila = selecion.get_selected()
        if fila is not None:
            nombre = modelo[fila][0]
            apellido = modelo[fila][1]
            edad = modelo[fila][2]
            genero = modelo[fila][3]
            muerto = modelo[fila][4]
            print("\nNombre: " + nombre +
                  "\nApellido: " + apellido +
                  "\nEdad: " + str(edad) +
                  "\nGenero: " + genero +
                  "\nMuerto: " + str(muerto))



    def combo_edited(self, widget, path, new_text, model):
        model[path][3] = new_text
        print(model[path][3])

    def on_change_muerto(self, toogle, boton):
        pass

    def compara_modelo(self, modelo, fila1, fila2):
        print("hola")
        columna_ordenada, _ = modelo.get_sort_column_id()

        # Verifica si la columna de edad es la correcta.
        if columna_ordenada != 2:
            print("no funciona")
            return 0  # Si no estamos ordenando por edad, no hacemos nada.

        # Obtén los valores de edad de ambas filas.
        edade1 = modelo.get_value(fila1, 2)
        edade2 = modelo.get_value(fila2, 2)

        # Imprime las edades para depurar.
        print("Comparando edades: {} vs {}".format(edade1, edade2))

        # Realiza la comparación de las edades.
        if edade1 < edade2:
            return -1
        elif edade1 == edade2:
            return 0
        else:
            return 1


if __name__ == "__main__":
    window = FiestraPrincipal()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()

        
