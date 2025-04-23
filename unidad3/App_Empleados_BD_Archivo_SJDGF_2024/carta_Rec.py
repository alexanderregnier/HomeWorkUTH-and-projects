'''
Archivo: carta_Rec.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 14-marzo-2024

Comentarios:
• La función crearPDFCartaRec genera una carta de recomendación en formato PDF.
• Esta función implementa el uso de ReportLab. ReportLab es una biblioteca de Python que se 
utiliza para generar documentos PDF de forma dinámica.
• Para utilizar ReportLab en Python, normalmente se instala mediante pip:
    pip install reportlab
'''
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY  # 0, 1, 2, 4
from datetime import date, datetime
from tkinter import messagebox as msb
from security import safe_command


def crearPDFCartaRec(nombre_empleado:str, fecha_ingreso:str, puesto:str):
    nombre_archivo = nombre_empleado.replace(" ", "_") + "_carta.pdf"
    hoy = date.today().strftime("%d/%m/%Y")

    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    elementos = []

    # Estilos para el documento (fuente y alineaciones):
    sty_fuente = ParagraphStyle('sty_fuente', fontName='Times-Roman', fontSize=12)
    sty_titulo = ParagraphStyle('sty_titulo', fontName='Times-Roman', fontSize=16)      #  fontWeight='bold'  # fontStyle='italic'
    sty_derecha = ParagraphStyle('sty_derecha', parent=sty_fuente, alignment=TA_RIGHT)
    sty_izquierda = ParagraphStyle('sty_izquierda', parent=sty_fuente, alignment=TA_LEFT) 
    sty_centro = ParagraphStyle('sty_centro', parent=sty_fuente, alignment=TA_CENTER)
    sty_justificado = ParagraphStyle('sty_justificado', parent=sty_fuente, alignment=TA_JUSTIFY)
    sty_titulo_centrado = ParagraphStyle('sty_titulo_centrado', parent=sty_titulo, alignment=TA_CENTER)

    titulo = Paragraph("<b>Carta de Recomendación Laboral</b>", sty_titulo_centrado)
    elementos.append(titulo)
    elementos.append(Spacer(1, 12*3))

    elementos.append(Paragraph(f"Hermosillo, Sonora, México; &nbsp; a &nbsp;{hoy}.", sty_derecha))
    elementos.append(Spacer(1, 12*2))

    elementos.append(Paragraph("A quien pueda interesar:", sty_izquierda))
    elementos.append(Spacer(1, 12*2))

    elementos.append(Paragraph("Reciba un cordial y respetuoso saludo.", sty_izquierda))
    elementos.append(Spacer(1, 12))

    antiguedad = calculaAntiguedad(fecha_ingreso)

    texto = f'''
    A través de estas lineas deseo hacer de su conocimiento que <b>{nombre_empleado}</b>, 
    quien laboró en mi organización durante <b>{antiguedad}</b>, es una persona intachable. 
    Ha demostrado ser un(a) excelente empleado(a), comprometido(a), responsable y fiel 
    cumplidor(a) de sus tareas. Siempre ha manifestado preocupación por mejorar, capacitarse 
    y actualizar sus conocimientos.
    <br/><br/>
    Durante estos años se ha desempeñado como: <b>{puesto}</b>, es por ello le sugiero 
    considere esta recomendación, con la confianza de que siempre estará a la altura de sus 
    compromisos y responsabilidades.
    <br/><br/>
    Sin nada más a qué referirme y esperando que esta misiva sea tomada en cuenta, dejo mi número 
    de contacto para cualquier información de interés.
    '''
    elementos.append(Paragraph(texto, sty_justificado))
    elementos.append(Spacer(1, 12*3))

    elementos.append(Paragraph("Atentamente,", sty_izquierda))
    elementos.append(Spacer(1, 12*3))

    firma = ''' 
        _____________________________
        <br/><br/>
        Ing. José Padilla Duarte.
        <br/><br/>
        Director General. '''
    elementos.append(Paragraph(firma, sty_centro))
    elementos.append(Spacer(1, 12))

    try:
        doc.build(elementos)    # Construir el documento PDF
        # os.system(nombre_archivo )  # Abrir el documento PDF
        from subprocess import Popen
        safe_command.run(Popen, nombre_archivo, shell=True)
    except:
        msb.showwarning("Archivo ocupado", f"El documento '{nombre_archivo}' está en uso.")


def calculaAntiguedad(fecha_str:str):
    ''' Devuelve una str con el número de años, meses y días que han transcurrido desde la fecha 
    que se proporciona hasta el día de hoy. '''
    fecha_date = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    dias_antiguedad = date.today() - fecha_date
    años = int(dias_antiguedad.days / 365.25)
    meses = int((dias_antiguedad.days - años*365.25) / 30.43) 
    dias = int(dias_antiguedad.days - años*365.25 - meses*30.43)
    if años == 1:
        antiguedad = f"{años} año"
    else:
        antiguedad = f"{años} años"
    if meses == 1:
        antiguedad += f", {meses} mes y "
    else:
        antiguedad += f", {meses} meses y "
    if dias == 1:
        antiguedad += f"{dias} día"
    else:
        antiguedad += f"{dias} días"
    return antiguedad
    # return f"{años} año(s) {meses} mes(es) y {dias} día(s)"
