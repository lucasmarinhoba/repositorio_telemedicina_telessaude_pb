# Repositório de Apoio à Telemedicina e Telessaúde da Paraíba

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
[![Acesso P�blico](https://img.shields.io/badge/Acessar-Portal_P�blico-success?style=for-the-badge)](https://apoiotelemedicinapb.streamlit.app/)

Portal público destinado a centralizar, organizar e facilitar o acesso a informações, projetos e serviços oficiais relacionados à telemedicina, telessaúde e saúde digital no estado da Paraíba.

> **Nota:** Este portal não substitui os sistemas oficiais da Secretaria de Estado da Saúde (SES-PB) ou de outras instituições, mas atua como um hub centralizador para direcionar o usuário rápida e facilmente para as fontes corretas.

## 📚 Principais Funcionalidades

- **Acesso Rápido:** Barra superior com links diretos para os principais sistemas (ex: Telessaúde SES-PB, Inserção PBCC, Tele-Estomatologia PB).
- **Artigos Informativos:** Conteúdos organizados por categorias sobre saúde digital e telemedicina.
- **Fluxogramas:** Diagramas visuais dos processos e fluxos de atendimento.
- **Perguntas Frequentes (FAQ):** Respostas para as dúvidas mais comuns da população e de profissionais.
- **Links e Serviços:** Catálogo completo de serviços externos e instituições parceiras.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Interface e Framework Web:** Streamlit
- **Armazenamento de Conteúdo:** Híbrido com JSON (para dados estruturados) e Markdown (para textos longos).
- **Hospedagem:** Streamlit Community Cloud (Deploy Contínuo atrelado ao GitHub).

## 🚀 Como executar o projeto localmente

### Pré-requisitos
- Python 3.11 ou superior instalado.
- Git.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/lucasmarinhoba/repositorio_telemedicina_telessaude_pb.git
   cd repositorio_telemedicina_telessaude_pb
   ```

2. **Crie e ative o ambiente virtual:**
   - No **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - No **Linux/Mac**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instale as dependências:**
   *(O arquivo `requirements.txt` completo será gerado nas próximas fases, mas a princípio, basta o streamlit)*
   ```bash
   pip install streamlit
   ```

4. **Execute a aplicação:**
   ```bash
   streamlit run app.py
   ```
   O portal será aberto automaticamente no seu navegador no endereço genérico: `http://localhost:8501`.

## 📄 Avisos Legais e Responsabilidade

Este portal possui finalidade estritamente **informativa e educacional**. As informações aqui apresentadas não substituem, sob nenhuma circunstância, a avaliação, diagnóstico, orientação ou atendimento realizado por profissionais de saúde habilitados.
