import pygame
import sys
import json
import os
import socket
import threading 
import queue
import itenschao

from time import sleep
import itenschao
import time as time_module

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('CinMón')
janela = pygame.display.set_mode((1024, 512))


import imagens
imagens.carregar()


import variaveis
import objetos
import funcoes_Classes
import cimons

# 1. Caminho para o SAVE (Pasta real onde o .exe ou .py está)
if getattr(sys, 'frozen', False):
    pasta_do_jogo = os.path.dirname(sys.executable)
else:
    pasta_do_jogo = os.path.dirname(os.path.abspath(__file__))

ARQUIVO_SAVE = os.path.join(pasta_do_jogo, "savegame.json")

player = funcoes_Classes.Player(variaveis.posx, variaveis.posy, 64, imagens.player, imagens.frente, objetos.player4)

estado = {
    'posicaox': 576,
    'posicaoy': 64,
    'posicao': (576, 64),
    'equipe': '',
    'mochila': '',
    'treinadores_derrotados': [],
    'posobj': variaveis.posobjatual,
    'escolhaioda': False,
    'gramas': 0,
    'gramasx': (),
    'gramasy': (),
    'gramas4': []
}

def salvarJogo(estado):
    #Transforma o dicionário em texto e salva em um arquivo.
    # O 'w' significa 'write' (escrever/sobrescrever)
    with open(ARQUIVO_SAVE, 'w') as arquivo:
        json.dump(estado, arquivo, indent=4) # indent=4 deixa o arquivo formatado e fácil de ler
    print("Jogo salvo com sucesso!")
    funcoes_Classes.limpar(janela, imagens.balaofala)
    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('jogo salvo com sucesso'), False, janela)
    sleep(1)

def menu_principal(janela, fundo_menu, imagem_botoes,som_clique):
    pygame.mixer.music.play(-1)
    x = (janela.get_width()  - imagem_botoes.get_width())  // 2
    y = (janela.get_height() - imagem_botoes.get_height()) // 2 + 80

    rect_carregar = pygame.Rect(x + 20, y,      imagem_botoes.get_width() - 40, 45)
    rect_novo     = pygame.Rect(x + 20, y + 45, imagem_botoes.get_width() - 40, 50)


    


    no_menu = True
    escolha = None

    while no_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(f"Clicou em: {mouse}")
                print(f"rect_carregar: {rect_carregar}")
                print(f"rect_novo: {rect_novo}")

                if rect_carregar.collidepoint(mouse):
                    print(f"Procurando save em: {ARQUIVO_SAVE}")
                    print(f"Existe: {os.path.exists(ARQUIVO_SAVE)}")
                    if os.path.exists(ARQUIVO_SAVE):
                        som_clique.play()
                        pygame.time.wait(250)
                        escolha = 'carregar'
                        no_menu = False
                    else:
                        print("Nenhum save encontrado!")

                elif rect_novo.collidepoint(mouse):
                    som_clique.play()
                    pygame.time.wait(250)
                    escolha = 'novo'
                    no_menu = False
        janela.blit(fundo_menu, (0, 0))
        janela.blit(imagem_botoes, (x, y))
        pygame.display.update()
    pygame.mixer.music.stop()
    return escolha




def carregar_jogo():

    if os.path.exists(ARQUIVO_SAVE):
        # O 'r' significa 'read' (ler)
        with open(ARQUIVO_SAVE, 'r') as arquivo:
            estado_recuperado = json.load(arquivo)
        print("Jogo carregado com sucesso!")
        return estado_recuperado
    else:
        print("Nenhum save encontrado. Iniciando um jogo novo.")
        return None 
    
def cenario(posobj):
    cenario1 = False
    cenario2 = False
    cenario3 = False
    cenario4 = False
    cenario5 = False
    cenario6 = False
    cenario9 = False
    centrocin = False
    loja = False
    if posobj == variaveis.posobj1:
        cenario1 = True
        variaveis.listatual = variaveis.lista1
        variaveis.listaobjatual = variaveis.listaobj1
    elif posobj == variaveis.posobj2:
        cenario2 = True
        variaveis.listatual = variaveis.lista2
        variaveis.listaobjatual = variaveis.listaobj2
    elif posobj == variaveis.posobj3:
        cenario3 = True
        variaveis.listatual = variaveis.lista3
        variaveis.listaobjatual = variaveis.listaobj3
    elif posobj == variaveis.posobj4 or posobj == ((448, 0), (576, 0), (715, 20), (843, 20)) or posobj == ((448, 0), (576, 0), (587, 20),(843, 20)) or posobj == ((448, 0), (576, 0), (587, 20),(715, 20)):
        cenario4 = True
        variaveis.listatual = variaveis.lista4
        variaveis.listaobjatual = variaveis.listaobj4
    elif posobj == variaveis.posobj5:
        cenario5 = True
        variaveis.listatual = variaveis.lista5
        variaveis.listaobjatual = variaveis.listaobj5
    elif posobj == variaveis.posobj6:
        cenario6 = True
        variaveis.listatual = variaveis.lista6
        variaveis.listaobjatual = variaveis.listaobj6
    elif posobj == variaveis.posobj7:
        centrocin = True
        variaveis.listatual = variaveis.lista7
        variaveis.listaobjatual = variaveis.listaobj7
    elif posobj == variaveis.posobj8:
        loja = True
        variaveis.listatual = variaveis.lista8
        variaveis.listaobjatual = variaveis.listaobj8
    elif posobj == variaveis.posobj9:
        cenario9 = True
        variaveis.listatual = variaveis.lista9
        variaveis.listaobjatual = variaveis.listaobj9
    return cenario1, cenario2, cenario3, cenario4, cenario5, cenario6, centrocin, loja, cenario9

def gerenciando_servidor(servidor):
    global fila_receber

    while True:
        try:
            dados = servidor.recv(2048).decode('utf-8')
            if not dados:
                print('SERVIDOR FECHOU')
                servidor.close()
                break
            pacote = json.loads(dados)
            fila_receber.put(pacote)

        except:
            print('ERRO NO SERVIDOR')
            servidor.close()
            break





def iniciar_servidor(HOST):
    print('CONECTANDO AO SERVIDOR...')
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.connect((HOST, 5555))
    except:
        print('ERRO AO CONECTAR NO SERVIDOR')
        return False
    
    thread = threading.Thread(target=(gerenciando_servidor), args=(servidor, ), daemon=True)
    thread.start()
    return servidor







treinador1 = funcoes_Classes.treinador('ewerton')
equipe1 = funcoes_Classes.equipe(2, 2, 0, [cimons.gengar.clonar(), cimons.lupi.clonar()])
for n in range(len(equipe1.lista)):
    equipe1.lista[n].xp += 25
    equipe1.lista[n].subir_nivel()
equipe1.curar()

treinador2 = funcoes_Classes.treinador('jl')
equipe2 = funcoes_Classes.equipe(1, 1, 0, [cimons.goku.clonar(), cimons.rath.clonar()])
for n in range(len(equipe2.lista)):
    equipe2.lista[n].xp += 45
    equipe2.lista[n].subir_nivel()
equipe2.curar()

treinador3 = funcoes_Classes.treinador('daniel')
equipe3 = funcoes_Classes.equipe(3, 3, 0, [cimons.lupi.clonar(), cimons.mclovin.clonar(), cimons.mewtwo.clonar()])
for n in range(len(equipe3.lista)):
    equipe3.lista[n].xp += 55
    if equipe3.lista[n].nome == 'lupi':
        equipe3.lista[n].xp += 80
    equipe3.lista[n].subir_nivel()
equipe3.curar()

treinador4 = funcoes_Classes.treinador('marcelo')
equipe4 = funcoes_Classes.equipe(1, 1, 0, [cimons.shiny_mega_rayquaza.clonar()])
for n in range(len(equipe4.lista)):
    equipe4.lista[n].xp += 100
    equipe4.lista[n].subir_nivel()
equipe4.curar()

treinador5 = funcoes_Classes.treinador('andre')
equipe5 = funcoes_Classes.equipe(1, 1, 0, [cimons.gengar.clonar(),cimons.mewtwo.clonar()])
for n in range(len(equipe5.lista)):
    equipe5.lista[n].xp += 80
    equipe5.lista[n].subir_nivel()
equipe5.curar()

treinador6 = funcoes_Classes.treinador('joloca')
equipe6 = funcoes_Classes.equipe(2, 2, 0, [cimons.gokussj.clonar(),cimons.narutobeast.clonar()])
for n in range(len(equipe6.lista)):
    equipe6.lista[n].xp += 75
    equipe6.lista[n].subir_nivel()
equipe6.curar()

treinador7 = funcoes_Classes.treinador('arthur duque')
equipe7 = funcoes_Classes.equipe(1, 1, 0, [cimons.homelander.clonar(), cimons.arceus.clonar()])
for n in range(len(equipe7.lista)):
    equipe7.lista[n].xp += 90
    if equipe7.lista[n].nome == 'arceus':
        equipe7.lista[n].xp += 140
    equipe7.lista[n].subir_nivel()
equipe7.curar()

#treinador = treinador2
#equipe_2 = equipe2
#treinador = treinador1
#equipe_2 = equipe1
listaT = [imagens.cenario5, imagens.cenario9]       #cenarios onde há treinadores
listaitems1 = [imagens.crachabola, imagens.potion]           #imagens que há na loja

rodando = True

itens_cenario = []
itens_gerados_para = None
itens_por_cenario = {}
batalha = False#
trainer = False#
ataques = False
fugir = False
verturno = True
selvagem = False#
aleatorio = False
aviso = False#
aviso2 = False
escolhendo = False
bolsa = False
morto = False

cenario1 = False
cenario2 = False
cenario3 = False
cenario4 = True#
cenario5 = False
cenario6 = False
cenario9 = False
centrocin = False
loja = False

musicaP = True
musicaB = False

carregar_save = True

equipe = ''
mochila = ''

menuloja = False
andada = 0

balao = False
marca = marca2 = False
mov1a = 1

di = False
es = False
ci = False
ba = False
tentou = False

time = False
balao = False
balao2 = False
escolhaioda = False#
falaioda = False#
falaioda_2 = False
aviso = False

'''
equipe = funcoes_Classes.equipe(1, 1, 0, [cimons.naruto.clonar()])
mochila = funcoes_Classes.mochila([imagens.crachabola], [0], 0)
equipe.lista[0].xp = 209
bla, bla2, equipe.lista[0] =equipe.lista[0].subir_nivel()
'''

escolha_menu = menu_principal(janela, imagens.fundo_menu, imagens.botoes_menu,imagens.som_clique)

if escolha_menu == 'novo':
    carregar_save = False
elif escolha_menu == 'carregar':
    carregar_save = True


server = False
server_ativo = False




while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                salvarJogo(estado)
            if evento.key == pygame.K_v:
                player.alternar_montaria()
            
    if carregar_save:
        carregar_save = False
        try:
            save = estado
            estado = carregar_jogo()
            if estado == None:
                estado = save
            
            estado['equipe'] = tuple(estado['equipe'])
            for n in estado['equipe']:
                n = tuple(n)
            if len(estado['equipe']) > 0:
                equipe = funcoes_Classes.equipe(0, 0, 0, [])
                for n in range(len(estado['equipe'])):
                    for k in cimons.cimons:
                        if estado['equipe'][n][0] == k.nome:
                            equipe.adicionar(k)
                            equipe.lista[n].xp = estado['equipe'][n][1]
                            equipe.lista[n].subir_nivel()
                            equipe.lista[n].hp = estado['equipe'][n][2]
                            if equipe.lista[n].hp <= 0:
                                equipe.derrotados += 1

            if estado['mochila'] != '':
                mochila = funcoes_Classes.mochila([imagens.crachabola, imagens.potion], [0, 0], 0)
                mochila.dinheiro = estado['mochila'][-1]
                for n in range(int(len(estado['mochila']) - 1)):
                    mochila.listaDeQtd[n] = estado['mochila'][n][1]
                
            escolhaioda = estado['escolhaioda']
            for n in range(len(estado['posobj'])):
                estado['posobj'][n] = tuple(estado['posobj'][n])
            
            variaveis.gramasatual = tuple(imagens.grama for _ in range(estado['gramas']))
            variaveis.gramasxatual = tuple(estado['gramasx'])
            variaveis.gramasyatual = tuple(estado['gramasy'])
            variaveis.gramas4_atual = []
            for n in range(len(variaveis.gramasxatual)):
                variaveis.gramas4_atual.append(variaveis.gramasatual[n].get_rect())
                variaveis.gramas4_atual[n].x = variaveis.gramasxatual[n]
                variaveis.gramas4_atual[n].y = variaveis.gramasyatual[n]

            variaveis.posobjatual = tuple(estado['posobj'])
            variaveis.posx = estado['posicaox']
            variaveis.posy = estado['posicaoy']
            player.rect.x = estado['posicaox']
            player.rect.y = estado['posicaoy']
            player.rect.x = estado['posicaox']
            player.rect.y = estado['posicaoy']

            equipe1.curar()
            equipe2.curar()
            equipe3.curar()
            equipe4.curar()
            
            cenario1, cenario2, cenario3, cenario4, cenario5, cenario6, centrocin, loja, cenario9 = cenario(variaveis.posobjatual)
        except:
            print('ERRO ERRO')

        
    tecla = pygame.key.get_pressed()

    if musicaP:
        funcoes_Classes.musicaPrincipal()
        musicaP = False

    if musicaB:
        funcoes_Classes.musicaBatalha()
        musicaB = False

    if (not batalha) and (not server) and (not server_ativo):
        if cenario1:
            fundo = imagens.cenario1
        elif cenario2:
            fundo = imagens.cenario2
        elif cenario3:
            fundo = imagens.cenario3
        elif cenario4:
            fundo = imagens.cenario4
        elif cenario5:
            fundo = imagens.cenario5
        elif cenario6:
            fundo = imagens.cenario6
        elif cenario9:
            fundo = imagens.cenario9
        elif centrocin or loja:
            fundo = imagens.centrocin

        if (not balao) and (not balao2):
            if tecla[pygame.K_RIGHT]:
                marca = True
                di = True
                es = False
                ci = False
                ba = False
            elif tecla[pygame.K_LEFT]:
                marca = True
                di = False
                es = True
                ci = False
                ba = False
            elif tecla[pygame.K_UP]:
                marca = True
                di = False
                es = False
                ci = True
                ba = False
            elif tecla[pygame.K_DOWN]:
                marca = True
                di = False
                es = False
                ci = False
                ba = True
            elif tecla[pygame.K_RETURN] and escolhaioda:
                server = True

            if di:
                if andada == 0:
                    andada += 1 
                else: 
                    andada = 0
                variaveis.posx, tentou = player.direita(variaveis.posx, variaveis.posy, janela, fundo, andada)
                if (not tentou):
                    di = False
                #sleep(0.1)
            elif es:
                if andada == 0:
                    andada += 1 
                else: 
                    andada = 0
                variaveis.posx, tentou = player.esquerda(variaveis.posx, variaveis.posy, janela, fundo, andada)
                if (not tentou):
                    es = False
                #sleep(0.1)
            elif ci:
                if andada == 0:
                    andada += 1 
                else: 
                    andada = 0
                variaveis.posy, tentou = player.cima(variaveis.posx, variaveis.posy, janela, fundo, andada)
                if (not tentou):
                    ci = False
                #sleep(0.1)
            elif ba:
                if andada == 0:
                    andada += 1 
                else: 
                    andada = 0
                variaveis.posy, tentou = player.baixo(variaveis.posx, variaveis.posy, janela, fundo, andada)
                if (not tentou):
                    ba = False
                #sleep(0.1)

        if tentou:
            if cenario4:
                if escolhaioda:
                    mudar = funcoes_Classes.verificar4_3(variaveis.posx, variaveis.posy, ba)
                    if mudar:
                        variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario3(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj3, variaveis.listatual, variaveis.lista3, variaveis.listaobjatual, variaveis.listaobj3, fundo)
                        cenario4 = False
                        cenario3 = True

                elif variaveis.posx == 704 and variaveis.posy == 448:
                    funcoes_Classes.limpar(janela, imagens.balaofala)
                    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('ainda nao'), batalha, janela)
                    sleep(1)
                ba = False
                tentou = False
            
            elif cenario3:
                mudar = funcoes_Classes.verificar3_4(player, objetos.porta2_4, variaveis.posx, variaveis.posy, ci)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario4(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj4, variaveis.listatual, variaveis.lista4, variaveis.listaobjatual, variaveis.listaobj4, fundo)
                    cenario3 = False
                    cenario4 = True
                    ci = False
                    tentou = False

                mudar = funcoes_Classes.verificar3_1(variaveis.posx, variaveis.posy, es)
                if mudar:
                    fundo, variaveis.posobjatual, variaveis.listatual, variaveis.gramasatual, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.gramas4_atual, variaveis.listaobjatual, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario1(player, variaveis.posobj1, variaveis.posobjatual, fundo, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.gramas4_atual, variaveis.gramas1, variaveis.gramasx1, variaveis.gramasy1, variaveis.posy, variaveis.listatual, variaveis.listaobjatual, variaveis.lista1, variaveis.listaobj1, variaveis.gramasatual, cenario2, cenario3)
                    cenario3 = False
                    cenario1 = True
                    es = False
                    tentou = False

                mudar = funcoes_Classes.verificar3_5(variaveis.posx, variaveis.posy, ci)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario5(player, variaveis.posobj5, variaveis.posobjatual, fundo, variaveis.posy, variaveis.listatual, variaveis.listaobjatual, variaveis.lista5, variaveis.listaobj5, cenario3, cenario6)
                    cenario3 = False
                    cenario5 = True
                    ci = False
                    tentou = False


            elif cenario1:
                mudar = funcoes_Classes.verificar1_3(variaveis.posx, variaveis.posy, di)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario3(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj3, variaveis.listatual, variaveis.lista3, variaveis.listaobjatual, variaveis.listaobj3, fundo)
                    cenario1 = False
                    cenario3 = True
                    di = False
                    tentou = False

                mudar = funcoes_Classes.verificar1_2(player, objetos.porta4)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario2(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj2, variaveis.listatual, variaveis.lista2, variaveis.listaobjatual, variaveis.listaobj2, fundo)
                    cenario1 = False
                    cenario2 = True
                    ci = False
                    tentou = False


            elif cenario2:
                mudar = funcoes_Classes.verificar2_1(variaveis.posx, variaveis.posy, ba)
                if mudar:
                    fundo, variaveis.posobjatual, variaveis.listatual, variaveis.gramasatual, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.gramas4_atual, variaveis.listaobjatual, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario1(player, variaveis.posobj1, variaveis.posobjatual, fundo, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.gramas4_atual, variaveis.gramas1, variaveis.gramasx1, variaveis.gramasy1, variaveis.posy, variaveis.listatual, variaveis.listaobjatual, variaveis.lista1, variaveis.listaobj1, variaveis.gramasatual, cenario2, cenario3)
                    cenario2 = False
                    cenario1 = True
                    ba = False
                    tentou = False

            
            elif cenario5:
                mudar = funcoes_Classes.verificar5_3(variaveis.posx, variaveis.posy, ba)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario3(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj3, variaveis.listatual, variaveis.lista3, variaveis.listaobjatual, variaveis.listaobj3, fundo)
                    cenario5 = False
                    cenario3 = True
                    ba = False
                    tentou = False

                mudar = funcoes_Classes.verificar5_6(variaveis.posx, variaveis.posy, di)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario6(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj6, variaveis.listatual, variaveis.lista6, variaveis.listaobjatual, variaveis.listaobj6, fundo, cenario5, centrocin, loja)
                    cenario5 = False
                    cenario6 = True
                    di = False
                    tentou = False

            
            elif cenario6:
                mudar = funcoes_Classes.verificar6_5(variaveis.posx, variaveis.posy, es)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario5(player, variaveis.posobj5, variaveis.posobjatual, fundo, variaveis.posy, variaveis.listatual, variaveis.listaobjatual, variaveis.lista5, variaveis.listaobj5, cenario3, cenario6)
                    cenario6 = False
                    cenario5 = True
                    es = False
                    tentou = False

                else:
                    mudar = funcoes_Classes.verificar6_centrocin(player, objetos.porta3_4, variaveis.posx, variaveis.posy, ci)
                    if mudar:
                        variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircentrocin(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj7, variaveis.listatual, variaveis.lista7, variaveis.listaobjatual, variaveis.listaobj7, fundo)
                        cenario6 = False
                        centrocin = True
                        ci = False
                        tentou = False

                    else:
                        mudar = funcoes_Classes.verificar6_loja(player, objetos.porta4_4, variaveis.posx, variaveis.posy, ci)
                        if mudar:
                            variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.irloja(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj8, variaveis.listatual, variaveis.lista8, variaveis.listaobjatual, variaveis.listaobj8, fundo)
                            cenario6 = False
                            loja = True
                            ci = False
                            tentou = False


                        else:
                            mudar = funcoes_Classes.verificar6_9(variaveis.posx, variaveis.posy, ci)
                            if mudar:
                                variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario9(player, variaveis.posobj9, variaveis.posobjatual, fundo, variaveis.posy, variaveis.listatual, variaveis.listaobjatual, variaveis.lista9, variaveis.listaobj9)
                                cenario6 = False
                                cenario9 = True
                                ci = False
                                tentou = False


            elif cenario9:
                mudar = funcoes_Classes.verificar9_6(variaveis.posx, variaveis.posy, ba)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario6(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj6, variaveis.listatual, variaveis.lista6, variaveis.listaobjatual, variaveis.listaobj6, fundo, cenario5, centrocin, loja)
                    cenario9 = False
                    cenario6 = True
                    ba = False
                    tentou = False


            
            elif centrocin:
                mudar = funcoes_Classes.verificarcentrocin_6(variaveis.posx, variaveis.posy, ba)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario6(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj6, variaveis.listatual, variaveis.lista6, variaveis.listaobjatual, variaveis.listaobj6, fundo, cenario5, centrocin, loja)
                    centrocin = False
                    cenario6 = True
                    ba = False
                    tentou = False

                
            elif loja:
                mudar = funcoes_Classes.verificarcentrocin_6(variaveis.posx, variaveis.posy, ba)
                if mudar:
                    variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posx, variaveis.posy = funcoes_Classes.ircenario6(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj6, variaveis.listatual, variaveis.lista6, variaveis.listaobjatual, variaveis.listaobj6, fundo, cenario5, centrocin, loja)
                    loja = False
                    cenario6 = True
                    ba = False
                    tentou = False

            estado['posobj'] = variaveis.posobjatual
            estado['gramas'] = len(variaveis.gramasatual)
            estado['gramasx'] = variaveis.gramasxatual          
            estado['gramasy'] = variaveis.gramasyatual
            estado['gramas4'] = len(variaveis.gramas4_atual)
                
#menu
        if escolhaioda:
            if tecla[pygame.K_m] or balao2:
                time = False
                balao2, mov1a, time = funcoes_Classes.menu(janela, equipe, balao2, mov1a, escolhendo, bolsa, tecla, marca2)
            elif time:
                rodando, time = funcoes_Classes.menu_time(janela, equipe, mov1a, 1, True, bolsa, balao2)


        if tecla[pygame.K_SPACE] or balao:
#inicio
            if cenario4 and (tecla[pygame.K_SPACE] or balao) and (not escolhaioda) and player.visual == imagens.atras:
                escolhaioda, escolha, balao, mov1a, rodando, aviso = funcoes_Classes.inicio(mov1a, ataques, escolhendo, bolsa, balao, janela, aviso, player, imagens.player, batalha, cenario1, marca2, tecla, escolhaioda)
                if escolhaioda:
                    equipe = funcoes_Classes.equipe(1, 1, 0, [escolha.clonar()])
                    estado['equipe'] = [(equipe.lista[0].nome, (equipe.lista[0].nivel - 1) * 10 + equipe.lista[0].xp, equipe.lista[0].hp)]
                    mochila = funcoes_Classes.mochila([imagens.crachabola, imagens.potion], [2,3], 0)
                    estado['mochila'] = [['crachabola', 2], ['potion', 3], 0]
                    estado['escolhaioda'] = True
                    estado['posobj'] = variaveis.posobj4


#centrocin
            elif centrocin and variaveis.posx == 448 and variaveis.posy == 192 and (tecla[pygame.K_SPACE]) and player.visual == imagens.atras:
                funcoes_Classes.curarfala(janela, player, batalha, variaveis.posx, variaveis.posy)
                equipe.curar()
                estado['equipe'] = [(equipe.lista[n].nome, sum(k  * 10 for k in range(1, equipe.lista[n].nivel)) + equipe.lista[n].xp, equipe.lista[n].hp) for n in range(len(equipe.lista))]



    #loja
            elif (loja and variaveis.posx == 448 and variaveis.posy == 192 and (tecla[pygame.K_SPACE]) and player.visual == imagens.atras) or balao:
                if (not balao):
                    voltesempre = True
                    funcoes_Classes.lojafala(janela, batalha)
                balao, menuloja, mov1a = funcoes_Classes.sounloja(janela, balao, tecla, marca2, mov1a) 

                if menuloja:
                    rodando, menuloja = funcoes_Classes.menuloja(janela, 1, menuloja, listaitems1, mochila)
                    qtd_cracha = mochila.listaDeQtd[mochila.listaDeles.index(imagens.crachabola)]
                    qtd_potion = mochila.listaDeQtd[mochila.listaDeles.index(imagens.potion)]
                    estado['mochila'] = [['crachabola', qtd_cracha], ['potion', qtd_potion], mochila.dinheiro]




#treinadores
        treinador, trainer = funcoes_Classes.encontrar_treinador(variaveis.posx, variaveis.posy, listaT, fundo)

        if trainer:
            if treinador == 'treinador1':
                indice = 'treinador1'
                treinador = treinador1
                equipe_2 = equipe1
            elif treinador == 'treinador2':
                indice = 'treinador2'
                treinador = treinador2
                equipe_2 = equipe2
            elif treinador == 'treinador3':
                indice = 'treinador3'
                treinador = treinador3
                equipe_2 = equipe3
            elif treinador == 'treinador4':
                indice = 'treinador4'
                treinador = treinador4
                equipe_2 = equipe4
            elif treinador == 'treinador5':
                indice = 'treinador5'
                treinador = treinador5
                equipe_2 = equipe5
            elif treinador == 'treinador6':
                indice = 'treinador6'
                treinador = treinador6
                equipe_2 = equipe6
            if equipe_2.timevivo() and indice not in estado['treinadores_derrotados']:
                batalha = True
                musicaB = True
                musicaP = False
                aviso = False
                funcoes_Classes.avisoCombate(janela, treinador)
            else:
                trainer = False


###
        nome_cenario_atual = None
        if cenario1: nome_cenario_atual = 'cenario1'
        elif cenario2: nome_cenario_atual = 'cenario2'
        elif cenario3: nome_cenario_atual = 'cenario3'
        elif cenario5: nome_cenario_atual = 'cenario5'
        elif cenario6: nome_cenario_atual = 'cenario6'
        elif cenario9: nome_cenario_atual = 'cenario9'
        elif centrocin: nome_cenario_atual = 'centrocin'
        elif loja: nome_cenario_atual = 'loja'


        itenschao.mochila_global = mochila
        itenschao.escolhaioda_global = escolhaioda
        itenschao.palavra_func = funcoes_Classes.palavra

        if itens_gerados_para != nome_cenario_atual:
            itens_gerados_para = nome_cenario_atual
            if nome_cenario_atual in ('centrocin', 'loja', None):
                itens_cenario = []
                itenschao.itens_cenario_global = []
            elif escolhaioda and mochila != '':
                if nome_cenario_atual not in itens_por_cenario or itenschao.verificar_respawn(nome_cenario_atual):
                    itens_por_cenario[nome_cenario_atual] = itenschao.gerar_itens(nome_cenario_atual, quantidade=2)
                    itenschao.tempo_por_cenario[nome_cenario_atual] = time_module.time()
                itens_cenario = itens_por_cenario[nome_cenario_atual]
                itenschao.itens_cenario_global = itens_cenario

       
        if nome_cenario_atual and nome_cenario_atual not in ('centrocin', 'loja'):
            if nome_cenario_atual in itens_por_cenario and len(itens_por_cenario[nome_cenario_atual]) == 0:
                if nome_cenario_atual not in itenschao.tempo_por_cenario:
                    itenschao.tempo_por_cenario[nome_cenario_atual] = time_module.time()

        if (not balao) and (not balao2):
            player.rect.x = variaveis.posx
            player.rect.y = variaveis.posy
            estado['posicaox'] = variaveis.posx
            estado['posicaoy'] = variaveis.posy
            estado['posicao'] = (variaveis.posx, variaveis.posy)
            estado['escolhaioda'] = escolhaioda

            janela.blit(fundo, (0, 0))
            for n in range(len(variaveis.posobjatual)):
                janela.blit(variaveis.listatual[n], (variaveis.posobjatual[n][0], variaveis.posobjatual[n][1]))

            janela.blit(player.visual, (variaveis.posx, variaveis.posy))

            if cenario1 or cenario5 or cenario9:
                for n in range(len(variaveis.gramasatual)):
                    janela.blit(variaveis.gramasatual[n], (variaveis.gramasxatual[n], variaveis.gramasyatual[n]))
                if player.colisaog(variaveis.gramas4_atual) and marca:
                    batalha, selvagem = funcoes_Classes.encontrarcin()
                    marca = False
                    if batalha:
                        musicaB = True
                        musicaP = False

            
            if mochila != '' and escolhaioda and nome_cenario_atual is not None:
                player_rect_atual = pygame.Rect(variaveis.posx, variaveis.posy, 64, 64)
                for item in itens_cenario:
                    item.desenhar(janela)
                itenschao.atualizar_itens(itens_cenario, player_rect_atual, mochila, imagens)

        
        if mochila != '' and escolhaioda:

            def blit_mini_texto(texto, x, y, escala=0.55):
                aux = 0
                for letra in funcoes_Classes.palavra(str(texto)):
                    if letra != ' ':
                        l = pygame.transform.scale(letra, (int(imagens.largural * escala), int(imagens.altural * escala)))
                        l_branco = l.copy()
                        l_branco.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MAX)
                        janela.blit(l_branco, (x + aux, y))
                        aux += int(imagens.largural * escala) + 2
                    else:
                        aux += int(imagens.largural * escala) + 4

            hud_w, hud_h = 130, 125
            hud_surf = pygame.Surface((hud_w, hud_h), pygame.SRCALPHA)
            pygame.draw.rect(hud_surf, (30, 30, 30, 220), (0, 0, hud_w, hud_h), border_radius=8)
            pygame.draw.rect(hud_surf, (200, 200, 200, 180), (0, 0, hud_w, hud_h), width=2, border_radius=8)
            janela.blit(hud_surf, (4, 4))

            linha_h = 36
            icon_size = 26
            texto_x = 44
            icon_x = 10

            y = 10
            crachabola_img = pygame.transform.scale(imagens.crachabola, (icon_size, icon_size))
            janela.blit(crachabola_img, (icon_x, y))
            qtd_cracha = mochila.listaDeQtd[mochila.listaDeles.index(imagens.crachabola)]
            blit_mini_texto(str(qtd_cracha), texto_x, y + 6)
            pygame.draw.line(janela, (150, 150, 150), (10, y + linha_h), (hud_w - 6, y + linha_h), 1)

            y = 10 + linha_h + 4
            potion_img = pygame.transform.scale(imagens.potion, (icon_size, icon_size))
            janela.blit(potion_img, (icon_x, y))
            qtd_potion = mochila.listaDeQtd[mochila.listaDeles.index(imagens.potion)]
            blit_mini_texto(str(qtd_potion), texto_x, y + 6)
            pygame.draw.line(janela, (150, 150, 150), (10, y + linha_h), (hud_w - 6, y + linha_h), 1)

            y = 10 + (linha_h + 4) * 2
            moeda_hud = pygame.transform.scale(imagens.moeda, (icon_size, icon_size))
            janela.blit(moeda_hud, (icon_x, y))
            blit_mini_texto(str(mochila.dinheiro), texto_x, y + 6)

        pygame.display.update()

          



    elif batalha:
        saveCenario = fundo
        fundo = imagens.fundo
        if selvagem:
            batalha, selvagem, aleatorio, aviso, rodando = funcoes_Classes.batalha_selvagem(mochila, player, fundo, janela, equipe, selvagem, batalha, tecla, trainer, aleatorio, balao, saveCenario)
        elif trainer:
            batalha, trainer, aviso, rodando = funcoes_Classes.batalha_treinador(player, mochila, treinador, fundo, janela, equipe, equipe_2, selvagem, batalha, tecla, trainer, balao)
        if equipe.verificar():
            cenario1 = False
            cenario2 = False
            cenario3 = False
            cenario4 = False
            cenario5 = False
            cenario6 = False
            cenario9 = False
            loja = False
            centrocin = True
            variaveis.posobjatual, variaveis.listatual, variaveis.listaobjatual, fundo, variaveis.posy, variaveis.posx = funcoes_Classes.ircentrocin(player, variaveis.posx, variaveis.posy, variaveis.posobjatual, variaveis.posobj7, variaveis.listatual, variaveis.lista7, variaveis.listaobjatual, variaveis.listaobj7, fundo)
            variaveis.posx = 448
            variaveis.posy = 192
            janela.blit(fundo, (0, 0))
            for n in range(len(variaveis.listatual)):
                if variaveis.listatual[n] == imagens.player:
                    janela.blit(player.visual, (variaveis.posx, variaveis.posy))
                else:
                    janela.blit(variaveis.listatual[n], (variaveis.posobjatual[n][0], variaveis.posobjatual[n][1]))
            funcoes_Classes.curarfala(janela, player, batalha, variaveis.posx, variaveis.posy)
            equipe.curar()
            estado['posobj'] = variaveis.posobjatual
        if (not batalha):
            musicaP = True
            musicaB = False
            contador_xp = 0
            estado['equipe'] = [(equipe.lista[n].nome, sum(k  * 10 for k in range(1, equipe.lista[n].nivel)) + equipe.lista[n].xp, equipe.lista[n].hp) for n in range(len(equipe.lista))]
            qtd_bola = mochila.listaDeQtd[mochila.listaDeles.index(imagens.crachabola)]
            qtd_potion = mochila.listaDeQtd[mochila.listaDeles.index(imagens.potion)]
            estado['mochila'] = [['crachabola', qtd_bola],['potion',qtd_potion], mochila.dinheiro]
            for n in ([equipe1, equipe2, equipe3, equipe4]):
                if (not n.timevivo()) and treinador not in estado['treinadores_derrotados']:
                    estado['treinadores_derrotados'].append(indice)
    elif server or server_ativo:
        if server:
            rodar = True
            server = False
            server_ativo = True
        funcoes_Classes.limpar(janela, imagens.balaofala)
        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('Aguarde'), False, janela)
        sleep(0.5)
        lista = []
        while rodar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodar = False
                    rodando = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        rodar = False
                    elif event.key == pygame.K_BACKSPACE and len(lista) > 0:
                        lista.pop()
                    else:
                        letra = event.unicode
                        if letra.isprintable():
                            letra = event.unicode
                            lista.append(letra)

            
            janela.blit(imagens.balaofala, (64, 384))
            frase = funcoes_Classes.palavra(f'HOST {"".join(lista)}')
            HOST = ''.join(lista)
            aux = 8
            for letra in frase:
                if letra != ' ':
                    janela.blit(letra, (64 + aux, 400))
                    aux += imagens.largural + 8
                else:
                    aux += imagens.largural + 16
            pygame.display.update()
        funcoes_Classes.limpar(janela, imagens.balaofala)
        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('conectando ao servidor'), False, janela)
        sleep(1)
        try:
            servidor = iniciar_servidor(HOST)
            if servidor != False:
                funcoes_Classes.limpar(janela, imagens.balaofala)
                funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('conectado'), False, janela)
                sleep(1)
                funcoes_Classes.limpar(janela, imagens.balaofala)
                funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('procurando adversario'), False, janela)

                aguardando = True
                cin = equipe.lancar()
                equipe.curar()
                meu_pacote = {'evento': 'COMECO', 'qtd': len(equipe.lista), 'nome': cin.nome, 'nivel': cin.nivel, 'hp': cin.hp}
                fila_receber = queue.Queue()
        except:
            print('erro')

        try:
            servidor.sendall(json.dumps(meu_pacote).encode('utf-8'))
            while fila_receber.empty():
                if aguardando:
                    sleep(0.5)
                    aguardando = False
            pacote = fila_receber.get()
            for cimon in cimons.cimons:
                if cimon.nome == pacote['nome']:
                    cin2 = cimon.clonar()
                    cin2.xp = sum(n * 10 for n in range(1, pacote['nivel']))
                    cin2.subir_nivel()
                    cin2.hp = pacote['hp']
                    online = True
                    funcoes_Classes.limpar(janela, imagens.balaofala)
                    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('adversario encontrado'), False, janela)

        except:
            print('ERRO AO ENVIAR DADOS AO SERVIDOR')
            online = False
            server = False
            server_ativo = False
            funcoes_Classes.limpar(janela, imagens.balaofala)
            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('nao foi possivel se conectar'), False, janela)

        aviso = False
        aviso2 = False
        trocado = False
        minha_vez = False
        ataques = False
        aviso_troca = False
        mov1 = 1
        mov2 = 1
        fundo = imagens.fundo
        funcoes_Classes.musicaBatalha()
        pacote = {'evento': 'MENU_BATALHA'}
        while online:
            rodando = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    online = False
                    rodando = False
            tecla = pygame.key.get_pressed()
            if (not aviso) or aviso2:
                escolhendo = False
                bolsa = False
                capturado = False
                morto = False
                segundo = ''
                auxhpc = 0
                auxc = 0
                if (not aviso2):
                    escolhido = equipe.lancar()
                escolhido2 = cin2
                sel = ''
                aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                if(not aviso_troca):
                    aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
                    auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                aviso_troca = False
                aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
                auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
                janela.blit(fundo, (0, 0))
                janela.blit(imagens.molde3, (0, 384))
                if (not aviso):
                    frase = f'um adversario esta te desafiando'
                    frase = funcoes_Classes.palavra(frase)
                    funcoes_Classes.rodarpalavra(frase, batalha, janela)
                sleep(1)
                funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'seu adversario escolheu {escolhido2.nome}'), True, janela)
                sleep(1)
                funcoes_Classes.comeco1(janela, fundo, False, variaveis.posx2, variaveis.posy2, escolhido2, aviso, aviso2, True, escolhido, escolhido2, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1)
                sleep(0.5)
                if (not aviso):
                    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'Va {escolhido.nome}'), True, janela)
                sleep(0.5)
                aviso = True
                if (not aviso2):
                    funcoes_Classes.comeco2(janela, fundo, False, True, variaveis.posx1, variaveis.posy1, variaveis.posx2, variaveis.posy2, sel, escolhendo, escolhido, escolhido2, segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto)
                sleep(0.5)
                aviso2 = False
            if (not escolhendo) and (not bolsa):
                temporizador = 0
                if escolhido.hp > 0 and pacote['evento'] != "TROCA" and pacote['evento'] != 'TROCA_DUPLA':
                    if tecla[pygame.K_SPACE] or minha_vez:# or auu == 'a':
                        sleep(0.2)
                        if (not ataques) and mov1 == 1 and mov2 == 1:
                            ataques = True
                        elif (not ataques) and mov1 == 2 and mov2 == 2:
                            funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('Voce nao pode fugir'), True, janela)
                            sleep(1)
                        elif (not ataques) and mov1 == 1 and mov2 == 2:
                            escolhendo = True
                            mov1 = mov2 = 1
                        elif (not ataques) and mov1 == 2 and mov2 == 1:
                            funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('Voce nao pode abrir a bolsa'), True, janela)
                            sleep(1)
                        else:
                            if mov1 == 1 and mov2 == 1:
                                atk = escolhido.ataques['ataque1']
                                des = 1
                            elif mov1 == 2 and mov2 == 1:
                                atk = escolhido.ataques['ataque2']
                                des = 2
                            elif mov1 == 1 and mov2 == 2 and len(escolhido.ataques) >= 3:
                                atk = escolhido.ataques['ataque3']
                                des = 3
                            elif mov1 == 2 and mov2 == 2 and len(escolhido.ataques) == 4:
                                atk = escolhido.ataques['ataque4']
                                des = 4
                            if (escolhido.ataques[f'ataque{des}'].pp > 0 or minha_vez) and pacote['evento'] != 'TROCA' and pacote['evento'] != 'TROCA_DUPLA':
                                meu_pacote = {'evento': 'ESCOLHA_GOLPE', 'golpe': atk.nome}
                                if (not minha_vez):
                                    servidor.sendall(json.dumps(meu_pacote).encode('utf-8'))
                                    funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('aguardando adversario'), True, janela)
                                    while fila_receber.empty():
                                        print('aguardando oponente...')
                                        sleep(0.5)
                                    pacote = fila_receber.get()
                                if (pacote['ID'] == 1 or minha_vez) and pacote['evento'] != 'TROCA':
                                    escolhido.ataques[f'ataque{des}'].pp -= 1
                                    funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'{escolhido.nome} usou {atk.nome}'), True, janela)
                                    sleep(0.2)
                                    if atk.efeito == 'dano':
                                        escolhido2.hp = pacote['novo_hp2']
                                        funcoes_Classes.animacao_ataque(janela, fundo, escolhido, escolhido2, auxhp1, auxhp2, auxxp1, True, atk.nome, escolhido.hp, pacote['hp_anterior2'], escolhido.hp, escolhido2.hp)
                                        if escolhido2.hp > 0:
                                            aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
                                        else:
                                            aux2 = 0   
                                        auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                        if atk.efetivo(escolhido2) == 2:
                                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'foi super efetivo'), True, janela)
                                        elif atk.efetivo(escolhido2) == 0.5:
                                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'nao foi muito efetivo'), True, janela)
                                    else:
                                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'atk de {escolhido.nome} aumentou'), True, janela)
                                        sup += 1
                                    if minha_vez:
                                        minha_vez = False
                                        pacote['evento'] = 'MENU_BATALHA'
                                    sleep(0.5)
                    elif tecla[pygame.K_BACKSPACE]:
                        if ataques:
                            ataques = False
                            mov1 = 1
                    elif tecla[pygame.K_LEFT] or tecla[pygame.K_a]:
                        if mov1 > 1:
                            save1 = mov1
                            mov1 -= 1
                    elif tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
                        if mov1 < 2:
                            save1 = mov1
                            mov1 += 1
                    elif tecla[pygame.K_UP]:
                        if mov2 > 1:
                            save2 = mov2
                            mov2 -= 1
                    elif tecla[pygame.K_DOWN]:
                        if mov2 < 2:
                            save2 = mov2
                            mov2 += 1
                    if ataques:
                        if mov1 == 1 and mov2 == 2 and len(escolhido.ataques) < 3:
                            mov1 = save1
                            mov2 = save2
                        elif mov1 == 2 and mov2 == 2 and len(escolhido.ataques) < 4:
                            mov1 = save1
                            mov2 = save2
                if pacote['evento'] == 'MENU_BATALHA' or escolhido2.hp <= 0:
                    janela.blit(fundo, (0, 0))
                    if (not ataques):
                        janela.blit(imagens.molde, (0, 384))
                        funcoes_Classes.seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                    else:
                        janela.blit(imagens.molde2, (0, 384))
                        funcoes_Classes.seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                        funcoes_Classes.golpes(escolhido, janela)

                    janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                    janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                    janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
                    janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                    janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                    janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                    janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                    funcoes_Classes.nomecin1(janela, funcoes_Classes.palavra(escolhido.nome), escolhido.nome)
                    funcoes_Classes.nomecin2(janela, funcoes_Classes.palavra(escolhido2.nome), escolhido.nome)
                    funcoes_Classes.nivelcin1(janela, funcoes_Classes.palavra(f'{escolhido.nivel}'))
                    funcoes_Classes.nivelcin2(janela, funcoes_Classes.palavra(f'{escolhido2.nivel}'))
                    if escolhido2.hp <= 0:   
                        sup2 = 0      
                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'{escolhido2.nome} desmaiou'), True, janela)
                        sleep(1)
                        escolhido2.hp_base = 0
                        funcoes_Classes.fainted2(janela, fundo, escolhido, escolhido2, variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32, imagens.altural * 1.5, False, True, auxhp1, aux1, aux1x, auxxp1)
                        if pacote['status'] == 'perdeu':
                            funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'Parabens voce venceu'), True, janela)
                            sleep(1)
                            batalha = False
                            online = False
                            server = False
                            server_ativo = False
                            servidor.close()
                            trainer = False
                            aviso = False
                            equipe.curar()
                            funcoes_Classes.musicaPrincipal()
                        else:
                            funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'aguardando adversario'), True, janela)
                            meu_pacote = {'evento': 'AGUARDANDO_REPOSICAO'}
                            servidor.sendall(json.dumps(meu_pacote).encode('utf-8'))
                            while fila_receber.empty():
                                sleep(0.5)
                            pacote = fila_receber.get()
                            pacote['evento'] = 'MENU_BATALHA'
                            for cimon in cimons.cimons:
                                if cimon.nome == pacote['nome']:
                                    cin2 = cimon.clonar()
                                    cin2.xp = sum(n * 10 for n in range(1, pacote['nivel']))
                                    cin2.subir_nivel()
                                    cin2.hp = pacote['hp']
                            escolhido2 = cin2
                            aviso2 = True
                elif pacote['evento'] == 'RESULTADO_TURNO':
                    fataque = f'{escolhido2.nome} usou {pacote["golpe_tomado"]}'
                    funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(fataque), True, janela)
                    sleep(0.2)
                    if pacote['golpe_tomado'] != 'dano':
                        escolhido.hp = pacote['novo_hp1']
                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        funcoes_Classes.animacao_ataque(janela, fundo, escolhido, escolhido2, auxhp1, auxhp2, auxxp1, False, pacote['golpe_tomado'], pacote['hp_anterior1'], escolhido2.hp, escolhido.hp, escolhido2.hp)
                        sleep(0.2)
                        if escolhido.hp > 0:
                            aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                        else:
                            aux1 = 0
                        auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                        if pacote['efetivo_tomado'] == "super efetivo":
                            funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('foi super efetivo'), True, janela)
                        elif pacote['efetivo_tomado'] == "pouco efetivo":
                            funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('nao foi muito efetivo'), True, janela) 
                    else:
                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'atk de {escolhido2.nome} aumentou'), True, janela)
                        sup2 += 1
                    if pacote['ID'] == 2 and (not trocado) and escolhido.hp > 0:
                        minha_vez = True
                    else:
                        minha_vez = False
                        trocado = False
                        pacote['evento'] = "MENU_BATALHA"
                    
                    sleep(0.5)             
                    janela.blit(fundo, (0, 0))
                    janela.blit(imagens.molde3, (0, 384))
                    janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                    janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                    janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra 1
                    janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                    funcoes_Classes.nomecin1(janela, funcoes_Classes.palavra(escolhido.nome), escolhido.nome)
                    funcoes_Classes.nomecin2(janela, funcoes_Classes.palavra(escolhido2.nome), escolhido2.nome)
                    funcoes_Classes.nivelcin1(janela, funcoes_Classes.palavra(f'{escolhido.nivel}'))
                    funcoes_Classes.nivelcin2(janela, funcoes_Classes.palavra(f'{escolhido2.nivel}'))
                    janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                    aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
                    auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                    janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                    janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                    sleep(0.5)
                    if escolhido.hp <= 0:
                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'{escolhido.nome} desmaiou'), True, janela)
                        sleep(1.5)
                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        sleep(1)
                        funcoes_Classes.fainted1(janela, fundo, escolhido, escolhido2, variaveis.posx1 - 48, variaveis.posy1 - 48, imagens.altural * 1.3, False, True, auxhp2, aux2)
                        sleep(1)
                        equipe.derrotados += 1
                        equipe.vivos -= 1
                        ################
                        if equipe.verificar():
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('voce ficou sem cinmons'), True, janela)
                            sleep(1)
                            equipe.curar()
                            batalha = False
                            trainer = False
                            aviso = False
                            online = False
                            server = False
                            server_ativo = False
                            servidor.close()
                            funcoes_Classes.musicaPrincipal()
                        else:
                            mov1 = mov2 = 1
                            morto = True
                            escolhendo = True
                elif pacote['evento'] == "TROCA" or pacote['evento'] == 'TROCA_DUPLA':
                    for cimon in cimons.cimons:
                        if cimon.nome == pacote['nome']:
                            cin2 = cimon.clonar()
                            cin2.xp = sum(n * 10 for n in range(1, pacote['nivel']))
                            cin2.subir_nivel()
                            cin2.hp = pacote['hp']
                    escolhido2 = cin2
                    if pacote['evento'] == 'TROCA_DUPLA':
                        aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
                        auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                    else:
                        aux2 = int(150 * (pacote['hp_anterior2'] / escolhido2.hp_max)//1)
                        auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                        aviso_troca = True
                    aviso2 = True
                    if pacote['evento'] == 'TROCA':
                        pacote['evento'] = 'RESULTADO_TURNO'
                        if (not trocado):
                            minha_vez = True
                    elif pacote['evento'] == 'TROCA_DUPLA':
                        pacote['evento'] = 'MENU_BATALHA'
                        trocado = False
            elif escolhendo:
                ataques = False
                if tecla[pygame.K_BACKSPACE] and (not morto):
                    escolhendo = False
                    mov1 = 1
                    mov2 = 2
                if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:# or ass == 'a':
                    if mov1 > 1:
                        mov1 -= 1
                elif tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:# or ass == 'd':
                    if mov1 < len([n for n in equipe.lista if n.hp > 0 and n != '']):
                        mov1 += 1
                janela.blit(fundo, (0, 0))
                janela.blit(imagens.molde3, (0, 384))
                if temporizador < 1:
                    funcoes_Classes.seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, False)
                    aux = 0
                    for n in [cin for cin in equipe.lista if cin.hp > 0 and cin != '']:
                        janela.blit(n.mini, (64 + aux * 128 * 1.5, 400))
                        aux += 1
                if (not morto):
                    janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                if (not morto):
                    janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                    janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                funcoes_Classes.nomecin1(janela, funcoes_Classes.palavra(escolhido.nome), escolhido.nome)
                funcoes_Classes.nomecin2(janela, funcoes_Classes.palavra(escolhido2.nome), escolhido2.nome)
                funcoes_Classes.nivelcin1(janela, funcoes_Classes.palavra(f'{escolhido.nivel}'))
                funcoes_Classes.nivelcin2(janela, funcoes_Classes.palavra(f'{escolhido2.nivel}'))
                if tecla[pygame.K_SPACE] or temporizador == 1:
                    listacin = [cin for cin in equipe.lista if cin.hp > 0 and cin != '']
                    temporizador += 1
                    segundo = escolhido
                    auxhpc = auxhp1
                    auxc = aux1
                    marca = False
                    if mov1 == 1 and temporizador == 2:
                        if listacin[0].hp > 0 and escolhido is not listacin[0]:
                            escolhido = equipe.lista[equipe.lista.index(listacin[0])]
                            marca = True
                    elif mov1 == 2 and temporizador == 2:
                        if listacin[1].hp > 0 and escolhido is not listacin[1]:
                            escolhido = equipe.lista[equipe.lista.index(listacin[1])]
                            marca = True
                    elif mov1 == 3 and temporizador == 2:
                        if listacin[2].hp > 0 and escolhido is not listacin[2]:
                            escolhido = equipe.lista[equipe.lista.index(listacin[2])]
                            marca = True
                    if segundo == escolhido and temporizador == 2:
                        marca = False
                        temporizador = 0
                    if temporizador == 2 and marca:
                        mov1 = mov2 = 1
                        if (not morto):
                            trocado = True
                        temporizador = 0
                        evento = 'TROCA' if (not morto) else 'COMECO2'
                        meu_pacote = {'evento': evento, 'nome': escolhido.nome, 'nivel': escolhido.nivel, 'hp': escolhido.hp}
                        servidor.sendall(json.dumps(meu_pacote).encode('utf-8'))
                        if (not morto):
                            funcoes_Classes.terminal(janela, segundo, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('aguardando adversario'), True, janela)
                            while fila_receber.empty():
                                sleep(0.5)
                            pacote = fila_receber.get()
                            funcoes_Classes.terminal(janela, segundo, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        funcoes_Classes.rodarpalavra(funcoes_Classes.palavra(f'Va {escolhido.nome}'), True, janela)
                        sleep(1.5)
                        funcoes_Classes.comeco2(janela, fundo, False, True, variaveis.posx1, variaveis.posy1, variaveis.posx2, variaveis.posy2, sel, escolhendo, escolhido, escolhido2,  segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto)
                        aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                        auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                        aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
                        auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
                        escolhendo = False
                        funcoes_Classes.terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        morto = False
                        sup = 0
                    elif temporizador == 2:
                        temporizador = 0
                sleep(0.1)
            pygame.display.update()


        


    print(variaveis.posy)
    pygame.display.update()
    sleep(0.1)