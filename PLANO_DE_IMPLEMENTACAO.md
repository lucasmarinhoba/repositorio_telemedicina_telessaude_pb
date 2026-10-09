# PLANO DE IMPLEMENTAÇÃO — Repositório de Apoio à Teleodontologia e Telessaúde da Paraíba

> Baseado no **Documento de Requisitos v2.0** (setembro/2026). Este plano não implementa código — organiza os requisitos em um roteiro executável de desenvolvimento, do zero até o deploy público, com preparação explícita para a evolução futura (busca, chatbot, RAG).

---

## Sumário

0. Análise inicial
1. Arquitetura
2. Estrutura de diretórios
3. Fases de desenvolvimento (visão geral e progressão incremental)
4. Detalhamento de cada fase (Fase 0 → Fase 14)
5. Estratégia de Git e GitHub
6. Barra superior de links (RF01)
7. Logos institucionais (RF02)
8. Organização do conteúdo
9. Especificação de design
10. Acessibilidade
11. Estratégia de testes
12. Deploy no Streamlit Community Cloud
13. Segurança e privacidade
14. Preparação para busca, chatbot e RAG
15. Roadmap futuro
16. Checklist final
17. Ordem recomendada de implementação
18. Conformidade com as diretrizes do briefing

---

# 0. Análise inicial

## 0.1. Resumo do projeto

Um portal público, institucional, em **Python + Streamlit**, hospedado gratuitamente no **Streamlit Community Cloud** e versionado no **GitHub**, cuja função é **centralizar e organizar** — não substituir — o acesso a informações, serviços, projetos, fluxogramas e materiais sobre teleodontologia, telessaúde e saúde digital na Paraíba. Ele funciona como uma porta de entrada única que direciona o usuário aos sistemas oficiais corretos (Telessaúde SES-PB, Inserção PBCC, Tele-Estomatologia PB), além de reunir conteúdo próprio (informações, FAQ, fluxogramas).

## 0.2. Objetivo principal

Publicar, com o menor custo e complexidade possíveis, uma URL pública e responsiva que atenda integralmente aos critérios de aceitação da seção 37 do documento de requisitos, sem fechar portas para a evolução futura para busca, painel administrativo, banco de dados, chatbot e arquitetura RAG.

## 0.3. Escopo do MVP

Incluído no MVP (derivado das seções 5, 37 e 48 do documento de requisitos):

- Página inicial com identidade do projeto, chamada para ação e destaque dos serviços externos.
- Barra superior fixa com os 3 links externos (Telessaúde SES-PB, Inserção PBCC, Tele-Estomatologia PB), expansível via arquivo de conteúdo.
- Página de Informações, organizada por categorias.
- Página de Fluxogramas (imagens/SVG estáticos).
- Página de Perguntas e Respostas (FAQ pré-cadastrado).
- Página de Links e Serviços (mesmos serviços externos, com descrição mais completa).
- Página Sobre, com aviso de caráter informativo obrigatório (seção 21).
- Área de logotipos institucionais (SES-PB, UFPB, PET Saúde Digital), com placeholders até o recebimento dos arquivos oficiais.
- Responsividade (desktop, tablet, celular) e acessibilidade básica (contraste, alt text, navegação simples).
- Deploy público via Streamlit Community Cloud, atualizável via `git push`.
- Conteúdo armazenado em arquivos (JSON/Markdown), sem banco de dados.

**Fora do MVP** (funcionalidade futura, não implementar agora):

- Busca textual (RF08) — ver justificativa na seção 0.6, item (a).
- Documentos extensos / repositório documental.
- Banco de dados (PostgreSQL ou outro).
- Painel administrativo / autenticação / edição online.
- Chatbot e arquitetura RAG.
- Domínio próprio (`teleodontologiapb.org` ou similar).

## 0.4. Funcionalidades futuras (fora do MVP, mas influenciam decisões de arquitetura hoje)

| Funcionalidade futura | Gatilho recomendado para implementar | Impacto arquitetural |
|---|---|---|
| Busca simples (client-side) | Quando o volume de conteúdo (FAQ + Informações) dificultar a leitura linear | Baixo — pode ser feita sem banco, filtrando JSON em memória |
| Documentos / biblioteca | Quando houver PDFs/materiais institucionais para publicar | Médio — precisa de um índice de metadados |
| Banco de dados | Quando surgir necessidade de painel administrativo, autenticação ou grande volume | Alto — introduz camada de persistência e migrations |
| Chatbot + RAG | Quando a base de conhecimento estiver estruturada e estável | Alto — introduz busca vetorial, LLM, custos de API |
| Domínio próprio | Quando o projeto tiver identidade pública consolidada | Baixo — configuração de DNS, não afeta código |

## 0.5. Arquitetura recomendada (resumo)

Aplicação Streamlit **monolítica e estática em termos de dados** (sem backend separado, sem banco), com conteúdo desacoplado do código em arquivos JSON/Markdown, componentes de UI reutilizáveis (`components/`) e uma camada fina de acesso a conteúdo (`utils/content_loader.py`) que isola o restante da aplicação da forma como os dados são armazenados hoje — o que permite trocar "arquivo local" por "banco de dados" ou "índice vetorial" no futuro sem reescrever as páginas. Detalhamento completo na seção 1.

## 0.6. Principais decisões técnicas

1. **Navegação interna via mecanismo nativo do Streamlit** (`pages/` + navegação lateral automática), em vez de uma navegação 100% customizada. Justificativa na seção 1.4.
2. **Conteúdo em JSON para dados estruturados** (links, FAQ, índice de informações) **+ Markdown para textos longos**. Justificativa na seção 8.
3. **Sem banco de dados no MVP.** Já determinado pelo próprio documento de requisitos (seção 32); este plano apenas confirma e reforça essa decisão.
4. **Sem autenticação/cadastro no MVP** (seção 36 do documento de requisitos).
5. **Git com um branch por fase/funcionalidade**, commits em Conventional Commits, um Pull Request por fase. Detalhamento na seção 5.
6. **Busca (RF08) tratada como pós-MVP**, não como parte do MVP. Justificativa abaixo.

## 0.7. Riscos técnicos identificados

| # | Risco | Impacto | Mitigação proposta |
|---|---|---|---|
| R1 | Confusão entre a "barra superior de serviços externos" (RF01) e a "navegação principal" do site (seção 12) — se implementadas como um único componente, geram uma barra confusa que mistura links internos e externos | Médio | Separar claramente os dois: barra superior fixa só com os 3 serviços externos; navegação entre páginas do próprio portal usando o menu lateral nativo do Streamlit |
| R2 | RF08 (Busca) tem redação ambígua quanto ao MVP | Médio | Ver decisão e justificativa no item 0.8(a) abaixo |
| R3 | Arquivos oficiais de logotipos (SES-PB, UFPB, PET Saúde Digital) ainda não fornecidos | Alto (bloqueia a Fase 10 se não houver plano B) | Usar placeholders versionados (retângulos com o nome da instituição) até o recebimento dos arquivos oficiais; documentar isso como pendência externa |
| R4 | Visual "padrão Streamlit" pode parecer um painel administrativo, não um portal institucional como o G1 | Médio | Tema customizado em `.streamlit/config.toml` + CSS leve via `st.markdown(..., unsafe_allow_html=True)` centralizado em um único componente, para não espalhar HTML pelo projeto |
| R5 | Streamlit Community Cloud gratuito "hiberna" aplicativos inativos (cold start de 30–60s no primeiro acesso) | Baixo/Médio | Aceitar como trade-off da gratuidade (RNF02); documentar no README; não é um problema de código a resolver agora |
| R6 | Links externos (governo/terceiros, incluindo página Glide) podem mudar de URL ou cair | Médio (manutenção contínua) | Centralizar links em `content/links.json`; revisão periódica manual (não é possível monitorar automaticamente sem infraestrutura extra no MVP) |
| R7 | Streamlit dificulta testes de UI automatizados tradicionais | Baixo | Testar a lógica pura (carregamento/validação de conteúdo) com `pytest`; testar a UI manualmente com checklist repetível (seção 11) |

## 0.8. Pontos do documento que precisam de atenção

**(a) RF08 — Busca: ambiguidade sobre pertencer ou não ao MVP.**
A seção "RF08 — Busca" do documento de requisitos diz que o portal deve ter busca "desde uma versão inicial ou, no máximo, em uma segunda etapa", mas o objetivo específico #12 ("possibilitar expansão *futura* para busca inteligente e chatbot") e a seção 39 ("Critério de simplicidade") tratam a busca como evolução, não como requisito do MVP. Essas duas partes se contradizem.

*Recomendação deste plano:* tratar a busca como a **primeira funcionalidade pós-MVP** (ver Roadmap, seção 15), não incluí-la nas Fases 0–14. Justificativa: (1) o próprio documento define os "Critérios de aceitação do MVP" (seção 37) e nenhum deles menciona busca; (2) incluir busca no MVP aumentaria o escopo contrariando a Regra 6 do briefing ("priorize simplicidade") e o "Critério de simplicidade" do próprio documento (seção 39); (3) uma busca "simples" bem-feita ainda exige decidir o que indexar, como apresentar resultados e como lidar com relevância — não é trivial o suficiente para caber em um MVP de conteúdo estático pequeno. Esta decisão deve ser confirmada com os responsáveis pelo projeto antes da Fase 5, já que envolve interpretação de um requisito ambíguo.

**(b) Posição dos logotipos institucionais.**
A seção 10 apresenta três posições possíveis (cabeçalho, próximo ao título, rodapé) mas já recomenda o rodapé, justificando que evita concorrência visual com o conteúdo. Este plano **adota a recomendação do próprio documento** (rodapé), com uma ressalva: como a SES-PB é a instituição responsável pelo projeto, é comum em portais governamentais também citar seu nome (não necessariamente o logo) no cabeçalho, próximo ao título. Isso é uma escolha de identidade visual, não um requisito técnico — sugerimos confirmar com os responsáveis institucionais antes da Fase 3, mas o plano segue com "logos apenas no rodapé" como padrão.

**(c) Arquivos oficiais de logotipos não fornecidos.**
O documento é explícito: "os arquivos oficiais dos logotipos deverão ser obtidos de fontes autorizadas". Nenhum arquivo foi anexado a este processo. Este plano **não inventa nem baixa logos de fontes não oficiais** (conforme a regra explícita do briefing). A Fase 10 usa placeholders neutros (caixas com o nome da instituição em texto) até que os arquivos cheguem — isso não bloqueia o deploy do MVP.

**(d) Estrutura de diretórios do documento de requisitos (seção 29) é sólida e é adotada como base**, com pequenos acréscimos (pasta `tests/`, pasta `docs/`) explicados na seção 2 deste plano — não é uma mudança de escopo, apenas suporte a testes e documentação, já previstos nas seções 13 e "Documentação" do próprio briefing.

**(e) Seções 33–35 (chat futuro / RAG)** não exigem nenhuma ação de código agora, mas impõem restrições de *como* o conteúdo do MVP deve ser escrito (com fonte identificável, granularidade por unidade de conteúdo). Isso é detalhado na seção 14 deste plano e deve ser respeitado desde a Fase 5 (Informações) e a Fase 7 (FAQ), para não ser necessário reescrever o conteúdo mais tarde.

---

# 1. Arquitetura

## 1.1. Diagrama textual

```text
                         ┌─────────────────────────┐
                         │        Usuário           │
                         │  (desktop / tablet /     │
                         │   smartphone)             │
                         └────────────┬─────────────┘
                                      │ HTTPS
                                      ▼
                    ┌───────────────────────────────────┐
                    │   Streamlit Community Cloud         │
                    │   (hospedagem gratuita, build       │
                    │    automático a partir do GitHub)   │
                    └────────────────┬────────────────────┘
                                      │ deploy contínuo (git push → main)
                                      ▼
┌──────────────────────────────────────────────────────────────────────┐
│                         Aplicação Streamlit                          │
│                                                                      │
│  app.py  ──────────────► roteador/entrypoint da aplicação            │
│    │                                                                 │
│    ├── components/  ───► header.py, top_links_bar.py, cards.py,      │
│    │                     footer.py, disclaimer.py (UI reutilizável)  │
│    │                                                                 │
│    ├── pages/       ───► 1_Informacoes.py, 2_Fluxogramas.py,         │
│    │                     3_Perguntas_e_Respostas.py,                 │
│    │                     4_Links_e_Servicos.py, 5_Sobre.py           │
│    │                     (navegação lateral nativa do Streamlit)     │
│    │                                                                 │
│    ├── utils/       ───► content_loader.py (única porta de entrada   │
│    │                     para ler conteúdo — abstrai JSON/Markdown)  │
│    │                                                                 │
│    ├── content/     ───► links.json, faq.json, informacoes/*.md,    │
│    │                     informacoes_index.json                     │
│    │                                                                 │
│    └── assets/      ───► logos/, images/, flowcharts/               │
└──────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
                          ┌───────────────────────┐
                          │  Serviços externos     │
                          │  (apenas links, sem     │
                          │   integração técnica)   │
                          │  - Telessaúde SES-PB    │
                          │  - Inserção PBCC        │
                          │  - Tele-Estomatologia PB│
                          └───────────────────────┘
```

## 1.2. Responsabilidade de cada componente

| Componente | Responsabilidade | Não deve fazer |
|---|---|---|
| `app.py` | Ponto de entrada; monta cabeçalho, barra superior, conteúdo da home e rodapé | Não deve conter lógica de outras páginas nem acessar arquivos de conteúdo diretamente (usa `utils/content_loader.py`) |
| `pages/*.py` | Uma página por área de navegação (Informações, Fluxogramas, FAQ, Links e Serviços, Sobre) | Não deve duplicar HTML/CSS do cabeçalho/rodapé — deve importar de `components/` |
| `components/*.py` | Funções de UI reutilizáveis e sem estado próprio | Não deve conter dados "chumbados" (hardcoded) — recebe dados como parâmetro ou busca via `utils/content_loader.py` |
| `utils/content_loader.py` | Única camada que sabe *onde* e *como* o conteúdo está armazenado hoje (arquivos) | Não deve conter lógica de apresentação (HTML/Streamlit) |
| `content/*` | Dados versionados (links, FAQ, textos) | Não deve conter código |
| `assets/*` | Arquivos binários (imagens, logos, fluxogramas) | Não deve conter texto/configuração |
| `.streamlit/config.toml` | Tema visual (cores, fontes) e configuração do servidor | Não deve conter segredos (isso é `.streamlit/secrets.toml`, que não é versionado) |

## 1.3. Como os componentes se relacionam

O fluxo de dados é sempre unidirecional: **`content/` → `utils/content_loader.py` → `components/` ou `pages/` → tela**. Nenhuma página ou componente lê arquivos de `content/` diretamente; tudo passa pela camada de carregamento. Essa é a única regra de acoplamento que este projeto precisa impor desde o início, porque é o ponto exato que vai mudar quando o projeto crescer (ver seção 14).

## 1.4. Por que esta arquitetura é adequada

- **Streamlit** já resolve servidor web, roteamento simples entre páginas e componentes de UI prontos — não há motivo para introduzir um frontend separado (React) nem uma API própria (FastAPI) para um portal de conteúdo majoritariamente estático, o que atende diretamente à Regra 5 do briefing e à seção 39 do documento de requisitos.
- **Arquivos versionados (Git) como "banco de dados" do MVP** eliminam a necessidade de infraestrutura de persistência, backups e credenciais — adequado ao volume de conteúdo previsto e à exigência de gratuidade (RNF02).
- **Navegação interna nativa do Streamlit** (pasta `pages/`, que gera automaticamente um menu lateral) foi escolhida em vez de uma navegação 100% customizada pelos seguintes motivos, comparando as duas alternativas:

| Critério | Navegação nativa (`pages/`) | Navegação 100% customizada (`st.navigation(position="hidden")` + barra própria) |
|---|---|---|
| Complexidade de implementação | Baixa — é automática ao criar arquivos em `pages/` | Média/alta — exige gerenciar estado de página, roteamento manual e CSS |
| Acessibilidade e teclado | Suportada nativamente pelo Streamlit | Precisa ser recriada manualmente |
| Comportamento em celular | Colapsa em menu "hambúrguer" automaticamente | Precisa ser implementado à mão |
| Risco de bugs conhecidos | Baixo | Existem relatos de comportamento instável ao combinar `st.navigation` com a pasta `pages/` e com trocas dinâmicas de página |
| Aderência ao "Critério de simplicidade" (seção 39 do documento) | Alta | Baixa |

*Decisão:* usar a navegação lateral nativa do Streamlit para as 6 áreas do site (Início, Informações, Fluxogramas, Perguntas e Respostas, Links e Serviços, Sobre — seção 12 do documento de requisitos), e reservar a **barra superior customizada apenas para os 3 links externos** (RF01), que é exatamente o que o documento pede como um componente visualmente separado, "à la G1". Isso evita reinventar um roteador e mantém o projeto simples, sem abrir mão do visual de portal — o tema customizado (seção 9 deste plano) é o que dá a aparência "institucional/portal", não a lógica de roteamento.

## 1.5. Como evitar acoplamento desnecessário

1. Nenhuma URL externa "chumbada" em mais de um lugar do código — todas vêm de `content/links.json`.
2. Nenhum componente de UI conhece o formato de arquivo do conteúdo (JSON vs. Markdown) — isso é responsabilidade exclusiva de `utils/content_loader.py`.
3. Textos institucionais fixos (ex.: aviso de caráter informativo) ficam em `content/`, não dentro de `components/disclaimer.py`, para poderem ser revisados por não-desenvolvedores sem tocar em código.

## 1.6. Como preparar o projeto para crescimento sem complexidade prematura

O único "ponto de extensão" que este plano cria deliberadamente é o `utils/content_loader.py`. Hoje ele lê arquivos locais; no futuro, pode passar a consultar um banco de dados, uma API ou um índice de busca, **sem que nenhuma página precise ser reescrita**, desde que a assinatura das funções (ex.: `carregar_faq()`, `carregar_links()`) permaneça a mesma. Esse é o principal investimento arquitetural do MVP voltado ao futuro, e é suficiente — não é necessário (nem recomendado) adicionar camadas de abstração além dessa agora.

---

# 2. Estrutura de diretórios

A estrutura proposta pelo documento de requisitos (seção 29) é adotada como base, com pequenos acréscimos justificados (marcados com ✦):

```text
repositorio-teleodontologia-telessaude-pb/
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
│   ├── links.json
│   ├── faq.json
│   ├── informacoes_index.json          ✦ índice das categorias/artigos de Informações
│   └── informacoes/                    ✦ um .md por artigo longo
│       ├── o-que-e-telessaude.md
│       └── ...
│
├── assets/
│   ├── logos/
│   │   ├── ses_pb.png                  (placeholder até arquivo oficial)
│   │   ├── ufpb.png                    (placeholder até arquivo oficial)
│   │   └── pet_saude_digital.png       (placeholder até arquivo oficial)
│   ├── images/
│   └── flowcharts/
│
├── components/
│   ├── header.py
│   ├── top_links_bar.py
│   ├── cards.py
│   ├── footer.py
│   └── disclaimer.py                   ✦ aviso de caráter informativo (seção 21), reutilizável
│
├── utils/
│   ├── content_loader.py
│   └── validators.py                   ✦ validação leve de schema do JSON (usada em pytest)
│
├── tests/                              ✦ testes automatizados (pytest)
│   ├── test_content_loader.py
│   └── test_links.py
│
├── docs/                               ✦ documentação técnica (não confundir com conteúdo do site)
│   ├── arquitetura.md
│   └── esquema-de-conteudo.md
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml                    (não versionado — ver .gitignore)
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 2.1. Finalidade de cada pasta/arquivo

| Item | Finalidade | Deve conter | NÃO deve conter |
|---|---|---|---|
| `app.py` | Página inicial e montagem do layout comum | Hero, chamada para os cards de Informações/Fluxogramas/FAQ, chamada aos componentes de cabeçalho/rodapé | Lógica de outras páginas, textos longos "chumbados" |
| `pages/` | Uma página por área de navegação | Import dos componentes + chamada às funções de `content_loader` | HTML/CSS duplicado, dados hardcoded |
| `content/links.json` | Fonte única dos serviços externos (RF01, RF09) | Lista de objetos `{nome, url, descricao}` | Lógica, HTML |
| `content/faq.json` | Fonte única do FAQ (RF07) | Lista de `{id, pergunta, resposta, fonte}` | HTML |
| `content/informacoes_index.json` | Índice das categorias e artigos de Informações (RF04) | Metadados (`id`, `categoria`, `titulo`, `arquivo`, `fonte`) | O texto longo em si (fica no `.md` correspondente) |
| `content/informacoes/*.md` | Corpo de cada artigo informativo | Texto em Markdown, com fonte citada ao final | Metadados de navegação (isso é papel do índice) |
| `assets/logos/` | Arquivos de logotipo institucionais | PNG/SVG em boa resolução, proporção original preservada | Distorções, versões não oficiais |
| `assets/images/` | Imagens de conteúdo (RF05) | Fotos/infográficos com título, descrição e fonte definidos no JSON correspondente | Imagens sem crédito/fonte quando aplicável |
| `assets/flowcharts/` | Fluxogramas (RF06) | SVG ou PNG | — |
| `components/` | UI reutilizável, sem dados fixos | Funções Python que recebem dados como parâmetro | Textos institucionais fixos (exceto `disclaimer.py`, que lê o texto de `content/`) |
| `utils/content_loader.py` | Único ponto de leitura de `content/` | Funções `carregar_links()`, `carregar_faq()`, `carregar_informacoes()` | Chamadas Streamlit (`st.*`) |
| `utils/validators.py` | Validação de schema dos JSON | Funções puras, sem I/O de tela | — |
| `tests/` | Testes automatizados | Testes de `content_loader` e `validators` | Testes de renderização visual (fora de escopo do MVP) |
| `docs/` | Documentação técnica interna | Notas de arquitetura e do esquema de conteúdo (útil para a futura ingestão em RAG) | Conteúdo do site (isso é `content/`) |
| `.streamlit/config.toml` | Tema visual e configuração do servidor | Paleta de cores, fonte, `[server]` se necessário | Segredos |
| `.streamlit/secrets.toml` | Segredos futuros (ex.: chave de API de LLM) | Nada no MVP — arquivo criado vazio/de exemplo (`secrets.toml.example`) e ignorado pelo Git | Segredos versionados |
| `requirements.txt` | Dependências Python fixadas | `streamlit`, e o que mais for adicionado (nenhuma outra biblioteca é necessária no MVP) | Bibliotecas não usadas |
| `.gitignore` | Arquivos que não devem ser versionados | `.venv/`, `__pycache__/`, `.streamlit/secrets.toml` | — |

---

# 3. Fases de desenvolvimento — visão geral

## 3.1. Lista de fases

```text
Fase 0  — Preparação
Fase 1  — Estrutura inicial
Fase 2  — Configuração visual (tema)
Fase 3  — Cabeçalho e barra superior de links externos
Fase 4  — Página inicial
Fase 5  — Página de Informações
Fase 6  — Página de Fluxogramas
Fase 7  — Página de Perguntas e Respostas (FAQ)
Fase 8  — Página de Links e Serviços
Fase 9  — Página Sobre + aviso de caráter informativo
Fase 10 — Logos institucionais e rodapé
Fase 11 — Responsividade e acessibilidade
Fase 12 — Testes
Fase 13 — Deploy
Fase 14 — Documentação e preparação para evolução futura
```

Essa divisão segue a sugestão do briefing, mas é mais granular que as "Fases de desenvolvimento" do próprio documento de requisitos (seção 38, que tem 6 fases). O mapeamento entre as duas é direto e não representa mudança de escopo:

| Fases deste plano | Fase do documento de requisitos (seção 38) |
|---|---|
| Fase 0, 1, 2 | Fase 1 — Estrutura |
| Fase 3, 4, 10 | Fase 2 — Interface |
| Fase 5, 6, 7, 8, 9 | Fase 3 — Conteúdo |
| Fase 11 | Fase 4 — Responsividade e acessibilidade |
| Fase 12, 13 | Fase 5 — Deploy |
| Fase 14 | Prepara a Fase 6 — Evolução (sem implementá-la) |

## 3.2. Progressão incremental (o que funciona ao final de cada fase)

```text
Fase 0  → Repositório existe, ambiente local funciona
Fase 1  → `streamlit run app.py` mostra uma página em branco funcional
Fase 2  → A aplicação tem identidade visual (cores, fonte) mesmo sem conteúdo
Fase 3  → Cabeçalho + barra superior com os 3 links externos funcionando
Fase 4  → Página inicial completa e navegável
Fase 5  → Página de Informações funcional com conteúdo real
Fase 6  → Página de Fluxogramas funcional
Fase 7  → FAQ funcional
Fase 8  → Página de Links e Serviços funcional
Fase 9  → Página Sobre funcional, aviso legal visível em todo o site
Fase 10 → Rodapé com logos (placeholders) em todas as páginas
Fase 11 → Site validado em mobile/tablet/desktop e com acessibilidade básica
Fase 12 → Testes automatizados e checklist manual aprovados
Fase 13 → Site publicado com URL pública
Fase 14 → Projeto documentado e pronto para receber a próxima etapa do roadmap
```

Cada fase deixa o projeto em um estado executável e verificável — nunca há uma fase que só "prepara" sem produzir algo visível ou testável.

---

# 4. Detalhamento de cada fase

Para cada fase: **Objetivo · Tarefas · Arquivos envolvidos · Dependências · Resultado esperado · Critérios de aceitação · Testes · Commits sugeridos**.

---

## Fase 0 — Preparação

**Objetivo:** ter o ambiente e o repositório prontos para começar a codificar.

**Tarefas:**
- Criar o repositório no GitHub com o nome `repositorio-teleodontologia-telessaude-pb` (seção 1.1 do documento).
- Criar ambiente virtual Python local (`venv`).
- Definir a versão mínima do Python do projeto (recomendado: 3.11, por ser estável e amplamente suportada pelo Streamlit Community Cloud).
- Criar `.gitignore` inicial (`.venv/`, `__pycache__/`, `.streamlit/secrets.toml`, `.DS_Store`).
- Criar `README.md` inicial (apenas nome do projeto e uma frase de propósito — será expandido na Fase 14).
- Fazer o primeiro commit e o primeiro push.

**Arquivos envolvidos:**
- Criados: `.gitignore`, `README.md`

**Dependências:** nenhuma (fase inicial).

**Resultado esperado:** repositório GitHub existente, clonável, com histórico de commit inicial.

**Critérios de aceitação:**
- [ ] Repositório criado e acessível no GitHub.
- [ ] `git clone` funciona em uma pasta limpa.
- [ ] `.gitignore` evita versionar `.venv/` e segredos.

**Testes:** nenhum teste automatizado nesta fase; verificação manual de que o clone funciona.

**Commits sugeridos:**
```text
chore: inicializa repositório com .gitignore e README
```

---

## Fase 1 — Estrutura inicial

**Objetivo:** ter a estrutura de pastas do projeto e uma aplicação Streamlit mínima rodando localmente.

**Tarefas:**
- Instalar Streamlit e congelar em `requirements.txt`.
- Criar a estrutura de diretórios completa definida na seção 2 (mesmo que vazias, usando `.gitkeep` onde necessário).
- Criar `app.py` mínimo (apenas `st.title(...)` de teste).
- Confirmar execução local com `streamlit run app.py`.

**Arquivos envolvidos:**
- Criados: `requirements.txt`, `app.py`, pastas `pages/`, `content/`, `assets/`, `components/`, `utils/`, `tests/`, `docs/`, `.streamlit/`

**Dependências:** Fase 0.

**Resultado esperado:** `streamlit run app.py` abre no navegador local e mostra um título de teste, sem erros.

**Critérios de aceitação:**
- [ ] `pip install -r requirements.txt` funciona em ambiente limpo.
- [ ] `streamlit run app.py` roda sem erros.
- [ ] Estrutura de pastas confere com a seção 2 deste plano.

**Testes:** execução manual local (`streamlit run app.py`); nenhum teste automatizado ainda (não há lógica para testar).

**Commits sugeridos:**
```text
chore: adiciona requirements.txt com streamlit
feat: cria estrutura inicial de diretórios do projeto
feat: cria app.py mínimo com página inicial de teste
```

---

## Fase 2 — Configuração visual (tema)

**Objetivo:** dar identidade visual institucional ao projeto antes de construir as telas, para que cada página nova já nasça com a aparência correta.

**Tarefas:**
- Definir paleta de cores, tipografia e espaçamento (ver seção 9 — Design).
- Criar `.streamlit/config.toml` com o tema (`[theme]`: cor primária, cor de fundo, fonte).
- Criar um pequeno utilitário de CSS central (`components/theme.py` ou função dentro de `header.py`) para os ajustes que o Streamlit não permite via `config.toml` (ex.: espaçamento da barra superior), aplicado uma única vez por página.

**Arquivos envolvidos:**
- Criados: `.streamlit/config.toml`
- Modificados: `app.py` (para carregar o tema/CSS central)

**Dependências:** Fase 1.

**Resultado esperado:** a página de teste da Fase 1 já aparece com as cores e fonte definitivas do projeto.

**Critérios de aceitação:**
- [ ] Cores e fonte do tema aplicadas sem necessidade de repetir CSS em cada página.
- [ ] Contraste de texto/fundo atende no mínimo WCAG AA (verificação manual com ferramenta de contraste).

**Testes:** inspeção visual manual; checagem de contraste com ferramenta simples (ex.: extensão de navegador ou calculadora de contraste).

**Commits sugeridos:**
```text
style: define paleta de cores e tipografia em .streamlit/config.toml
style: cria utilitário central de CSS para ajustes finos de layout
```

---

## Fase 3 — Cabeçalho e barra superior de links externos (RF01)

**Objetivo:** implementar o cabeçalho com nome/logo do projeto e a barra horizontal de serviços externos, no estilo de portal (G1), conforme seção 6 deste plano.

**Tarefas:**
- Criar `content/links.json` com os 3 links iniciais (Telessaúde SES-PB, Inserção PBCC, Tele-Estomatologia PB).
- Criar `utils/content_loader.py` com a função `carregar_links()`.
- Criar `components/header.py` (nome/título do projeto).
- Criar `components/top_links_bar.py`, que lê `carregar_links()` e renderiza a barra horizontal, com links abrindo em nova aba.
- Integrar cabeçalho + barra superior em `app.py` (e, futuramente, em todas as páginas de `pages/`).

**Arquivos envolvidos:**
- Criados: `content/links.json`, `utils/content_loader.py`, `components/header.py`, `components/top_links_bar.py`
- Modificados: `app.py`

**Dependências:** Fase 2 (tema já definido, para estilizar a barra corretamente).

**Resultado esperado:** ao abrir a aplicação, o usuário vê o cabeçalho e, logo abaixo, a barra com os 3 serviços clicáveis, cada um abrindo em nova aba.

**Critérios de aceitação:**
- [ ] A barra existe e está visualmente separada do restante do conteúdo (RF01).
- [ ] Os 3 links abrem em nova aba (RF01.1).
- [ ] Novos links podem ser adicionados apenas editando `content/links.json`, sem tocar em `top_links_bar.py` (RF01.2).
- [ ] A barra se adapta a telas menores (verificação visual, aprofundada na Fase 11).

**Testes:**
- `pytest`: `carregar_links()` retorna uma lista não vazia e cada item tem `nome`, `url`, `descricao`.
- Manual: clicar nos 3 links e confirmar que abrem os endereços corretos em nova aba.

**Commits sugeridos:**
```text
feat: adiciona content/links.json com os serviços externos iniciais
feat: cria content_loader com função carregar_links
feat: cria componente de cabeçalho (header.py)
feat: cria barra superior de links externos (top_links_bar.py)
test: adiciona teste de carregamento e schema de links.json
```

---

## Fase 4 — Página inicial

**Objetivo:** completar `app.py` como página inicial real, conforme a hierarquia da seção 8 do documento de requisitos.

**Tarefas:**
- Criar seção de "hero" (título do projeto, subtítulo, botão "Explorar conteúdos").
- Criar `components/cards.py` (cartões de atalho: Informações, Fluxogramas, Perguntas e Respostas).
- Adicionar seção "Conteúdos em destaque" (pode reaproveitar os mesmos cards nesta fase; conteúdo real virá nas Fases 5–8).
- Adicionar espaço reservado para a área de instituições (o conteúdo real dos logos entra na Fase 10 — aqui só a estrutura/layout).

**Arquivos envolvidos:**
- Criados: `components/cards.py`
- Modificados: `app.py`

**Dependências:** Fase 3.

**Resultado esperado:** página inicial completa visualmente, com navegação funcional para as páginas que ainda serão implementadas (podem ficar como placeholders até a Fase correspondente).

**Critérios de aceitação:**
- [ ] Hierarquia da página confere com o diagrama da seção 8 do documento de requisitos.
- [ ] Os cards de atalho existem e apontam para as páginas corretas.
- [ ] Botão "Explorar conteúdos" leva a algum destino coerente (ex.: página de Informações).

**Testes:** manual — navegação a partir da home até cada página/atalho.

**Commits sugeridos:**
```text
feat: adiciona seção hero na página inicial
feat: cria componente de cards de atalho (cards.py)
feat: integra cards de Informações, Fluxogramas e FAQ na home
```

---

## Fase 5 — Página de Informações (RF04)

**Objetivo:** implementar a página de conteúdos informativos, organizados por categoria.

**Tarefas:**
- Definir o schema de `content/informacoes_index.json` (categoria, título, arquivo `.md`, fonte).
- Escrever os primeiros artigos em `content/informacoes/*.md` (ex.: "O que é telessaúde", "O que é teleodontologia"), cada um com a fonte citada ao final (ver seção 14 — preparação para RAG).
- Adicionar `carregar_informacoes()` em `utils/content_loader.py`.
- Criar `pages/1_Informacoes.py`, agrupando artigos por categoria (Teleodontologia, Telessaúde, Saúde Digital, Serviços, Projetos, Educação, Pesquisa, Legislação — seção 14 do documento, categorias iniciais podem ser um subconjunto).

**Arquivos envolvidos:**
- Criados: `content/informacoes_index.json`, `content/informacoes/*.md`, `pages/1_Informacoes.py`
- Modificados: `utils/content_loader.py`

**Dependências:** Fase 4.

**Resultado esperado:** página de Informações navegável por categoria, com textos reais (mesmo que iniciais/poucos).

**Critérios de aceitação:**
- [ ] Existe pelo menos uma categoria com pelo menos um artigo.
- [ ] Cada artigo cita a fonte da informação (seção 44/45 do documento — "Confiabilidade").
- [ ] Novo conteúdo pode ser adicionado editando apenas `informacoes_index.json` + um novo `.md`, sem alterar `pages/1_Informacoes.py`.

**Testes:**
- `pytest`: todo item do índice aponta para um arquivo `.md` que existe de fato.
- `pytest`: todo item do índice tem campo `fonte` preenchido.
- Manual: navegação entre categorias.

**Commits sugeridos:**
```text
feat: define schema do índice de informações (informacoes_index.json)
feat: adiciona content_loader.carregar_informacoes
docs: adiciona primeiros artigos de Informações em Markdown
feat: cria página de Informações (pages/1_Informacoes.py)
test: valida que todo artigo do índice existe e cita fonte
```

---

## Fase 6 — Página de Fluxogramas (RF06)

**Objetivo:** implementar a seção de fluxogramas.

**Tarefas:**
- Definir onde os fluxogramas ficam (`assets/flowcharts/`) e um pequeno JSON de metadados (`content/fluxogramas.json`: título, arquivo, descrição textual — a descrição textual é importante para acessibilidade e para a futura indexação em RAG, seção 14).
- Adicionar `carregar_fluxogramas()` em `utils/content_loader.py`.
- Criar `pages/2_Fluxogramas.py`, exibindo cada fluxograma com título, imagem e descrição/alt text.

**Arquivos envolvidos:**
- Criados: `content/fluxogramas.json`, `assets/flowcharts/*.svg` (ou `.png`), `pages/2_Fluxogramas.py`
- Modificados: `utils/content_loader.py`

**Dependências:** Fase 5 (reaproveita o mesmo padrão de content_loader).

**Resultado esperado:** página de Fluxogramas funcional com pelo menos um fluxograma real (ex.: o exemplo da seção 16 do documento de requisitos — fluxo de decisão sobre teleatendimento).

**Critérios de aceitação:**
- [ ] Pelo menos um fluxograma publicado.
- [ ] Todo fluxograma tem texto alternativo/descrição (RNF05).
- [ ] Imagens não excessivamente pesadas (RNF06) — recomenda-se SVG ou PNG otimizado.

**Testes:**
- `pytest`: todo item de `fluxogramas.json` aponta para um arquivo existente em `assets/flowcharts/` e tem descrição não vazia.
- Manual: verificação visual de nitidez/tamanho.

**Commits sugeridos:**
```text
feat: adiciona metadados de fluxogramas (content/fluxogramas.json)
feat: adiciona content_loader.carregar_fluxogramas
feat: cria página de Fluxogramas (pages/2_Fluxogramas.py)
assets: adiciona primeiro fluxograma (fluxo de teleatendimento)
```

---

## Fase 7 — Página de Perguntas e Respostas / FAQ (RF07)

**Objetivo:** implementar o FAQ com as perguntas já sugeridas no documento de requisitos (seção 17).

**Tarefas:**
- Criar `content/faq.json` com as perguntas: "O que é telessaúde?", "O que é teleodontologia?", "Qual a diferença entre teleodontologia e telessaúde?", "Onde encontro os serviços de telessaúde da Paraíba?" (esta última reaproveitando `links.json`).
- Adicionar `carregar_faq()` em `utils/content_loader.py`.
- Criar `pages/3_Perguntas_e_Respostas.py`, exibindo cada pergunta como um item expansível (`st.expander`).

**Arquivos envolvidos:**
- Criados: `content/faq.json`, `pages/3_Perguntas_e_Respostas.py`
- Modificados: `utils/content_loader.py`

**Dependências:** Fase 6.

**Resultado esperado:** FAQ funcional com as 4 perguntas mínimas do documento de requisitos.

**Critérios de aceitação:**
- [ ] As 4 perguntas da seção 17 do documento estão presentes.
- [ ] Cada resposta é redigida em linguagem acessível (seção 6 — "assumir que o usuário pode não ter conhecimento técnico").
- [ ] Cada entrada do FAQ tem um `id` estável (necessário para a futura citação de fontes pelo chatbot — seção 14 deste plano).

**Testes:**
- `pytest`: `faq.json` não tem `id` duplicado; todo item tem `pergunta` e `resposta` não vazios.
- Manual: abrir/fechar os itens expansíveis.

**Commits sugeridos:**
```text
feat: adiciona content/faq.json com as 4 perguntas iniciais
feat: adiciona content_loader.carregar_faq
feat: cria página de Perguntas e Respostas (pages/3_Perguntas_e_Respostas.py)
test: valida unicidade de id e campos obrigatórios do FAQ
```

---

## Fase 8 — Página de Links e Serviços (RF09)

**Objetivo:** implementar a página dedicada aos recursos externos, reaproveitando `content/links.json` já criado na Fase 3, agora com apresentação mais completa (título, descrição, instituição, botão de acesso).

**Tarefas:**
- Enriquecer `content/links.json` com o campo `instituicao`, se ainda não existir.
- Criar `pages/4_Links_e_Servicos.py`, exibindo cada serviço em formato de card, com botão "Acessar serviço" abrindo em nova aba.

**Arquivos envolvidos:**
- Modificados: `content/links.json`
- Criados: `pages/4_Links_e_Servicos.py`

**Dependências:** Fase 3 (reaproveita `carregar_links()`); pode ser feita em paralelo com as Fases 5–7.

**Resultado esperado:** página com os 3 serviços em formato de card, mais completos que a barra superior.

**Critérios de aceitação:**
- [ ] Cada serviço mostra título, descrição, instituição e botão de acesso (seção 19 do documento).
- [ ] Adicionar um novo serviço não exige alterar `pages/4_Links_e_Servicos.py`, apenas `content/links.json`.

**Testes:**
- `pytest`: reaproveita o teste de schema de `links.json` da Fase 3, agora exigindo também o campo `instituicao`.
- Manual: clique nos botões "Acessar serviço".

**Commits sugeridos:**
```text
feat: adiciona campo instituicao em content/links.json
feat: cria página de Links e Serviços (pages/4_Links_e_Servicos.py)
```

---

## Fase 9 — Página Sobre + aviso de caráter informativo (RF10, seção 21)

**Objetivo:** implementar a página Sobre e o aviso legal obrigatório, exibido de forma consistente em todo o site.

**Tarefas:**
- Redigir o texto da página Sobre (objetivo, contexto, instituições envolvidas, fontes, aviso de caráter informativo, informações sobre atualização do conteúdo).
- Criar `content/sobre.md` (texto revisável sem tocar em código).
- Criar `components/disclaimer.py`, que lê um texto curto de aviso (pode vir de `content/` também) e é chamado a partir do rodapé (Fase 10) ou do topo da página Sobre, conforme decisão de design.
- Criar `pages/5_Sobre.py`.

**Arquivos envolvidos:**
- Criados: `content/sobre.md`, `components/disclaimer.py`, `pages/5_Sobre.py`

**Dependências:** Fase 8.

**Resultado esperado:** página Sobre publicada; aviso de caráter informativo visível de forma consistente (ex.: no rodapé de todas as páginas, e por completo na página Sobre).

**Critérios de aceitação:**
- [ ] O aviso de caráter informativo está presente e com a redação da seção 21 (ou versão revisada pelos responsáveis pelo projeto — o documento deixa claro que o texto final deve ser revisado por eles, não pelo desenvolvedor).
- [ ] A página Sobre contém todos os itens da seção 20 do documento (objetivo, contexto, instituições, fontes, aviso, atualização de conteúdo).

**Testes:** manual — revisão de conteúdo por um responsável do projeto (não é um teste técnico, é uma validação editorial necessária antes do deploy).

**Commits sugeridos:**
```text
docs: adiciona texto da página Sobre (content/sobre.md)
feat: cria componente de aviso de caráter informativo (disclaimer.py)
feat: cria página Sobre (pages/5_Sobre.py)
```

---

## Fase 10 — Logos institucionais e rodapé (RF02)

**Objetivo:** implementar a área de instituições/apoio no rodapé, com os 3 logotipos (ou placeholders).

**Tarefas:**
- Verificar se os arquivos oficiais de logo (SES-PB, UFPB, PET Saúde Digital) já foram recebidos dos responsáveis; se não, criar placeholders neutros com o nome da instituição em texto, versionados em `assets/logos/`, claramente identificados como temporários (ex.: nome de arquivo `ses_pb_placeholder.png`).
- Criar `components/footer.py`, exibindo os 3 logos/placeholders lado a lado, com altura máxima uniforme e `object-fit: contain` (ou equivalente) para não distorcer proporções diferentes.
- Integrar o rodapé (com `disclaimer.py` embutido, ver Fase 9) em todas as páginas.

**Arquivos envolvidos:**
- Criados: `components/footer.py`, `assets/logos/*` (placeholders, se necessário)
- Modificados: `app.py`, todos os arquivos em `pages/`

**Dependências:** Fase 9.

**Resultado esperado:** rodapé consistente em todas as páginas, com espaço para os 3 logos, sem distorção, mesmo com placeholders.

**Critérios de aceitação:**
- [ ] Existe espaço para SES-PB, UFPB e PET Saúde Digital (seção 37 do documento).
- [ ] Nenhum logo aparece esticado/espremido (proporção original preservada).
- [ ] Fica documentado em `docs/` (ou no README) que os logos atuais são placeholders pendentes de substituição pelos arquivos oficiais.

**Testes:** manual — inspeção visual em diferentes larguras de tela (a fundo na Fase 11).

**Commits sugeridos:**
```text
assets: adiciona placeholders dos logos institucionais (SES-PB, UFPB, PET Saúde Digital)
feat: cria componente de rodapé com área de instituições (footer.py)
feat: integra rodapé e aviso informativo em todas as páginas
docs: documenta pendência de substituição dos logos por arquivos oficiais
```

---

## Fase 11 — Responsividade e acessibilidade

**Objetivo:** validar e ajustar o site para diferentes tamanhos de tela e critérios básicos de acessibilidade.

**Tarefas:**
- Testar todas as páginas em três larguras: desktop, tablet, celular (usando as ferramentas de desenvolvedor do navegador e, se possível, um dispositivo real).
- Verificar contraste de texto/fundo em todos os componentes (não só no tema base).
- Auditar todas as imagens/fluxogramas quanto a texto alternativo.
- Revisar a hierarquia de títulos (h1/h2/h3 coerente, sem "pular" níveis).
- Verificar tamanho de fonte mínimo e área de toque dos botões/links em mobile.
- Ajustar a barra superior (Fase 3) para se comportar bem em telas estreitas (quebra de linha ou rolagem horizontal, decisão de design registrada na seção 9).

**Arquivos envolvidos:**
- Modificados: `components/top_links_bar.py`, `components/header.py`, `components/footer.py`, `.streamlit/config.toml`, páginas em `pages/` (ajustes pontuais)

**Dependências:** Fases 3–10 (precisa de todo o conteúdo/telas já implementados).

**Resultado esperado:** site utilizável e legível em qualquer um dos três tamanhos de tela, sem elementos cortados ou sobrepostos.

**Critérios de aceitação:** ver checklist detalhado na seção 10 deste plano.

**Testes:** checklist manual de responsividade e acessibilidade (seção 10); não há teste automatizado de UI no MVP (justificado na seção 11).

**Commits sugeridos:**
```text
fix: ajusta barra superior para telas estreitas
fix: corrige contraste insuficiente em cards da página inicial
fix: adiciona textos alternativos faltantes em imagens e fluxogramas
style: ajusta hierarquia de títulos para estrutura semântica correta
```

---

## Fase 12 — Testes

**Objetivo:** consolidar e rodar a suíte de testes automatizados e o checklist manual antes do deploy.

**Tarefas:**
- Revisar e completar os testes de `pytest` criados incrementalmente nas Fases 3–8 (schema de JSON, existência de arquivos referenciados, campos obrigatórios).
- Rodar o checklist manual completo de responsividade/acessibilidade/links (seção 10 e 11 deste plano).
- Testar manualmente todos os links externos (os 3 serviços) a partir da aplicação publicada localmente.

**Arquivos envolvidos:**
- Modificados/finalizados: `tests/test_content_loader.py`, `tests/test_links.py`

**Dependências:** Fase 11.

**Resultado esperado:** suíte de testes automatizados passando (`pytest`), checklist manual sem pendências.

**Critérios de aceitação:**
- [ ] `pytest` roda sem falhas.
- [ ] Todos os itens do checklist da seção 10/11 marcados.
- [ ] Todos os links externos testados manualmente e funcionando.

**Testes:** esta é a própria fase de testes — ver estratégia completa na seção 11 deste plano.

**Commits sugeridos:**
```text
test: completa cobertura de testes de content_loader e validators
chore: executa checklist manual de acessibilidade e responsividade
```

---

## Fase 13 — Deploy

**Objetivo:** publicar a aplicação no Streamlit Community Cloud com URL pública.

**Tarefas:** ver passo a passo completo na seção 12 deste plano.

**Arquivos envolvidos:**
- Modificados/confirmados: `requirements.txt`, `.streamlit/config.toml`
- Criados (se necessário): `runtime.txt` (fixar versão do Python, se a opção não estiver disponível diretamente nas configurações do app)

**Dependências:** Fase 12 (só publicar depois de testado).

**Resultado esperado:** URL pública `https://<nome-do-app>.streamlit.app` funcionando, sem depender de `localhost` (RNF01).

**Critérios de aceitação:**
- [ ] URL pública acessível de fora da rede do desenvolvedor (testar em outro dispositivo/rede).
- [ ] Todas as páginas carregam sem erro no ambiente publicado.
- [ ] Atualizações futuras via `git push` para `main` refletem automaticamente no site publicado.

**Testes:** smoke test pós-publicação (checklist na seção 12.3).

**Commits sugeridos:**
```text
chore: fixa versão do Python e das dependências para o deploy
docs: adiciona instruções de deploy no README
```
*(Nenhum commit "publica o site" é necessário — o deploy é uma ação de configuração no Streamlit Community Cloud, não uma mudança de código, ver seção 12.)*

---

## Fase 14 — Documentação e preparação para evolução futura

**Objetivo:** deixar o projeto documentado e organizado para que qualquer desenvolvedor (ou o mesmo desenvolvedor, meses depois) consiga dar continuidade, incluindo a evolução para busca, chatbot e RAG.

**Tarefas:**
- Completar o `README.md` (propósito, como rodar localmente, como o conteúdo é organizado, como fazer deploy, como contribuir).
- Escrever `docs/arquitetura.md` (versão resumida da seção 1 deste plano).
- Escrever `docs/esquema-de-conteudo.md` (schema de cada JSON/Markdown, pensando explicitamente em como isso alimentará uma futura ingestão em RAG — seção 14 deste plano).
- Revisar se todo conteúdo publicado tem fonte identificável (pré-requisito para o chatbot futuro, seção 35 do documento de requisitos).

**Arquivos envolvidos:**
- Modificados: `README.md`
- Criados: `docs/arquitetura.md`, `docs/esquema-de-conteudo.md`

**Dependências:** Fase 13.

**Resultado esperado:** projeto publicado, documentado e com um roadmap claro para as próximas etapas (seção 15 deste plano).

**Critérios de aceitação:**
- [ ] Um desenvolvedor novo consegue clonar o repositório e rodar o projeto localmente seguindo apenas o README.
- [ ] A documentação de arquitetura reflete o que foi de fato implementado (não o que foi planejado e mudou).

**Testes:** revisão de documentação (não é teste automatizado).

**Commits sugeridos:**
```text
docs: completa README com instruções de uso, deploy e contribuição
docs: adiciona documentação de arquitetura (docs/arquitetura.md)
docs: adiciona documentação do esquema de conteúdo (docs/esquema-de-conteudo.md)
```

---

# 5. Estratégia de Git e GitHub

## 5.1. Branches

- **`main`** — branch principal, sempre em estado publicável. Nunca se commita diretamente nela após a Fase 0.
- **`feature/<nome-da-fase-ou-tarefa>`** — uma branch por fase (ou por tarefa relevante dentro de uma fase grande). Exemplos: `feature/estrutura-inicial`, `feature/barra-superior-links`, `feature/pagina-informacoes`, `feature/deploy-streamlit-cloud`.

## 5.2. Quando criar uma branch

No início de cada fase (ou subtarefa significativa dentro de uma fase), a partir da `main` atualizada.

## 5.3. Quando fazer merge

Quando os critérios de aceitação da fase (seção 4) estiverem cumpridos e os testes daquela fase passarem localmente.

## 5.4. Quando abrir Pull Request

Assim que o incremento mínimo da fase estiver pronto para revisão — mesmo em um projeto solo, abrir PR mantém o histórico organizado, permite revisão posterior e já deixa o projeto pronto para receber colaboradores ou CI automatizado no futuro.

## 5.5. Quando fazer commits

A cada mudança logicamente completa e testável — nunca "um commit por fase". As sugestões de commit em cada fase (seção 4) mostram a granularidade esperada: em geral, um commit por arquivo/funcionalidade nova, um commit por ajuste relevante de estilo, e commits de `test`/`docs` separados do `feat` correspondente quando fizer sentido.

## 5.6. Convenção de mensagens (Conventional Commits)

| Prefixo | Uso neste projeto |
|---|---|
| `feat:` | Nova funcionalidade (nova página, novo componente, novo campo de conteúdo) |
| `fix:` | Correção de bug ou de comportamento incorreto (ex.: contraste, link quebrado) |
| `docs:` | Documentação (README, `docs/`, texto de conteúdo do site como `sobre.md`) |
| `style:` | Mudança puramente visual/CSS/tema, sem alterar comportamento |
| `refactor:` | Reorganização de código sem mudar comportamento externo |
| `test:` | Adição/ajuste de testes |
| `chore:` | Tarefas de manutenção (dependências, configuração, `.gitignore`) |
| `assets:` | Adição/atualização de arquivos de mídia (logos, imagens, fluxogramas) — extensão prática do Conventional Commits para este projeto, já usada nas sugestões acima |

## 5.7. Tags

Ao final da Fase 13 (deploy bem-sucedido), criar a tag `v0.1.0-mvp`, marcando a primeira versão pública do site.

---

# 6. Barra superior de links (RF01) — como implementar no Streamlit

Esta seção detalha a decisão já registrada na seção 1.4: a barra superior de serviços externos é um componente próprio e simples, separado da navegação interna do site.

## 6.1. Por que ela é diferente da navegação interna

A "navegação principal" do site (Início, Informações, Fluxogramas, FAQ, Links e Serviços, Sobre) muda de página dentro da própria aplicação. Já a barra superior (RF01) sempre leva o usuário para **fora** do site, para sistemas de terceiros. Tratá-las como o mesmo componente confundiria o usuário (ele não saberia, ao olhar, quais links o mantêm no portal e quais o tiram dele) — esse é exatamente o Risco R1 identificado na seção 0.7.

## 6.2. Abordagem recomendada

1. Os dados dos links vivem em `content/links.json` (já definido na Fase 3), no formato sugerido pelo próprio documento de requisitos (seção 30).
2. `components/top_links_bar.py` lê esses dados via `utils/content_loader.carregar_links()` e monta uma barra horizontal, usando colunas do Streamlit (`st.columns`) ou um pequeno bloco HTML centralizado (`st.markdown(..., unsafe_allow_html=True)`) — a decisão entre as duas técnicas é de estilo (a segunda dá mais controle visual para imitar a estética "G1"; a primeira é mais simples e 100% nativa). Recomenda-se a abordagem HTML centralizada em um único componente, para ficar mais próxima do "visual de portal profissional" pedido, mantendo o HTML restrito a este único arquivo (sem espalhar `unsafe_allow_html` pelo projeto).
3. Cada item é um link (`<a href="..." target="_blank" rel="noopener noreferrer">`), não um botão de submissão de formulário — importante para abrir em nova aba (RF01.1) sem recarregar a aplicação Streamlit.
4. A barra é chamada logo abaixo do cabeçalho, em `app.py` e em todas as páginas de `pages/` (ou centralizada em uma função `render_layout_comum()` chamada no início de cada página, para não repetir a chamada manualmente em 6 arquivos).
5. Adicionar um novo link no futuro é apenas adicionar um objeto em `content/links.json` — nenhum código muda (RF01.2).

## 6.3. Comportamento em telas menores

Ver detalhamento na seção 10 (Acessibilidade) e Fase 11: em telas estreitas, os itens da barra devem quebrar em múltiplas linhas ou permitir rolagem horizontal suave, nunca sobrepor ou cortar texto.

---

# 7. Logos institucionais (RF02)

## 7.1. Onde ficam

Conforme a recomendação do próprio documento de requisitos (seção 10) e a decisão registrada na seção 0.8(b) deste plano: **no rodapé**, em uma área "Apoio / Instituições", separada visualmente do conteúdo principal.

## 7.2. Organização dos arquivos

```text
assets/
└── logos/
    ├── ses_pb.png
    ├── ufpb.png
    └── pet_saude_digital.png
```

Nomes de arquivo estáveis e previsíveis, para que a substituição futura por arquivos oficiais seja apenas uma troca de arquivo, sem alterar código.

## 7.3. Como evitar distorção

- Preservar a proporção original de cada logo (nunca forçar largura e altura fixas iguais para todos).
- Definir uma **altura máxima uniforme** (ex.: 48–64px) e deixar a largura livre (`width: auto`), com `object-fit: contain` se renderizado via HTML/CSS.
- Não recortar, não aplicar zoom, não colorir/alterar os logos.

## 7.4. Como lidar com diferentes proporções

Alinhar os logos em uma linha (ou grade, em telas estreitas) com espaçamento (`gap`) uniforme entre eles, centralizados verticalmente entre si, mesmo que suas larguras finais sejam diferentes.

## 7.5. Como manter a identidade visual limpa

- Fundo neutro atrás dos logos (branco ou o fundo padrão do rodapé — nunca uma cor que "brigue" com as cores das marcas).
- Espaço em branco (padding) suficiente ao redor de cada logo.
- Não adicionar bordas, sombras ou efeitos decorativos sobre os logos — eles devem aparecer exatamente como fornecidos pelas instituições.

## 7.6. Como lidar com os arquivos oficiais

- **Este plano não inventa nem baixa logotipos de fontes não oficiais.** É uma pendência explícita a ser resolvida pelos responsáveis do projeto junto a SES-PB, UFPB e PET Saúde Digital.
- Até o recebimento dos arquivos oficiais, usar placeholders neutros (retângulo com o nome da instituição em texto), claramente marcados como temporários no nome do arquivo e documentados em `docs/`.
- Ao receber os arquivos oficiais, a substituição é apenas uma troca de arquivo em `assets/logos/` — nenhuma mudança de código é necessária, desde que os nomes de arquivo sejam mantidos (ou atualizados junto com a referência em `components/footer.py`, caso o formato mude, ex. de `.png` para `.svg`).
- Recomenda-se confirmar com cada instituição se existe um manual de identidade visual com regras de uso do logotipo (tamanho mínimo, área de proteção, cores permitidas) e seguir essas regras à risca — isso está fora do escopo técnico deste plano, mas é uma responsabilidade do projeto antes da publicação definitiva (a Fase 13 pode ir ao ar com placeholders; a troca pelos logos oficiais deve acontecer assim que possível, mas não precisa bloquear o MVP).

---

# 8. Organização do conteúdo

## 8.1. Comparação de formatos

| Critério | JSON | Markdown | YAML |
|---|---|---|---|
| Ideal para | Listas estruturadas com schema fixo (links, FAQ, índices) | Textos longos em prosa | Configuração/dados estruturados legíveis por humanos |
| Facilidade de edição manual | Média (colchetes/aspas atrapalham textos longos) | Alta | Alta |
| Facilidade de validação de schema | Alta (bibliotecas padrão, `json` é nativo do Python) | Baixa (texto livre) | Alta, mas exige dependência extra (`pyyaml`) |
| Diff no Git (legibilidade de mudanças) | Boa para itens curtos | Excelente para textos longos | Boa |
| Risco de erro de sintaxe | Baixo para listas curtas, cresce com textos longos embutidos | Muito baixo | Baixo |
| Dependência extra necessária | Nenhuma (`json` é da biblioteca padrão) | Nenhuma (Streamlit renderiza Markdown nativamente) | `pyyaml` (dependência adicional) |
| Facilidade de uso futuro em busca/RAG | Alta (fácil de iterar programaticamente) | Alta (texto já é o formato ideal para indexação) | Alta, mas exige parsing extra |

## 8.2. Decisão

**Abordagem híbrida:**
- **JSON** para tudo que é uma lista com estrutura fixa e mais curta: `links.json`, `faq.json`, `informacoes_index.json`, `fluxogramas.json`. Vantagem: zero dependências extras (o módulo `json` já vem com o Python), fácil de validar programaticamente (Fase 12), fácil de consumir depois por um futuro mecanismo de busca ou ingestão em RAG.
- **Markdown** para o corpo de textos longos: artigos de Informações (`content/informacoes/*.md`) e a página Sobre (`content/sobre.md`). Vantagem: muito mais fácil e seguro de editar/revisar por alguém sem conhecimento técnico (não precisa se preocupar com aspas, vírgulas, chaves), excelente diff no Git, e o Streamlit renderiza Markdown nativamente sem esforço.
- **YAML não é adotado no MVP:** não traz benefício real sobre JSON para o tamanho e formato de dados deste projeto, e adicionaria uma dependência (`pyyaml`) sem necessidade — contrariaria a Regra 6 do briefing ("priorize simplicidade"). Pode ser reconsiderado no futuro se o projeto ganhar um painel de edição de conteúdo voltado a pessoas não técnicas que prefiram a sintaxe do YAML.

## 8.3. Regra geral

Nenhum texto de conteúdo do site (FAQ, informações, avisos, links) deve ficar escrito diretamente dentro de arquivos `.py`. Se um texto aparece hardcoded em um componente ou página, isso é um sinal de que ele deveria estar em `content/`.

---

# 9. Especificação de design

## 9.1. Princípios

Institucional, moderno, simples, limpo — transmitindo saúde, tecnologia, confiabilidade, organização e acessibilidade (seção 7 do documento de requisitos). Evitar qualquer aparência de "painel administrativo".

## 9.2. Layout e hierarquia visual

1. Cabeçalho (nome/título do projeto)
2. Barra superior de serviços externos (RF01)
3. Conteúdo da página (hero + cards na home; conteúdo específico nas demais páginas)
4. Rodapé (aviso de caráter informativo + área de instituições/logos)

## 9.3. Tipografia

- Fonte sem serifa, legível em telas pequenas (ex.: a fonte padrão do sistema ou uma fonte web gratuita como Inter/Source Sans — a escolha final de uma fonte customizada, se houver, deve considerar o custo de carregamento, seção 27/RNF06).
- Tamanho base de texto ≥ 16px, para legibilidade (RNF05).
- Hierarquia clara entre título de página (maior), títulos de seção e corpo de texto.

## 9.4. Cores

Paleta sugerida com base no conceito "saúde + tecnologia + confiabilidade" (sem inventar as cores oficiais da marca SES-PB, que devem ser confirmadas com a instituição se houver manual de identidade visual):

- Cor primária: um azul ou azul-esverdeado (associado a saúde/tecnologia/confiabilidade em portais institucionais de saúde).
- Cor de destaque (para botões/CTAs): um tom que contraste bem com a cor primária, mantendo contraste AA sobre fundo branco/claro.
- Fundo predominante claro (branco ou cinza muito claro), para leveza e legibilidade.
- Texto em cinza-escuro (não preto puro, para reduzir fadiga visual) sobre fundo claro.

*Observação:* se SES-PB, UFPB ou o projeto tiverem uma paleta institucional definida, ela deve prevalecer sobre esta sugestão — este plano não deve ser interpretado como definição final de marca.

## 9.5. Espaçamento

Espaçamento generoso entre seções (evitar poluição visual), consistente entre páginas — recomenda-se definir uma escala simples (ex.: múltiplos de 8px) usada em todos os componentes.

## 9.6. Cabeçalho e barra de links

Ver seção 6. Visualmente: cabeçalho com fundo neutro/claro e o nome do projeto em destaque; barra de links logo abaixo, com fundo levemente diferente do restante da página (para reforçar a separação visual pedida na RF01), itens dispostos horizontalmente com espaçamento uniforme.

## 9.7. Cards

Usados na home (atalhos) e nas páginas de Informações/Links e Serviços. Estrutura: título, ícone ou imagem pequena (opcional), descrição curta, ação (link/botão). Cantos levemente arredondados, sombra sutil ou borda fina — sem exagero.

## 9.8. Botões

Um único estilo primário de botão (cor de destaque, texto claro) para ações principais ("Explorar conteúdos", "Acessar serviço"); links secundários podem ser apenas texto sublinhado/colorido, sem necessidade de todo link virar um botão.

## 9.9. Rodapé

Aviso de caráter informativo (texto curto, sempre visível) + área de instituições com os 3 logos (seção 7). Fundo levemente diferenciado do conteúdo, para marcar o fim da página.

## 9.10. Área institucional

Ver seção 7 (Logos institucionais) — no rodapé, com padding generoso e alinhamento centralizado.

## 9.11. Comportamento mobile

- Barra superior: quebra em múltiplas linhas ou rolagem horizontal suave (nunca corte texto).
- Cards: empilhados verticalmente (1 coluna) em vez de lado a lado.
- Navegação interna: usa o menu lateral nativo do Streamlit, que já colapsa automaticamente em um ícone de menu ("hambúrguer") em telas estreitas.
- Botões e links: área de toque mínima recomendada de 44×44px.

---

# 10. Acessibilidade

## 10.1. Checklist de tarefas específicas

- [ ] **Contraste:** todo texto sobre fundo colorido/imagem atinge no mínimo a razão de contraste AA (4.5:1 para texto normal, 3:1 para texto grande) — verificar com ferramenta de contraste, não apenas visualmente.
- [ ] **Tamanho de fonte:** corpo de texto ≥16px; nada de texto menor que 12px em qualquer dispositivo.
- [ ] **Textos alternativos:** toda imagem, logo e fluxograma tem um `alt` (ou descrição textual equivalente, no caso de fluxogramas complexos) definido no JSON de metadados correspondente — nunca deixado em branco.
- [ ] **Navegação:** a navegação interna (menu lateral nativo) deve ser operável via teclado (isso já é garantido pelo componente nativo do Streamlit, mas deve ser verificado).
- [ ] **Estrutura semântica:** um único H1 por página (título da página), H2 para seções, H3 para subseções — nunca "pular" nível apenas por efeito visual (usar CSS para tamanho, não a hierarquia de título, quando o objetivo for só estético).
- [ ] **Não depender apenas de cor:** links devem ser diferenciáveis do texto comum por mais que a cor (ex.: sublinhado), e mensagens de erro/sucesso não devem depender só da cor (ex.: vermelho/verde) para serem compreendidas.
- [ ] **Responsividade:** ver seção 9.11 e Fase 11.
- [ ] **Compatibilidade com dispositivos móveis:** testar com leitor de tela básico do próprio celular (VoiceOver/TalkBack) ao menos na página inicial e no FAQ, para pegar problemas grosseiros de leitura.

## 10.2. Observação sobre limitações do Streamlit

O Streamlit não dá controle total sobre a estrutura HTML gerada (parte dela é interna ao framework). Este plano assume um nível de acessibilidade **pragmático e alcançável** dentro dessas limitações — não uma conformidade formal com WCAG 2.1 AA completa, que exigiria testes com ferramentas especializadas e possivelmente ajustes que o Streamlit não permite fazer de forma simples. Isso é proporcional ao tamanho do projeto (Regra 6 do briefing) e deve ser comunicado como tal aos responsáveis pelo projeto.

---

# 11. Estratégia de testes

## 11.1. O que faz sentido testar automaticamente

Dado que a aplicação é majoritariamente conteúdo estático renderizado pelo Streamlit (difícil de testar via `pytest` de forma significativa), o foco dos testes automatizados é a **camada de dados**, não a interface visual:

- Todo arquivo JSON de conteúdo é um JSON válido.
- Todo item de `links.json` tem `nome`, `url` (formato de URL válido) e `descricao`.
- Todo item de `faq.json` tem `id` único, `pergunta` e `resposta` não vazios.
- Todo item de `informacoes_index.json` aponta para um arquivo `.md` que de fato existe em `content/informacoes/`.
- Todo item de `fluxogramas.json` aponta para um arquivo existente em `assets/flowcharts/` e tem descrição não vazia.

Essas verificações usam `pytest` puro (sem necessidade de Selenium/Playwright), e são rápidas de rodar a cada mudança de conteúdo — inclusive úteis para pegar erros de digitação antes do deploy.

## 11.2. O que é validado manualmente (checklist, não automação)

- Navegação entre todas as páginas.
- Todos os links externos (3 serviços) abrindo corretamente em nova aba.
- Responsividade em três larguras de tela (desktop, tablet, celular).
- Contraste visual (com ferramenta simples de contraste).
- Textos alternativos presentes (revisão visual/código).
- Tempo de carregamento percebido (nenhuma imagem excessivamente pesada, RNF06).

## 11.3. O que **não** é feito no MVP (e por quê)

- **Testes end-to-end automatizados de UI** (Selenium/Playwright): desproporcional para um portal de conteúdo majoritariamente estático deste tamanho; o custo de manter esses testes (que quebram a cada pequena mudança visual) supera o benefício no MVP.
- **Testes de carga:** o volume de acesso esperado e a hospedagem gratuita (com limites já conhecidos) não justificam testes de carga formais nesta fase.
- **CI automatizado (GitHub Actions) rodando os testes a cada push:** é uma melhoria natural, mas não obrigatória para o MVP — pode ser adicionada na Fase 14 ou depois, como uma tarefa de baixo custo e alto valor para quando houver mais de um contribuidor.

## 11.4. Teste de deploy

Ver checklist de smoke test pós-publicação na seção 12.3.

---

# 12. Deploy no Streamlit Community Cloud

## 12.1. Pré-requisitos

- Repositório no GitHub com o projeto (branch `main` atualizada e testada — Fase 12 concluída).
- `requirements.txt` na raiz do projeto, listando as dependências reais (para o MVP, basicamente `streamlit`; não é necessário fixar a versão exata a menos que se queira reprodutibilidade estrita, mas é recomendável, ex. `streamlit>=1.40`).
- Conta no GitHub conectável ao Streamlit Community Cloud.

## 12.2. Passo a passo

1. Confirmar que `requirements.txt` está atualizado e correto (sem bibliotecas não usadas, sem bibliotecas padrão do Python listadas por engano).
2. (Opcional, mas recomendado) Fixar a versão do Python do projeto: isso pode ser feito diretamente nas configurações avançadas do app no painel do Streamlit Community Cloud, ou via um arquivo `runtime.txt` na raiz (ex.: `python-3.11`), dependendo do que estiver disponível na interface no momento do deploy.
3. Acessar `share.streamlit.io` e entrar com a conta do GitHub.
4. Clicar em "New app".
5. Selecionar o repositório, a branch (`main`) e o caminho do arquivo principal (`app.py`).
6. Definir o nome/subdomínio do app (isso define a URL final, no formato `https://<nome-escolhido>.streamlit.app`).
7. Clicar em "Deploy" e aguardar o build (instalação de dependências e inicialização).
8. Se o MVP não usa nenhuma chave de API/segredo, a seção de "Secrets" pode ficar vazia — não é obrigatória para este projeto. Ela já deve existir como conceito (`.streamlit/secrets.toml`, não versionado) para quando funcionalidades futuras precisarem de credenciais (ver seção 13 — Segurança).
9. Após o build concluir, acessar a URL pública gerada e validar (checklist abaixo).

## 12.3. Checklist de smoke test pós-publicação

- [ ] A URL pública abre sem erro, a partir de uma rede diferente da do desenvolvedor (ex.: dados móveis, ou pedir para outra pessoa testar).
- [ ] Todas as 6 áreas de navegação carregam (Início, Informações, Fluxogramas, FAQ, Links e Serviços, Sobre).
- [ ] Os 3 links da barra superior abrem os serviços corretos em nova aba.
- [ ] As imagens, fluxogramas e logos (mesmo que placeholders) carregam corretamente.
- [ ] O site é usável em um celular real (não apenas no simulador do navegador).
- [ ] Não há nenhuma referência a `localhost`/`127.0.0.1` em nenhum lugar da aplicação publicada (RNF01).

## 12.4. Atualização contínua

Qualquer novo `git push` para a branch `main` (após merge de uma nova feature/branch) republica automaticamente a aplicação no Streamlit Community Cloud — não há passo manual de deploy além do primeiro cadastro do app. Isso deve ser testado uma vez ainda na Fase 13 (ex.: um pequeno commit de ajuste de texto) para confirmar que o pipeline de atualização funciona antes de considerar o deploy "concluído".

## 12.5. Observação sobre o nível gratuito

O Streamlit Community Cloud gratuito hiberna aplicativos sem acesso por um tempo, e o primeiro acesso após a hibernação leva alguns segundos a mais para "acordar" o app. Isso é um comportamento esperado do plano gratuito (coerente com a exigência de gratuidade, RNF02) e deve ser comunicado no README como uma característica conhecida, não como um bug a corrigir no MVP.

---

# 13. Segurança e privacidade

## 13.1. O que se aplica agora (MVP)

- Nenhum dado pessoal é coletado (não há formulário de cadastro, login ou captura de dados do usuário) — conforme seção 36 do documento de requisitos.
- Nenhum segredo/chave de API é necessário no MVP, já que não há integração técnica com sistemas externos (os "links" são apenas âncoras HTML, não chamadas de API).
- Ainda assim, criar desde já o padrão `.streamlit/secrets.toml` (arquivo vazio ou de exemplo, `secrets.toml.example`, versionado) e garantir que `.streamlit/secrets.toml` real esteja no `.gitignore` — isso evita que, quando uma chave de API for necessária no futuro (ex.: para o chatbot), ela seja acidentalmente commitada por falta de hábito já estabelecido.
- Todo o conteúdo do repositório (código e `content/`) é público, pois o repositório GitHub e o Streamlit Community Cloud gratuito operam sobre repositórios públicos — portanto, nenhum dado sensível (senhas, chaves, dados pessoais de terceiros) deve jamais ser colocado em `content/` ou em qualquer arquivo versionado.
- Links externos apontam para domínios de terceiros; o portal não é responsável pelo conteúdo desses sites, mas deve manter a curadoria de que os links apontam para os serviços oficiais corretos (risco R6, seção 0.7).
- Conteúdo relacionado à saúde deve manter o aviso de caráter informativo (seção 21) sempre visível, e toda informação deve citar fonte (seção 44) — isso é mais uma questão de confiabilidade editorial do que de segurança técnica, mas está diretamente ligado à responsabilidade do projeto.

## 13.2. O que só será necessário com funcionalidades futuras

| Funcionalidade futura | Necessidade de segurança que ela introduz |
|---|---|
| Painel administrativo / edição online | Autenticação, controle de acesso, proteção contra edição não autorizada |
| Banco de dados | Backup, controle de acesso ao banco, proteção contra injeção de dados maliciosos em formulários |
| Chatbot / RAG | Gestão segura de chave de API de LLM (via `st.secrets`, nunca hardcoded), limitação de uso/custo, política de resposta a perguntas fora do escopo de saúde |
| Coleta de dados pessoais (se algum dia introduzida) | Avaliação de finalidade, base legal, política de privacidade, tempo de retenção — conforme legislação aplicável (LGPD), a ser avaliado com apoio jurídico quando/se essa necessidade surgir |

---

# 14. Preparação para busca, chatbot e RAG

## 14.1. Por que isso importa desde o MVP

O documento de requisitos é explícito: a arquitetura atual deve **facilitar**, não impedir, a evolução para busca inteligente e chatbot com RAG. As decisões abaixo não implementam nada disso agora — apenas evitam retrabalho quando chegar a hora.

```text
Portal (MVP)
   ↓
Base de conhecimento (conteúdo já organizado com id/fonte)
   ↓
Busca (primeira evolução pós-MVP)
   ↓
Recuperação de documentos (indexação do conteúdo)
   ↓
LLM (modelo de linguagem consultando o conteúdo recuperado)
   ↓
Chat (interface conversacional)
```

## 14.2. Decisões do MVP que facilitam essa evolução

1. **Cada unidade de conteúdo tem um identificador estável** (`id` no FAQ, caminho de arquivo estável nos artigos de Informações) — necessário para que, no futuro, o chatbot possa citar exatamente qual FAQ ou artigo embasou uma resposta (requisito explícito da seção 35 do documento: "indicar as fontes utilizadas").
2. **Toda informação cita sua fonte** desde o MVP (seção 44) — sem isso, seria necessário reescrever todo o conteúdo antes de alimentar um sistema de RAG, já que a citação de fonte é um requisito do próprio chatbot futuro.
3. **Conteúdo textual em Markdown/JSON, nunca "preso" dentro de imagens** — um fluxograma, por exemplo, deve ter uma descrição textual equivalente (já exigida por acessibilidade, seção 10), que também serve como o texto que futuramente será indexado, já que texto dentro de uma imagem não pode ser buscado ou recuperado por um sistema de RAG sem OCR.
4. **`utils/content_loader.py` como camada única de acesso ao conteúdo** — no futuro, um script de ingestão para uma base vetorial (ou uma API FastAPI, se o projeto migrar para essa arquitetura) pode reaproveitar exatamente essas mesmas funções de carregamento, sem duplicar lógica de leitura de arquivos.
5. **Granularidade de conteúdo pensada para recuperação** — por exemplo, cada pergunta do FAQ é uma unidade independente (não um único bloco de texto com todas as perguntas), o que já é o formato ideal para ser transformado em um "chunk" de RAG no futuro, sem necessidade de dividir o texto manualmente depois.

## 14.3. O que explicitamente não é feito agora

- Nenhuma biblioteca de embeddings, banco vetorial ou LLM é adicionada ao `requirements.txt` no MVP.
- Nenhuma interface de chat é criada.
- Nenhuma chamada a API de IA é feita.

---

# 15. Roadmap futuro

```text
MVP
 ↓
Portal público
 ↓
Busca
 ↓
Documentos
 ↓
Base de conhecimento
 ↓
Chat
 ↓
RAG
 ↓
IA
```

| Etapa | Objetivo | Novas tecnologias | Impacto na arquitetura | Quando vale a pena |
|---|---|---|---|---|
| **MVP** | Centralizar informação e serviços com o menor custo/complexidade | Python, Streamlit, GitHub, Streamlit Community Cloud | Base deste plano | Agora |
| **Portal público** | MVP publicado, estável, recebendo os primeiros usuários reais | — | Nenhuma (é o resultado da Fase 13) | Imediatamente após a Fase 13 |
| **Busca** | Permitir encontrar conteúdo por palavra-chave, sem depender de navegar por categoria | Nenhuma nova biblioteca necessariamente — uma busca simples pode filtrar os JSON já existentes em memória | Baixo — não exige banco de dados | Quando o volume de FAQ/Informações crescer o suficiente para dificultar a navegação linear (ex.: dezenas de itens) |
| **Documentos** | Publicar PDFs/materiais institucionais mais extensos | Biblioteca de leitura de PDF, se for preciso extrair texto para indexação | Médio — exige um índice de metadados de documentos, semelhante ao já usado para Informações | Quando houver material institucional relevante para disponibilizar além dos textos curtos do MVP |
| **Base de conhecimento** | Consolidar todo o conteúdo (FAQ, Informações, Documentos) em uma estrutura única, pesquisável e com metadados ricos (fonte, data, categoria) | Possivelmente um banco de dados leve (ex.: SQLite) ou continuar em arquivos, dependendo do volume | Médio | Quando o conteúdo dos itens anteriores estiver maduro e for necessário unificá-los para alimentar busca/chat de forma consistente |
| **Chat** | Interface conversacional simples para perguntas frequentes | Um modelo de linguagem (via API), interface de chat no Streamlit | Alto — primeira introdução de custo de API e de gestão de segredos (`st.secrets`) | Quando a base de conhecimento estiver estruturada e estável, e houver orçamento/aprovação institucional para o uso de uma API de IA |
| **RAG** | Fazer o chat responder com base no conteúdo real do repositório, citando fontes, em vez de "alucinar" respostas | Índice de busca semântica (embeddings + banco vetorial) | Alto — nova camada de indexação e de custo (geração de embeddings) | Junto com o Chat, ou logo em seguida, para cumprir o requisito de "evitar respostas sem base documental" (seção 35 do documento) |
| **IA (evolução ampla)** | Recursos adicionais de IA além do chat (ex.: sumarização automática, recomendação de conteúdo relacionado) | Depende do recurso específico | Variável | Caso a caso, após o Chat + RAG estarem consolidados e existir demanda concreta |

---

# 16. Checklist final

Derivado diretamente da seção 37 do documento de requisitos, mais os itens de processo definidos por este plano:

**Infraestrutura e publicação**
- [ ] Repositório criado no GitHub.
- [ ] Ambiente Python configurado (venv + `requirements.txt`).
- [ ] Streamlit configurado (`.streamlit/config.toml`).
- [ ] Estrutura de diretórios criada (seção 2).
- [ ] O portal possui uma URL pública.
- [ ] O portal funciona sem depender de `localhost`.
- [ ] O projeto está versionado no GitHub.
- [ ] O projeto pode ser atualizado através do GitHub (`git push` → redeploy automático testado).

**Conteúdo e funcionalidades do MVP**
- [ ] Página inicial implementada.
- [ ] Barra superior de links criada, com os 3 links iniciais funcionando.
- [ ] Página de Informações existente, com pelo menos um artigo por categoria inicial.
- [ ] Área de Fluxogramas existente, com pelo menos um fluxograma.
- [ ] FAQ criado, com as 4 perguntas mínimas do documento.
- [ ] Página de Links e Serviços criada.
- [ ] Página Sobre criada, com aviso de caráter informativo visível.
- [ ] Área de logotipos existente, com espaço para SES-PB, UFPB e PET Saúde Digital (placeholders aceitáveis até o recebimento dos arquivos oficiais).
- [ ] Conteúdo pode ser atualizado sem grande alteração estrutural do código (JSON/Markdown).

**Qualidade**
- [ ] O site funciona em computador.
- [ ] O site funciona em celular.
- [ ] Contraste, fontes e textos alternativos revisados (seção 10).
- [ ] Testes automatizados de conteúdo passando (`pytest`).
- [ ] Checklist manual de responsividade/links/acessibilidade concluído.

**Documentação e evolução futura**
- [ ] README completo.
- [ ] Documentação de arquitetura e de esquema de conteúdo criadas (`docs/`).
- [ ] Pendência de logos oficiais documentada, se ainda não resolvida.
- [ ] Decisão sobre busca (RF08 — tratada como pós-MVP) confirmada com os responsáveis do projeto.

---

# 17. Ordem recomendada de implementação

Sequência definitiva, fase a fase, do início ao deploy:

1. **Fase 0 — Preparação:** repositório, ambiente, `.gitignore`, primeiro commit.
2. **Fase 1 — Estrutura inicial:** `requirements.txt`, pastas do projeto, `app.py` mínimo rodando localmente.
3. **Fase 2 — Tema visual:** cores, tipografia, `.streamlit/config.toml`.
4. **Fase 3 — Cabeçalho + barra superior:** `links.json`, `content_loader`, `header.py`, `top_links_bar.py`.
5. **Fase 4 — Página inicial completa:** hero, cards de atalho.
6. **Fase 5 — Informações:** índice + artigos em Markdown + página.
7. **Fase 6 — Fluxogramas:** metadados + assets + página.
8. **Fase 7 — FAQ:** `faq.json` + página.
9. **Fase 8 — Links e Serviços:** página dedicada reaproveitando `links.json`.
10. **Fase 9 — Sobre + aviso informativo:** texto revisado + componente reutilizável.
11. **Fase 10 — Logos e rodapé:** placeholders ou arquivos oficiais, componente de rodapé em todas as páginas.
12. **Fase 11 — Responsividade e acessibilidade:** ajustes finos em todos os componentes.
13. **Fase 12 — Testes:** `pytest` completo + checklist manual.
14. **Fase 13 — Deploy:** publicação no Streamlit Community Cloud, smoke test.
    → **A partir daqui, o projeto está pronto para publicação e uso público (MVP concluído).**
15. **Fase 14 — Documentação e preparação para evolução futura:** README, `docs/`, revisão de fontes citadas.
    → **A partir daqui, o projeto está pronto para iniciar a próxima etapa do roadmap (seção 15), a começar pela busca.**

As Fases 5 a 9 podem, na prática, ser desenvolvidas em uma ordem ligeiramente diferente entre si (todas dependem apenas da Fase 4, não umas das outras) — a ordem acima é a recomendada por seguir a prioridade de conteúdo do próprio documento de requisitos, mas não é uma dependência técnica rígida entre elas.

---

# 18. Conformidade com as diretrizes do briefing

- Nenhum código foi implementado neste documento — apenas pseudocódigo ilustrativo pontual na seção 6, conforme explicitamente solicitado ("explique como implementar isso no Streamlit").
- Nenhum requisito do documento de requisitos foi omitido; a única reinterpretação feita (RF08 — Busca) foi explicitamente apontada, justificada e marcada como pendente de confirmação (seção 0.8a).
- Nenhum requisito desnecessário foi adicionado; os acréscimos à estrutura de diretórios (`tests/`, `docs/`) servem diretamente às seções "Testes" e "Documentação" já pedidas pelo próprio briefing.
- Banco de dados não foi introduzido no MVP, com justificativa própria reforçando a decisão já tomada no documento de requisitos (seção 32).
- Nenhum frontend além do Streamlit foi introduzido.
- Alternativas técnicas foram comparadas e uma foi escolhida em pelo menos três pontos centrais: navegação interna nativa vs. customizada (seção 1.4), formato de conteúdo JSON/Markdown/YAML (seção 8), e tratamento de branches/commits (seção 5).
- MVP e funcionalidades futuras estão claramente separados ao longo de todo o documento (seções 0.3, 0.4 e 15 em especial).

