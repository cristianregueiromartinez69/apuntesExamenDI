import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ConexionClasicosDB import ConexionBD

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejercicio modelos clasicos")
        self.set_resizable(False)
        self.set_size_request(550,500)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        #conexion con la base de datos
        self.base = ConexionBD("modelosClasicos.db")
        self.base.conectaBD()
        self.base.creaCursor()

        #consulta numeros de albarán
        lista_numeros = self.base.consultaSenParametros("SELECT DISTINCT numeroAlbaran FROM detalleVentas")

        #numero auxiliar albaran pulsado
        self.aux_numero_albaran = None

        #label del albarán
        self.label_albara = Gtk.Label(label = "Albará")

        #grid con los datos del albarán
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(10)
        self.grid.set_row_spacing(10)

        #labels
        self.label_numero_albara = Gtk.Label(label = "Número Albará")
        self.label_numero_cliente = Gtk.Label(label = "Número Cliente")
        self.label_nome_cliente = Gtk.Label(label = "Nome Cliente")
        self.label_data = Gtk.Label(label = "Data")
        self.label_data_entrega = Gtk.Label(label = "Data Entrega")
        self.label_apelidos= Gtk.Label(label = "Apelidos")

        #textos
        self.txt_numero_cliente = Gtk.Entry()
        self.txt_nome_cliente = Gtk.Entry()
        self.txt_data = Gtk.Entry()
        self.txt_data_entrega = Gtk.Entry()
        self.txt_apelidos = Gtk.Entry()

        #combobox del numero de albarans
        self.modelo_combobox_numero_albarans = Gtk.ListStore(int)


        #añadimos al modelo de datos del combo, los numero de albarans
        for numero in lista_numeros:
            self.modelo_combobox_numero_albarans.append(numero)

        #establecemos el combo y le metemos el model
        self.comboBox_numero_albarans = Gtk.ComboBox()
        self.comboBox_numero_albarans.set_active(0)
        self.comboBox_numero_albarans.set_model(self.modelo_combobox_numero_albarans)

        #hacemos una celda para la representacion de datos
        self.celda_textos_numero_albarans_combo = Gtk.CellRendererText()
        self.comboBox_numero_albarans.pack_start(self.celda_textos_numero_albarans_combo, True)
        self.comboBox_numero_albarans.add_attribute(self.celda_textos_numero_albarans_combo, "text", 0)

        #empezamos a añadir cosas al grid
        self.grid.attach(self.label_numero_albara, 0, 0, 1, 1)
        self.grid.attach_next_to(self.comboBox_numero_albarans, self.label_numero_albara, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.label_numero_cliente, self.label_numero_albara, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.txt_numero_cliente, self.label_numero_cliente, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.label_nome_cliente, self.label_numero_cliente, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.txt_nome_cliente, self.label_nome_cliente, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.label_data, self.comboBox_numero_albarans, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.txt_data, self.label_data, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.label_data_entrega, self.label_data, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.txt_data_entrega, self.label_data_entrega, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.label_apelidos, self.label_data_entrega, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.txt_apelidos, self.label_apelidos, Gtk.PositionType.RIGHT, 1, 1)

        #conexiones
        self.comboBox_numero_albarans.connect("changed", self.on_combo_edited)

        #añadiendo cosas al layout vertical
        self.cajaVertical.pack_start(self.label_albara, True, True, 0)
        self.cajaVertical.pack_start(self.grid, True, True, 0)


        self.add(self.cajaVertical)

        self.show_all()

    '''
    Metodo para obtener el numero pulsado en el comboBox
    Luego lo pasamos a una consulta
    Los valores devueltos los ponemos en los textos
    '''
    def on_combo_edited(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.modelo_combobox_numero_albarans = combo.get_model()
            numero = self.modelo_combobox_numero_albarans[fila][0]
            self.aux_numero_albaran = numero
            consulta = self.base.consultaConParametros("select v.numeroAlbara as numero_albaran, v.numeroCliente as numero_cliente, c.nomeCliente as nombre_cliente, v.dataAlbara as data_albaran, v.dataEntrega as data_entrega, c.apelidosCliente as apellidos_cliente from ventas v LEFT JOIN clientes c  on c.numeroCliente = v.numeroCliente WHERE v.numeroAlbara = ?", numero)

            self.establecer_valores_textos(consulta[0][1], consulta[0][2], consulta[0][3], consulta[0][4], consulta[0][5])

    '''
    Metodo para establecer los valores de los textos para la consulta
    '''
    def establecer_valores_textos(self, txt_numero_cliente, txt_nome_cliente, txt_data, txt_data_entregam, txt_apelidos):
        self.txt_numero_cliente.set_text(str(txt_numero_cliente))
        self.txt_nome_cliente.set_text(str(txt_nome_cliente))
        self.txt_data.set_text(str(txt_data))
        self.txt_data_entrega.set_text(str(txt_data_entregam))
        self.txt_apelidos.set_text(str(txt_apelidos))

if __name__ == "__main__":
    window = FiestraPrincipal()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()


'''
select v.numeroAlbara as numero_albaran,
v.numeroCliente as numero_cliente,
c.nomeCliente as nombre_cliente,
v.dataAlbara as data_albaran,
v.dataEntrega as data_entrega,
c.apelidosCliente as apellidos_cliente
from ventas v LEFT JOIN clientes c 
on c.numeroCliente = v.numeroCliente 
WHERE v.numeroAlbara = 3
'''