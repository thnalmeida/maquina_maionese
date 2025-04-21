# maquina_maionese

# 🥄 Máquina de Maionese

Um sistema de busca de receitas inspirado no jogo **Stardew Valley**, desenvolvido como parte da disciplina **Algoritmos e Programação II**, ministrada pelo professor **Hokama** na Universidade Federal de Itajubá (UNIFEI).

## 🎮 Contexto

No universo de Stardew Valley, os jogadores podem fabricar diversos itens a partir de receitas que combinam ingredientes variados. Pensando nisso, este projeto simula uma **máquina de busca** que permite:

- 🔍 Consultar os **ingredientes necessários** para fabricar um item (ex: "Elixir da vida")
- 🔄 Verificar **quais receitas utilizam** um determinado item (ex: "Madeira")

## 🧠 Conceitos aplicados

Este projeto foi idealizado para aplicar e reforçar os seguintes conceitos:

- Estruturas de dados: **tabela hash** com resolução de colisões via **árvores binárias de busca**
- Programação orientada a objetos (POO)
- Manipulação de arquivos (`craft.txt`)
- Modularidade e boas práticas de codificação em **Python**

## ⚙️ Como funciona

As receitas são carregadas a partir de um arquivo de texto (`craft.txt`). O sistema armazena essas informações em duas tabelas hash:

- `TabelaHash`: armazena as receitas com seus ingredientes
- `TabelaItens`: armazena os itens e as receitas onde são utilizados

Ambas as tabelas resolvem colisões com **árvores binárias de busca**.

Ao rodar o programa, o usuário pode digitar os seguintes comandos:

| Comando        | Descrição                                                        |
|----------------|------------------------------------------------------------------|
| `r <nome>`     | Busca a receita pelo nome e exibe seus ingredientes              |
| `i <item>`     | Exibe todas as receitas que utilizam o item                      |
| `p r`          | Imprime a tabela de receitas com as árvores                     |
| `p i`          | Imprime a tabela de itens com as árvores                        |
| `q`            | Encerra o programa                                               |

## ▶️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/maquina-de-maionese.git
   cd maquina-de-maionese
Adicione um arquivo chamado craft.txt com as receitas

Execute o programa:
bash
Copy
Edit
python maquina_maionese.py

📌 Este projeto foi desenvolvido como parte da disciplina Algoritmos e Programação II da UNIFEI, sob orientação do professor Hokama.

🧠 Inspiração
"Máquina de Maionese" é uma brincadeira com o item clássico do jogo Stardew Valley e simboliza o espírito divertido e criativo do projeto.

🐍 Requisitos
Python 3.6+
Um terminal para rodar o script e interagir via comandos

🎓 Projeto acadêmico com propósito didático.


