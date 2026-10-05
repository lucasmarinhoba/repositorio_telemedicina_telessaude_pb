import streamlit as st

def render_about_section():
    """Renderiza a página 'Sobre' com as informações do projeto (RF10)."""
    st.markdown("<h2 style='color: #0078B4;'>ℹ️ Sobre o Projeto</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Conteúdo principal
    st.markdown("""
    O **PET-Saúde Informação e Saúde Digital no SUS – Paraíba** é um projeto voltado à qualificação da informação em saúde e ao uso estratégico de dados no SUS, promovendo a transformação digital e a integração entre profissionais, estudantes e serviços de saúde.
    
    Nos **GT03 - Atenção Básica** e **GT04 - Atenção Média e Alta Complexidade**, o trabalho envolve principalmente:
    * Telessaúde e Tele-estomatologia;
    * Educação permanente;
    * Letramento digital;
    * Proteção de dados pessoais;
    * Melhoria do registro e uso das informações de saúde.
    
    O projeto também busca integrar soluções como **Telessaúde PB**, **Tele-estomatologia** e **Saúde Meet**, contribuindo para um atendimento mais integrado e eficiente na Atenção Básica.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Redes sociais / Instagram
    st.markdown("""
    <div style="background-color: #F0F4F8; padding: 20px; border-radius: 10px; border-left: 5px solid #E1306C;">
        <h4 style="margin-top: 0; color: #333;">📱 Acompanhe nossas ações</h4>
        <p style="margin-bottom: 10px; color: #555;">Siga nosso Instagram para ficar por dentro das novidades, eventos e ações de letramento digital em saúde:</p>
        <a href="https://www.instagram.com/petsaude.digital/" target="_blank" style="
            display: inline-block;
            background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            text-decoration: none;
            font-weight: bold;
        ">@petsaude.digital ↗</a>
    </div>
    """, unsafe_allow_html=True)
