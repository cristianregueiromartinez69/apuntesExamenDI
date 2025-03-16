import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class RegistrosGrid(Gtk.Grid):
    def __init__(self):
        super().__init__()
        self.set_row_spacing(10)
        self.set_column_spacing(10)

        self.labelDni = Gtk.Label(label="DNI")
        self.txtDni = Gtk.Entry()

        self.labelNombre = Gtk.Label(label="Nombre")
        self.txtNombre = Gtk.Entry()

        self.labelApellido = Gtk.Label(label="Apellido")
        self.txtApellido = Gtk.Entry()

        self.labelNumTelfono = Gtk.Label(label="Telefono")
        self.txtNumTelfono = Gtk.Entry()

        self.attach(self.labelDni, 0, 0, 1, 1)
        self.attach_next_to(self.txtDni,self.labelDni, Gtk.PositionType.RIGHT, 1, 1)

        self.attach_next_to(self.labelNombre,self.labelDni,Gtk.PositionType.BOTTOM ,1, 1)
        self.attach_next_to(self.txtNombre,self.labelNombre,Gtk.PositionType.RIGHT, 1, 1)

        self.attach_next_to(self.labelApellido,self.labelNombre,Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.txtApellido,self.labelApellido,Gtk.PositionType.RIGHT, 1, 1)

        self.attach_next_to(self.labelNumTelfono, self.labelApellido, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.txtNumTelfono, self.labelNumTelfono, Gtk.PositionType.RIGHT, 1, 1)

