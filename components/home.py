import streamlit as st

def render_welcome():
    """Renderiza a seção de boas-vindas da página inicial (RF03)."""
    html = """
    <div style="text-align: center; padding: 20px 10px 30px 10px;">
        <p style="font-size: 1.1rem; color: #444; max-width: 800px; margin: 0 auto; line-height: 1.6;">
            Portal público destinado a centralizar, organizar e facilitar o acesso a informações, 
            projetos e serviços oficiais relacionados à <strong>telemedicina</strong>, 
            <strong>telessaúde</strong> e <strong>saúde digital</strong> no estado da Paraíba.
        </p>
        <p style="font-size: 0.9rem; color: #888; margin-top: 15px;">
            ⚠️ Este portal possui finalidade informativa e educacional. Não substitui atendimento profissional.
        </p>
    </div>
    """
    if hasattr(st, 'html'):
        st.html(html)
    else:
        st.markdown(html, unsafe_allow_html=True)


def render_navigation_cards():
    """Renderiza os cards de navegação para as seções do portal (RF03)."""
    
    cards = [
        {
            "icon": "📋",
            "title": "Informações",
            "description": "Artigos e conteúdos organizados por categorias sobre saúde digital e telemedicina.",
            "page": "informacoes"
        },
        {
            "icon": "🔀",
            "title": "Fluxogramas",
            "description": "Diagramas visuais dos processos e fluxos de atendimento em telessaúde.",
            "page": "fluxogramas"
        },
        {
            "icon": "❓",
            "title": "Perguntas Frequentes",
            "description": "Respostas para as dúvidas mais comuns sobre telemedicina e telessaúde.",
            "page": "faq"
        },
        {
            "icon": "🔗",
            "title": "Links e Serviços",
            "description": "Catálogo completo de serviços externos e instituições parceiras.",
            "page": "links_servicos"
        },
        {
            "icon": "ℹ️",
            "title": "Sobre",
            "description": "Objetivo do portal, contexto institucional e informações de contato.",
            "page": "sobre"
        }
    ]
    
    # Gerar os cards em HTML para controle visual total
    cards_html = ""
    for card in cards:
        cards_html += f"""
        <div style="
            background-color: #F0F4F8;
            border: 1px solid #cce4f0;
            border-radius: 12px;
            padding: 25px 20px;
            text-align: center;
            min-width: 200px;
            max-width: 220px;
            flex: 1;
            transition: transform 0.2s, box-shadow 0.2s;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">{card['icon']}</div>
            <h3 style="color: #0078B4; margin: 0 0 8px 0; font-size: 1.1rem;">{card['title']}</h3>
            <p style="color: #555; font-size: 0.85rem; margin: 0; line-height: 1.4;">{card['description']}</p>
        </div>
        """
    
    html = f"""
    <div style="
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        padding: 10px 20px 40px 20px;
    ">
        {cards_html}
    </div>
    """
    
    if hasattr(st, 'html'):
        st.html(html)
    else:
        st.markdown(html, unsafe_allow_html=True)
