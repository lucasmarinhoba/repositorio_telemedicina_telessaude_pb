import streamlit as st
import os

def render_footer():
    """Renderiza o rodapé com os logotipos institucionais (RF02)."""
    st.write("---")  # Linha divisória
    
    st.markdown("<p style='text-align: center; color: #666; font-size: 0.9rem; font-weight: bold;'>Realização e Apoio Institucional:</p>", unsafe_allow_html=True)
    
    # Criar colunas para alinhar os logos (ajustando a proporção de espaço entre elas)
    # Colocamos colunas vazias nas bordas para centralizar melhor os logos
    spacer_left, col1, col2, col3, spacer_right = st.columns([1, 2, 2, 2, 1])
    
    base_path = os.path.join("assets", "logos")
    
    with col1:
        if os.path.exists(os.path.join(base_path, "ses_pb.png")):
            st.image(os.path.join(base_path, "ses_pb.png"), use_container_width=True)
        else:
            st.write("Logo SES-PB pendente")
            
    with col2:
        if os.path.exists(os.path.join(base_path, "ufpb.png")):
            st.image(os.path.join(base_path, "ufpb.png"), use_container_width=True)
        else:
            st.write("Logo UFPB pendente")
            
    with col3:
        if os.path.exists(os.path.join(base_path, "pet_saude_digital.png")):
            st.image(os.path.join(base_path, "pet_saude_digital.png"), use_container_width=True)
        else:
            st.write("Logo PET Saúde pendente")
