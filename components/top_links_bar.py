import streamlit as st
from utils.content_loader import carregar_links

def render_top_links_bar():
    """Renderiza a barra superior com os links externos (RF01)."""
    links = carregar_links()
    
    if not links:
        return
    
    # Montar HTML da barra de links
    html_links = []
    for link in links:
        html_links.append(f"""
            <a href="{link['url']}" target="_blank" rel="noopener noreferrer" style="
                display: inline-block;
                padding: 10px 20px;
                margin: 5px;
                background-color: #F0F4F8;
                color: #0078B4;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                border: 1px solid #cce4f0;
                transition: background-color 0.3s;
            ">
                {link['nome']} ↗
            </a>
        """)
    
    html_bar = f"""
    <div style="
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-bottom: 30px;
        padding: 15px 0;
        border-top: 1px solid #E0E0E0;
        border-bottom: 1px solid #E0E0E0;
    ">
        {''.join(html_links)}
    </div>
    """
    
    st.markdown(html_bar, unsafe_allow_html=True)
