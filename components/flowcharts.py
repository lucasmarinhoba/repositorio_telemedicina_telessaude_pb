import streamlit as st
import os
from utils.content_loader import carregar_fluxogramas

def render_flowcharts_section():
    """Renderiza a seção de fluxogramas (RF06)."""
    st.markdown("<h2 style='color: #0078B4;'>🔀 Fluxogramas de Atendimento</h2>", unsafe_allow_html=True)
    st.markdown("Selecione um fluxograma abaixo para visualizar os caminhos, etapas e o diagrama completo.")
    st.write("---")
    
    fluxos = carregar_fluxogramas()
    
    if not fluxos:
        st.info("Nenhum fluxograma cadastrado no momento.")
        return

    for fluxo in fluxos:
        # Usa um expander (sanfona) para cada fluxo
        with st.expander(f"📌 {fluxo['titulo']}", expanded=False):
            st.markdown(f"<p style='color: #555; margin-bottom: 20px;'><i>{fluxo['descricao']}</i></p>", unsafe_allow_html=True)
            
            st.markdown("#### 📍 Caminhos do Fluxo")
            
            # Renderizar as etapas numeradas
            for i, etapa in enumerate(fluxo['etapas'], 1):
                st.markdown(f"**{i}.** {etapa}")
            
            st.write("---")
            st.markdown("#### 🖼️ Visualizar Diagrama")
            
            # Verificar se a imagem existe e renderizar
            if os.path.exists(fluxo['imagem']):
                st.image(fluxo['imagem'], caption=fluxo['titulo'], use_container_width=True)
            else:
                st.error(f"⚠️ Imagem não encontrada no caminho: {fluxo['imagem']}")
