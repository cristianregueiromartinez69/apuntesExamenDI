import gi
from gi.overrides.Gtk import TreeStore

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Arbolitos(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Arbolitos ejercicios")
        self.set_resizable(False)
        self.set_size_request(400, 400)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)

        self.modeloArbol = TreeStore(str, str, int)

        self.vistaArbol = Gtk.TreeView(model = self.modeloArbol)

        self.equipos = [
            "Real Madrid", "Barcelona", "Manchester United", "Liverpool", "Bayer Munich",
            "Milan", "Inter de Milan", "Olimpique de Lyon", "Ajax", "Nápoles"
        ]
        self.jugadores = [
            "mbappe", "rodrygo", "vinicius", "negreira", "Hernandez Hernandez", "rashford", "Maguire",
            "salah", "Alezander arnold", "kane", "Musiala", "leao", "Morata", "lukaku", "brozovic",
            "juninho", "antony", "higuain"
        ]
        self.salario = [
            100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000
        ]

        for equipo in self.equipos:
            punteroEquipo = self.modeloArbol.append(None, [equipo, "", 0])
            for i, jugador in enumerate(self.jugadores):
                punteroJugador = self.modeloArbol.append(punteroEquipo,
                                                         [equipo, jugador, 0])
                self.modeloArbol.append(punteroJugador,
                                        [equipo, jugador, self.salario[i]])

        self.columnaNombres = Gtk.TreeViewColumn()
        self.celdaNombres = Gtk.CellRendererText()
        self.vistaArbol.append_column(self.columnaNombres)
        self.columnaNombres.pack_start(self.celdaNombres, True)
        self.columnaNombres.add_attribute(self.celdaNombres, "text", 0)

        self.columnaJugadores = Gtk.TreeViewColumn()
        self.celdaJugadores = Gtk.CellRendererText()
        self.vistaArbol.append_column(self.columnaJugadores)
        self.columnaJugadores.pack_start(self.celdaJugadores, True)
        self.columnaJugadores.add_attribute(self.celdaJugadores, "text", 1)

        self.columnaMoney = Gtk.TreeViewColumn()
        self.celdaMoney = Gtk.CellRendererText()
        self.vistaArbol.append_column(self.columnaMoney)
        self.columnaMoney.pack_start(self.celdaMoney, True)
        self.columnaMoney.add_attribute(self.celdaMoney, "text", 2)

        self.cajaVertical.pack_start(self.vistaArbol, True, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

if __name__ == '__main__':
    win = Arbolitos()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()



