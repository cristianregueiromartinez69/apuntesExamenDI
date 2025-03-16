import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Botones(Gtk.Box):
    def __init__(self):
        super().__init__()

        self.botonInserccion = Gtk.Button(label="Insercion")
        self.botonActualizar = Gtk.Button(label="Actualizar")
        self.botonBorrar = Gtk.Button(label="Borrar")
        self.botonCancelar = Gtk.Button(label="Cancelar")

        self.pack_start(self.botonInserccion, True, True, 0)
        self.pack_start(self.botonActualizar, True, True, 0)
        self.pack_start(self.botonBorrar, True, True, 0)
        self.pack_start(self.botonCancelar, True, True, 0)

