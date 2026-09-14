import streamlit as st
from utils.style import apply_custom_css

st.set_page_config(
    page_title='Telemedicina PB',
    page_icon='🏥',
    layout='wide'
)

# Aplicar configurações visuais e CSS customizado
apply_custom_css()

st.title('Telemedicina e Telessaúde PB')
st.write('Bem-vindo ao repositório! A **Fase 2 (Configuração Visual)** foi aplicada com sucesso.')
