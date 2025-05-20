# INTEGRANTES 
# Marcela Torro RM557658
# Matheus V. RM555177 
# Matheus Queiroz RM558801
# Gustavo Attanazio RM559098
# Rodrigo Leme RM550266


class Cores:
    RESET = '\033[0m'
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    ROXO = '\033[95m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'

class Node:
    def __init__(self, palavra):
        self.palavra = palavra
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None
        self.contador_palavras = 0

    def inserir(self, palavra):
        if self.raiz is None:
            self.raiz = Node(palavra)
            self.contador_palavras += 1
        else:
            if self._inserir_iterativo(palavra):
                self.contador_palavras += 1

    def _inserir_iterativo(self, palavra):
        atual = self.raiz
        while True:
            if palavra < atual.palavra:
                if atual.esquerda is None:
                    atual.esquerda = Node(palavra)
                    return True
                atual = atual.esquerda
            elif palavra > atual.palavra:
                if atual.direita is None:
                    atual.direita = Node(palavra)
                    return True
                atual = atual.direita
            else:
                return False

    def autocomplete(self, prefixo):
        resultado = []
        self._autocomplete_recursivo(self.raiz, prefixo, resultado)
        return sorted(resultado)
    
    def _autocomplete_recursivo(self, node, prefixo, resultado):
        if node is None:
            return

        if node.palavra.startswith(prefixo):
            resultado.append(node.palavra)

        if node.palavra > prefixo:
            self._autocomplete_recursivo(node.esquerda, prefixo, resultado)
        
        if node.palavra < prefixo or node.palavra.startswith(prefixo):
            self._autocomplete_recursivo(node.direita, prefixo, resultado)


# ------- terminal <3 -------

def banner():
    print(f"{Cores.ROXO}="*50)
    print()  
    print(f"    BEM-VINDO(A) AO AUTOCOMPLETADOR DE PALAVRAS")
    print()  
    print("="*50)
    print()  
    print("Digite um prefixo para buscar sugestões de palavras.")
    print(f"Digite {Cores.VERMELHO}'sair' {Cores.ROXO}para encerrar o programa. {Cores.RESET}")
    print("="*50 + Cores.RESET)

def main():
    arvore = Arvore()
    
    banner()
    print(f"{Cores.AMARELO}⏳ Carregando dicionário, por favor aguarde...\n{Cores.RESET}")
    
    try:
        with open("dicionario_pt.txt", "r", encoding="utf-8") as arquivo:
            palavras = set(l.strip() for l in arquivo if l.strip())
        
        for palavra in palavras:
            arvore.inserir(palavra)
        
        print(f"{Cores.VERDE}✅ Dicionário carregado com sucesso!")
        print(f"📚 Total de palavras carregadas: {arvore.contador_palavras}{Cores.RESET}")
        
        while True:
            print("\n" + "-"*50)
            prefixo = input(
                f"{Cores.AZUL}🔍 Digite um prefixo para buscar (ou digite {Cores.VERMELHO}'sair'{Cores.AZUL} para encerrar): {Cores.RESET}"
            ).strip()

            if prefixo.lower() == 'sair':
                print(f"\n{Cores.ROXO}👋 Encerrando o programa... Até a próxima!{Cores.RESET}")
                break

            if not prefixo:
                print(f"{Cores.VERMELHO}⚠️  Você precisa digitar algo para buscar!{Cores.RESET}")
                continue
            
            sugestoes = arvore.autocomplete(prefixo)
            
            if sugestoes:
                print(f"\n{Cores.VERDE}✨ Sugestões para '{prefixo}' ({len(sugestoes)} encontradas):\n{Cores.RESET}")
                for i, palavra in enumerate(sugestoes[:20], 1):
                    print(f"{i:2}. {palavra}")
                if len(sugestoes) > 20:
                    print(f"... e mais {len(sugestoes) - 20} sugestões.")
            else:
                print(f"{Cores.VERMELHO}❌ Nenhuma sugestão encontrada.{Cores.RESET}")
    
    except FileNotFoundError:
        print(f"{Cores.VERMELHO}🚫 Erro: O arquivo 'dicionario_pt.txt' não foi encontrado.{Cores.RESET}")
    except Exception as e:
        print(f"{Cores.VERMELHO}⚠️  Erro ao processar o dicionário: {e}{Cores.RESET}")

if __name__ == "__main__":
    main()
