import os

from reportlab.graphics.shapes import Drawing, Line
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from modelos_clasicos.ConexionClasicosDB import ConexionBD

def imprimir_pdf(numero_albaran):

    # estilos
    estilo_parrafo_albaran = ParagraphStyle(
        name="albara",
        fontSize=10,
        fontName="Helvetica",
        textColor=colors.blue
    )

    estilo_parrafo_detalle = ParagraphStyle(
        name="detalle",
        fontSize=10,
        fontName="Helvetica",
        textColor=colors.blue
    )

    #parrafo
    parrafo_albaran = Paragraph("Albará", estilo_parrafo_albaran)
    parrafo_detalle = Paragraph("Detalle", estilo_parrafo_detalle)

    #conexion base de datos
    db = ConexionBD("modelosClasicos.db")
    db.conectaBD()
    db.creaCursor()

    consulta_primera_tabla = db.consultaConParametros(
        "SELECT a.numeroAlbara, a.dataAlbara, a.numeroCliente, a.dataEntrega, c.nomeCliente, c.apelidosCliente FROM ventas a LEFT JOIN clientes c ON c.numeroCliente = a.numeroCliente WHERE a.numeroAlbara = ?", numero_albaran)

    consulta_segunda_tabla = db.consultaConParametros(
        "SELECT d.codigoProduto as codigo_producto, p.nomeProduto as nombre_producto, d.cantidade as cantidad_producto, d.prezoUnitario as precio_producto FROM detalleVentas d LEFT JOIN produtos p on d.codigoProduto = p.codigoProduto WHERE d.numeroAlbaran = ?", numero_albaran)



    #tabla modelos clasicos
    cabecera_tabla_modelos_clasicos = ["MODELOS", "CLASICOS"]

    tabla_modelo_clasicos = Table(
        data=[cabecera_tabla_modelos_clasicos],
        colWidths=[60,60],
        rowHeights=[20]
    )
    tabla_modelo_clasicos.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.black),
        ('TEXTCOLOR', (0,0), (0,0), colors.white),
        ('BACKGROUND', (0,1), (0,1), colors.white),
        ('TEXTCOLOR', (0,1), (0,1), colors.black),
        ('BOX', (0,0), (-1, -1), 1.0, colors.black),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8)
    ]))

    #tabla albaran
    datos_primera_fila_tabla_albaran = [
        "Numero albará", consulta_primera_tabla[0][0], "Data", consulta_primera_tabla[0][1]
    ]

    datos_segunda_fila_tabla_albaran = [
        "Numero cliente", consulta_primera_tabla[0][2], "Data entrega", consulta_primera_tabla[0][3]
    ]

    datos_tercera_fila_tabla_albaran = [
        "Nome cliente", consulta_primera_tabla[0][4], "apelidos", consulta_primera_tabla[0][5]
    ]

    tabla_datos_albaran = Table(
        data=[datos_primera_fila_tabla_albaran, datos_segunda_fila_tabla_albaran, datos_tercera_fila_tabla_albaran],
        colWidths=[100, 30, 100, 75],
        rowHeights=[20,20,20]
    )

    tabla_datos_albaran.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.lightblue),
        ('BACKGROUND', (2, 0), (-1, 1), colors.blue),
        ('BOX', (0,0), (-1,-1), 1, colors.grey),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 12)
    ]))

    #tabla_datos_detalle
    cabecera_tabla_datos_detalle = ["Código producto", "Descripción", "Cantidade", "Prezo unitario"]

    datos_detalle = [cabecera_tabla_datos_detalle]
    for fila in consulta_segunda_tabla:
        datos_detalle.append(list(fila))

    tabla_detalle = Table(
        data=datos_detalle,
        colWidths=[90, 60, 90, 70]
    )

    tabla_detalle.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 1, colors.grey),
        ("BACKGROUND", (0,0), (-1, 0), colors.lightblue),
        ("INNERGRID", (0,0), (0,0), 1, colors.grey)
    ]))



    #contenido
    contenido_tabla_modelos_clasicos = [tabla_modelo_clasicos, Spacer(0,10)]
    contenido_parrafo_albaran = [parrafo_albaran, Spacer(0,10)]
    contenido_tabla_albaran = [tabla_datos_albaran, Spacer(0,10)]
    contenido_parrafo_detalle = [parrafo_detalle, Spacer(0,10)]
    contenido_tabla_detalle = [tabla_detalle, Spacer(0,10)]

    #frames
    frame_tabla_modelos_clasicos = Frame(x1=200, y1=700, width=200, height=60, showBoundary=0)
    frame_parrafo_albaran = Frame(x1=130, y1=680, width=60, height=30, showBoundary=0)
    frame_tabla_albaran = Frame(x1=100, y1=600, width=360, height=90, showBoundary=0)
    frame_parrafo_detalle = Frame(x1=130, y1=560, width=60, height=30, showBoundary=0)
    frame_tabla_detalle = Frame(x1=100, y1=420, width=369, height=150, showBoundary=0)

    def añadir_frames(canvas, doc):
        frame_tabla_modelos_clasicos.addFromList(contenido_tabla_modelos_clasicos, canvas)
        frame_parrafo_albaran.addFromList(contenido_parrafo_albaran, canvas)
        frame_tabla_albaran.addFromList(contenido_tabla_albaran, canvas)
        frame_parrafo_detalle.addFromList(contenido_parrafo_detalle, canvas)
        frame_tabla_detalle.addFromList(contenido_tabla_detalle, canvas)

    # page template
    doc = BaseDocTemplate("ejercicioAlbaran.pdf", pagesize=A4)
    plantilla = PageTemplate(id="Albarans", frames=[
        frame_tabla_modelos_clasicos,
        frame_parrafo_albaran,
        frame_tabla_albaran,
        frame_parrafo_detalle,
        frame_tabla_detalle
    ], onPage=añadir_frames)
    doc.addPageTemplates([plantilla])

    #construccion del documento
    doc.build([Spacer(0, 1)])



