import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DatosTreeView2(Gtk.Grid):
    def __init__(self):
        super().__init__()

        self.labelNombre = Gtk.Label(label="Nombre: ")
        self.txtNombre = Gtk.Entry()

        self.labelApellido = Gtk.Label(label="Apellido: ")
        self.txtApellido = Gtk.Entry()

        self.labelEdad = Gtk.Label(label="Edad: ")
        self.txtEdad = Gtk.Entry()

        self.comboGenero = Gtk.ComboBox()
        self.modeloCombo = Gtk.ListStore(str)
        self.datosGenero = ["masculino", "femenino", "trans de mierda"]

        for dato in self.datosGenero:
            self.modeloCombo.append((dato,))

        self.comboGenero = Gtk.ComboBox.new_with_model(model = self.modeloCombo)
        self.comboGenero.set_active(0)

        self.celdaTexto = Gtk.CellRendererText()
        self.comboGenero.pack_start(self.celdaTexto, True)
        self.comboGenero.add_attribute(self.celdaTexto, "text", 0)

        self.botonMuerto = Gtk.CheckButton(label="Muerto")

        self.attach(self.labelNombre, 0, 0, 1, 1)
        self.attach_next_to(self.txtNombre, self.labelNombre,Gtk.PositionType.RIGHT, 1, 1)

        self.attach_next_to(self.labelApellido, self.labelNombre, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.txtApellido, self.labelApellido, Gtk.PositionType.RIGHT, 1, 1)

        self.attach_next_to(self.labelEdad, self.labelApellido, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.txtEdad, self.labelEdad, Gtk.PositionType.RIGHT, 1, 1)

        self.attach_next_to(self.comboGenero, self.labelEdad, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.botonMuerto, self.comboGenero, Gtk.PositionType.RIGHT, 1, 1)