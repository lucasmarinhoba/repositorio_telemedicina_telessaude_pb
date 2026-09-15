# Repositório de Apoio à Telemedicina e Telessaúde no Estado da Paraíba

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
[![Acesso Público](https://img.shields.io/badge/Acessar-Portal_Público-success?style=for-the-badge)](https://apoiotelemedicinapb.streamlit.app/)

Portal público destinado a centralizar, organizar e facilitar o acesso a informações, projetos e serviços oficiais relacionados à telemedicina, telessaúde e saúde digital no estado da Paraíba.

> **Nota:** Este portal não substitui os sistemas oficiais da Secretaria de Estado da Saúde (SES-PB) ou de outras instituições, mas atua como um hub centralizador para direcionar o usuário rápida e facilmente para as fontes corretas.

## 📚 Principais Funcionalidades

- **Acesso Rápido:** Barra superior com links diretos para os principais sistemas (Telessaúde SES-PB, Inserção PBCC, Tele-Estomatologia PB).
- **Página Inicial:** Tela de boas-vindas com cards de navegação para todas as seções do portal.
- **Artigos Informativos:** Conteúdos organizados por categorias sobre saúde digital e telemedicina.
- **Fluxogramas:** Diagramas visuais dos processos e fluxos de atendimento.
- **Perguntas Frequentes (FAQ):** Respostas para as dúvidas mais comuns da população e de profissionais.
- **Links e Serviços:** Catálogo completo de serviços externos e instituições parceiras.
- **Rodapé Institucional:** Logotipos das instituições parceiras (SES-PB, UFPB, PET Saúde Digital).

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Interface e Framework Web:** Streamlit
- **Armazenamento de Conteúdo:** Híbrido com JSON (para dados estruturados) e Markdown (para textos longos).
- **Hospedagem:** Streamlit Community Cloud (Deploy Contínuo atrelado ao GitHub).

## 📂 Estrutura do Projeto

```
repositorio_telemedicina_telessaude_pb/
├── app.py                  # Ponto de entrada principal da aplicação
├── requirements.txt        # Dependências do projeto
├── .streamlit/
│   └── config.toml         # Configuração do tema visual (cores e fontes)
├── components/             # Componentes visuais reutilizáveis
│   ├── header.py           # Cabeçalho institucional
│   ├── top_links_bar.py    # Barra de links externos (RF01)
│   ├── home.py             # Página inicial com cards (RF03)
│   └── footer.py           # Rodapé com logotipos (RF02)
├── utils/                  # Utilitários
│   ├── style.py            # CSS customizado
│   └── content_loader.py   # Carregamento de conteúdo JSON
├── content/                # Dados de conteúdo
│   └── links.json          # Lista de links externos
├── assets/
│   ├── logos/              # Logotipos institucionais
│   ├── images/             # Imagens gerais
│   └── flowcharts/         # Fluxogramas
├── pages/                  # Páginas adicionais (futuras)
├── tests/                  # Testes automatizados
└── docs/                   # Documentação complementar
```

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
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   streamlit run app.py
   ```
   O portal será aberto automaticamente no seu navegador em: `http://localhost:8501`.

## 📌 Progresso do Desenvolvimento

- [x] **Fase 0:** Preparação do repositório
- [x] **Fase 1:** Estrutura inicial (diretórios, app.py, requirements)
- [x] **Fase 2:** Configuração visual (tema e CSS)
- [x] **Fase 3:** Cabeçalho e barra de links externos (RF01)
- [x] **Fase 4:** Página inicial com cards de navegação (RF03)
- [x] **Fase 10:** Logotipos institucionais no rodapé (RF02)
- [ ] **Fase 5:** Página de Informações (RF04)
- [ ] **Fase 6:** Página de Fluxogramas (RF06)
- [ ] **Fase 7:** Página de Perguntas e Respostas (RF07)
- [ ] **Fase 8:** Página de Links e Serviços (RF09)
- [ ] **Fase 9:** Página Sobre + Aviso Legal (RF10)

> Para mais detalhes, consulte o arquivo [STATUS.md](STATUS.md).

## 📄 Avisos Legais e Responsabilidade

Este portal possui finalidade estritamente **informativa e educacional**. As informações aqui apresentadas não substituem, sob nenhuma circunstância, a avaliação, diagnóstico, orientação ou atendimento realizado por profissionais de saúde habilitados.
