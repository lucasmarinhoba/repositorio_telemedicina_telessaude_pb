import streamlit as st

def render_header():
    """Renderiza o cabeçalho institucional do portal."""
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #0078B4; margin-bottom: 0; padding-bottom: 0;">Repositório de Apoio à Telemedicina e Telessaúde</h1>
            <p style="font-size: 1.2rem; color: #555; margin-top: 5px;">Estado da Paraíba</p>
        </div>
        """,
        unsafe_allow_html=True
    )
