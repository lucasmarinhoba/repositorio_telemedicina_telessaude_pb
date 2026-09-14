import streamlit as st

def apply_custom_css():
    st.markdown("\""
    <style>
        /* Esconder rodapé e cabeçalho padrão do Streamlit para um visual mais limpo */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Ajustes de espaçamento do container principal para dar cara de portal */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
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
    "\"", unsafe_allow_html=True)
