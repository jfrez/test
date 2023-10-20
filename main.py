import streamlit as st
from streamlit_jupyter import StreamlitPatcher, tqdm
cuando = st.date_input("Cuando:")
especial = st.checkbox("Especial", value=False)
feriado = st.checkbox("Feriado", value=False)
if st.button('Resultados: ' ,type="primary"):
  st.write("Hola Mundo!")