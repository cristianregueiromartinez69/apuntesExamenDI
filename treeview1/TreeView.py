import gi

from treeview1.DB import ConexionBD

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from InserccionesGrid import RegistrosGrid
from Botonera import Botones
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejemplo con treeView")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.base = ConexionBD("usuarios.db")

        self.datosBase = self.base.consultaSenParametros("SELECT * FROM usuarios")

        self.columnasTabla = ["DNI", "Nombre", "Apellido", "Número de teléfono"]

        self.listStoreTabla = Gtk.ListStore(str, str, str, str)

        for dato in self.datosBase:
            self.listStoreTabla.append(dato)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.vista = Gtk.TreeView(model = self.listStoreTabla)

        self.objetoSeleccion = self.vista.get_selection()

        self.listStoreTabla.set_sort_func(1, self.compara_modelo)


        self.objetoSeleccion.connect("changed", self.on_seleccion_tabla)

        for i in range(len(self.columnasTabla)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(self.columnasTabla[i], celda, text = i)
            self.vista.append_column(columna)

        self.cajaVertical.pack_start(self.vista, True, True, 0)

        self.formulario = RegistrosGrid()
        self.botoncitos = Botones()

        #conexiones
        self.botoncitos.botonInserccion.connect("clicked", self.inserccionesTabla)
        self.botoncitos.botonActualizar.connect("clicked", self.updateUsuario)

        self.cajaVertical.pack_start(self.formulario, True, True, 0)
        self.cajaVertical.pack_start(self.botoncitos, True, True, 0)
        self.add(self.cajaVertical)

        self.show_all()

    def on_seleccion_tabla(self, treeview):
        modelo, fila = treeview.get_selected()

        if fila is not None:
            print(modelo[fila][0] + " " +  modelo[fila][1] + " " + modelo[fila][2] + " " +  modelo[fila][3])
            self.formulario.txtDni.set_text(modelo[fila][0])
            self.formulario.txtNombre.set_text(modelo[fila][1])
            self.formulario.txtApellido.set_text(modelo[fila][2])
            self.formulario.txtNumTelfono.set_text(modelo[fila][3])

    def updateUsuario(self, boton):
        if self.formulario.txtDni.get_text() != "" and self.formulario.txtNombre.get_text() != "" and self.formulario.txtApellido.get_text() != "" and self.formulario.txtNumTelfono.get_text() != "":

            newNombre = self.formulario.txtNombre.get_text()
            oldDni = self.formulario.txtDni.get_text()
            self.base.update_data(newNombre, oldDni)
            print("Usuario actualizado correctamente")


    def inserccionesTabla(self, boton):
        if self.formulario.txtDni.get_text() != "" and self.formulario.txtNombre.get_text() != "" and self.formulario.txtApellido.get_text() != "" and self.formulario.txtNumTelfono.get_text() != "":
            dni = self.formulario.txtDni.get_text()
            nombre = self.formulario.txtNombre.get_text()
            apellido = self.formulario.txtApellido.get_text()
            telefono = self.formulario.txtNumTelfono.get_text()

            datoInserccion = [
                dni, nombre, apellido, telefono,
            ]

            self.base.insertar_usuario(datoInserccion)
            self.listStoreTabla.append((dni, nombre, apellido, telefono))
            print("usuario insertado correctamente")
            self.limpiarCampos()
        else:
            print("No hay datos para insertar")


    def limpiarCampos(self):
        self.formulario.txtDni.set_text("")
        self.formulario.txtNombre.set_text("")
        self.formulario.txtApellido.set_text("")
        self.formulario.txtNumTelfono.set_text("")


    def compara_modelo(self, modelo, fila1, fila2, datosUsuario):
        columna_ordenada, _ = modelo.get_sort_column_id()
        valor1 = modelo.get_value(fila1, columna_ordenada)
        valor2 = modelo.get_value(fila2, columna_ordenada)
        if valor1 < valor2:
            return -1
        elif valor1 == valor2:
            return 0
        else:
            return 1

if __name__ == "__main__":
    window = VentanaPrincipal()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()

'''
def update_data(self, newNombre, oldDni):
    with self.conn:
        self.conn.execute("UPDATE usuarios SET nombre = ? WHERE dni = ?", (newNombre, oldDni))

'''
