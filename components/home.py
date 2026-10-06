import streamlit as st

def render_welcome():
    """Renderiza a seção de boas-vindas da página inicial organizada (RF03)."""
    
    # Criando duas colunas para dividir a tela: Texto (esquerda) e Instagram (direita)
    col_texto, col_insta = st.columns([1.2, 1], gap="large")
    
    with col_texto:
        st.markdown("<h2 style='color: #0078B4; margin-top: 0;'>Bem-vindo ao Portal</h2>", unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.15rem; color: #444; line-height: 1.6; margin-bottom: 20px;">
            Este é o repositório público destinado a centralizar, organizar e facilitar o acesso a informações, 
            projetos e serviços oficiais relacionados à <strong>telemedicina</strong>, 
            <strong>telessaúde</strong> e <strong>saúde digital</strong> no estado da Paraíba.
        </p>
        """, unsafe_allow_html=True)
        
        st.info("⚠️ **Aviso Legal:** Este portal possui finalidade informativa e educacional. Não substitui atendimento profissional.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botão de atalho para a página Sobre
        st.markdown("""
        <a href="?page=sobre" target="_self" style="
            display: inline-block;
            background-color: #0078B4;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">Conhecer o Projeto ➔</a>
        """, unsafe_allow_html=True)

    with col_insta:
        st.markdown("<h3 style='color: #E1306C; margin-top: 0; text-align: center;'>📱 Conheça o PET Saúde Digital</h3>", unsafe_allow_html=True)
        
        # Incorporação oficial (Embed) da postagem do Instagram fornecida
        st.markdown("""
        <div style="display: flex; justify-content: center; width: 100%;">
            <iframe 
                src="https://www.instagram.com/p/DdolUi1HHu5/embed" 
                width="350" 
                height="500" 
                frameborder="0" 
                scrolling="no" 
                allowtransparency="true" 
                style="border: 1px solid #dbdbdb; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
            </iframe>
        </div>
        """, unsafe_allow_html=True)
