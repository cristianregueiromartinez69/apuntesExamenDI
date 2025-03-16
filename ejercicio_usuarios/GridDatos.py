import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridDatos(Gtk.Grid):
    def __init__(self, datos):
        super().__init__()

        self.set_row_spacing(10)
        self.set_column_spacing(10)

        self.nombre_label = Gtk.Label(label="Nombre")
        self.dni_label = Gtk.Label(label="DNI")
        self.datos = datos

        self.modelo_combo = Gtk.ListStore(str)
        for dato in self.datos:
            self.modelo_combo.append(dato)

        self.combo_perfiles = Gtk.ComboBox.new_with_model(model=self.modelo_combo)
        self.celda_texto = Gtk.CellRendererText()
        self.combo_perfiles.pack_start(self.celda_texto, True)
        self.combo_perfiles.add_attribute(self.celda_texto, "text", 0)
        self.combo_perfiles.set_active(-1)

        self.nombre_text = Gtk.Entry()
        self.dni_text = Gtk.Entry()

        self.boton_insertar = Gtk.Button(label="Insertar")
        self.boton_borrar = Gtk.Button(label="Borrar")

        self.attach(self.nombre_label, 0, 0, 1, 1)
        self.attach_next_to(self.nombre_text, self.nombre_label, Gtk.PositionType.RIGHT, 1, 1)
        self.attach_next_to(self.dni_label, self.nombre_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.dni_text, self.dni_label, Gtk.PositionType.RIGHT, 1, 1)
        self.attach_next_to(self.combo_perfiles, self.dni_text, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.boton_insertar, self.combo_perfiles, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.boton_borrar, self.boton_insertar, Gtk.PositionType.RIGHT, 1, 1)
