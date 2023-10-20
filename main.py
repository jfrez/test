import streamlit as st
cuando = st.date_input("Cuando:")
especial = st.checkbox("Especial", value=False)
feriado = st.checkbox("Feriado", value=False)
if st.button('Resultados: ' ,type="primary"):
  st.write("Hola Mundo!")
