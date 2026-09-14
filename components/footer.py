import streamlit as st
import os
import base64

def img_to_base64(image_path):
    """Lê a imagem e converte para base64 para uso direto no HTML/CSS."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

def render_footer():
    """Renderiza o rodapé com os logotipos institucionais padronizados (RF02)."""
    st.write("---")  # Linha divisória
    
    st.markdown("<p style='text-align: center; color: #666; font-size: 0.9rem; font-weight: bold;'>Realização e Apoio Institucional:</p>", unsafe_allow_html=True)
    
    base_path = os.path.join("assets", "logos")
    
    # Carregando as imagens
    ses_pb_b64 = img_to_base64(os.path.join(base_path, "ses_pb.png"))
    ufpb_b64 = img_to_base64(os.path.join(base_path, "ufpb.png"))
    pet_b64 = img_to_base64(os.path.join(base_path, "pet_saude_digital.png"))
    
    # Todos os logos bem menores. SES e PET com 35px, UFPB com 28px (para equilibrar o formato quadrado).
    # Gap reduzido de 50px para 30px para ficarem mais próximos, centralizados.
    html_footer = f"""
    <div style="display: flex; justify-content: center; align-items: center; gap: 30px; flex-wrap: wrap; margin-top: 10px; margin-bottom: 20px;">
        <img src="data:image/png;base64,{ses_pb_b64}" alt="SES-PB" style="height: 35px; width: auto; object-fit: contain;">
        <img src="data:image/png;base64,{ufpb_b64}" alt="UFPB" style="height: 28px; width: auto; object-fit: contain;">
        <img src="data:image/png;base64,{pet_b64}" alt="PET Saúde Digital" style="height: 35px; width: auto; object-fit: contain;">
    </div>
    """
    
    if hasattr(st, 'html'):
        st.html(html_footer)
    else:
        st.markdown(html_footer, unsafe_allow_html=True)
