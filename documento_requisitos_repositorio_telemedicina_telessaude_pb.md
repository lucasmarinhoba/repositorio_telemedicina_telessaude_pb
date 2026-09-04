# Documento de Requisitos
## Repositório de Apoio à Telemedicina e Telessaúde da Paraíba

**Versão:** 2.0  
**Data:** setembro de 2026  
**Status:** Planejamento / Especificação inicial  
**Linguagem preferencial:** Python  
**Proposta de framework:** Streamlit  
**Hospedagem inicial:** Streamlit Community Cloud + GitHub

---

# 1. Identificação do projeto

## 1.1. Nome

**Repositório de Apoio à Telemedicina e Telessaúde da Paraíba**

Nome curto para uso na interface:

**Telemedicina e Telessaúde PB**

Nome sugerido para o repositório GitHub:

`repositorio-telemedicina-telessaude-pb`

---

# 2. Contexto do projeto

O projeto consiste no desenvolvimento de um portal público destinado a centralizar, organizar e facilitar o acesso a informações relacionadas à telemedicina, telessaúde e saúde digital na Paraíba.

A proposta é criar um ponto de entrada único para informações, materiais, projetos, serviços, fluxogramas, imagens, perguntas e respostas e links para plataformas externas relacionadas ao tema.

O portal não deverá substituir os sistemas oficiais. Seu papel será atuar como um **repositório de apoio e organização da informação**, direcionando o usuário para as fontes e serviços apropriados.

Entre os recursos externos que deverão estar disponíveis no portal estão:

- Telessaúde SES-PB — https://telessaude.ses.pb.gov.br/
- Inserção PBCC — https://insercaopbcc.com/
- Tele-Estomatologia PB — https://tele-estomatologia-pb.glide.page/

A lista de links deverá ser expansível para permitir a inclusão de novos projetos, sistemas e instituições.

---

# 3. Justificativa

Informações relacionadas à telemedicina e telessaúde podem estar distribuídas entre diferentes instituições, projetos, páginas e documentos.

Isso dificulta a localização de informações por usuários que não conhecem previamente os sistemas existentes.

O portal pretende reduzir essa dificuldade por meio de uma interface simples, visual e organizada.

A proposta é semelhante, em conceito de navegação, a um portal de informações: o usuário entra no site, encontra uma barra superior com os principais serviços externos e, na página, acessa conteúdos organizados por assunto.

---

# 4. Objetivo geral

Desenvolver um portal web público, gratuito, simples e visualmente agradável para reunir e disponibilizar informações de apoio sobre telemedicina e telessaúde na Paraíba.

---

# 5. Objetivos específicos

O sistema deverá:

1. Centralizar informações relacionadas à telemedicina e telessaúde na Paraíba.
2. Facilitar a localização de serviços e projetos existentes.
3. Disponibilizar imagens e materiais gráficos.
4. Disponibilizar fluxogramas.
5. Disponibilizar uma seção de perguntas e respostas.
6. Reunir links para sistemas e projetos externos.
7. Destacar as instituições e projetos relacionados ao portal por meio de seus logotipos.
8. Ser acessível publicamente pela Internet.
9. Não depender de `localhost` para acesso dos usuários.
10. Utilizar Python como principal linguagem.
11. Utilizar inicialmente ferramentas gratuitas.
12. Possibilitar expansão futura para busca inteligente e chatbot.

---

# 6. Público-alvo

O portal deverá ser desenvolvido para diferentes perfis de usuários.

## Público primário

- profissionais da saúde;
- estudantes;
- pesquisadores;
- gestores;
- profissionais envolvidos com telessaúde;
- participantes de projetos de saúde digital.

## Público secundário

- população em geral;
- pessoas interessadas em telemedicina;
- instituições de ensino;
- instituições de saúde;
- outros projetos e pesquisadores relacionados ao tema.

A interface deverá assumir que o usuário pode não possuir conhecimento técnico sobre telemedicina ou informática.

---

# 7. Conceito da interface

O portal deverá seguir uma proposta visual:

> **Institucional + moderna + simples + informativa**

A interface não deverá parecer um sistema administrativo complexo.

Deverá transmitir:

- saúde;
- tecnologia;
- confiabilidade;
- organização;
- acessibilidade.

---

# 8. Estrutura geral da página inicial

A página inicial deverá seguir aproximadamente a seguinte hierarquia:

```text
┌────────────────────────────────────────────────────────────┐
│ LOGO / NOME DO PROJETO                                     │
├────────────────────────────────────────────────────────────┤
│ Telessaúde SES-PB │ Inserção PBCC │ Tele-Estomatologia PB │
├────────────────────────────────────────────────────────────┤
│                                                            │
│       REPOSITÓRIO DE APOIO À TELEMEDICINA                 │
│              E TELESSAÚDE DA PARAÍBA                      │
│                                                            │
│      Informação, serviços, projetos e materiais            │
│                                                            │
│                 [ Explorar conteúdos ]                     │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│   📚 Informações    🔄 Fluxogramas    ❓ Perguntas          │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                 CONTEÚDOS EM DESTAQUE                      │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│              INSTITUIÇÕES / APOIO                          │
│                                                            │
│     [SES-PB]       [UFPB]       [PET Saúde Digital]        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

# 9. Barra superior de links

## RF01 — Barra de serviços externos

O site deverá possuir uma barra horizontal na região superior da página, inspirada na lógica de navegação de grandes portais de notícias, como o G1.

A finalidade da barra será fornecer acesso rápido aos principais serviços e projetos externos.

### Links iniciais

**Telessaúde SES-PB**

https://telessaude.ses.pb.gov.br/

**Inserção PBCC**

https://insercaopbcc.com/

**Tele-Estomatologia PB**

https://tele-estomatologia-pb.glide.page/

---

## RF01.1 — Comportamento

Cada item da barra deverá funcionar como um link clicável.

Ao clicar, o usuário deverá ser direcionado ao respectivo serviço externo.

Preferencialmente, os links deverão abrir em uma nova aba, evitando que o usuário perca o portal.

---

## RF01.2 — Expansibilidade

A barra deverá ser construída de forma que novos links possam ser adicionados posteriormente.

Exemplo:

```text
TELessaúde SES-PB
Inserção PBCC
Tele-Estomatologia
Projeto X
Projeto Y
Documentos
```

Os links não deverão ficar espalhados diretamente pelo código principal da aplicação.

Recomenda-se armazená-los em uma estrutura de conteúdo, como:

```text
content/links.json
```

---

# 10. Identidade institucional

## RF02 — Área de logotipos

O portal deverá possuir uma área destinada aos logotipos das instituições e projetos associados.

Inicialmente deverão existir espaços para:

1. **Secretaria de Estado da Saúde da Paraíba — SES-PB**
2. **Universidade Federal da Paraíba — UFPB**
3. **PET Saúde Digital**

A área poderá ficar:

- no cabeçalho;
- próxima ao título;
- ou no rodapé.

### Recomendação

A solução preferencial é utilizar:

```text
Cabeçalho:
Nome do portal

Conteúdo:
...

Rodapé:
Apoio / Instituições
[SES-PB] [UFPB] [PET Saúde Digital]
```

Isso evita que os logotipos concorram visualmente com o conteúdo principal.

---

# 11. Regras para os logotipos

Os logotipos deverão:

- manter suas proporções originais;
- possuir boa resolução;
- possuir espaço visual adequado;
- possuir identificação textual quando necessário;
- não sofrer distorção;
- respeitar as regras de uso das respectivas marcas.

Os arquivos poderão ficar em:

```text
assets/
└── logos/
    ├── ses_pb.png
    ├── ufpb.png
    └── pet_saude_digital.png
```

Os arquivos oficiais dos logotipos deverão ser obtidos de fontes autorizadas pelas respectivas instituições.

---

# 12. Navegação principal

O portal deverá possuir as seguintes áreas:

```text
Início
Informações
Fluxogramas
Perguntas e Respostas
Links e Serviços
Sobre
```

A navegação deverá permanecer simples.

---

# 13. RF03 — Página inicial

A página inicial deverá apresentar:

- nome do projeto;
- descrição resumida;
- acesso aos principais conteúdos;
- destaque para os serviços externos;
- área de instituições/projetos associados.

---

# 14. RF04 — Página de informações

Deverá existir uma área para conteúdos informativos.

Possíveis categorias:

```text
Informações
│
├── Telemedicina
├── Telessaúde
├── Saúde Digital
├── Serviços
├── Projetos
├── Educação
├── Pesquisa
└── Legislação
```

As categorias poderão ser modificadas conforme o desenvolvimento do projeto.

---

# 15. RF05 — Imagens

O portal deverá permitir a apresentação de imagens relacionadas ao conteúdo.

Exemplos:

- imagens institucionais;
- infográficos;
- diagramas;
- ilustrações;
- imagens de projetos;
- materiais educacionais.

Quando aplicável, deverão ser apresentadas:

- título;
- descrição;
- fonte;
- créditos.

---

# 16. RF06 — Fluxogramas

Deverá existir uma seção específica para fluxogramas.

Os fluxogramas deverão representar processos relacionados à telessaúde e telemedicina.

Exemplo conceitual:

```text
              INÍCIO
                 │
                 ▼
        Necessidade de atendimento
                 │
                 ▼
        Serviço de telessaúde?
             /       \
           SIM        NÃO
            │          │
            ▼          ▼
      Teleatendimento  Fluxo
            │         presencial
            ▼
       Atendimento
            │
            ▼
           FIM
```

Na primeira versão, os fluxogramas poderão ser imagens ou SVG.

No futuro poderão se tornar componentes interativos.

---

# 17. RF07 — Perguntas e Respostas

O sistema deverá possuir uma seção de perguntas e respostas.

A primeira versão poderá utilizar perguntas previamente cadastradas.

Exemplos:

### O que é telessaúde?

Resposta explicativa em linguagem acessível.

### O que é telemedicina?

Resposta explicativa baseada em fontes confiáveis.

### Qual a diferença entre telemedicina e telessaúde?

Resposta comparativa.

### Onde encontro os serviços de telessaúde da Paraíba?

Apresentação dos links relevantes.

---

# 18. RF08 — Busca

Recomenda-se que o portal possua uma busca simples desde uma versão inicial ou, no máximo, em uma segunda etapa.

Exemplo:

```text
┌───────────────────────────────────────────┐
│ 🔎 Pesquisar no repositório...            │
└───────────────────────────────────────────┘
```

A pesquisa deverá futuramente procurar em:

- artigos;
- FAQ;
- documentos;
- projetos;
- serviços;
- informações.

---

# 19. RF09 — Links e Serviços

Deverá existir uma página dedicada aos recursos externos.

Cada recurso poderá possuir:

```text
Título
Descrição
Instituição
Link
```

Exemplo:

```text
TELessaúde SES-PB

Serviço relacionado à telessaúde no estado da Paraíba.

[ Acessar serviço ]
```

---

# 20. RF10 — Página Sobre

A página deverá apresentar:

- objetivo do projeto;
- contexto;
- instituições envolvidas;
- fontes de informação;
- aviso de caráter informativo;
- informações sobre atualização do conteúdo.

---

# 21. Responsabilidade sobre o conteúdo

Como o projeto envolve saúde, o portal deverá deixar claro que seus conteúdos possuem caráter informativo.

Deverá existir aviso semelhante a:

> **Este portal possui finalidade informativa e educacional. As informações aqui apresentadas não substituem avaliação, diagnóstico, orientação ou atendimento realizado por profissionais de saúde.**

O texto definitivo deverá ser revisado pelos responsáveis pelo projeto.

---

# 22. Requisitos não funcionais

## RNF01 — Acesso público

O site deverá estar disponível pela Internet.

Não deverá exigir que o usuário execute:

```text
localhost
127.0.0.1
```

A aplicação deverá possuir uma URL pública.

---

# 23. RNF02 — Gratuidade

A primeira versão deverá utilizar serviços gratuitos.

Arquitetura inicial:

```text
GitHub
   │
   ▼
Streamlit Community Cloud
   │
   ▼
URL pública
   │
   ▼
Usuários
```

O Streamlit Community Cloud oferece hospedagem gratuita e integração com repositórios GitHub. A documentação oficial informa que as aplicações podem ser publicadas e compartilhadas publicamente. 

---

# 24. RNF03 — Linguagem

A linguagem principal deverá ser:

**Python**

---

# 25. RNF04 — Responsividade

O portal deverá funcionar em:

- computadores;
- notebooks;
- tablets;
- smartphones.

A interface deverá ser adaptada para telas menores.

---

# 26. RNF05 — Acessibilidade

O sistema deverá considerar:

- contraste adequado;
- fontes legíveis;
- organização clara;
- textos alternativos para imagens;
- navegação simples;
- não depender somente de cores;
- compatibilidade com dispositivos móveis.

---

# 27. RNF06 — Desempenho

A primeira versão deverá evitar:

- imagens excessivamente grandes;
- bibliotecas desnecessárias;
- vídeos pesados hospedados diretamente no projeto;
- processamento excessivo durante a abertura da página.

---

# 28. Arquitetura tecnológica

## Stack inicial

| Camada | Tecnologia |
|---|---|
| Linguagem | Python |
| Framework web | Streamlit |
| Controle de versão | Git |
| Repositório | GitHub |
| Hospedagem | Streamlit Community Cloud |
| Conteúdo inicial | JSON/Markdown |
| Imagens | PNG/JPG/WebP |
| Fluxogramas | SVG/PNG |
| Banco de dados | Não necessário no MVP |

A documentação oficial do Streamlit descreve o Community Cloud como uma plataforma gratuita que se conecta diretamente ao GitHub e permite publicar aplicações. 

---

# 29. Estrutura do projeto

Estrutura inicial recomendada:

```text
repositorio-telemedicina-telessaude-pb/
│
├── app.py
│
├── pages/
│   ├── 1_Informacoes.py
│   ├── 2_Fluxogramas.py
│   ├── 3_Perguntas_e_Respostas.py
│   ├── 4_Links_e_Servicos.py
│   └── 5_Sobre.py
│
├── content/
│   ├── informacoes.json
│   ├── faq.json
│   └── links.json
│
├── assets/
│   ├── logos/
│   │   ├── ses_pb.png
│   │   ├── ufpb.png
│   │   └── pet_saude_digital.png
│   │
│   ├── images/
│   │
│   └── flowcharts/
│
├── components/
│   ├── header.py
│   ├── top_links.py
│   ├── cards.py
│   └── footer.py
│
├── utils/
│   └── helpers.py
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 30. Organização dos links

Os links deverão ficar separados da lógica da aplicação.

Exemplo conceitual:

```json
[
  {
    "nome": "Telessaúde SES-PB",
    "url": "https://telessaude.ses.pb.gov.br/",
    "descricao": "Portal de Telessaúde da Secretaria de Estado da Saúde da Paraíba"
  },
  {
    "nome": "Inserção PBCC",
    "url": "https://insercaopbcc.com/",
    "descricao": "Projeto/serviço relacionado"
  },
  {
    "nome": "Tele-Estomatologia PB",
    "url": "https://tele-estomatologia-pb.glide.page/",
    "descricao": "Projeto de Tele-Estomatologia da Paraíba"
  }
]
```

A descrição deverá ser revisada de acordo com as informações oficiais de cada serviço.

---

# 31. Organização do FAQ

O FAQ deverá seguir estrutura semelhante:

```json
[
  {
    "pergunta": "O que é telessaúde?",
    "resposta": "..."
  },
  {
    "pergunta": "O que é telemedicina?",
    "resposta": "..."
  }
]
```

Isso permitirá adicionar perguntas sem modificar a estrutura principal do site.

---

# 32. Banco de dados

## MVP

Não será utilizado banco de dados.

A decisão tem como objetivo manter o projeto:

- simples;
- gratuito;
- fácil de desenvolver;
- fácil de hospedar;
- fácil de manter.

Os conteúdos poderão ser armazenados em:

- JSON;
- Markdown;
- arquivos de imagem;
- SVG.

## Futuro

Caso o projeto necessite de:

- painel administrativo;
- usuários;
- autenticação;
- edição online;
- histórico;
- grande volume documental;
- estatísticas;
- chatbot;

poderá ser introduzido um banco de dados.

Uma possibilidade futura seria PostgreSQL.

---

# 33. Chat futuro

O sistema deverá ser desenvolvido com possibilidade de receber posteriormente um chat.

A arquitetura deverá permitir a seguinte evolução:

```text
VERSÃO 1

Portal
 ├── Informações
 ├── FAQ
 ├── Fluxogramas
 └── Links


VERSÃO 2

Portal
 ├── Informações
 ├── FAQ
 ├── Fluxogramas
 ├── Busca
 └── Documentos


VERSÃO 3

Portal
 ├── Conteúdo
 ├── Busca
 └── Chat
       │
       ▼
    Base de conhecimento
       │
       ▼
      IA
```

---

# 34. Possível arquitetura do chatbot

No futuro, recomenda-se utilizar uma arquitetura de RAG — Retrieval-Augmented Generation.

Fluxo:

```text
Usuário
   │
   ▼
Pergunta
   │
   ▼
Sistema de busca
   │
   ▼
Base de conhecimento
   │
   ├── FAQ
   ├── Documentos
   ├── Informações
   └── Projetos
   │
   ▼
Contexto recuperado
   │
   ▼
Modelo de IA
   │
   ▼
Resposta
   │
   ▼
Fonte / referência
```

Isso permitiria que o chat respondesse com base nos conteúdos disponibilizados no próprio repositório.

---

# 35. Requisitos do futuro chatbot

O chatbot deverá:

- aceitar perguntas em linguagem natural;
- pesquisar a base de conhecimento;
- apresentar respostas em linguagem acessível;
- indicar as fontes utilizadas;
- evitar respostas sem base documental;
- direcionar o usuário para serviços oficiais quando apropriado.

O chatbot não deverá ser tratado como substituto de atendimento médico.

---

# 36. Segurança e privacidade

O MVP deverá evitar coleta desnecessária de dados pessoais.

Não deverá existir necessidade de cadastro de usuário para acessar os conteúdos públicos.

Caso funcionalidades futuras exijam dados pessoais, deverão ser avaliados:

- finalidade da coleta;
- necessidade;
- armazenamento;
- segurança;
- política de privacidade;
- requisitos legais aplicáveis.

---

# 37. Critérios de aceitação do MVP

O MVP será considerado concluído quando:

- [ ] O portal possuir uma URL pública.
- [ ] O portal funcionar sem `localhost`.
- [ ] A página inicial estiver implementada.
- [ ] Existir barra superior de links.
- [ ] A barra possuir os três links inicialmente definidos.
- [ ] Os links externos funcionarem.
- [ ] Existir área de informações.
- [ ] Existir área de fluxogramas.
- [ ] Existir FAQ.
- [ ] Existir área de logotipos.
- [ ] Houver espaço para SES-PB.
- [ ] Houver espaço para UFPB.
- [ ] Houver espaço para PET Saúde Digital.
- [ ] O site funcionar em computador.
- [ ] O site funcionar em celular.
- [ ] O conteúdo puder ser atualizado sem grande alteração estrutural do código.
- [ ] O projeto estiver versionado no GitHub.
- [ ] O projeto puder ser atualizado através do GitHub.

---

# 38. Fases de desenvolvimento

## Fase 1 — Estrutura

- criar repositório;
- configurar Python;
- instalar Streamlit;
- criar `app.py`;
- criar estrutura de diretórios;
- criar identidade visual inicial.

## Fase 2 — Interface

- criar cabeçalho;
- criar barra superior;
- criar página inicial;
- criar cards;
- criar rodapé;
- criar área de logotipos.

## Fase 3 — Conteúdo

- implementar informações;
- implementar FAQ;
- implementar fluxogramas;
- implementar imagens;
- implementar links.

## Fase 4 — Responsividade e acessibilidade

- testar celular;
- testar tablet;
- verificar contraste;
- revisar textos;
- adicionar textos alternativos.

## Fase 5 — Deploy

- criar `requirements.txt`;
- conectar GitHub;
- configurar Streamlit Community Cloud;
- tornar aplicação pública;
- testar URL externa.

## Fase 6 — Evolução

- busca;
- documentos;
- banco de dados;
- painel administrativo;
- chatbot;
- RAG.

---

# 39. Critério de simplicidade

Um princípio fundamental do projeto deverá ser:

> **Não adicionar complexidade antes que ela seja necessária.**

Portanto, o MVP não deverá utilizar:

- frontend React;
- backend separado;
- banco de dados obrigatório;
- autenticação;
- microsserviços;
- infraestrutura paga.

A arquitetura deverá permanecer simples enquanto o volume e a complexidade do projeto forem pequenos.

---

# 40. Evolução tecnológica

Caso o portal cresça, a arquitetura poderá evoluir para:

```text
                    FRONTEND
                       │
                       ▼
                     API
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      PostgreSQL     Busca          IA
                         │
                         ▼
                    Base vetorial
```

Nesse cenário, uma possível tecnologia para a API seria FastAPI.

Entretanto, essa arquitetura não faz parte do MVP.

---

# 41. Hospedagem e publicação

A aplicação deverá ser hospedada inicialmente no Streamlit Community Cloud.

Fluxo:

```text
Desenvolvedor
     │
     ▼
Git
     │
     ▼
GitHub
     │
     ▼
Streamlit Community Cloud
     │
     ▼
Aplicação pública
     │
     ▼
Usuários
```

O Streamlit Community Cloud permite conectar uma aplicação a um repositório GitHub e disponibilizá-la publicamente por uma URL `streamlit.app`. Alterações enviadas ao repositório podem atualizar a aplicação publicada.

---

# 42. Domínio futuro

Inicialmente será utilizada a URL fornecida pelo Streamlit.

Posteriormente poderá ser considerado um domínio próprio, por exemplo:

```text
telemedicinapb.org
```

ou outro domínio definido pelos responsáveis pelo projeto.

O domínio próprio não é requisito do MVP.

---

# 43. Gestão de conteúdo

O conteúdo deverá ser organizado de forma que seja possível atualizar:

- perguntas;
- respostas;
- links;
- descrições;
- imagens;
- fluxogramas;
- informações institucionais.

sem necessidade de reestruturar toda a aplicação.

---

# 44. Fontes

Os conteúdos deverão priorizar:

1. fontes institucionais;
2. órgãos públicos;
3. universidades;
4. projetos oficiais;
5. documentos técnicos;
6. literatura científica, quando aplicável.

As fontes deverão ser apresentadas quando forem relevantes para a informação disponibilizada.

---

# 45. Princípios do projeto

O desenvolvimento deverá seguir os seguintes princípios:

### Simplicidade

O usuário deverá encontrar rapidamente o que procura.

### Confiabilidade

Informações de saúde deverão possuir fontes adequadas.

### Acessibilidade

O portal deverá ser compreensível por diferentes públicos.

### Transparência

Quando possível, o usuário deverá conseguir identificar a origem da informação.

### Expansibilidade

A estrutura deverá permitir crescimento.

### Gratuidade

O MVP deverá evitar custos de infraestrutura.

---

# 46. Resumo da solução

A solução proposta é:

```text
┌──────────────────────────────────────────────────┐
│      REPOSITÓRIO DE APOIO À TELEMEDICINA        │
│             E TELESSAÚDE DA PARAÍBA             │
├──────────────────────────────────────────────────┤
│ Telessaúde │ Inserção PBCC │ Tele-Estomatologia │
├──────────────────────────────────────────────────┤
│                                                  │
│                  INÍCIO                          │
│                                                  │
│       Informações sobre telessaúde               │
│                                                  │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐   │
│  │Informações │ │Fluxogramas │ │    FAQ     │   │
│  └────────────┘ └────────────┘ └────────────┘   │
│                                                  │
│              Conteúdos e imagens                │
│                                                  │
├──────────────────────────────────────────────────┤
│              INSTITUIÇÕES / APOIO               │
│                                                  │
│       SES-PB     UFPB     PET Saúde Digital     │
│                                                  │
├──────────────────────────────────────────────────┤
│                      SOBRE                       │
└──────────────────────────────────────────────────┘
```

---

# 47. Visão de longo prazo

O projeto deverá evoluir de:

**portal de informações**

para:

**repositório estruturado de conhecimento**

e posteriormente para:

**plataforma inteligente de acesso ao conhecimento sobre telemedicina e telessaúde na Paraíba.**

A evolução prevista é:

```text
Portal
  ↓
Repositório
  ↓
Busca
  ↓
Base de conhecimento
  ↓
Chat
  ↓
RAG + IA
```

Essa estratégia permite começar com uma aplicação pequena, gratuita e simples, sem comprometer a possibilidade de desenvolvimento de funcionalidades mais avançadas no futuro.

---

# 48. Definição final do MVP

### Nome

**Repositório de Apoio à Telemedicina e Telessaúde da Paraíba**

### Tecnologia

**Python + Streamlit**

### Hospedagem

**Streamlit Community Cloud**

### Repositório

**GitHub**

### Interface

**Portal institucional moderno, simples e responsivo**

### Barra superior

- Telessaúde SES-PB
- Inserção PBCC
- Tele-Estomatologia PB

### Conteúdo

- Informações
- Imagens
- Fluxogramas
- Perguntas e respostas
- Links e serviços

### Instituições/logotipos

- Secretaria de Estado da Saúde da Paraíba — SES-PB
- Universidade Federal da Paraíba — UFPB
- PET Saúde Digital

### Futuro

- busca;
- documentos;
- banco de dados;
- painel de gerenciamento;
- chatbot;
- RAG;
- IA.

---

# 49. Referências técnicas

- Streamlit Community Cloud: https://docs.streamlit.io/deploy/streamlit-community-cloud
- Deploy de aplicações Streamlit: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app
- Compartilhamento de aplicações: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app

