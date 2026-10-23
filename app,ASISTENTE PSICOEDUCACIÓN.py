

import sqlite3

import streamlit as st

import streamlit as st
from datetime import datetime

# CONFIGURACION GENERAL
st.set_page_config(
    page_title="Mi espacio emocional",
    page_icon="🌈",
    layout="wide"
)

# COLORES Y ESTILOS
st.markdown("""
<style>
.stApp {
    background-color: #F7F5FF;
    color: #26345B;
}

h1, h2, h3 {
    color: #49347D !important;
}

p, label, .stMarkdown {
    color: #26345B;
    font-size: 18px;
    line-height: 1.7;
}

.bienvenida {
    background: linear-gradient(120deg, #D9F3FF, #F1E2FF);
    padding: 28px;
    border-radius: 22px;
    margin-bottom: 22px;
}

.tarjeta {
    padding: 22px;
    border-radius: 20px;
    min-height: 180px;
    margin-bottom: 14px;
}

.azul { background-color: #DDF2FF; }
.rosa { background-color: #FFE3EF; }
.verde { background-color: #DDF7EA; }
.amarillo { background-color: #FFF1C9; }

.stButton > button {
    border-radius: 14px;
    min-height: 48px;
    font-size: 17px;
    font-weight: bold;
    background-color: #8065D9;
    color: white;
    border: none;
    width: 100%;
}

.stButton > button:hover {
    background-color: #6048B5;
    color: white;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    font-size: 18px;
}

section[data-testid="stSidebar"] {
    background-color: #EAE5FF;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.markdown("""
<div class="bienvenida">
    <h1>🌈 ¡Hola! Este es tu espacio</h1>
    <h3>Un lugar para aprender, expresarte y cuidarte.</h3>
    <p>
    Aquí podés conocer más sobre la dislexia, registrar tus emociones
    y descubrir herramientas para tu día a día.
    </p>
</div>
""", unsafe_allow_html=True)

# MENU
seccion = st.sidebar.radio(
    "💜 Elegí una sección",
    [
        "🏠 Inicio",
        "📘 Psicoeducación",
        "💗 Registro emocional",
        "🌱 Herramientas y recursos"
    ]
)

# INICIO
if seccion == "🏠 Inicio":

    st.subheader("✨ ¿Qué te gustaría hacer hoy?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="tarjeta azul">
        <h2>📘 Psicoeducación</h2>
        <p>Aprendé sobre la dislexia con información sencilla
        y estrategias para tu vida cotidiana.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ir a Psicoeducación", key="ir_psico"):
            st.session_state.seccion_destino = "📘 Psicoeducación"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="tarjeta rosa">
        <h2>💗 Registro emocional</h2>
        <p>Identificá cómo te sentís y expresá tus emociones
        con tus propias palabras.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ir al Registro Emocional", key="ir_emociones"):
            st.session_state.seccion_destino = "💗 Registro emocional"
            st.rerun()

    st.markdown("""
    <div class="tarjeta verde">
    <h3>🌟 Recordá</h3>
    <p>Tu manera de aprender no define tu valor.
    Cada persona tiene sus tiempos, capacidades y fortalezas.</p>
    </div>
    """, unsafe_allow_html=True)

# PSICOEDUCACION
elif seccion == "📘 Psicoeducación":

    st.header("📘 Conocer la dislexia")

    st.markdown("""
    <div class="tarjeta azul">
    <h3>¿Qué es la dislexia?</h3>
    <p>Es una dificultad específica del aprendizaje que puede afectar
    la precisión o fluidez al leer y la escritura. No significa falta
    de inteligencia ni de esfuerzo.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💡 Estrategias para estudiar"):
        st.write("""
        - Dividir las tareas en pasos pequeños.
        - Usar audios y lectura en voz alta.
        - Incorporar pausas breves.
        - Utilizar textos claros y bien organizados.
        - Reconocer los avances, incluso los pequeños.
        """)

    with st.expander("💜 Cuidar las emociones"):
        st.write("""
        La frustración puede aparecer cuando una tarea resulta difícil.
        Identificar lo que sentís, pedir ayuda y descansar también
        son formas válidas de cuidarte.
        """)

# REGISTRO EMOCIONAL
elif seccion == "💗 Registro emocional":

    st.header("💗 ¿Cómo te sentís hoy?")
    st.write("Tomate un momento para reconocer cómo estás.")

    emocion = st.selectbox(
        "Elegí la emoción que más se acerca a lo que sentís",
        [
            "😊 Alegría",
            "😌 Tranquilidad",
            "😟 Preocupación",
            "😢 Tristeza",
            "😠 Enojo",
            "😰 Ansiedad",
            "😕 Confusión",
            "💭 Otra emoción"
        ]
    )

    intensidad = st.slider(
        "¿Con qué intensidad la sentís?",
        min_value=1,
        max_value=10,
        value=5
    )

    situacion = st.text_area(
        "¿Qué pasó o qué estás pensando?",
        placeholder="Podés escribir unas palabras. No hace falta contar todo.",
        key="situacion_emocional"
    )

    ayuda = st.selectbox(
        "¿Qué podría ayudarte en este momento?",
        [
            "Todavía no lo sé",
            "Descansar un momento",
            "Hablar con alguien de confianza",
            "Respirar tranquilamente",
            "Organizar la tarea en pasos pequeños",
            "Pedir ayuda"
        ]
    )

    if st.button("💾 Guardar registro", key="guardar_registro"):
        nuevo_registro = {
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "emocion": emocion,
            "intensidad": intensidad,
            "situacion": situacion,
            "ayuda": ayuda
        }

        if "registros_emocionales" not in st.session_state:
            st.session_state.registros_emocionales = []

        st.session_state.registros_emocionales.append(nuevo_registro)

        st.success("💜 Registro guardado durante esta sesión.")

    if st.session_state.get("registros_emocionales"):
        st.subheader("🌷 Tus registros de esta sesión")

        for registro in reversed(st.session_state.registros_emocionales):
            with st.expander(
                f"{registro['fecha']} · {registro['emocion']}"
            ):
                st.write(f"**Intensidad:** {registro['intensidad']}/10")
                st.write(f"**Situación:** {registro['situacion'] or 'Sin comentario'}")
                st.write(f"**Qué podría ayudar:** {registro['ayuda']}")

# HERRAMIENTAS
elif seccion == "🌱 Herramientas y recursos":

    st.header("🌱 Pequeñas herramientas para tu día")

    st.markdown("""
    <div class="tarjeta verde">
    <h3>🌬️ Pausa para respirar</h3>
    <p>Apoyá los pies en el suelo, relajá los hombros e inhalá
    suavemente. Después, exhalá sin forzar. Repetilo a tu ritmo.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tarjeta amarillo">
    <h3>📝 Organizar una tarea</h3>
    <p>1. Elegí una sola tarea.<br>
    2. Dividila en pasos pequeños.<br>
    3. Hacé una pausa cuando la necesites.<br>
    4. Reconocé lo que lograste.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Este asistente ofrece apoyo psicoeducativo. "
        "No reemplaza la evaluación ni el acompañamiento de "
        "profesionales de la salud."
    )

# PIE DE PAGINA
st.divider()
st.caption(
    "💜 Tu ritmo también es progreso. "
    "Herramienta de apoyo psicoeducativo."
)


st.set_page_config(page_title="Mi asistente emocional", page_icon="🧠")

st.title("🧠 Asistente de Psicoeducación")
st.subheader("Un espacio para reconocer tus emociones")

st.write(
    "Esta herramienta busca ayudarte a identificar y registrar "
    "tus emociones con palabras sencillas."
)

st.info(
    "Este asistente es una herramienta educativa. "
    "No realiza diagnósticos ni reemplaza la atención psicológica."
)

emocion = st.selectbox(
    "¿Cómo te sentís hoy?",
    ["Elegí una emoción", "Estoy Alegre", "Estoy Triste", "Siento Ansiedad","Siento Frustración", "Siento Enojo", " Tengo Calma"])

if emocion != "Elegí una emoción":

 st.write ( "Seleccionaste: **{emociones{emocion}**")


if emocion == "Ansiedad":
        st.info("Podés hacer una pausa y respirar lentamente.")
    
elif emocion == "Tristeza":
        st.info("Podés darte un momento para reconocer lo que sentís.")
elif emocion == "Frustración": 
         st.info("Descansá un momento y volvé a "
         "intentarlo " "de a poco. ¡Vos podés!"
       ) 

         
elif emocion == "Enojo":
 st.info("Podés detenerte un momento antes de responder.")

elif emocion == "Alegría":
        st.info("Podés disfrutar este momento y reconocer qué te hace bien.")
elif emocion == "Calma":
 st.info("Podés identificar qué te ayuda a sentirte en calma.")

st.subheader("Mi registro emocional")

              
              
              
if"registro_emocional" not in st.session_state:
 st.session_state.registro_emocional = ""

import streamlit as st

st.title("Mi asistente emocional")

respuestas = {
    "Frustración": (
        "Entiendo que te sientas frustrado. "
        "Podés descansar unos minutos y dividir "
        "la tarea en partes pequeñas."
    ),
    "Ansiedad": (
        "Entiendo que te sientas así. "
        "Podés apoyar los pies en el suelo y "
        "respirar lentamente, sin forzar la respiración."
    ),
     "Tristeza": (
        "Siento que te estés sintiendo triste. "
        "Podés descansar un momento o hablar "
        "con alguien de confianza."
    ),
    "Enojo": (
        "Parece que algo te hizo enojar. "
        "Podés hacer una pausa y volver a intentarlo "
        "cuando te sientas preparado."
    ),
    "Cansancio": 
        "Parece que necesitás descansar. "
        "Hacé una pausa y después retomá una tarea pequeña."
          ,
"Alegría": (
        "¡Qué bueno que te sientas así! "
        "Reconocé tus logros y el esfuerzo que hiciste."
    )
}

emocion = st.selectbox(
    "¿Qué emoción estás sintiendo?",
    list(respuestas.keys())
)

if st.button("Ver acompañamiento"):
    st.subheader("Estoy acá para acompañarte")
    st.write(respuestas[emocion])


registro = st.text_area(
    "¿Querés contar qué te está pasando?",
    placeholder="Podés escribir con tus propias palabras...",
    key="registro_emocional"
)


if st.button("Mostrar mi registro"):
    if registro.strip():
        st.write("Tu registro:")
        st.write(registro)
    else:
        st.warning("Primero escribí algo sobre cómo te sentís.")

if st.button("Limpiar registro"):
    st.session_state.registro_emocional = ""
    st.rerun()

    
    

st.subheader("📖 Ayuda para usar el asistente")

st.write("""
- Elegí la emoción que mejor describa cómo te sentís.
- Leé la sugerencia con tranquilidad.
- Escribí si querés contar algo más.
- No hay respuestas correctas o incorrectas.
- Podés tomarte tu tiempo.
""")


# Crear o abrir la base de datos
conexion = sqlite3.connect ("emociones.db")

# Crear una tabla para los registros
conexion.execute("""
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT DEFAULT CURRENT_TIMESTAMP,
        emocion TEXT NOT NULL,
        nota TEXT
    )
""")
# Guardar un registro de ejemplo
conexion.execute(
    "INSERT INTO registros (emocion, nota) VALUES (?, ?)",
    ("Frustración", "Me costó leer un texto")
)

conexion.commit()
conexion.close()
