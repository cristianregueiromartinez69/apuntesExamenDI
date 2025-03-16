import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_size_request(200, 200)
        self.set_resizable(False)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.labelNombre = Gtk.Label(label="Nombre: ")
        self.cajaVertical.pack_start(self.labelNombre, True, True, 0)

        self.txtEscribir = Gtk.Entry()
        self.cajaVertical.pack_start(self.txtEscribir, True, True, 0)

        self.btnEnter = Gtk.Button(label="Enter")
        self.btnEnter.connect("clicked", self.on_btn_clicked, self.txtEscribir, self.labelNombre)
        self.cajaVertical.pack_start(self.btnEnter, True, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

    def on_btn_clicked(self, buton, texto, label):
        if texto.get_text() == "":
            print("Escribe un texto anormal")
        else:
            label.set_label("Un saludo para: " + self.txtEscribir.get_text())
            self.txtEscribir.set_text("")







if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra
    Gtk.main()




'''

        self.set_size_request(200, 200) #definimos el tamaño de la ventana
        self.set_resizable(False) #indicamos que no se puede estirar la ventana

        self.caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10) #declaramos el layout, que será vertical
        self.add(self.caja)

  

        self.lbSaudo = Gtk.Label(label="Nombre: ")
        self.caja.pack_start(self.lbSaudo, True, True, 0)

        self.txtSaudo = Gtk.Entry()
        self.caja.pack_start(self.txtSaudo, True, True, 0)
        self.txtSaudo.connect("activate", self.saludo_boton) #activamos la tecla enter

        self.btnSaudo = Gtk.Button(label="Pulsame")
        self.caja.pack_start(self.btnSaudo, True, True, 0)

        self.btnSaudo.connect("clicked", self.saludo_boton) #conectamos el boton con una funcion
        self.show_all() #mostramos el layout


    def saludo_boton(self, button):
        if self.txtSaudo.get_text() == "":
            print("El nombre está vacío")
        else:
            self.lbSaudo.set_label("Un saludo para " + self.txtSaudo.get_text())
            self.txtSaudo.set_text("")

'''