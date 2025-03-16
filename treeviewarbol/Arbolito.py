import gi
from gi.overrides.Gtk import TreeStore

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Arbolito ejemplo")
        self.set_size_request(500, 500)
        self.set_resizable(False)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.modeloListArbol = TreeStore(str, int)

        for abuelo in range(5):
            abueloPutero = self.modeloListArbol.append(None, [f"Abuelo {abuelo}", abuelo])
            for papa in range(4):
                papaPutero = self.modeloListArbol.append(abueloPutero, [f"Padre {papa} del abuelo {abuelo}", papa])
                for hijo in range(2):
                    self.modeloListArbol.append(papaPutero, [f"Nieto{hijo} del padre {papa} del abuelo {abuelo}", hijo])

        self.vistaArbol = Gtk.TreeView(model = self.modeloListArbol)

        self.columnaParentesco = Gtk.TreeViewColumn()
        self.vistaArbol.append_column(self.columnaParentesco)
        self.celdaParentesco = Gtk.CellRendererText()
        self.columnaParentesco.pack_start(self.celdaParentesco, True)
        self.columnaParentesco.add_attribute(self.celdaParentesco, "text", 0)

        self.columnaOrden = Gtk.TreeViewColumn()
        self.vistaArbol.append_column(self.columnaOrden)
        self.celdaOrden = Gtk.CellRendererText()
        self.columnaOrden.pack_start(self.celdaOrden, True)
        self.columnaOrden.add_attribute(self.celdaOrden, "text", 1)

        self.cajaVertical.pack_start(self.vistaArbol, True, True, 0)
        self.add(self.cajaVertical)
        self.show_all()


if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()

'''

        # Creamos un contenedor vertical para organizar los widgets dentro de la ventana
        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Creamos un modelo de datos jerárquico con dos columnas: una cadena (str) y un entero (int)
        self.modelo = TreeStore(str, int)

        # Rellenamos el modelo con datos en una estructura de árbol
        for avo in range(5):  
            # Añadimos un nodo "Avo" (abuelo) de nivel superior
            punteiroAvo = self.modelo.append(None, [f"Avo {avo} ", avo])  
            for pai in range(4):
                # Añadimos un nodo "Pai" (padre) como hijo del abuelo
                punteiroPai = self.modelo.append(punteiroAvo, [f"Pai {pai} do avo {avo}", pai])  
                for fillo in range(2):
                    # Añadimos un nodo "Neto" (nieto) como hijo del padre
                    self.modelo.append(punteiroPai, [f"Neto {fillo} do pai {pai} do avo {avo}", fillo])

        # Creamos el TreeView, que se usará para mostrar la estructura jerárquica
        self.treeVista = Gtk.TreeView(model=self.modelo)

        # Primera columna del TreeView (Parentesco)
        self.treeColumna = Gtk.TreeViewColumn("Parentesco")  
        self.treeVista.append_column(self.treeColumna)  # Añadimos la columna al TreeView
        self.celdaVista = Gtk.CellRendererText()  # Definimos el renderizador de texto para la celda
        self.treeColumna.pack_start(self.celdaVista, True)  # Añadimos el renderizador a la columna
        self.treeColumna.add_attribute(self.celdaVista, 'text', 0)  # Asociamos la celda con la primera columna del modelo (texto)

        # Segunda columna del TreeView (Orden numérico)
        self.treeColumna2 = Gtk.TreeViewColumn("Orde")  
        self.treeVista.append_column(self.treeColumna2)  # Añadimos la columna al TreeView
        self.celdaVista2 = Gtk.CellRendererText()  # Renderizador de texto para la segunda columna
        self.treeColumna2.pack_start(self.celdaVista2, True)  # Añadimos el renderizador a la columna
        self.treeColumna2.add_attribute(self.celdaVista2, 'text', 1)  # Asociamos la celda con la segunda columna del modelo (números)

        # Añadimos el TreeView al contenedor vertical
        self.cajaVertical.pack_start(self.treeVista, True, True, 0)

        # Añadimos el contenedor vertical a la ventana
        self.add(self.cajaVertical)
        self.show_all()  # Mostramos todos los widgets en la ventana

# Bloque principal del programa
if __name__ == '__main__':
    win = FiestraPrincipal()  # Creamos una instancia de la ventana principal
    win.connect("destroy", Gtk.main_quit)  # Conectamos la señal de cerrar la ventana con la función que termina el programa
    Gtk.main()  # Iniciamos el bucle principal de GTK

Explicación General:

    Modelo de datos (TreeStore)
        Se usa TreeStore(str, int), lo que significa que cada fila tendrá dos valores: un texto y un número.
        Se estructura en forma de árbol con tres niveles: "Avo" (abuelo), "Pai" (padre) y "Neto" (nieto).

    TreeView y sus columnas
        Se crea un Gtk.TreeView que usa self.modelo como fuente de datos.
        Se agregan dos columnas: "Parentesco" (para nombres) y "Orde" (para números).
        Se usan Gtk.CellRendererText() para mostrar texto en ambas columnas.

    Estructura de la GUI
        Se usa un Gtk.Box vertical para organizar los elementos.
        La ventana es de tamaño fijo y no es redimensionable.

Este código crea una ventana con un TreeView que muestra una estructura jerárquica de relaciones familiares simuladas.

'''