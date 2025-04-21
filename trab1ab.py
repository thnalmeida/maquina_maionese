
#Carregar um arquivo de receitas
#Armazenar as receitas em uma tabela hash (dicionário) 
#Permitir as buscas por receitas digitando o comando "r"
#Permitir a busca por ingrediente com o comando "i"
#Impressão das árvores binárias

#definindo o tamanho fixo da tabela hash, como teremos mais receitas do que numero de "casas", resolveremos os conflitos (COLISÃO) por meio de árvore binária
#COLISAO: mais de uma receita indo pra mesma posição
TAMANHO_TABELA = 29

#função de hash fornecida
#essa função transforma uma string (como o nome de uma receita) em um número entre 0 e 28 para indexar a tabela. 
#Usa os códigos ASCII dos caracteres da string com multiplicadores.
def calcular_hash(s):
    mult = 1 
    hash_value = 0 
    for c in s: 
        hash_value += mult * ord(c) 
        mult += 1 
    return hash_value % TAMANHO_TABELA

#classe para representar um nó da árvore binária
class NoArvore:
    def __init__(self, chave, valor):
        self.chave = chave  #nome da receita 
        self.valor = valor  #ingredientes
        self.esq = None  #subárvore esquerda
        self.dir = None  #subárvore direita

#classe para representar a árvore binária de busca
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor):
        def _inserir(no, chave, valor):
            if no is None:
                return NoArvore(chave, valor)
            if chave < no.chave:
                no.esq = _inserir(no.esq, chave, valor)
            elif chave > no.chave:
                no.dir = _inserir(no.dir, chave, valor)
            else:
                no.valor = valor  #atualiza os ingredientes se a receita já existe
            return no
        self.raiz = _inserir(self.raiz, chave, valor)

    def buscar(self, chave):
        def _buscar(no, chave):
            if no is None:
                return None
            if chave < no.chave:
                return _buscar(no.esq, chave)
            elif chave > no.chave:
                return _buscar(no.dir, chave)
            else:
                return no.valor
        return _buscar(self.raiz, chave)

    def __str__(self):
        def pre_ordem(no):
            if no is None:
                return "None"
            return f"({no.chave}, {pre_ordem(no.esq)}, {pre_ordem(no.dir)})"
        return pre_ordem(self.raiz)

#classe da tabela hash
class TabelaHash:
    def __init__(self):
        self.dados = [None] * TAMANHO_TABELA  #tabela com tamanho fixo de 29 posições
        
    #CHAVE = nome da receita // VALOR = ingredientes
    def inserir(self, chave, valor):
        indice = calcular_hash(chave)
        if self.dados[indice] is None:
            self.dados[indice] = ArvoreBinariaBusca()  #cria uma árvore binária se a posição estiver vazia
        self.dados[indice].inserir(chave, valor)  #insere o par (chave, valor) na árvore da posição

    #busca a receita na tabela hash
    def buscar(self, chave):
        indice = calcular_hash(chave)
        arvore = self.dados[indice]
        if arvore:
            return arvore.buscar(chave)
        return None

    #imprime a tabela inteira com as árvores, a função será chamada posteriormente quando o usuário digitar "p r"
    def imprimir_receitas(self):
        for i in range(TAMANHO_TABELA):
            if self.dados[i] is None or self.dados[i].raiz is None:
                print("None")
            else:
                print(self.dados[i])

    # imprime a tabela de itens no mesmo formato das receitas
    def imprimir_itens(self, tabela_itens):
        def pre_ordem(no):
            if no is None:
                return "None"
            item = no.chave
            receitas = no.valor
            return f"({item}, {pre_ordem(no.esq)}, {pre_ordem(no.dir)})"

        for i in range(TAMANHO_TABELA):
            if tabela_itens.dados[i] and tabela_itens.dados[i].raiz:
                print(pre_ordem(tabela_itens.dados[i].raiz))
            else:
                print("None")

#classe para a segunda tabela hash que armazena item e a lista de receitas onde é usado
#Nessa tabela: CHAVE: item/ingrediente //  VALOR =  lista com os nomes das receitas que usam aquele item
class TabelaItens:
    def __init__(self):
        self.dados = [None] * TAMANHO_TABELA

    def inserir(self, item, receita):
        indice = calcular_hash(item)
        if self.dados[indice] is None:
            self.dados[indice] = ArvoreBinariaBusca()

        # Se o item já existe na árvore, atualiza a lista de receitas
        receitas_existentes = self.dados[indice].buscar(item)
        if receitas_existentes:
            if receita not in receitas_existentes:
                receitas_existentes.append(receita)
        else:
            self.dados[indice].inserir(item, [receita])

    def buscar(self, item):
        indice = calcular_hash(item)
        if self.dados[indice]:
            return self.dados[indice].buscar(item)
        return None

#função para carregar receitas a partir do arquivo
def carregar_receitas(nome_arquivo, tabela_receitas, tabela_itens):
    #abrindo o arquivo com as receitas e armazenando na tabela hash
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    nome_receita = None  #variável que armazena o nome da receita
    ingredientes = []  #lista com os ingredientes da receita

    for linha in linhas:  #iterando cada linha do arquivo
        linha = linha.strip()

        if linha == "":  #ao encontrar uma linha em branco, salva a receita anterior na tabela hash
            if nome_receita:
                tabela_receitas.inserir(nome_receita, ingredientes)
                for item in ingredientes:
                    partes = item.split()
                    nome_item = " ".join(partes[:-1])
                    tabela_itens.inserir(nome_item, nome_receita)
                nome_receita = None
                ingredientes = []
        elif nome_receita is None:
            nome_receita = linha
        else:
            ingredientes.append(linha)

    if nome_receita:
        tabela_receitas.inserir(nome_receita, ingredientes)
        for item in ingredientes:
            partes = item.split()
            nome_item = " ".join(partes[:-1])
            tabela_itens.inserir(nome_item, nome_receita)

def main():
    tabela_receitas = TabelaHash()
    tabela_itens = TabelaItens()
    carregar_receitas("craft.txt", tabela_receitas, tabela_itens)  #chama a função para carregar as receitas do arquivo na tabela
                
    #laço para que o usuário digite comandos repetidamente 
    while True:
        comando = input().strip()
        if comando == 'q':  #se o usuário digitar "q" para o programa
            break
        elif comando.startswith('r '):  #comando r = realiza busca pela receita
            nome_receita = comando[2:].strip()  #Remover 'r ' e espaços para ficar com o nome da receita apenas na busca
            ingredientes = tabela_receitas.buscar(nome_receita)  

            if ingredientes:
                print(f"{nome_receita}")
                for item in ingredientes:
                    print(f"{item}")
            else:
                print(f"{nome_receita}")
                print("Não encontrado")
        elif comando == "p r":  #comando p r = imprime a tabela hash com as árvores
            tabela_receitas.imprimir_receitas()
        elif comando == "p i":  #comando p i = imprime a tabela hash com os itens
            tabela_receitas.imprimir_itens(tabela_itens)
        elif comando.startswith('i '):  #comando i = busca item e mostra onde ele é usado
            nome_item = comando[2:].strip()
            receitas = tabela_itens.buscar(nome_item)
            print(f"{nome_item}")
            if receitas:
                for nome in receitas:
                    print(nome)
            else:
                print("Não encontrado")
        else:
            print("Não encontrado")

if __name__ == "__main__":
    main()

