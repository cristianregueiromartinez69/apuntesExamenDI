import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ComboBoxGenero import ComboBoxGenero
class GridDatos(Gtk.Grid):
    def __init__(self):
        super().__init__()

        self.set_row_spacing(10)
        self.set_column_spacing(10)

        self.dni_label = Gtk.Label(label="DNI")
        self.nombre_label = Gtk.Label(label="Nombre")
        self.apellido_label = Gtk.Label(label="Apellido")

        self.telefono_label = Gtk.Label(label="Telefono")
        self.comboBoxgenero = ComboBoxGenero()
        self.buttonMuerto = Gtk.CheckButton(label="Muerto")

        self.dni_text = Gtk.Entry()
        self.nombre_text = Gtk.Entry()
        self.apellido_text = Gtk.Entry()
        self.telefono_text = Gtk.Entry()

        self.fondoGrid = Gtk.Grid()

        self.fondoGrid.attach(self.dni_label, 0, 0, 1, 1)
        self.fondoGrid.attach_next_to(self.dni_text, self.dni_label, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.nombre_label, self.dni_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.nombre_text, self.nombre_label, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.apellido_label, self.nombre_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.apellido_text, self.apellido_label, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.telefono_label, self.apellido_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.telefono_text, self.telefono_label, Gtk.PositionType.RIGHT, 1, 1)

        self.fondoGrid.attach_next_to(self.comboBoxgenero, self.telefono_text, Gtk.PositionType.BOTTOM, 1, 1)
        self.fondoGrid.attach_next_to(self.buttonMuerto, self.comboBoxgenero, Gtk.PositionType.BOTTOM, 1, 1)

        self.add(self.fondoGrid)