# Relatório de Estado Atual - Repositório de Apoio à Telemedicina e Telessaúde PB

## Visão Geral
O projeto encontra-se em desenvolvimento ativo, estruturado como uma aplicação web baseada em Python utilizando o framework Streamlit. O foco atual tem sido estabelecer a base arquitetural, identidade visual e a mecânica principal de navegação e renderização de conteúdos dinâmicos.

## Estrutura e Layout Implementados
A aplicação abandonou a barra lateral móvel padrão do Streamlit em favor de um **Layout de Colunas Fixas**:
* **Coluna Esquerda (Navegação):** Contém os links customizados em formato de texto clicável, roteando o usuário através de parâmetros de URL para simular páginas reais.
* **Coluna Direita (Conteúdo Principal):** Centraliza o Cabeçalho, a Barra de Links de Acesso Rápido, o conteúdo da página ativa e o Rodapé Institucional.

## Fases e Funcionalidades Concluídas
* **Fases 0, 1 e 2 (Base e Estilização):** Ambiente configurado, estrutura de pastas construída e identidade visual (cores, ocultação de elementos padrão) definida.
* **Fase 3 (Cabeçalho e Links Rápidos):** Componentes estáticos implementados, carregando links de sistemas externos a partir do arquivo `content/links.json`.
* **Fase 4 (Página Inicial):** Tela de boas-vindas com texto institucional implementada (a navegação por cards centrais foi descontinuada em favor do menu lateral, conforme solicitado).
* **Fase 6 (Fluxogramas):** Componente capaz de ler a base de dados `content/fluxogramas.json`, exibindo caminhos descritivos e diagramas clínicos (Paraíba contra o Câncer e Teleodontologia).
* **Fase 10 (Rodapé Institucional):** Rodapé implementado com os devidos ajustes de peso visual (CSS) para os logotipos das instituições (SES-PB, UFPB, PET Saúde Digital).

## Próximos Passos (Pendências)
* **Fase 5 (Artigos/Informações):** Criação da base de conhecimento com textos informativos sobre saúde digital.
* **Fase 7 (Perguntas Frequentes - FAQ):** Módulo de perguntas e respostas para dúvidas comuns.
* **Fase 8 (Links e Serviços):** Página dedicada listando o catálogo completo de ferramentas.
* **Fase 9 (Sobre):** Página detalhando a autoria e os objetivos do projeto.

## Considerações Técnicas
* A aplicação utiliza uma abordagem leve de dados, dispensando banco de dados relacional e utilizando apenas leitura de arquivos estáticos (`.json` e `.md`).
* O roteamento interno foi totalmente customizado via URL (query params) para entregar a experiência de navegação com menu fixo solicitada para a interface.
