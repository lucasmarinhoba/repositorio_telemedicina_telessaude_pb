import streamlit as st

def render_header():
    """Renderiza o cabeçalho institucional do portal."""
    html_header = '<div style="text-align: center; margin-bottom: 20px;"><h1 style="color: #0078B4; margin-bottom: 0; padding-bottom: 0;">Repositório de Apoio à Telemedicina e Telessaúde</h1><p style="font-size: 1.2rem; color: #555; margin-top: 5px;">Estado da Paraíba</p></div>'
    
    if hasattr(st, 'html'):
        st.html(html_header)
    else:
        st.markdown(html_header, unsafe_allow_html=True)
