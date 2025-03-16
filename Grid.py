import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ventana Grid")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.fondoGrid = Gtk.Grid()
        self.cajaHorizontal = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing=6)
        self.fondoGrid.set_column_spacing(15)
        self.fondoGrid.set_row_spacing(15)
        self.cajaVertical.pack_start(self.fondoGrid, True, True, 0)

        self.labelNombre = Gtk.Label(label="Nombre")
        self.textNombre = Gtk.Entry()

        self.labelApellido = Gtk.Label(label="Apellido")
        self.textApellido = Gtk.Entry()

        self.labelEdad = Gtk.Label(label="Edad")
        self.txtEdad = Gtk.Entry()

        self.labelDireccion = Gtk.Label(label="Direccion")
        self.txtDireccion = Gtk.Entry()

        self.labelProfesion = Gtk.Label(label="Profesion")
        self.txtProfesion = Gtk.Entry()

        self.fondoGrid.attach(self.labelNombre, 0, 0, 1, 1)
        self.fondoGrid.attach_next_to(self.textNombre, self.labelNombre, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.labelApellido, self.labelNombre, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.textApellido, self.labelApellido, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.labelEdad, self.labelApellido, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.txtEdad, self.labelEdad, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.labelDireccion, self.labelEdad, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.txtDireccion, self.labelDireccion, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.labelProfesion, self.labelDireccion, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.txtProfesion, self.labelProfesion, Gtk.PositionType.RIGHT, 1, 1)

        self.botonAceptar = Gtk.Button(label="Insertar")
        self.botonCancelar = Gtk.Button(label="Cancelar")

        self.botonAceptar.connect("clicked", self.on_botn_aceptar)
        self.botonCancelar.connect("clicked", self.on_btn_cancelar)

        self.cajaHorizontal.pack_start(self.botonAceptar, True, True, 0)
        self.cajaHorizontal.pack_start(self.botonCancelar, True, True, 0)

        self.cajaVertical.pack_start(self.cajaHorizontal, True, True, 0)


        



        self.add(self.cajaVertical)
        self.show_all()

    def on_botn_aceptar(self, boton):
        if self.textNombre.get_text() != "" and self.textApellido.get_text() != "" and self.txtEdad.get_text() != "" and self.txtDireccion.get_text() != "" and self.txtProfesion.get_text() != "":
            if self.checkNumber(self.txtEdad):
                print("datos insertados correctamente en la base de datos")
                self.limpiarCampos()
            else:
                print("numero incorrecto, introduce uno válido")
                self.txtEdad.set_text("")
        else:
            print("rellena los campos faltantes gilipollas")

    def checkNumber(self, numeroEdad):
        txtNumero = numeroEdad.get_text()
        if txtNumero.isdigit():
            return True

    def on_btn_cancelar(self, boton):
        self.limpiarCampos()

    def limpiarCampos(self):
        self.textNombre.set_text("")
        self.textApellido.set_text("")
        self.txtEdad.set_text("")
        self.txtDireccion.set_text("")
        self.txtProfesion.set_text("")

if __name__ == '__main__':
    win = VentanaPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra
    Gtk.main()





'''

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("EjemploGtkGrid")
        self.set_size_request(200, 250) #definimos el tamaño de la ventana
        self.set_resizable(False) #indicamos que no se puede estirar la ventana

        self.maia = Gtk.Grid()

        self.boton1 = Gtk.Button(label="boton 1")
        self.boton2 = Gtk.Button(label="boton 2")
        self.boton3 = Gtk.Button(label="boton 3")
        self.boton4 = Gtk.Button(label="boton 4")
        self.boton5 = Gtk.Button(label="boton 5")
        self.boton6 = Gtk.Button(label="boton 6")
        self.boton7 = Gtk.Button(label="boton 7")
        self.boton8 = Gtk.Button(label="boton 8")
        self.boton9 = Gtk.Button(label="boton 9")
        self.boton10 = Gtk.Button(label="boton 10")
        self.boton11 = Gtk.Button(label="boton 11")
        self.boton12 = Gtk.Button(label="boton 12")


        self.maia.attach(self.boton1, 0, 0, 1, 1)
        self.maia.attach(self.boton2, 1, 0, 2, 1)
        self.maia.attach_next_to(self.boton3, self.boton1, Gtk.PositionType.BOTTOM, 1, 4)
        self.maia.attach_next_to(self.boton4, self.boton2, Gtk.PositionType.BOTTOM, 2, 3)
        self.maia.attach_next_to(self.boton5, self.boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.maia.attach_next_to(self.boton6, self.boton5, Gtk.PositionType.RIGHT, 1, 1)
        self.maia.attach_next_to(self.boton7, self.boton3, Gtk.PositionType.BOTTOM, 4, 4)

        self.maia.attach_next_to(self.boton8, self.boton7, Gtk.PositionType.BOTTOM, 2, 2)
        self.maia.attach_next_to(self.boton9, self.boton8, Gtk.PositionType.BOTTOM, 1, 1)
        self.maia.attach_next_to(self.boton10, self.boton9, Gtk.PositionType.RIGHT, 1, 1)
        self.maia.attach_next_to(self.boton11, self.boton9, Gtk.PositionType.BOTTOM, 2, 3)
        self.maia.attach_next_to(self.boton12, self.boton8, Gtk.PositionType.RIGHT, 3, 6)

        self.add(self.maia)


        self.show_all() #mostramos los elementos




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra todo
    Gtk.main()

'''