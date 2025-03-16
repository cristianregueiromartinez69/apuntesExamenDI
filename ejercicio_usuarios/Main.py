import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from conexionBD import ConexionBD
from GridDatos import GridDatos

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejercicio usuarios")
        self.set_size_request(400, 400)
        self.set_resizable(False)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.base = ConexionBD("perfisUsuarios.bd")

        self.base.conectaBD()
        self.cursor = self.base.creaCursor()

        self.listaPerfiles = self.base.consultaSenParametros("SELECT nomePerfil FROM perfis")


        self.datosView = self.base.consultaSenParametros(
            "SELECT u.nome AS nome_usuario, u.dni AS dni_usuario, p.nomePerfil AS perfil_usuario FROM usuarios u LEFT JOIN perfisUsuario pu ON u.dni = pu.dniUsuario LEFT JOIN perfis p ON pu.idPerfil = p.idPefil"
        )

        self.modelo_datos = Gtk.ListStore(str, str, str)

        self.modelo_datos.set_sort_func(0, self.compara_modelo)

        self.modelo_combo = Gtk.ListStore(str)

        for dato in self.listaPerfiles:
            self.modelo_combo.append([dato[0]])

        for dato in self.datosView:
            self.modelo_datos.append([dato[0], dato[1], dato[2]])

        self.view = Gtk.TreeView(model = self.modelo_datos)
        self.object_seleccion = self.view.get_selection()
        self.auxDni = None

        self.object_seleccion.connect("changed", self.on_seleccion_view)

        self.celdaNombre = Gtk.CellRendererText()
        self.columnaNombre = Gtk.TreeViewColumn("Nome", self.celdaNombre, text = 0)
        self.view.append_column(self.columnaNombre)

        self.celdaDni = Gtk.CellRendererText()
        self.columnaDni = Gtk.TreeViewColumn("DNI", self.celdaDni, text = 1)
        self.view.append_column(self.columnaDni)

        self.renderer_combo = Gtk.CellRendererCombo()
        self.renderer_combo.set_property("editable", True)
        self.renderer_combo.set_property("model", self.modelo_combo)
        self.renderer_combo.set_property("text-column", 0)
        self.renderer_combo.set_property("has-entry", False)
        self.renderer_combo.connect("edited", self.on_combo_edited, self.modelo_datos)

        self.columnaCombo = Gtk.TreeViewColumn("Perfil", self.renderer_combo, text = 2)
        self.view.append_column(self.columnaCombo)

        self.datos_insertar = GridDatos(self.listaPerfiles)
        self.datos_insertar.combo_perfiles.connect("changed", self.on_combo_datos_connect)
        self.datos_insertar.boton_insertar.connect("clicked", self.on_inserccion_view)

        self.aux_tipo_perfil_datos = None
        self.cajaVertical.pack_start(self.view, True, True, 0)
        self.cajaVertical.pack_start(self.datos_insertar, True, True, 0)
        self.add(self.cajaVertical)

        self.show_all()

    def on_combo_edited(self, widget, path, new_text, model):
        model[path][2] = new_text
        print(model[path][2])
        print(self.auxDni)
        self.base.consultaConParametros(
            "UPDATE perfis SET nomePerfil = ? WHERE idPefil in (SELECT idPerfil FROM perfisUsuario WHERE dniUsuario = ?)",
            model[path][2], self.auxDni
        )

        print(model[path][2])

    def on_seleccion_view(self, selection):
        modelo, fila = selection.get_selected()
        if fila is not None:
            nombre = modelo[fila][0]
            dni = modelo[fila][1]
            self.auxDni = dni
            tipoPerfil = modelo[fila][2]
            print("Nombre: " + nombre + " Dni: " + dni + " Tipo Perfil: " + tipoPerfil)

    def compara_modelo(self, modelo, fila1, fila2, columna_ordenada):
        nombre1 = modelo[fila1][columna_ordenada]
        nombre2 = modelo[fila2][columna_ordenada]
        print("Nombre1: " + nombre1 + " Nombre2: " + nombre2)

        if nombre1 < nombre2:
            return -1
        elif nombre1 == nombre2:
            return 0
        else:
            return 1

    def on_combo_datos_connect(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.datos_insertar.modelo_combo = self.datos_insertar.combo_perfiles.get_model()
            tipo_perfil = self.datos_insertar.modelo_combo[fila][0]
            self.aux_tipo_perfil_datos = tipo_perfil


    def on_inserccion_view(self, boton):
        if self.datos_insertar.dni_text != "" and self.datos_insertar.nombre_text != "" and self.aux_tipo_perfil_datos is not None:
            nombre = self.datos_insertar.nombre_text.get_text()
            dni = self.datos_insertar.dni_text.get_text()
            tipoPerfil = self.aux_tipo_perfil_datos
            self.modelo_datos.append([nombre, dni, tipoPerfil])

            dato_id_ordenado = self.base.consultaSenParametros("SELECT idPefil FROM perfis ORDER BY idPefil DESC")

            aux_dato_id_ordenado = None
            for i in range(len(dato_id_ordenado)):
                aux_dato_id_ordenado = dato_id_ordenado[i]
                break

            new_dato_id = int(aux_dato_id_ordenado[0]) + 1

            self.base.engadeRexistro("INSERT INTO usuarios(nome, dni, departamento, correoe, activo) values (?,?,?,?,?)", nombre, dni, "Calidade", "ejemplocorreo@hotmail.com", 1)

            self.base.engadeRexistro("INSERT INTO perfis(idPefil, nomePerfil, descricion) VALUES (?, ?, ?)", new_dato_id, tipoPerfil, "Descripcion de prueba")

            self.base.engadeRexistro("INSERT INTO perfisUsuario(dniUsuario, idPerfil, permiso) VALUES (?, ?, ?)", dni, new_dato_id, 2)


            print("Datos insertados correctamente")
            self.limpiar_campos()
        else:
            print("Inserta todos los datos por favor :)")

    def limpiar_campos(self):
        self.datos_insertar.nombre_text.set_text("")
        self.datos_insertar.dni_text.set_text("")
        self.datos_insertar.combo_perfiles.set_active(-1)





if __name__ == "__main__":
    window = FiestraPrincipal()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()