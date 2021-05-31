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
board =[
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

# ===== ALGORITMOS PRINCIPAIS ===== #
# Avalia se o valor adicionado na tabela é válido
def avalia(board, i, j, val):
	for it in range(9):
		#	Linha
		if board[i][it]== val:
			return False
		#	Coluna
		if board[it][j]== val:
			return False

		#	Bloco
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3):
		for j in range (jt * 3, jt * 3 + 3):
			if board[i][j]== val:
				return False
	return True

#   Função principal
def resolveSudoku(board, i, j):
	
	while board[i][j]!= 0:
		if (i < 8):
			i += 1
		elif (i == 8 and j < 8):
			i = 0
			j += 1
		elif (i == 8 and j == 8):
			return True

	pygame.event.pump()	

	for it in range(1, 10):
		if avalia(board, i, j, it):
			
			#	Atribui um elemento (1 a 9) à variável. 
			board[i][j] = it

			global x, y
			x = i
			y = j
			# white color background\
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(0)

			#	Chamada que forma uma árvore de profundidade
			if resolveSudoku(board, i, j):
				return True
			
			#	Atribui 0 se a busca não atinge um resultado satisfatório (backtracking)
			board[i][j] = 0

			# white color background\
			screen.fill((255, 255, 255))
		
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(0)
				
	return False
	
run = True
flag1 = 0
flag2 = 0
error = 0

# Loop tela principal
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
		if not resolveSudoku(board, 0, 0):
			error = 1
		flag2 = 0	
	if val != 0:			
		draw_val(val)
		if avalia(board, int(x), int(y), val):
			board[int(x)][int(y)]= val
			flag1 = 0
		val = 0			
	draw()
	if flag1 == 1:
		draw_box()		

	# Atualiza a janela
	pygame.display.update()

# Fecha a janela	
pygame.quit()	
	
