import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl


st.set_page_config(page_title='CDT')

archivo_cdt = st.sidebar.file_uploader('Choose a CSV file', type='csv')

option1 = st.selectbox(
    'Participante 1:',
    ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
)

option2 = st.selectbox(
    'Participante 2:',
    ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
)

option4 = st.selectbox(
    'Participante 3:',
    ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
)


option3 = st.selectbox(
    'Horario:',
    ('','Turno Mañana - 8:00 a 16:00','Turno Tarde - 16:00 to 00:00','Turno Noche - 00:00 to 08:00')
)

def add_note():
    # Aquí puedes agregar el código para guardar la nota en una base de datos
    st.write(f"Comentarios del Turno: {note}")
    st.write(f"Comentarios del Turno: {note2}")
    st.write(f"Comentarios del Turno: {note3}")
# Mostrar el campo de entrada de texto para agregar notas
note = st.text_input('*', key='new_note')
note2 = st.text_input('*', key='new_note2')
note3 = st.text_input('*', key='new_note3')

from PIL import Image
image = Image.open('tecnotree.jpg')
st.image(image, caption='')


from datetime import datetime

# Obtener la fecha actual
today = datetime.today().strftime('%Y-%m-%d')

# Mostrar la fecha actual en Streamlit
st.header('Service Desk - Cambio de Turno - {}'.format(today) )

# Dividir la pantalla en dos columnas
col1, col2, col3 = st.columns(3)

# Mostrar Turnos del Equipo
st.subheader('{}'.format(option3))


# Mostrar los partcipantes
with col1:
    st.subheader('{}'.format(option1))
with col2:
    st.subheader('{}'.format(option2))
with col3:
    st.subheader('{}'.format(option4))



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
        horario = st.sidebar.radio("Inicio Actividad",('','22:00','23:00','00:00','1:00','2:00'))

    st.subheader('Actividad CENAM:{}'.format(encargado))
    st.subheader('* La actividad en CENAM comienza a las : {}hs'.format(horario))

if acti_aup:
    with col1:
        encargado2 = st.sidebar.selectbox(
        'Encargado 2:',
        ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
        )
        horario2 = st.sidebar.radio("Inicio 2da Actividad",('','22:00','23:00','00:00','1:00','2:00'))

    st.subheader('---')
    st.subheader('Actividad AUP:{}'.format(encargado2))
    st.subheader('* La actividad en AUP comienza a las : {}hs'.format(horario2))

if acti_ecuador:
    with col1:
        encargado3 = st.sidebar.selectbox(
        'Encargado 3:',
        ('','Carlos Novoa', 'Gonzales Ivan', 'Pacciarioni Gastón', 'Barrionuevo Matías','Brian LLanos','Emiliano Godoy', 'Paula Aviles','Rodrigo Ginenez')
        )
        horario3 = st.sidebar.radio("Inicio 3ra Actividad",('','22:00','23:00','00:00','1:00','2:00'))
    
    st.subheader('Actividad ECUADOR:{}'.format(encargado3))
    st.subheader('La actividad en ECUADOR comienza a las : {}hs'.format(horario3))


# Leer el excel
if archivo_cdt:
    st.markdown('---')
    df = pd.read_csv(archivo_cdt, engine='python')
    # Convertir el DataFrame a una tabla HTML
    tabla_html = df.to_html(index=False)
    st.write(tabla_html, unsafe_allow_html=True)

