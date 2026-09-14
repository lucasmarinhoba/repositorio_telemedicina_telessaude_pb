import streamlit as st
from utils.style import apply_custom_css
from components.header import render_header
from components.top_links_bar import render_top_links_bar

st.set_page_config(
    page_title='Telemedicina PB',
    page_icon='🏥',
    layout='wide'
)

# Aplicar configurações visuais e CSS customizado
apply_custom_css()

# Renderizar Cabeçalho e Barra Superior
render_header()
render_top_links_bar()

st.write('---')
st.write('Bem-vindo ao repositório! A **Fase 3 (Cabeçalho e Links)** foi aplicada com sucesso.')
