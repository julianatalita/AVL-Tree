**Atividade realizada para a disciplina de Algoritmos e Estruturas de Dados no CIn (UFPE).**

***OBJETIVO***

**O objetivo era implementar uma Binary Search Tree com balanceamento do tipo AVL,
capaz de adicionar, remover e procurar o nível de um nó da árvore. Assim como imprimir
em ordem, pós-ordem e pré ordem.**

***REQUISITOS DA ATIVIDADE***

Seu trabalho é ajudar Robervalda, implementando uma AVL e disponibilizando funções para que Robervalda possa verificar se as árvores que ela está montando estão ficando corretas. Com isso, cabe a você implementar a seguinte funcionalidade:

- Adicionar um elemento à árvore;
- Remover um elemento da árvore;
- Procurar o nível de um elemento;
- Imprimir a árvore (em ordem, pós-ordem e pré-ordem)

Seu programa irá receber entradas do tipo FUNÇÃO ARGUMENTO, como pode ser visto na seguinte lista:

- ADICIONA X1
- REMOVE X2
- NIVEL X3
- PRINT PREORDEM
- PRINT EMORDEM
- PRINT POSORDEM
- FIM

*Observação:*

- Xi pertence aos números naturais
- O seu programa deverá executar as funcionalidades solicitadas por Robervalda e construir a árvore AVL de acordo com os valores adicionados e removidos.
- Seu programa apenas finalizará quando a entrada FIM for recebida.


Ao tentar remover ou buscar o nível de um nó cujo valor não exista na árvore o seu programa deverá imprimir:

Valor x inexistente

Onde:


x é o valor cuja função foi solicitada

Ao buscar o nível de um nó cujo valor exista na árvore seu programa deverá retornar:

Nivel de x: i

Onde:


x é o valor cujo a busca do nível foi solicitada.

i é o nível de x. Considere que a raiz tem nível 0, os filhos da raiz têm nível 1, e assim por diante.

Ao solicitar a impressão da árvore, deve ser impressa na ordem que foi informada após o comando no formato:

[X1,X2,X3,X4,X5,X6,...,XN]

Onde:


Xi representa os nós da árvore, na ordem especificada (em ordem, pré-ordem ou pós-ordem).

A saída deve começar com [ e finalizar com ].

Cada nó deve ser separado por uma vírgula.


Requisitos:

- Certifique-se de ter o Python instalado em sua máquina. Caso não tenha, você pode baixá-lo em python.org.
- Clone este repositório em sua máquina local usando o seguinte comando: git clone 
- Execute 
