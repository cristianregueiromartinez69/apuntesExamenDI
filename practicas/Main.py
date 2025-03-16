import gi
from gi.overrides.Gtk import ListStore

from listbox.datosListBox import DatosListBox

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ConnectionDB import ConexionBD
from gridDatos import GridDatos
from Botonera import Botonera

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Principal")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.base = ConexionBD("usuarios.db")

        self.datos_base = self.base.consultaSenParametros("SELECT * FROM usuarios")

        self.columnas_tabla = ["DNI", "NOME", "APELLIDOS", "TELEFONO"]

        self.datosStore = ListStore(str, str, str, str)

        for datos in self.datos_base:
            self.datosStore.append(datos)

        self.vista = Gtk.TreeView(model = self.datosStore)

        self.selection_vista = self.vista.get_selection()

        self.selection_vista.connect("changed", self.on_seleccion_vista_changed)

        for i in range(len(self.columnas_tabla)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(self.columnas_tabla[i], celda, text = i)
            self.vista.append_column(columna)

        self.cajaVertical.pack_start(self.vista, True, True, 0)

        #grid datos
        self.gridDatos = GridDatos()

        #conexion combo datos
        self.gridDatos.comboBoxgenero.connect("changed", self.on_combobox_genero_changed)
        self.gridDatos.buttonMuerto.connect("clicked", self.on_button_muerto_clicked)
        self.auxGenero = None
        self.auxPulsado = None

        self.cajaVertical.pack_start(self.gridDatos, True, True, 0)

        #lista datos
        self.listaNombres = Gtk.ListBox()
        self.listaNombres.connect("row-activated", self.on_activate_lista_nombres)




        #consulta nombres
        self.nombres = self.base.consultaSenParametros("SELECT name FROM usuarios")
        for nombre in self.nombres:
            self.listaNombres.add(DatosListBox(nombre))

        self.cajaVertical.pack_start(self.listaNombres, True, True, 0)

        #botonera
        self.botones = Botonera()
        self.botones.bottonInsertar.connect("clicked", self.on_insert_data)

        self.cajaVertical.pack_start(self.botones, True, True, 0)

        self.add(self.cajaVertical)
        self.show_all()



    def on_seleccion_vista_changed(self, seleccion):
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            print("\nDNI: " + modelo[fila][0] +
                  "\nNome: " + modelo[fila][1] +
                  "\nAPELLIDOS: " + modelo[fila][2] +
                  "\nTELEFONO: " + modelo[fila][3])

    def on_insert_data(self, boton):
        if self.gridDatos.dni_text.get_text() != "" and self.gridDatos.nombre_text.get_text() != "" and self.gridDatos.apellido_text.get_text() != "" and self.gridDatos.telefono_text.get_text() != "" and self.auxGenero is not None:
            dni = self.gridDatos.dni_text.get_text()
            nombre = self.gridDatos.nombre_text.get_text()
            apellido = self.gridDatos.apellido_text.get_text()
            telefono = self.gridDatos.telefono_text.get_text()

            nuevo_usuario = [
                dni, nombre, apellido, telefono
            ]
            self.base.insertar_usuario(nuevo_usuario)
            self.datosStore.append((dni, nombre, apellido, telefono))
            print("datos insertados correctamente")

        else:
            print("todo incorrecto")


    def on_combobox_genero_changed(self, combo):
        modelo = combo.get_model()
        fila = combo.get_active_iter()
        if fila is not None:
            genero = modelo.get_value(fila, 0)
            self.auxGenero = genero


    def on_button_muerto_clicked(self, boton):
        pulsado = boton.get_active()
        self.auxPulsado = pulsado

    def on_activate_lista_nombres(self, listBox, fila):
        print("Nombre seleccionado: " + fila.dato)


if __name__ == "__main__":
    window = FiestraPrincipal()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()


