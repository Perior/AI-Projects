#   Programa que soluciona um sudoku como um problema de satisfação de restrições.
#                                           por: Pedro Rodrigues Bandeira da Rocha

#   Componentes do CSP:
#   Variaveis: Espaços vazios da tabela.
#   Dominio: Números possíveis que as variaveis podem assumir => {1,2,3,4,5,6,7,8,9}.
#   Restrições: Para o Sudoku => Colunas, Linhas e Blocos.
#   Heuristica: Variaveis com menor número de dominios possiveis irão ser atribuidas primeiro.

import pygame

# inicializa font do pygame
pygame.font.init()

# Tamanho da Janela
screen = pygame.display.set_mode((500, 500))

# Titulo
pygame.display.set_caption("SUDOKU SOLVER")

x = 0
y = 0
dif = 500 / 9
val = 0

# Tabela do Sudoku [Modificar aqui para testes]
board = [
        [0, 1, 0, 0, 6, 0, 0, 0, 0],
        [4, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 6, 7, 0, 0, 8, 0, 0],
        [0, 0, 7, 0, 0, 4, 2, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 4, 3],
        [0, 0, 0, 0, 0, 0, 0, 8, 4],
        [7, 0, 0, 0, 8, 0, 5, 0, 1],
        [0, 5, 0, 0, 0, 0, 7, 3, 0]
    ]

# ===== Funções auxiliares do Pygame ===== #
#   Fontes de teste
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (255, 0, 0), (y * dif-3, (x + i)*dif), (y * dif + dif + 3, (x + i)*dif), 7)
		pygame.draw.line(screen, (255, 0, 0), ( (y + i)* dif, x * dif ), ((y + i) * dif, x * dif + dif), 7)

#   Desenha o quadro do sudoku no display	
def draw():

	# Desenha as linhas
	for i in range (9):
		for j in range (9):
			if board[i][j]!= 0:

				# Pinta de azul variáveis já preenchidas
				pygame.draw.rect(screen, (0, 153, 153), (j * dif, i * dif, dif + 1, dif + 1))

				# Adiciona os valores default colocados em "board".
				text1 = font1.render(str(board[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (j * dif + 15, i * dif + 15))

	# Faz as linhas pretas	
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	

# Adiciona valor na variável em branco
def draw_val(val):
	text1 = font1.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (y * dif + 15, x * dif + 15))

# ===== FUNÇÕES PRINCIPAIS ===== #
#   DEFINE
possib = [1,2,3,4,5,6,7,8,9]

#   Restrições (Constraints):
def checaLinha(board, index):
    return [x for x in possib if x not in [board[index][i] for i in range(9)]]

def checaColuna(board, index):
    return [x for x in possib if x not in [board[i][index] for i in range(9)]]

def checaBloco(board, index):
    box_col = index[1] // 3
    box_lin = index[0] // 3

    return [x for x in possib if x not in [board[i][j] for i in range(box_lin*3, box_lin*3 + 3) for j in range(box_col * 3, box_col*3 + 3)]]

#   Função que calcula os domínios de cada variavel de acordo com as restrições do problema.
def evaluate(board, lista):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                lista.append(set(checaLinha(board, i)).intersection(checaColuna(board, j), checaBloco(board, (i,j))))
            elif board[i][j] >= 1:
                lista.append(set())
    
    #   Heuristica: Aqui ordeno a lista de dominios (com indices das variaveis),
    #   para sempre começar pela variavel com menos valores possíveis.
    dominios = [i for i in enumerate(lista)]
    dominios.sort(key=lambda x: len(x[1]))
    return dominios

#   Checa se todos os domínios são 0 (vazios).
def resultado(lista):
    it = iter(lista)
    if all(len(l) == 0 for l in it):
        return True
    
    return False

#   Função principal
def resolveSudoku(board):
    lista = []

    #   "dominios" recebe uma lista de duplas ordenadas com os
    #   índices e domínios possíveis de cada variavel.
    dominios = evaluate(board, lista)
    
    #   Lista com apenas os domínios das variaveis
    checkList = list(x[1] for x in dominios)
    
    pygame.event.pump()
    
    #   Finaliza a função quando todas as variaveis não possuem possibilidades do domínio.
    if(resultado(checkList)):
        return True

    #   A função irá se chamar recursivamente, recalculando os possíveis domínios a cada chamada.
    #   Atribuindo às variaveis um valor do domínio, se existir.
    for i in dominios:
        itemList = i[1]
        if(len(itemList) != 0):

            #   Tentar um loop com os elementos da lista para excluir o .pop()
            board[i[0]//9][i[0]%9] = itemList.pop()

            #   display do pygame
            global x, y
            x = i[0]//9
            y = i[0]%9
            screen.fill((255,255,255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(500)
            
            if(resolveSudoku(board)):
                return True

            board[i[0]//9][i[0]%9] = 0

            #pygame
            screen.fill((255,255,255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(500)
    
    return False


# ===== utilizada para primeiros testes ===== #
#   Organiza a saída do algoritmo
def print_board(board):
    print('\n SUDOKU NÃO-RESOLVIDO: \n')
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    
    #   Chama a função principal
    resolveSudoku(board)

    print('\n SUDOKU RESOLVIDO: \n')
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# MAIN
if __name__ == '__main__':
    
    run = True
    flag1 = 0
    flag2 = 0
    error = 0
    # The loop thats keep the window running
    while run:
        # White color background
        screen.fill((255, 255, 255))
        # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                run = False
            # Get the number to be inserted if key pressed	
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    flag2 = 1
        if flag2 == 1:
            if not resolveSudoku(board):
                error = 1
            flag2 = 0			
        draw()
        if flag1 == 1:
            draw_box()		

        # Atualiza a janela
        pygame.display.update()

        # Fecha a janela
    pygame.quit()