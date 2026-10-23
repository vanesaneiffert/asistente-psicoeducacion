

import streamlit as st

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
    ["Elegí una emoción", "Alegría", "Tristeza", "Ansiedad","Frustración", "Enojo", "Calma"])

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



import sqlite3
import streamlit as st
from datetime import datetime





st.title("💛 Mi Asistente Emocional")
st.write("Registrá cómo te sentís hoy.")

emocion = st.selectbox(
    "¿Qué emoción sentís?",
    [
        "Frustración",
        "Ansiedad",
        "Tristeza",
        "Alegría",
        "Enojo",
        "Cansancio"
    ]
)

intensidad = st.slider
"Intensidad de la emoción",
    


st.button("Guardar mi emoción")
