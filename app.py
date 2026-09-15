import streamlit as st
from utils.style import apply_custom_css
from components.header import render_header
from components.top_links_bar import render_top_links_bar
from components.home import render_welcome, render_navigation_cards
from components.footer import render_footer

st.set_page_config(
    page_title='Telemedicina PB',
    page_icon='🏥',
    layout='wide'
)

# Aplicar configurações visuais e CSS customizado
apply_custom_css()

# Cabeçalho e Barra Superior de Links Externos
render_header()
render_top_links_bar()

# Conteúdo da Página Inicial (RF03)
render_welcome()
render_navigation_cards()

# Rodapé Institucional (RF02)
render_footer()
