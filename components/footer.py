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
    
    # Renderizando com HTML e Flexbox para forçar que todas tenham a exata mesma altura e se auto-alinhem
    html_footer = f"""
    <div style="display: flex; justify-content: center; align-items: center; gap: 50px; flex-wrap: wrap; margin-top: 10px; margin-bottom: 30px;">
        <img src="data:image/png;base64,{ses_pb_b64}" alt="SES-PB" style="height: 65px; object-fit: contain;">
        <img src="data:image/png;base64,{ufpb_b64}" alt="UFPB" style="height: 65px; object-fit: contain;">
        <img src="data:image/png;base64,{pet_b64}" alt="PET Saúde Digital" style="height: 65px; object-fit: contain;">
    </div>
    """
    
    if hasattr(st, 'html'):
        st.html(html_footer)
    else:
        st.markdown(html_footer, unsafe_allow_html=True)
