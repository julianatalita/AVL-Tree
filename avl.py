def maior(valor1, valor2):
    if valor1 >= valor2:
        return valor1
    return valor2


class Arvore():
    def __init__(self):
        self.raiz = None
        self.qntd_nos = 0

    def nivel(self, no_buscado):
        no_atual = self.raiz
        nivel = 0
        while no_atual != None and no_atual.valor != no_buscado:
            nivel += 1
            if no_buscado > no_atual.valor:
                no_atual = no_atual.direita
            elif no_buscado < no_atual.valor:
                no_atual = no_atual.esquerda
            
        if no_atual == None:
            print('Valor {} inexistente'.format(no_buscado))
        else:
            print('Nivel de {}: {}'. format(no_buscado, nivel))
    

    def buscar(self, raiz, valor_buscado):
        if raiz == None or valor_buscado == raiz.valor:
            return raiz
        if valor_buscado < raiz.valor:
            return self.buscar(raiz.esquerda, valor_buscado)
        else:
            return self.buscar(raiz.direita, valor_buscado)


    def adicionar(self, valor_adicionar):
        raiz = self.raiz
        pai = None
        adicionado = No(valor_adicionar)
        continuar = True
        while raiz != None:
            pai = raiz
            
            if adicionado.valor < raiz.valor:
                raiz = raiz.esquerda
            elif adicionado.valor > raiz.valor:
                raiz = raiz.direita
            else:
                raiz = None
                continuar = False
        if continuar:
            adicionado.pai = pai
            if pai == None:
                self.raiz = adicionado
            elif adicionado.valor < pai.valor:
                pai.esquerda = adicionado
            else:
                pai.direita = adicionado

            self.balancear(adicionado)
        

    def atualiza_altura(self, no):
        if no != None:
                no.altura = maior(self.getAltura(no.direita), self.getAltura(no.esquerda)) + 1


    def balancear(self, no_movimentado):
        while no_movimentado != None:
            
            self.atualiza_altura(no_movimentado)
            
            balanceamento_no = self.fator_balanceamento(no_movimentado)
        
            if balanceamento_no > 1 and self.fator_balanceamento(no_movimentado.esquerda) >= 0:
                no_movimentado = self.rotacao_direita(no_movimentado)
            elif balanceamento_no < -1 and self.fator_balanceamento(no_movimentado.direita) <= 0:
                no_movimentado = self.rotacao_esquerda(no_movimentado)
            elif balanceamento_no > 1 and self.fator_balanceamento(no_movimentado.esquerda) < 0:
                no_movimentado.esquerda = self.rotacao_esquerda(no_movimentado.esquerda)
                no_movimentado = self.rotacao_direita(no_movimentado)
            elif balanceamento_no < -1 and self.fator_balanceamento(no_movimentado.direita) > 0:
                no_movimentado.direita = self.rotacao_direita(no_movimentado.direita)
                no_movimentado = self.rotacao_esquerda(no_movimentado)

            if no_movimentado == no_movimentado.pai:
                no_movimentado = None
            else:     
                no_movimentado = no_movimentado.pai


    def minimo(self, no):
        while no.esquerda != None:
            no = no.esquerda
        return no
        
    
    def maximo(self, no):
        while no.direita != None:
            no = no.direita
        return no


    def transplante(self, no_1, no_2):
        if no_1.pai == None:
            self.raiz = no_2
            
        elif no_1 == no_1.pai.esquerda:
            no_1.pai.esquerda = no_2
        else:
            no_1.pai.direita = no_2
        if no_2 != None:
            no_2.pai = no_1.pai


    def remover(self, valor):
        no_remover = self.buscar(self.raiz, valor)
        if no_remover == None:
            print('Valor {} inexistente'.format(valor))
        else:
            
            if no_remover.esquerda == None and no_remover.direita == None:    
                self.transplante(no_remover, no_remover.direita)
                balanceado = no_remover.pai
            elif no_remover.esquerda == None:    
                self.transplante(no_remover, no_remover.direita)
                balanceado = no_remover.direita

            elif no_remover.direita == None:    
                self.transplante(no_remover, no_remover.esquerda)
                balanceado = no_remover.esquerda

            else:
                no_movimentado = self.minimo(no_remover.direita)
                balanceado = no_movimentado.pai
                if balanceado == no_remover:
                    balanceado = no_movimentado

                if no_movimentado != no_remover.direita:
                    self.transplante(no_movimentado, no_movimentado.direita)
                    no_movimentado.direita = no_remover.direita
                    no_movimentado.direita.pai = no_movimentado
                    self.atualiza_altura(no_movimentado.direita)
                self.transplante(no_remover, no_movimentado)
                no_movimentado.esquerda = no_remover.esquerda
                no_movimentado.esquerda.pai = no_movimentado
                self.atualiza_altura(no_movimentado.esquerda)
                self.atualiza_altura(no_movimentado)
                
            self.balancear(balanceado)

    
    def rotacao_esquerda(self, no):

        filho = no.direita
        no.direita = filho.esquerda

        if filho.esquerda != None:
            filho.esquerda.pai = no

        filho.pai = no.pai

        if no.pai == None:
            self.raiz = filho
        elif no == no.pai.esquerda:
            no.pai.esquerda = filho
        else:
            no.pai.direita = filho
        
        filho.esquerda = no
        no.pai = filho
        
        self.atualiza_altura(no)
        self.atualiza_altura(filho)

        return filho


    def rotacao_direita(self, no):
        filho = no.esquerda
        no.esquerda = filho.direita

        if filho.direita != None:
            filho.direita.pai = no

        filho.pai = no.pai

        if no.pai == None:
            self.raiz = filho
        elif no == no.pai.esquerda:
            no.pai.esquerda = filho
        else:
            no.pai.direita = filho
        
        filho.direita = no
        no.pai = filho

        self.atualiza_altura(no)
        self.atualiza_altura(filho)

        return filho


    def getAltura(self, no):
        if not no:
            return 0
        return no.altura    
    

    def preordem(self, raiz, texto = None):
        if texto == None:
            texto = ''
            
        if raiz != None:

            texto = str(raiz.valor) + ','
            texto_esquerda = self.preordem(raiz.esquerda, texto)
            texto_direita = self.preordem(raiz.direita, texto)
            if texto == None:
                texto = ''
            if texto_esquerda ==  None:
                texto_esquerda = ''
            if texto_direita == None:
                texto_direita = ''
            texto = texto + texto_esquerda + texto_direita
            return texto
    

    def ordem(self, raiz, texto = None):
        if texto == None:
            texto = ''
            
        if raiz:
            
            texto_esquerda = self.ordem(raiz.esquerda, texto)
            texto = str(raiz.valor) + ','
            texto_direita = self.ordem(raiz.direita, texto)
            texto = texto_esquerda + texto_direita
        return texto 


    def posordem(self, raiz, texto=None):
        if texto == None:
            texto = ''
        if raiz:
        
            texto_esquerda = self.posordem(raiz.esquerda, texto)
            texto_direita = self.posordem(raiz.direita, texto)
            texto += texto_esquerda + texto_direita + str(raiz.valor) + ','

        return texto


    def fator_balanceamento(self, no):
        if no == None:
            return 0
        else:
            fb = self.getAltura(no.esquerda) - self.getAltura(no.direita)
            return fb


class No():
    def __init__(self, valor, pai = None, altura = 1, direita = None, esquerda = None):
        self.valor = valor
        self.pai = pai
        self.altura = altura
        self.direita = direita
        self.esquerda = esquerda

    def __str__(self):
        return str(self.valor)

def main():
    rodar = True
    arvore = Arvore()
    while rodar:
        entrada = input()
        comando = entrada.split()

        funcao = comando[0]
        texto = '['
        if funcao == 'ADICIONA':
            arvore.adicionar( int(comando[1]))
        elif funcao == 'REMOVE':
            arvore.remover( int(comando[1]))
        elif funcao == 'NIVEL':
            arvore.nivel(int(comando[1]))
        elif entrada == 'PRINT PREORDEM':    
            if arvore.raiz == None:
                print('[]')
            else:
                texto += (arvore.preordem(arvore.raiz))
                print(texto[:-1] + ']')
        elif entrada == 'PRINT EMORDEM':
            if arvore.raiz == None:
                print('[]')
            else:
                texto += (arvore.ordem(arvore.raiz))
                print(texto[:-1] + ']')
        elif entrada == 'PRINT POSORDEM':
            if arvore.raiz == None:
                print('[]')
            else:
                texto += (arvore.posordem(arvore.raiz))
                print(texto[:-1] + ']')
        else:
            rodar = False

if __name__ == '__main__':
    main()
