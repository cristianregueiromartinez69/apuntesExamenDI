import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Botonera(Gtk.FlowBox):
    def __init__(self):
        super().__init__()

        self.set_valign(Gtk.Align.START)
        self.set_max_children_per_line(3)
        self.set_selection_mode(Gtk.SelectionMode.NONE)

        self.botonInserccion = Gtk.Button(label="Insertar")
        self.botonActualizar = Gtk.Button(label="Actualizar")
        self.botonBorrar = Gtk.Button(label="Borrar")
        self.botonAceptar = Gtk.Button(label="Aceptar")
        self.botonCancelar = Gtk.Button(label="Cancelar")

        self.add(self.botonInserccion)
        self.add(self.botonActualizar)
        self.add(self.botonBorrar)
        self.add(self.botonAceptar)
        self.add(self.botonCancelar)