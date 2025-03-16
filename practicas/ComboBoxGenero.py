import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ComboBoxGenero(Gtk.ComboBox):
    def __init__(self):
        super().__init__()

        self.generos = ["Hombre", "Mujer", "Trans leproso", "No tengo soy autista"]
        self.listStoreGeneros = Gtk.ListStore(str)

        for genero in self.generos:
            self.listStoreGeneros.append((genero,))


        self.set_model(self.listStoreGeneros)

        celdaGeneros = Gtk.CellRendererText()
        self.pack_start(celdaGeneros, True)
        self.add_attribute(celdaGeneros, "text", 0)

        self.set_active(0)
