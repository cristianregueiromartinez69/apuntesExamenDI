import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejemplo comboBox")
        self.set_size_request(400, 200)
        self.set_resizable(False)

        self.modeloDatos = Gtk.ListStore(int, str)

        self.modeloDatos.append([1, 'Ana Pérez'])
        self.modeloDatos.append([2, 'Juanita de los montes'])
        self.modeloDatos.append([3, 'Alex el niño soldado'])
        self.modeloDatos.append([4, 'Veronica cancerita'])
        self.modeloDatos.append([5, 'Moroccan mahalam'])

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.comboNombres = Gtk.ComboBox.new_with_model_and_entry(model=self.modeloDatos)
        self.comboNombres.set_entry_text_column(1)
        self.comboNombres.set_active(0)

        self.txtCadroTexto = self.comboNombres.get_child()
        self.cajaVertical.pack_start(self.comboNombres, True, True, 0)

        self.botonEnter = Gtk.Button(label="Enter")
        self.botonEnter.connect("clicked", self.on_boton_enter_clicked)
        self.cajaVertical.pack_start(self.botonEnter, True, True, 0)

        #conexiones
        self.comboNombres.connect("changed", self.on_selection_changed_combo)

        # Creamos un modelo de datos para el ComboBox de países
        self.modelo_paises = Gtk.ListStore(str)  # Solo almacena cadenas de texto
        self.paises = ["Portugal", "Irlanda", "Países Bajos", "España", "Jovenlandia", "Noruega", "China",
                       "Estados Unidos", "Suiza", "Ghana"]

        # Agregamos los países al modelo
        for pais in self.paises:
            self.modelo_paises.append((pais,))

        # Creamos el ComboBox y le asignamos el modelo de datos de países
        self.cmbPaises = Gtk.ComboBox.new_with_model(model=self.modelo_paises)

        # Creamos una celda de texto para mostrar los datos en el ComboBox
        self.celdaTexto = Gtk.CellRendererText()
        self.cmbPaises.pack_start(self.celdaTexto, True)
        self.cmbPaises.add_attribute(self.celdaTexto, "text", 0)  # Mostramos la primera columna del modelo (el país)

        # Establecemos la primera opción como seleccionada por defecto
        self.cmbPaises.set_active(0)

        self.cajaVertical.pack_start(self.cmbPaises, True, True, 0)

        # Creamos un ComboBox de selección de colores sin un modelo de datos explícito
        self.cmbColores = Gtk.ComboBoxText()
        self.cmbColores.set_entry_text_column(0)  # Indica que el texto editable está en la primera columna

        # Agregamos opciones de colores al ComboBox
        self.cmbColores.append_text("Rojo")
        self.cmbColores.append_text("Azul")
        self.cmbColores.append_text("Amarillo")
        self.cmbColores.append_text("Verde")
        self.cmbColores.append_text("Rosa")
        self.cmbColores.append_text("Negro")
        self.cmbColores.append_text("Blanco")

        # Creamos un ComboBox para seleccionar iconos
        self.cmbIconos = Gtk.ComboBox()

        # Modelo de datos para el ComboBox de iconos (nombre y referencia al icono)
        self.modeloIconos = Gtk.ListStore(str, str)
        self.modeloIconos.append(("Nuevo", "document_new"))
        self.modeloIconos.append(("Abrir", "document_open"))
        self.modeloIconos.append(("Guardar", "document_save"))

        # Asignamos el modelo al ComboBox de iconos
        self.cmbIconos.set_model(self.modeloIconos)

        # Creamos una celda de tipo icono
        self.celdaGraficos = Gtk.CellRendererPixbuf()
        self.cmbIconos.pack_start(self.celdaGraficos, True)
        self.cmbIconos.add_attribute(self.celdaGraficos, "icon_name", 1)  # Usamos la segunda columna (icono)

        # Agregamos todos los ComboBox a la caja vertical
        self.cajaVertical.pack_start(self.cmbIconos, True, True, 0)
        self.cajaVertical.pack_start(self.cmbColores, True, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

    def on_selection_changed_combo(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.modeloDatos = combo.get_model()
            idModel = self.modeloDatos[fila][0]
            nome = self.modeloDatos[fila][1]

            print("Id: " + str(idModel) + ", nome: " + str(nome))

    def on_boton_enter_clicked(self, boton):
        nombre = self.txtCadroTexto.get_text()
        if nombre is not None:
            self.modeloDatos.append([9, nombre])
            self.txtCadroTexto.set_text("")


if __name__ == '__main__':
    window = FiestraPrincipal()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()


'''

       
      

        

        # Creamos un ComboBox de selección de colores sin un modelo de datos explícito
        self.cmbColores = Gtk.ComboBoxText()
        self.cmbColores.set_entry_text_column(0)  # Indica que el texto editable está en la primera columna

        # Agregamos opciones de colores al ComboBox
        self.cmbColores.append_text("Rojo")
        self.cmbColores.append_text("Azul")
        self.cmbColores.append_text("Amarillo")
        self.cmbColores.append_text("Verde")
        self.cmbColores.append_text("Rosa")
        self.cmbColores.append_text("Negro")
        self.cmbColores.append_text("Blanco")

        # Creamos un ComboBox para seleccionar iconos
        self.cmbIconos = Gtk.ComboBox()

        # Modelo de datos para el ComboBox de iconos (nombre y referencia al icono)
        self.modeloIconos = Gtk.ListStore(str, str)
        self.modeloIconos.append(("Nuevo", "document_new"))
        self.modeloIconos.append(("Abrir", "document_open"))
        self.modeloIconos.append(("Guardar", "document_save"))

        # Asignamos el modelo al ComboBox de iconos
        self.cmbIconos.set_model(self.modeloIconos)

        # Creamos una celda de tipo icono
        self.celdaGraficos = Gtk.CellRendererPixbuf()
        self.cmbIconos.pack_start(self.celdaGraficos, True)
        self.cmbIconos.add_attribute(self.celdaGraficos, "icon_name", 1)  # Usamos la segunda columna (icono)

        # Agregamos todos los ComboBox a la caja vertical
        self.cajaVertical.pack_start(self.cmbIconos, True, True, 0)
        self.cajaVertical.pack_start(self.cmbPaises, True, True, 0)
        self.cajaVertical.pack_start(self.cmbColores, True, True, 0)

        # Agregamos la caja con los ComboBox a la ventana
        self.add(self.cajaVertical)
        self.show_all()  # Mostramos todos los elementos de la ventana

   


'''