import streamlit as st
from utils.style import apply_custom_css
from components.header import render_header
from components.top_links_bar import render_top_links_bar
from components.home import render_welcome
from components.flowcharts import render_flowcharts_section
from components.about import render_about_section
from components.footer import render_footer

st.set_page_config(
    page_title='Telessaúde PB',
    page_icon='🏥',
    layout='wide',
    initial_sidebar_state="collapsed"
)

# Ocultar a sidebar padrão e aplicar CSS customizado
apply_custom_css()

# Ler a página atual a partir da URL (se não tiver, o padrão é 'inicio')
page = st.query_params.get("page", "inicio")

# ================= CABEÇALHO E BARRA SUPERIOR =================
# Renderizamos fora das colunas para que no celular fiquem no topo!
render_header()
render_top_links_bar()

# ================= LAYOUT DE DUAS COLUNAS FIXAS =================
# Coluna de Menu (Esquerda) e Coluna de Conteúdo (Direita)
col_menu, col_conteudo = st.columns([1, 4], gap="large")

with col_menu:
    # white-space: nowrap e font-size ajustado evitam que a palavra "Navegação" quebre feio no celular
    st.markdown("<h2 style='color: #0078B4; margin-top: 0px; white-space: nowrap; font-size: 1.6rem;'>Navegação</h2>", unsafe_allow_html=True)
    
    # Função para criar links clicáveis bonitos simulando um menu sem quebras de linha no HTML
    def nav_link(target, label, icon=""):
        is_active = (page == target)
        bg = "#F0F4F8" if is_active else "transparent"
        weight = "bold" if is_active else "normal"
        color = "#005a87" if is_active else "#0078B4"
        border = "4px solid #0078B4" if is_active else "4px solid transparent"
        
        return f'<a href="?page={target}" target="_self" style="display: block; font-size: 1.3rem; padding: 12px 15px; margin-bottom: 5px; color: {color}; background-color: {bg}; border-left: {border}; text-decoration: none; font-weight: {weight}; border-radius: 0 8px 8px 0; transition: background-color 0.2s;">{icon} {label}</a>'

    menu_html = f'<div style="display: flex; flex-direction: column; margin-top: 10px;">{nav_link("inicio", "Início", "🏠")}{nav_link("artigos", "Artigos", "📋")}{nav_link("fluxogramas", "Fluxogramas", "🔀")}{nav_link("faq", "Dúvidas", "❓")}{nav_link("sobre", "Sobre", "ℹ️")}</div>'
    
    if hasattr(st, 'html'):
        st.html(menu_html)
    else:
        st.markdown(menu_html, unsafe_allow_html=True)

with col_conteudo:
    if page == "inicio":
        render_welcome()
    elif page == "fluxogramas":
        render_flowcharts_section()
    elif page == "sobre":
        render_about_section()
    else:
        st.info(f"Página **{page.capitalize()}** em construção (Fases futuras).")

# ================= RODAPÉ =================
st.markdown("<br><br><br>", unsafe_allow_html=True)
render_footer()
