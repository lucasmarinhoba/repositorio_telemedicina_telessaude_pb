import streamlit as st
from utils.style import apply_custom_css
from components.header import render_header
from components.top_links_bar import render_top_links_bar
from components.home import render_welcome, render_navigation_cards
from components.flowcharts import render_flowcharts_section
from components.footer import render_footer

st.set_page_config(
    page_title='Telemedicina PB',
    page_icon='🏥',
    layout='wide'
)

# Aplicar configurações visuais e CSS customizado
apply_custom_css()

# Cabeçalho e Barra Superior de Links Externos (sempre visíveis)
render_header()
render_top_links_bar()

# ================= MENU LATERAL =================
st.sidebar.image("assets/logos/ses_pb.png", use_container_width=True)
st.sidebar.markdown("---")
menu_opcoes = ["Início", "Fluxogramas"]
escolha = st.sidebar.radio("Navegação:", menu_opcoes)
st.sidebar.markdown("---")
# ================================================

# Roteamento simples de páginas
if escolha == "Início":
    render_welcome()
    render_navigation_cards()
elif escolha == "Fluxogramas":
    render_flowcharts_section()

# Rodapé Institucional (RF02)
render_footer()
