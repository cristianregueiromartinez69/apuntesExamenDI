import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from DatosInserccion import DatosTreeView2
from Botonera import Botonera
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Fiestra Tree View Ordenada")
        self.set_size_request(500, 500)
        self.set_resizable(False)

        self.filtradoGenero = None


        self.cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.datosGrid = DatosTreeView2()
        self.botonera = Botonera()
        self.datosTreeView = [
            ("Alejandro", "yañez messeguer", 18, "masculino", 0),
            ("Carlos", "pascual sanchez", 34, "masculino", 1),
            ("Veronica", "prados montesinos", 25, "femenino", 1),
            ("Bob", "jhonson reller", 90, "masculino", 0),
            ("Diego", "vazquez pumez", 56, "trans de mierda", 1)
        ]

        self.modelo = Gtk.ListStore(str, str, int, str, bool)

        self.modelo_filtrado = self.modelo.filter_new()
        self.modelo_filtrado.set_visible_func(self.filtro_usuario_genero)
        self.modelo.set_sort_func(2, self.compara_modelo)


        #asignamos el array al modelo de datos liststore
        for dato in self.datosTreeView:
            self.modelo.append(dato)

        #asignamos el modelo de datos al treeview
        self.treewView = Gtk.TreeView(model=self.modelo_filtrado)

        #obtenemos la seleccion del treeview que marca el usuario
        self.seleccionTreeView = self.treewView.get_selection()

        #conectamos la señal de la seleccion del usuario
        self.seleccionTreeView.connect("changed", self.on_selection_changed_treeView)

        #-----------------------apartado dni y nombre--------------------#


        #declaramos una celda de tipo texto
        self.celdasNombreDni = Gtk.CellRendererText()

        #añadimos los datos de las filas dni y nombre a una columna
        for i, tituloColumna in enumerate(["Dni", "Nome"]):
            columna = Gtk.TreeViewColumn(tituloColumna, self.celdasNombreDni, text=i)
            self.treewView.append_column(columna)

        #------------------------apartado edad--------------------------#

        self.celdaProgressEdad = Gtk.CellRendererProgress()
        self.columnaEdad = Gtk.TreeViewColumn("Edad", self.celdaProgressEdad, value = 2)
        self.treewView.append_column(self.columnaEdad)
        self.columnaEdad.set_sort_column_id(2)

        #-----------------------------modeloCombo---------------------------·#

        self.modeloCombo = Gtk.ListStore(str)
        self.modeloCombo.append(["Mujer"])
        self.modeloCombo.append(["Hombre"])
        self.modeloCombo.append(["Trans leproso"])


        self.celdaComboGenero = Gtk.CellRendererCombo()
        self.celdaComboGenero.set_property("editable", True)
        self.celdaComboGenero.props.model = self.modeloCombo

        self.celdaComboGenero.set_property("text-column", 0)
        self.celdaComboGenero.set_property("has-entry", False)

        self.celdaComboGenero.connect("changed", self.on_genero_changed, 3)
        self.columnaGenero = Gtk.TreeViewColumn("Genero", self.celdaComboGenero, text = 3)
        self.treewView.append_column(self.columnaGenero)

        #------------------------------booleano muerto-------------------------------#

        self.celdaMuerto = Gtk.CellRendererToggle()
        self.celdaMuerto.set_property("activatable", True)
        self.columnaMuerto = Gtk.TreeViewColumn("Muerto", self.celdaMuerto, active = 4)
        self.treewView.append_column(self.columnaMuerto)


        self.celdaMuerto.connect("toggled", self.on_persona_muerta)

        #------------------------------radio buttons filtrado-----------------------------#

        self.cajaHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.radioButtonHombre = Gtk.RadioButton(label="Hombre")
        self.radioButtonMujer = Gtk.RadioButton.new_with_label_from_widget(self.radioButtonHombre, label = "Mujer")
        self.radioButtonTrans = Gtk.RadioButton.new_with_label_from_widget(self.radioButtonHombre, label = "Trans")

        self.cajaHorizontal.pack_start(self.radioButtonHombre, True, True, 0)
        self.cajaHorizontal.pack_start(self.radioButtonMujer, True, True, 0)
        self.cajaHorizontal.pack_start(self.radioButtonTrans, True, True, 0)

        self.radioButtonHombre.connect("toggled", self.on_genero_filtrado, "Hombre")
        self.radioButtonMujer.connect("toggled", self.on_genero_filtrado, "Mujer")
        self.radioButtonTrans.connect("toggled", self.on_genero_filtrado, "Trans")





        #--------------------------------------conexiones------------------------#
        self.botonera.botonInserccion.connect("clicked", self.on_insertar_datos)
        self.datosGrid.comboGenero.connect("changed", self.on_genero_combo_changed)
        self.datosGrid.botonMuerto.connect("clicked", self.on_ya_vali_wey)
        self.botonera.botonCancelar.connect("clicked", self.on_cancelar_operacion)

        #-----------------------------añadiendo cositas -------------------------#
        self.cajaPrincipal.pack_start(self.cajaHorizontal, True, True, 0)
        self.cajaPrincipal.pack_start(self.treewView, True, True, 0)
        self.cajaPrincipal.pack_start(self.datosGrid, True, True, 0)
        self.cajaPrincipal.pack_start(self.botonera, True, True, 0)
        self.add(self.cajaPrincipal)
        self.show_all()

    def on_genero_combo_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.datosGrid.modeloCombo = self.datosGrid.comboGenero.get_model()
            resultado = self.datosGrid.modeloCombo[fila][0]
            return resultado

    def on_ya_vali_wey(self, boton):
        rrsultado = boton.get_active()
        return rrsultado

    def on_insertar_datos(self, boton):
        if self.datosGrid.txtNombre.get_text() != "" and self.datosGrid.txtApellido.get_text() != "" and self.datosGrid.txtEdad.get_text() != "":
            nombre = self.datosGrid.txtNombre.get_text()
            apellidos = self.datosGrid.txtApellido.get_text()
            edad = int(self.datosGrid.txtEdad.get_text())
            genero = self.on_genero_combo_changed(self.datosGrid.comboGenero)
            muerto = bool(self.on_ya_vali_wey(self.datosGrid.botonMuerto))


            self.modelo.append((nombre, apellidos, edad, genero, muerto))
            self.limpiar_campos()



    def limpiar_campos(self):
        self.datosGrid.txtNombre.set_text("")
        self.datosGrid.txtApellido.set_text("")
        self.datosGrid.txtEdad.set_text("")

    def on_cancelar_operacion(self, boton):
        self.limpiar_campos()

    def on_selection_changed_treeView(self, treeView):
        model,iterador = treeView.get_selected()
        if iterador is not None:
            datos = model[iterador]
            print("Nombre: ", datos[0] + "\nApellidos: ", datos[1] +
                  "\nEdad: " + str(datos[2]) + "\nGenero: ", datos[3] + "\nEstado: " + str(datos[4]))

    def on_genero_changed(self, celda, fila, filaGenero, columna):
        self.modelo[fila][columna] = celda.props.model[filaGenero][0]
        newGenero = celda.props.model[filaGenero][0]
        print(newGenero)

    def filtro_usuario_genero(self, modelo, fila, datos):
        if self.filtradoGenero is None or self.filtradoGenero == "None":
            return True
        else:
            return modelo[fila][3] == self.filtradoGenero

    def on_genero_filtrado(self, radioButton, genero):
        if radioButton.get_active():
            if genero == "Hombre":
                self.filtradoGenero = "masculino"
            elif genero == "Mujer":
                self.filtradoGenero = "femenino"
            elif genero == "Trans":
                self.filtradoGenero = "trans de mierda"
            else:
                self.filtradoGenero = None
            self.modelo_filtrado.refilter()

    def on_persona_muerta(self, control, fila):
        self.modelo[fila][4] = not self.modelo[fila][4]
        print(self.modelo[fila][4])

    def compara_modelo(self, modelo, fila1, fila2):
        columna_ordenada, _ = modelo.get_sort_column_id()
        edade1 = modelo.get_value(fila1, columna_ordenada)
        edade2 = modelo.get_value(fila2, columna_ordenada)

        print(edade1, edade2)
        if edade1 < edade2:
            return -1
        elif edade1 == edade2:
            return 0
        elif edade1 > edade2:
            return 1




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()






'''
        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.base = ConexionBD("usuarios.db")

        self.filtradoGenero = None


        self.modelo = Gtk.ListStore(str, str, int, str, bool)
        self.modelo_filtrado = self.modelo.filter_new()
        self.modelo_filtrado.set_visible_func(self.filtro_usuario_xenero)
        self.modelo.set_sort_func(2, self.compara_modelo)

        self.datosbase = self.base.consultaSenParametros("SELECT * FROM usuarios2")

        for registro in self.datosbase:
            self.modelo.append(registro)

        
        self.datos = [
                    ("12345678K", "pepe", 18, "masculino", 0),
                    ("12312312H", "Javier", 30, "masculino", 1),
                    ("98778965", "Veronica", 89, "femenino", 1),
                    ("67675454", "Alejandro", 67, "masculino", 0),
                ]
        

       # self.trvDatosUsuarios = Gtk.TreeView(model = self.modelo)
        self.trvDatosUsuarios = Gtk.TreeView(model=self.modelo_filtrado)
        self.seleccion = self.trvDatosUsuarios.get_selection()
        self.seleccion.connect("changed", self.on_seleccion_changed)
        self.celdaInicio = Gtk.CellRendererText()

        for i, tituloColumna in enumerate(["Dni", "Nome"]):
            self.celdaInicio = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, self.celdaInicio, text = i)
            self.trvDatosUsuarios.append_column(columna)


        self.seleccion_ordenacion = self.trvDatosUsuarios.get_selection()


        self.celdaProgress = Gtk.CellRendererProgress()
        self.columna = Gtk.TreeViewColumn("Edade", self.celdaProgress, value = 2)
        self.trvDatosUsuarios.append_column(self.columna)
        self.columna.set_sort_column_id(2)

        self.modeloCombo = Gtk.ListStore(str)
        self.modeloCombo.append(["Muller"])
        self.modeloCombo.append(["Home"])
        self.modeloCombo.append(["No hay más"])

        self.celdaCombo = Gtk.CellRendererCombo()
        self.celdaCombo.set_property("editable", True)
        self.celdaCombo.props.model = self.modeloCombo
        self.celdaCombo.set_property("text-column", 0)
        self.celdaCombo.set_property("has-entry", False)
        self.celdaCombo.connect("changed", self.on_celdaXenero_changed, self.modelo, 3)
        self.columnagenero = Gtk.TreeViewColumn("Xenero", self.celdaCombo, text = 3)
        self.trvDatosUsuarios.append_column(self.columnagenero)

        #añadiendo a los fallecidos
        self.celdaFallecido = Gtk.CellRendererToggle()
        self.celdaFallecido.set_property("activatable", True)  # Hacer que sea interactiva
        self.columnaFallecido = Gtk.TreeViewColumn("Fallecido", self.celdaFallecido, active = 4)
        self.trvDatosUsuarios.append_column(self.columnaFallecido)

        self.cajaFiltrarHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.rbButtonHome = Gtk.RadioButton(label = "Home")
        self.rbButtonMuller = Gtk.RadioButton.new_with_label_from_widget(self.rbButtonHome, label = "Muller")
        self.rbButtonNoHayMas = Gtk.RadioButton.new_with_label_from_widget(self.rbButtonHome, label = "No hay más")

        self.cajaFiltrarHorizontal.pack_start(self.rbButtonHome, False, False, 0)
        self.cajaFiltrarHorizontal.pack_start(self.rbButtonMuller, False, False, 0)
        self.cajaFiltrarHorizontal.pack_start(self.rbButtonNoHayMas, False, False, 0)

        self.rbButtonHome.connect("toggled", self.on_genero_toggled, "Home", self.modelo_filtrado)
        self.rbButtonHome.connect("toggled", self.on_genero_toggled, "Muller", self.modelo_filtrado)
        self.rbButtonHome.connect("toggled", self.on_genero_toggled, "No hay más", self.modelo_filtrado)

        self.cajaVertical.pack_start(self.cajaFiltrarHorizontal, False, False, 0)


        self.celdaFallecido.connect("toggled", self.on_toogled_chanded, self.modelo)

        self.cajaVertical.pack_start(self.trvDatosUsuarios, False, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

    def on_seleccion_changed(self, seleccion):
        model, iterador = seleccion.get_selected()
        if iterador != None:
            dni = model[iterador][0]
            return dni

    def on_celdaXenero_changed(self, celda, fila, filaXenero, modelo, columna):
        print(celda.props.model[filaXenero][0])
        print(modelo[fila][columna])
        modelo[fila][columna] = celda.props.model[filaXenero][0]
        newGenero = celda.props.model[filaXenero][0]
        dni = self.on_seleccion_changed(self.seleccion)
        self.base.update_usuarios2(newGenero, dni)

    def on_toogled_chanded(self, control, fila, modelo):
        #modelo[fila][4] = not modelo[fila][4]
        modelo[fila][4] = False if  control.get_active() else True
        print(modelo[fila][4])
        dni = self.on_seleccion_changed(self.seleccion)
        if modelo[fila][4]:
            self.base.update_fallecido(1, dni)
        else:
            self.base.update_fallecido(0, dni)

    def on_genero_toggled(self, radioButton, genero, modelo):
        if radioButton.get_active():
            self.filtradoGenero = genero
            #self.filtradoGenero = radioButton.props.label
            self.modelo_filtrado.refilter()

    def filtro_usuario_xenero(self, modelo, fila, datos):
        if self.filtradoGenero is None or self.filtradoGenero == "None":
            return True
        else:
            return modelo[fila][3] == self.filtradoGenero

    def compara_modelo(self, modelo, fila1, fila2, datosUsuario):
        columna_ordenada, _ = modelo.get_sort_column_id()
        edade1 = modelo.get_value(fila1, columna_ordenada)
        edade2 = modelo.get_value(fila2, columna_ordenada)

        if edade1 < edade2:
            return -1
        elif edade1 == edade2:
            return 0
        elif edade1 > edade2:
            return 1

        Mostra el ultimo campo de la tabla de usuarios2 que es un bool
1. que se muestra
2. si clicamos que se cambie le modelo
3. que tenga repercusión en la tabla



if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
 '''


'''
def on_insertar_datos(self, boton):
    if self.datosGrid.txtNombre.get_text() != "" and \
       self.datosGrid.txtApellido.get_text() != "" and \
       self.datosGrid.txtEdad.get_text() != "":

        nombre = self.datosGrid.txtNombre.get_text()
        apellidos = self.datosGrid.txtApellido.get_text()

        # Convertimos edad a entero
        try:
            edad = int(self.datosGrid.txtEdad.get_text())
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            return  # Salimos del método si hay error

        genero = self.on_genero_combo_changed(self.datosGrid.comboGenero)

        # Convertimos muerto a booleano
        muerto = bool(self.on_ya_vali_wey(self.datosGrid.botonMuerto))

        # Insertamos la tupla correctamente en el modelo
        self.modelo.append((nombre, apellidos, edad, genero, muerto))

        self.limpiar_campos()

'''