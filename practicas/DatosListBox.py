import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ListaDatos(Gtk.ListBoxRow):
    def __init__(self, dato):
        super().__init__()
        self.dato = dato
        self.add(Gtk.Label(label=dato))