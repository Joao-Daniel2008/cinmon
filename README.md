# 🎮 CinMon

![Estilo do Jogo](https://img.shields.io/badge/Estilo-Pixel_Art-blueviolet?style=for-the-badge)
![Engine](https://img.shields.io/badge/Made%20with-Pygame-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Jog%C3%A1vel-success?style=for-the-badge)

> Projeto da disciplina Introdução à Programação — CIn/UFPE

CinMón é um jogo de RPG de turno fortemente inspirado na clássica saga Pokémon, mas com uma reviravolta única: ele se passa no universo do CIn (Centro de Informática) da UFPE! Prepare-se para enfrentar os desafios da vida acadêmica, explorar os cenários do centro em pixel art e capturar criaturas selvagens enquanto tenta sobreviver aos treinadores do bloco.
Sua jornada começa no laboratório do Professor Iyoda, onde você escolhe seu primeiro CinMon e recebe suas primeiras Crachabolas. A partir daí, o mundo do CIn é seu: explore as moitas para encontrar criaturas selvagens, evolua seu time, enfrente treinadores em batalhas táticas por turno e visite o Centro Cin para curar seus companheiros ou a Loja para reabastecer seus itens.


🛍️ Itens Coletáveis

Ao explorar os cenários, você encontrará itens espalhados pelo mapa que podem ser coletados apenas passando por cima deles:

- Crachabola: usada durante batalhas para tentar capturar CinMons selvagens e expandir seu time

- Poção: recupera o HP do seu CinMon durante o combate, mantendo-o apto para batalhar

- CinReais: a moeda do jogo, usada para comprar mais itens na loja do Seu Jailson

---

## 👥 Membros da Equipe

| Membro |
|---|
| André Bessa da Costa |
| Ewerton Manoel Fernandes |
| João Daniel de Mélo Miranda|
| João Lucas Gomes da Silva |
| João Lucas Tavares Cavalcanti |
| Marcelo Guilherme de Barros Herminio |

---

## 📖 Sinopse e Objetivo

Você joga na pele de Cin, um calouro do Centro de Informática que, ao invés de se preocupar apenas com provas e projetos, descobre um mundo paralelo de batalhas e criaturas escondido nas dependências do CIn. Seu objetivo é explorar todos os cenários do campus, das moitas selvagens aos corredores internos do bloco, capturar e evoluir seus CinMons, e desafiar os grandes Mestres Treinadores que dominam cada área. Ao longo da jornada, você acumula experiência, itens e conhecimento, até se tornar o maior Player do CIn!

### 👥 Personagens de Destaque

- **Professor Iyoda**: o mestre lendário que guia (e testa) seus conhecimentos e habilidades.
- **Treinadores Adversários**: enfrente figuras conhecidas como *Ewerton*, *JL*, *José* e *João Daniel* em batalhas táticas.
- **Seu Jailson**: o herói do suporte! Atua como enfermeiro (cura seus CinMons) e vendedor (reabastece seus suprimentos).

---

## 🚀 Funcionalidades

- **Batalhas Estilo Clássico**: sistema de combate em turnos contra CinMons selvagens e outros treinadores.
- **Exploração no CIn**: caminhe pelos cenários em Pixel Art e explore as famosas "moitas" para encontrar novas criaturas.
- **Itens Coletáveis**: colete Crachabolas, Poções e CinReais espalhados pelos cenários.
- **HUD de Inventário**: acompanhe seus itens em tempo real durante a exploração.
- **Modo Versus**: suporte para batalha online para desafiar seus amigos de laboratório.
- **Trilha Sonora Dinâmica**: músicas que mudam de acordo com o contexto (exploração, batalha, menu).
- **Sistema de Salvamento**: salve o progresso da sua jornada a qualquer momento.

---

## 📸 Capturas de Tela

<img width="915" height="353" alt="Batalha entre CinMons" src="https://github.com/user-attachments/assets/2a2dfe6a-723c-45f0-984f-b71c7b8fb845" />

*⚔️ Sistema de batalha por turno: Naruto Beast (Lv 8) enfrenta Rayquaza (Lv 2)*

<img width="505" height="394" alt="Exploração do cenário" src="https://github.com/user-attachments/assets/66f3cf65-4f60-4423-a547-7c4b2acc81a3" />

*🌿 Exploração dos cenários do CIn: moitas escondem CinMons selvagens e treinadores aguardam o desafio*

<img width="557" height="301" alt="Cenário com treinador" src="https://github.com/user-attachments/assets/31372a41-028e-4da3-963a-c80b56a1c56d" />

*🏫 Cenário interno do CIn: o Professor Iyoda e as Crachabolas aguardam o jogador*

<img width="524" height="327" alt="Centro Cin" src="https://github.com/user-attachments/assets/edebc4fb-a0c3-42de-b03f-41aded5a56ea" />

*🏥 Centro Cin: onde você cura seus CinMons e se prepara para os próximos desafios*

---

## 🧱 Arquitetura do Projeto

O jogo foi desenvolvido com a biblioteca Pygame e estruturado de forma modular. A pasta `assets/` contém todos os recursos visuais e sonoros, e os arquivos principais ficam na raiz:

```
assets/
├── imagens/
│   ├── batalha/        — sprites de batalha, barras de HP/XP, moldes
│   ├── letras/         — fonte pixel art customizada (a-z, 0-9)
│   ├── menus/          — telas de menu, botões, balões de fala
│   └── cenarios/       — fundos dos cenários (cenario1 a cenario9)
├── musicas/            — trilhas sonoras (menu, batalha, chefes)
└── sons/               — efeitos sonoros (ataque, nível, coleta de item)

jogo.py             — loop principal, gerenciamento de cenários, eventos e estados
funcoes_Classes.py  — classes principais e funções de batalha, animações e troca de cenário
cimons.py           — instâncias de todas as criaturas disponíveis no jogo
imagens.py          — carregamento centralizado de todos os assets visuais e sonoros
variaveis.py        — variáveis globais de estado (posições, listas de objetos por cenário)
objetos.py          — retângulos de colisão dos objetos do mapa
itenschao.py        — sistema de itens coletáveis no chão (classe ItemChao)
```

**Descrição dos módulos principais:**

- **`jogo.py`**: arquivo principal. Contém o loop de jogo, gerenciamento de cenários, eventos de teclado, estados (batalha, menu, multiplayer, loja, centrocin) e o sistema de save/load.
- **`funcoes_Classes.py`**: define as classes `Player`, `Cimons`, `equipe`, `mochila`, `treinador` e `ataques`. Também contém todas as funções de batalha, animações, troca de cenário e lógica de menus.
- **`cimons.py`**: instancia todos os CinMons do jogo (lupi, rath, goku, mclovin, mewtwo, naruto, rayquaza, homelander) com seus atributos e movimentos.
- **`imagens.py`**: carrega centralizadamente todos os assets (imagens, sons, músicas) usando `pathlib` para compatibilidade entre sistemas.
- **`variaveis.py`**: armazena variáveis globais compartilhadas entre módulos: posições do player, listas de objetos e gramas por cenário.
- **`objetos.py`**: define os `pygame.Rect` de colisão de todos os objetos estáticos do mapa (portas, mesas, npcs).
- **`itenschao.py`**: sistema de itens coletáveis. Define a classe `ItemChao` com lógica de spawn em posições fixas por cenário, coleta por colisão, efeito sonoro e respawn automático por tempo.

---

## 🛠️ Ferramentas, Bibliotecas e Frameworks

| Ferramenta | Justificativa |
|---|---|
| **Python** | Linguagem principal do projeto, indicada pela disciplina |
| **Pygame** | Biblioteca para jogos 2D : renderização gráfica, captura de eventos, áudio e colisões |
| **Socket** | Implementação do sistema multiplayer  |
| **JSON** |Salvamento do estado do jogo (save/load) |
| **Git/GitHub** | Controle de versão e colaboração entre os integrantes |
| **VS Code** | Ambiente de desenvolvimento utilizado pela equipe |
| **Pixilart** | Criação e edição dos sprites e pixel art do jogo |
| **Pixabay** | Banco de imagens e sons complementares |

---

## 📚 Conceitos da Disciplina Utilizados

- **Programação Orientada a Objetos (POO)**: a estrutura do jogo é baseada em classes como `Player`, `Cimons`, `equipe`, `mochila`, `treinador`, `ataques` e `ItemChao`, definidas em `funcoes_Classes.py` e `itenschao.py`, onde cada uma reúne os dados e comportamentos relacionados a uma entidade específica do jogo.

- **Encapsulamento**: as classes escondem sua lógica interna e expõem apenas o necessário. A classe `Cimons` em `funcoes_Classes.py`, por exemplo, cuida sozinha do crescimento do personagem: ganho de XP, subida de nível e atualização de atributos são feitos internamente pelo método `subir_nivel()`. Da mesma forma, a classe `mochila` controla o saldo e os itens através do método `comprar()`.

- **Abstração**: detalhes complexos são ocultados atrás de métodos simples. Em `itenschao.py`, `verificar_coleta()` esconde a lógica de colisão com o player. Em `funcoes_Classes.py`, `colisaon()` da classe `Player` abstrai a verificação com todos os objetos do mapa, ambos retornam apenas `True` ou `False`.

- **Composição**: objetos são construídos a partir de outros objetos. Em `funcoes_Classes.py`, a classe `equipe` agrupa instâncias de `Cimons` em `self.lista` e oferece métodos como `curar()`, `verificar()` e `lancar()` para gerenciá-las em conjunto. A `mochila` segue o mesmo princípio com `listaDeles` e `listaDeQtd`.

- **Reutilização de código**: o método `clonar()` da classe `Cimons` em `funcoes_Classes.py` permite criar cópias completamente independentes de uma criatura. Usado em `cimons.py` e em `jogo.py`, é fundamental para que treinadores diferentes possam ter o mesmo tipo de CinMon sem compartilhar HP, nível ou estado de batalha.

- **Polimorfismo**: o método `efetivo()` da classe `ataques` em `funcoes_Classes.py` produz resultados distintos dependendo de quem recebe o ataque , retorna `2`, `0.5` ou `1` conforme a combinação de tipos. É chamado dentro de `batalha_selvagem()` e `batalha_treinador()` para calcular o dano final.

- **Listas**: estrutura central do jogo. Em `variaveis.py`, listas armazenam objetos e gramas de cada cenário. Em `funcoes_Classes.py`, `self.lista` da classe `equipe` gerencia o time de CinMons. Em `itenschao.py`, `itens_cenario_global` armazena os itens ativos no mapa, atualizada dinamicamente conforme o jogador coleta.

- **Dicionários**: em `funcoes_Classes.py`, os ataques de cada `Cimons` são mapeados dinamicamente em `self.ataques` (`{'ataque1': ..., 'ataque2': ...}`). Em `jogo.py`, o dicionário `estado` representa o progresso completo do jogo - posição, equipe, inventário e treinadores derrotados - e é convertido em JSON pelo método `salvarJogo()`.
---

## 📝 Divisão de Trabalho

- **André Bessa**: Desenvolveu o menu inicial, o HUD, o sistema de itens coletáveis e integrou as músicas e efeitos sonoros.
- **Ewerton Manoel**: Desenvolveu as mecânicas de batalha e atuou na criação e design dos personagens.
- **João Daniel**: Responsável pela estruturação geral do jogo, desenvolvimento da movimentação e implementação das mecânicas principais e de batalha.
- **João Lucas Gomes**: Responsável por toda a identidade visual, incluindo o design de cenários, sprites e personagens.
- **João Lucas Tavares**: Desenvolveu a introdução da narrativa, o sistema de Sprint, a documentação técnica (README) e auxiliou nas mecânicas de batalha.
- **Marcelo Herminio**: Desenvolveu o sistema de cura, criou as artes das poções, aprimorou a mecânica da bolsa e auxiliou na integração de áudio.

---

## 📈 Desafios, Erros e Lições Aprendidas

**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**

Não planejar adequadamente a estrutura do código antes de adicionar novas funcionalidades, o que gerou bugs visuais difíceis de rastrear: como o HUD e os itens coletáveis sumindo durante as animações de movimento do personagem. O problema vinha do fato de o jogo usar `time.sleep()` em vez de um clock de frames, fazendo com que a tela fosse redesenhada várias vezes sem incluir esses elementos. Lidamos revisando e reorganizando o fluxo de renderização conforme os problemas apareciam, centralizando o desenho do HUD e dos itens dentro da própria função de movimento para garantir que aparecessem em todos os frames..

**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**

Aprender a usar o Pygame e o GitHub, já que nenhum dos dois era do conhecimento do grupo. No Pygame, o maior obstáculo foi entender o loop de jogo e como gerenciar estados (batalha, menu, exploração) de forma organizada. No GitHub, o desafio foi lidar com conflitos de merge em arquivos compartilhados por toda a equipe. Lidamos estudando documentação e tutoriais, praticando junto com o desenvolvimento do próprio jogo e adotando um fluxo de trabalho com comunicação constante para evitar sobrescrever o trabalho uns dos outros.

**Quais as lições aprendidas durante o projeto?**

A principal lição foi a importância de planejar a arquitetura do código antes de sair implementando. Pequenas decisões tomadas no início, como usar variáveis globais em excesso ou não separar responsabilidades entre módulos, geraram retrabalho considerável no final. Além disso, aprendemos que comunicação constante entre os membros da equipe é tão importante quanto o código em si, e que trabalhar com controle de versão desde o início do projeto torna tudo mais organizado e seguro.

---

## 🚀 Como Jogar

**Requisitos:**
- Python 3.12 ou inferior instalado
- Pygame 2.x instalado

**Instalação:**
```bash
git clone https://github.com/Joao-Daniel2008/cinmon.git
cd cinmon
pip install pygame
python jogo.py
```

**Controles:**

| Tecla | Ação |
|:---:|:---|
| **◀ ▲ ▼ ▶** | Movimentação do personagem / Navegação nos menus |
| **Espaço** | Interagir / Confirmar / Prosseguir diálogos |
| **Backspace** | Voltar / Cancelar |
| **M** | Abrir a Bolsa / Menu de CinMons |
| **S** | Salvar o jogo |
| **V** | Sprint (aumentar a velocidade) |

---

**Boa jornada e vire o maior jogador de Cinmon do CIn! 🏆**
