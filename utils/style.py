import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        /* Esconder rodapé e cabeçalho padrão do Streamlit para um visual mais limpo */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Esconder menu lateral móvel do Streamlit (hamburguer e área lateral) */
        [data-testid="collapsedControl"] { display: none !important; }
        section[data-testid="stSidebar"] { display: none !important; }
        
        /* Ajustes de espaçamento do container principal para usar bem as laterais e o topo */
        .block-container {
            padding-top: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 1400px;
        }
        
        /* Estilo base para links institucionais */
        a {
            color: #0078B4;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)
