import pygame
import imagens
import variaveis
import objetos
import funcoes_Classes
import cimons
import json
import os
import sys

from time import sleep

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

janela = pygame.display.set_mode((variaveis.largura, variaveis.altura))

def salvarJogo(estado):
#Transforma o dicionário em texto e salva em um arquivo.
    # O 'w' significa 'write' (escrever/sobrescrever)
    with open(ARQUIVO_SAVE, 'w') as arquivo:
        json.dump(estado, arquivo, indent=4) # indent=4 deixa o arquivo formatado e fácil de ler
    print("Jogo salvo com sucesso!")
    funcoes_Classes.limpar(janela, imagens.balaofala)
    funcoes_Classes.rodarpalavra(funcoes_Classes.palavra('jogo salvo com sucesso'), False, janela)
    sleep(1)


def carregar_jogo():
    """Lê o arquivo de texto e transforma de volta em um dicionário."""
    # Primeiro checamos se o arquivo existe para o jogo não dar erro
    if os.path.exists(ARQUIVO_SAVE):
        # O 'r' significa 'read' (ler)
        with open(ARQUIVO_SAVE, 'r') as arquivo:
            estado_recuperado = json.load(arquivo)
        print("Jogo carregado com sucesso!")
        return estado_recuperado
    else:
        print("Nenhum save encontrado. Iniciando um jogo novo.")
        return None # Retorna None se não existir save
    
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

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('CinMón')



treinador1 = funcoes_Classes.treinador('ewerton')
equipe1 = funcoes_Classes.equipe(2, 2, 0, [cimons.rayquaza.clonar(), cimons.lupi.clonar()])
equipe1.lista[0].xp = 10
equipe1.lista[1].xp = 10
equipe1.lista[0].subir_nivel()
equipe1.lista[1].subir_nivel()
equipe1.curar()

treinador2 = funcoes_Classes.treinador('jl')
equipe2 = funcoes_Classes.equipe(1, 1, 0, [cimons.goku.clonar()])
equipe2.lista[0].xp = 30
equipe2.lista[0].subir_nivel()
equipe2.curar()

treinador3 = funcoes_Classes.treinador('daniel')
equipe3 = funcoes_Classes.equipe(3, 3, 0, [cimons.lupi.clonar(), cimons.mclovin.clonar(), cimons.mewtwo.clonar()])
for n in range(len(equipe3.lista)):
    equipe3.lista[n].xp += 100
    if equipe3.lista[n].nome == 'mewtwo':
        equipe3.lista[n].xp += 50 
    equipe3.lista[n].subir_nivel()
equipe3.curar()

treinador4 = funcoes_Classes.treinador('jose')
equipe4 = funcoes_Classes.equipe(3, 3, 0, [cimons.lupi.clonar(), cimons.rath.clonar(), cimons.rayquaza.clonar()])
for n in range(len(equipe4.lista)):
    equipe4.lista[n].xp += 100
    if equipe4.lista[n].nome == 'rayquaza':
        equipe4.lista[n].xp += 50 
    equipe4.lista[n].subir_nivel()
equipe4.curar()


#treinador = treinador2
#equipe_2 = equipe2
#treinador = treinador1
#equipe_2 = equipe1
listaT = [imagens.cenario5, imagens.cenario9]       #cenarios onde há treinadores
listaitems1 = [imagens.crachabola]                  #imagens que há na loja

rodando = True

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
'''
equipe = funcoes_Classes.equipe(1, 1, 0, [cimons.naruto.clonar()])
mochila = funcoes_Classes.mochila([imagens.crachabola], [0], 0)
equipe.lista[0].xp = 209
bla, bla2, equipe.lista[0] =equipe.lista[0].subir_nivel()
'''





while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                salvarJogo(estado)
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
                mochila = funcoes_Classes.mochila([imagens.crachabola], [0], 0)
                mochila.dinheiro = estado['mochila'][1]
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

    if (not batalha):
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
                escolhaioda, escolha, balao, mov1a = funcoes_Classes.inicio(mov1a, ataques, escolhendo, bolsa, balao, janela, aviso, player, imagens.player, batalha, cenario1, marca2, tecla, escolhaioda)
                if escolhaioda:
                    equipe = funcoes_Classes.equipe(1, 1, 0, [escolha.clonar()])
                    estado['equipe'] = [(equipe.lista[0].nome, (equipe.lista[0].nivel - 1) * 10 + equipe.lista[0].xp, equipe.lista[0].hp)]
                    mochila = funcoes_Classes.mochila([imagens.crachabola], [2], 0)
                    estado['mochila'] = [['crachabola', 2], 0]
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
                    estado['mochila'] = [['crachabola', mochila.listaDeQtd[mochila.listaDeles.index(imagens.crachabola)]], mochila.dinheiro]




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
            if equipe_2.timevivo() and indice not in estado['treinadores_derrotados']:
                batalha = True
                musicaB = True
                musicaP = False
                aviso = False
                funcoes_Classes.avisoCombate(janela, treinador)
            else:
                trainer = False


###

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
            '''
            for j in variaveis.listaobjatual:
                pygame.draw.rect(janela, (255, 0, 0), j, 4)
            for j in variaveis.gramas4_atual:
                pygame.draw.rect(janela, (0, 255, 0), j, 4)
            '''
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
            estado['mochila'] = [['crachabola', mochila.listaDeQtd[mochila.listaDeles.index(imagens.crachabola)]], mochila.dinheiro]
            for n in ([equipe1, equipe2, equipe3, equipe4]):
                if (not n.timevivo()) and treinador not in estado['treinadores_derrotados']:
                    estado['treinadores_derrotados'].append(indice)



    print(variaveis.posx)
    pygame.display.update()
    sleep(0.1)