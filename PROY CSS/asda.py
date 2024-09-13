# Crear una nueva presentación para Senku
prs_senku = Presentation()

# Definir un esquema para cada diapositiva
slides_content_senku = [
    ("Senku Ishigami: Un Líder en 'Dr. Stone'", "Análisis de las cualidades de liderazgo de Senku"),
    ("Introducción", "Breve presentación del personaje y la serie."),
    ("Intelecto y Conocimiento Científico", "Capacidad de aplicar el conocimiento científico para resolver problemas.\nInspiración y liderazgo a través de su intelecto."),
    ("Visión y Objetivos Claros", "Restaurar la civilización a través de la ciencia.\nObjetivos definidos y comprensibles para sus seguidores."),
    ("Innovación y Creatividad", "Creación de nuevas tecnologías con recursos limitados.\nCapacidad de encontrar soluciones innovadoras."),
    ("Determinación y Resolución", "Capacidad para superar obstáculos y desafíos.\nFirmeza en sus objetivos y sacrificios personales."),
    ("Trabajo en Equipo y Colaboración", "Capacidad para trabajar con otros y delegar tareas.\nInspiración y motivación de su equipo."),
    ("Conclusión", "Resumen de las cualidades de liderazgo de Senku.\nImpacto de su liderazgo en la serie."),
    ("Preguntas y Respuestas", "Espacio para discutir y responder preguntas sobre la presentación.")
]

# Añadir diapositivas según el esquema
for title, content in slides_content_senku:
    slide_layout = prs_senku.slide_layouts[1]  # Diseño de diapositiva con título y contenido
    slide = prs_senku.slides.add_slide(slide_layout)
    
    title_placeholder = slide.shapes.title
    content_placeholder = slide.placeholders[1]
    
    title_placeholder.text = title
    content_placeholder.text = content

# Guardar la presentación
pptx_file_senku = "/mnt/data/Senku_Ishigami_Lider.pptx"
prs_senku.save(pptx_file_senku)

pptx_file_senku
