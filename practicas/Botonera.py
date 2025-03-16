import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Botonera(Gtk.Box):
    def __init__(self):
        super().__init__()

        self.bottonInsertar = Gtk.Button(label="Insertar")
        self.bottonBorrar = Gtk.Button(label="Borrar")

        self.cajaHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.cajaHorizontal.pack_start(self.bottonInsertar, True, True, 0)
        self.cajaHorizontal.pack_start(self.bottonBorrar, True, True, 0)

        self.add(self.cajaHorizontal)