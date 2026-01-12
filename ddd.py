import pandas as pd
import plotly.express as px
import streamlit as st

datos= pd.read_csv('vehicles_us.csv')

st.title('Autos para la venta')
st.header('Distribución por precio')

# Primer gráfico
boton1 = st.checkbox('Construir gráfica', key="precio")
if boton1:
    st.write('Histograma por precio')
    grafico1 = px.histogram(datos, x='price')
    st.plotly_chart(grafico1, width="stretch")

st.header('Estado del vehículo')

# Segundo gráfico
boton2 = st.checkbox('Construir gráfica', key="kilometraje")
if boton2:
    st.write('Histograma kilometraje')
    grafico2 = px.histogram(datos, x="odometer")
    st.plotly_chart(grafico2, width="stretch")

st.header('Relación precio - kilometraje')

# Tercer gráfico
boton3 = st.checkbox('Construir gráfica', key="relacion")
if boton3:
    st.write('Precio vs kilometraje')
    grafico3 = px.scatter(
        datos,
        x="odometer",
        y="price",
        title='Precio vs kilometraje',
        color_discrete_sequence=["green"]
    )
    st.plotly_chart(grafico3, width="stretch")