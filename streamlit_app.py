import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl
from PIL import Image
from datetime import datetime

st.set_page_config(page_title='CDT')

archivo_cdt = st.sidebar.file_uploader('Choose a CSV file', type='csv')

# Dividir la pantalla en dos columnas
col1, col2, col3 = st.columns(3)

# Mostrar los partcipantes
with col1:
    option1 = st.selectbox(
    ' Participante 1:',
    ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
)


with col2:
    option2 = st.selectbox(
    ' Participante 2:',
    ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
)


with col3:
    option4 = st.selectbox(
    ' Participante 3:',
    ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
)


def add_note():
    # Aquí puedes agregar el código para guardar la nota en una base de datos.
    st.subheader(f"Comentarios del Turno:")
    st.write(f" {note}")
    st.write(f" {note2}")
    st.write(f" {note3}")

# Mostrar el campo de entrada de texto para agregar notas
st.subheader('Comentarios del Turno👇')
note = st.text_input('', key='new_note')
note2 = st.text_input('', key='new_note2')
note3 = st.text_input('', key='new_note3')


option3 = st.sidebar.radio(
        'Horario:',
        ('','Turno Mañana - 8:00 a 16:00','Turno Tarde - 16:00 to 00:00','Turno Noche - 00:00 to 08:00')
    )

#Mostrar Imagen TN3
image = Image.open('tecnotree.jpg')
st.image(image, caption='')
st.subheader('')
st.subheader('')
# Obtener la fecha actual
today = datetime.today().strftime('%Y-%m-%d')
st.subheader('')
st.subheader('')
# Mostrar la fecha actual en Streamlit
st.header('Service Desk - Cambio de Turno - {}'.format(today) )
st.subheader('')
st.subheader('')
# Mostrar Turnos del Equipo
st.subheader('{}'.format(option3))
st.subheader('')
st.subheader('')
# Mostrar participantes
st.subheader(f"Participantes:  {option1} - {option2} - {option4}")
st.subheader('')
st.subheader('')

add_note()

st.sidebar.subheader('Actividades Service Desk')

acti_cenam = st.sidebar.checkbox('Actividad Cenam')
acti_aup = st.sidebar.checkbox('Actividad AUP')
acti_ecuador = st.sidebar.checkbox('Actividad Ecuador')


if acti_cenam:
    with col1:
        encargado = st.sidebar.selectbox(
        'Encargado:',
        ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
        )
        horario = st.sidebar.radio("Inicio Actividad CENAM",('','22:00','23:00','00:00','1:00','2:00'))

    st.subheader(f'Actividad CENAM: {encargado} ')
    st.subheader(f'La actividad en CENAM comienza a las : {horario}hs')

if acti_aup:
    with col1:
        encargado2 = st.sidebar.selectbox(
        'Encargado 2:',
        ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
        )
        horario2 = st.sidebar.radio("Inicio Actividad AUP",('','22:00','23:00','00:00','1:00','2:00'))

    st.subheader('---')
    st.subheader(f'Actividad AUP:{encargado2}')
    st.subheader(f'La actividad en AUP comienza a las : {horario2}hs')

if acti_ecuador:
    with col1:
        encargado3 = st.sidebar.selectbox(
        'Encargado 3:',
        ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
        )
        horario3 = st.sidebar.radio("Inicio Actividad ECUADOR",('','22:00','23:00','00:00','1:00','2:00'))
    
    st.subheader(f'Actividad ECUADOR:{encargado3}')
    st.subheader(f'La actividad en ECUADOR comienza a las : {horario3}hs')
    st.subheader('')

# Leer el excel
if archivo_cdt:
    st.markdown('---')
    st.subheader('')
    df = pd.read_csv(archivo_cdt, engine='python')
    # Convertir el DataFrame a una tabla HTML
    tabla_html = df.to_html(index=False)
    st.write(tabla_html, unsafe_allow_html=True)
