import pygame
import imagens
import variaveis
import objetos
import copy
#joalucaasmacio
import time
import random
#betas
pygame.mixer.init()
som_atk = pygame.mixer.Sound(imagens.caminho_atk)
som_atk.set_volume(0.8)
som_nivel = pygame.mixer.Sound(imagens.caminho_nivel)
som_nivel.set_volume(0.8)


class Player:
    def __init__(self, posx, posy, velocidade, imagem, visual, rect):
        self.posicao = (posx, posy)
        self.velocidade = velocidade
        self.imagem = imagem
        self.visual = visual
        self.rect = rect

    def movimento(self, posx, posy, di, es, ci, ba, janela, fundo, andada):
        for n in range(1, 5):
            janela.blit(fundo, (0, 0))
            for k in range(len(variaveis.posobjatual)):
                janela.blit(variaveis.listatual[k], (variaveis.posobjatual[k][0], variaveis.posobjatual[k][1]))
            if fundo == imagens.cenario1 or fundo == imagens.cenario5 or fundo == imagens.cenario9:
                for j in range(len(variaveis.gramasatual)):
                    janela.blit(variaveis.gramasatual[j], (variaveis.gramasxatual[j], variaveis.gramasyatual[j]))
            if di:
                self.posicao = (posx - self.velocidade + (self.velocidade / 4) * n, posy)
                if andada == 0:
                    self.visual = imagens.andando_direita1
                else:
                    self.visual = imagens.andando_direita2
            elif es:
                self.posicao = (posx + self.velocidade - (self.velocidade / 4) * n, posy)
                if andada == 0:
                    self.visual = imagens.andando_esquerda1
                else:
                    self.visual = imagens.andando_esquerda2
            elif ba:
                self.posicao = (posx, posy - self.velocidade + (self.velocidade / 4) * n)
                if andada == 0:
                    self.visual = imagens.andando_frente1
                else:
                    self.visual = imagens.andando_frente2
            elif ci:
                self.posicao = (posx, posy + self.velocidade - (self.velocidade / 4) * n)
                if andada == 0:
                    self.visual = imagens.andando_atras1
                else:
                    self.visual = imagens.andando_atras2
            janela.blit(self.visual, self.posicao)
            pygame.display.update()
            time.sleep(0.05)

                
    
    def direita(self, posx, posy, janela, fundo, andada):
        tentou = False
        di = True
        es = False
        ci = False
        ba = False
        save = posx
        posx += self.velocidade
        self.posicao = (posx, posy)
        self.rect.x = posx
        self.rect.y = posy
        if self.limiten(posx, posy) or self.colisaon():
            posx = save
            self.posicao = (posx, posy)
            self.rect.x = posx
            self.rect.y = posy
            tentou = True
        else:
            self.movimento(posx, posy, di, es, ci, ba, janela, fundo, andada)
        self.visual = imagens.direita
        return posx, tentou
        

    def esquerda(self, posx, posy, janela, fundo, andada):
        tentou = False
        di = False
        es = True
        ci = False
        ba = False
        save = posx
        posx -= self.velocidade
        self.posicao = (posx, posy)
        self.rect.x = posx
        self.rect.y = posy
        if self.limiten(posx, posy) or self.colisaon():
            posx = save
            self.posicao = (posx, posy)
            self.rect.x = posx
            self.rect.y = posy
            tentou = True
        else:
            self.movimento(posx, posy, di, es, ci, ba, janela, fundo, andada)
        self.visual = imagens.esquerda
        return posx, tentou
    
    def cima(self, posx, posy, janela, fundo, andada):
        tentou = False
        di = False
        es = False
        ci = True
        ba = False
        save = posy
        posy -= self.velocidade
        self.posicao = (posx, posy)
        self.rect.x = posx
        self.rect.y = posy
        if self.limiten(posx, posy) or self.colisaon():
            posy = save
            self.posicao = (posx, posy)
            self.rect.x = posx
            self.rect.y = posy
            tentou = True
        else:
            self.movimento(posx, posy, di, es, ci, ba, janela, fundo, andada)
        self.visual = imagens.atras
        return posy, tentou

    def baixo(self, posx, posy, janela, fundo, andada):
        tentou = False
        di = False
        es = False
        ci = False
        ba = True
        save = posy
        posy += self.velocidade
        self.posicao = (posx, posy)
        self.rect.x = posx
        self.rect.y = posy
        if self.limiten(posx, posy) or self.colisaon():
            posy = save
            self.posicao = (posx, posy)
            self.rect.x = posx
            self.rect.y = posy
            tentou = True
        else:
            self.movimento(posx, posy, di, es, ci, ba, janela, fundo, andada)
        self.visual = imagens.frente
        return posy, tentou

    def limiten(self, posx, posy):
        if posx >= variaveis.largura or posx < 0 or posy >= variaveis.altura or posy < 0:
            return True
        else:
            return False
    
    def colisaon(self):
        for k in variaveis.listaobjatual:
            if self.rect.colliderect(k) and k is not objetos.player4:
                return True
        return False
    
    def colisaog(self, gramas):
        for k in gramas:
            if self.rect.colliderect(k):
                return True
        return False
    

class ataques:
    def __init__(self, nome, tipo, efeito, dano_base, dano, pp, pp_max):
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito
        self.dano_base = dano_base
        self.dano = dano
        self.pp = pp
        self.pp_max = pp_max
    
    def clonar(self):
        return ataques(
            self.nome,
            self.tipo,
            self.efeito,
            self.dano_base,
            self.dano,
            self.pp,
            self.pp_max
        )

    def efetivo(self, self2):
        if self.tipo == 'normal':
            if self2.tipo == 'lutador':
                return 0.5
            elif self2.tipo == 'voador':
                return 2
            else:
                return 1
        elif self.tipo == 'lutador':
            if self2.tipo == 'normal' or self2.tipo == 'escuridao':
                return 2
            elif self2.tipo == 'voador' or self2.tipo == 'psiquico':
                return 0.5
            else:
                return 1
        elif self.tipo == 'voador':
            if self2.tipo == 'normal' or self2.tipo == 'dragao':
                return 0.5
            elif self2.tipo == 'lutador':
                return 2
            else:
                return 1
        elif self.tipo == 'fogo':
            if self2.tipo == 'voador':
                return 2
            elif self2.tipo == 'dragao':
                return 0.5
            else:
                return 1
        elif self.tipo == 'psiquico':
            if self2.tipo == 'lutador':
                return 2
            elif self2.tipo == 'escuridao':
                return 0.5
            else:
                return 1
        elif self.tipo == 'escuridao':
            if self2.tipo == 'psiquico':
                return 2
            elif self2.tipo == 'lutador':
                return 0.5
            else:
                return 1
        elif self.tipo == 'dragao':
            if self2.tipo == 'dragao':
                return 2
            else:
                return 1
        



class Cimons:
    def __init__(self, nome, tipo, imagemc, imagemf, mini, hp_base, hp, hp_max, nivel, xp, ataques, lista, evolucao, status):
        self.nome = nome
        self.tipo = tipo
        self.imagemc = imagemc
        self.imagemf = imagemf
        self.mini = mini
        self.hp_base = hp_base
        self.hp = hp
        self.hp_max = int((hp_base + (nivel - 1) ** 1.1)//1)
        self.nivel = nivel
        self.xp = xp
        self.ataques = ataques
        self.lista = lista
        for n in self.ataques:
            self.ataques[n].dano = int((self.ataques[n].dano_base + ((self.nivel - 1) ** 1.1) / 2 )//1)
        self.evolucao = evolucao
        self.status = status

    def subir_nivel(self):
        aprendido = []
        niveis = 0
        while self.xp >= self.nivel * 10:
            self.xp -= self.nivel * 10
            niveis += 1
            self.nivel += 1
            self.hp_max = int((self.hp_base + (self.nivel - 1) ** 1.1)//1)
            for n in self.ataques:
                self.ataques[n].dano = int((self.ataques[n].dano_base + ((self.nivel - 1) ** 1.1) / 2)//1)
            if len(self.lista) > 0 and self.lista[0] != 0:
                self.ataques[f'ataque{len(self.ataques) + 1}'] = self.lista[0]
                aprendido.append(self.lista[0].nome)
                self.lista.pop(0)
            elif len(self.lista) > 0:
                self.lista.pop(0)
        if len(self.evolucao) > 0:
            if self.nivel >= self.evolucao[1]:
                self = self.evoluir()
        return aprendido, niveis, self

    def evoluir(self):
        nivel = self.nivel
        xp = self.xp
        hp = self.hp
        self = self.evolucao[0].clonar()
        self.hp = hp
        for n in range(1, nivel):
            self.xp += n * 10
        self.xp += xp
        self.subir_nivel()
        return self

    
    def clonar(self):
        
        novos_ataques = {}

        for chave, ataque in self.ataques.items():
            novos_ataques[chave] = ataque.clonar()

        return Cimons(
            self.nome, 
            self.tipo, 
            self.imagemc, 
            self.imagemf, 
            self.mini, 
            self.hp_base, 
            self.hp, # Reseta o HP atual para o máximo ao nascer selvagem
            self.hp_max, 
            self.nivel, 
            self.xp, 
            novos_ataques,
            self.lista.copy(),
            self.evolucao,
            self.status
        )

class equipe:
    def __init__(self, quantidade, vivos, derrotados, listaDeles):
        self.quantidade = quantidade
        self.vivos = vivos
        self.derrotados = derrotados
        self.lista = listaDeles
    
    def lancar(self):
        escolhido = ''
        if self.timevivo():
            for n in range(len(self.lista)):
                if self.lista[n].hp > 0:
                    escolhido = self.lista[n]
                    return escolhido
        return escolhido

    def verificar(self):
        if self.vivos <= 0:
            return True
        else:
            return False
        
    def timevivo(self):
        if self.vivos > 0:
            return True
        else:
            return False
        
    def curar(self):
        for q in range(self.quantidade):
            self.lista[q].hp = self.lista[q].hp_max
            for k in range(len(self.lista[q].ataques)):
                self.lista[q].ataques[f'ataque{k + 1}'].pp = self.lista[q].ataques[f'ataque{k + 1}'].pp_max
        self.derrotados = 0
        self.vivos = len(self.lista)
    
    def adicionar(self, cinmon):
        if len(self.lista) < 3:
            self.lista.append(cinmon.clonar())
            self.vivos += 1
            self.quantidade += 1
    
    def capturar(self, sel):
        capturar = False
        vezes = 0
        razao_hp = sel.hp / sel.hp_max
        chance = (1 - razao_hp) ** 1.5
        chance = max(0.6, min(chance, 1))
        sorteado = random.random()
        if(sorteado < chance):
            vezes += 1
            chance = (1 - razao_hp) ** 1.5
            chance = max(0.4, min(chance, 0.95))
            if sorteado < chance:
                vezes += 1
                chance = (1 - razao_hp) ** 1.5
                chance = max(0.1, min(chance, 0.9))
                if sorteado < chance:
                    vezes += 1
                    capturar = True
        time.sleep(1)
        return capturar, vezes

class mochila:

    def __init__(self, listaDeles, listaDeQtd, dinheiro):
        self.listaDeles = listaDeles
        self.listaDeQtd = listaDeQtd
        self.dinheiro = dinheiro

    def comprar(self, objeto):
        comprou = False
        if objeto == 'crachabola' and self.dinheiro >= 30:
            self.dinheiro -= 30
            self.listaDeQtd[self.listaDeles.index(imagens.crachabola)] += 1
            comprou = True
        elif objeto == 'potion' and self.dinheiro >= 35:
            self.dinheiro -= 35
            self.listaDeQtd[self.listaDeles.index(imagens.potion)] += 1
            comprou = True
        return comprou


    


class treinador():

    def __init__(self, nome):
        self.nome = nome

        

        
import cimons


def musicaPrincipal():
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load(imagens.caminho_musicaPrincipal)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def musicaBatalha():
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load(imagens.caminho_batalha_tema)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)



def batalha_selvagem(self, player, fundo, janela, equipe, selvagem, batalha, tecla, trainer, aleatorio, balao, cenario):
    sup = 0
    sup2 = 0
    while batalha:
        rodando = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                batalha = False
                rodando = False
        tecla = pygame.key.get_pressed()
        if (not aleatorio):
            escolhendo = False
            capturado = False
            bolsa = False
            fugir = False
            ataques = False
            verturno = True
            aviso = False
            morto = False
            escolhido2 = ''
            segundo = ''
            auxhpc = 0
            auxc = 0
            cimons_ = selvagens_do_cenario(cenario)
            sel = random.choice(cimons_).clonar()
            nivel_dos_selvagens(cenario, sel)
            aleatorio = True
            mov1 = 1
            mov2 = 1
        if (not aviso):
            escolhido = equipe.lancar()
            aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
            auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
            aux2 = int(150 * (sel.hp / sel.hp_max)//1)
            auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
            aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
            auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            aviso = True
            aviso2 = False
            frase = f'Um {sel.nome} selvagem apareceu'
            frase = palavra(frase)
            rodarpalavra(frase, batalha, janela)
            time.sleep(1)
            comeco1(janela, fundo, selvagem, variaveis.posx2, variaveis.posy2, sel, aviso, aviso2, trainer, escolhido, escolhido2, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1)
            time.sleep(1)
            rodarpalavra(palavra(f'Va {escolhido.nome}'), batalha, janela)
            time.sleep(1)
            comeco2(janela, fundo, selvagem, trainer, variaveis.posx1, variaveis.posy1, variaveis.posx2, variaveis.posy2, sel, escolhendo, escolhido, escolhido2, segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto)
            time.sleep(1)
        if (not escolhendo) and (not bolsa):
            temporizador = 0
            if escolhido.hp > 0:
                if tecla[pygame.K_SPACE]:# or auu == 'a':
                    time.sleep(0.2)
                    if (not ataques) and mov1 == 1 and mov2 == 1:
                        ataques = True
                    elif (not ataques) and mov1 == 2 and mov2 == 2:
                        fugir = True
                    elif (not ataques) and mov1 == 1 and mov2 == 2:
                        escolhendo = True
                    elif (not ataques) and mov1 == 2 and mov2 == 1:
                        bolsa = True
                        mov1 = 1
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
                            if escolhido.ataques[f'ataque{des}'].pp > 0:
                                escolhido.ataques[f'ataque{des}'].pp -= 1
                                terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                rodarpalavra(palavra(f'{escolhido.nome} usou {atk.nome}'), batalha, janela)
                                time.sleep(0.2)
                                if atk.efeito == 'dano':
                                    dano = int(((int(atk.dano * atk.efetivo(sel)//1) + int((sup * 0.5 * escolhido.nivel)//1)) * escolhido.status)//1)
                                    animacao_ataque(janela, fundo, escolhido, sel, auxhp1, auxhp2, auxxp1, verturno, atk, escolhido.hp, sel.hp, escolhido.hp, sel.hp - dano)
                                    sel.hp -= dano
                                    if sel.hp > 0:
                                        aux2 = int(150 * (sel.hp / sel.hp_max)//1)
                                    else:
                                        aux2 = 0
                                    auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                    if atk.efetivo(sel) == 2:
                                        rodarpalavra(palavra(f'foi super efetivo'), batalha, janela)
                                    elif atk.efetivo(sel) == 0.5:
                                        rodarpalavra(palavra(f'nao foi muito efetivo'), batalha, janela)
                                    time.sleep(1)
                                else:
                                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                    rodarpalavra(palavra(f'atk de {escolhido.nome} aumentou'), batalha, janela)
                                    time.sleep(0.5)
                                    sup += 1
                                verturno = False        #trocar o turno
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

            if verturno or sel.hp <= 0:
                janela.blit(fundo, (0, 0))
                if (not ataques):
                    janela.blit(imagens.molde, (0, 384))
                    seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                else:
                    janela.blit(imagens.molde2, (0, 384))
                    seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                    golpes(escolhido, janela)

                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
                nomecin2(janela, palavra(sel.nome), sel.nome)
                nivelcin1(janela, palavra(f'{escolhido.nivel}'))
                nivelcin2(janela, palavra(f'{sel.nivel}'))
                if sel.hp <= 0 or fugir:
                    if fugir:
                        terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra('Conseguiu Escapar'), batalha, janela)
                        time.sleep(2)
                    elif sel.hp <= 0:         
                        terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'{sel.nome} desmaiou'), batalha, janela)
                        time.sleep(1)
                        fainted2(janela, fundo, escolhido, sel, variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32, imagens.altural * 1.5, selvagem, trainer, auxhp1, aux1, aux1x, auxxp1)
                        time.sleep(1)
                        sel.hp_base = 0
                        savexp1 = escolhido.xp
                        savenivel = escolhido.nivel
                        escolhido.xp += sel.nivel * 10
                        savexp = escolhido.xp - savexp1
                        saveperso = escolhido
                        aprendido, niveis, escolhido = escolhido.subir_nivel()
                        equipe.lista[equipe.lista.index(saveperso)] = escolhido
                        aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
                        auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
                        animacao_xp(janela, fundo, escolhido, sel, auxhp1, aux1, aux1x, auxxp1, niveis, savenivel, savexp, savexp1)
                        terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        if saveperso != escolhido:
                            terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'{saveperso.nome} evoluiu para {escolhido.nome}'), batalha, janela)
                            time.sleep(1)
                        if niveis > 0:
                            pygame.mixer.music.pause()
                            som_nivel.play()
                            terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'{escolhido.nome} subiu de nivel'), batalha, janela)
                            time.sleep(1.5)
                            for nome in aprendido:
                                terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                rodarpalavra(palavra(f'{escolhido.nome} aprendeu {nome}'), batalha, janela)
                                time.sleep(1.5)
                                pygame.mixer.music.unpause()
                    batalha = False
                    selvagem = False
                    aleatorio = False
                    aviso = False
            else:
                atks = [sel.ataques[n] for n in sel.ataques]
                atq = random.choice(atks)
                terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                fataque = f'{sel.nome} usou {atq.nome}'
                rodarpalavra(palavra(fataque), batalha, janela)
                time.sleep(0.2)
                if atq.efeito == 'dano':
                    dano = int(((int(atq.dano * atq.efetivo(escolhido)//1) + int((sup2 * 0.5 * sel.nivel)//1)) * sel.status)//1)
                    time.sleep(0.2)
                    animacao_ataque(janela, fundo, escolhido, sel, auxhp1, auxhp2, auxxp1, verturno, atq, escolhido.hp, sel.hp, escolhido.hp - dano, sel.hp)
                    escolhido.hp -= dano
                    if escolhido.hp > 0:
                        aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                    else:
                        aux1 = 0
                    auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    if atq.efetivo(escolhido) == 2:
                        rodarpalavra(palavra(f'foi super efetivo'), batalha, janela)
                    elif atq.efetivo(escolhido) == 0.5:
                        rodarpalavra(palavra(f'nao foi muito efetivo'), batalha, janela)
                else:
                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    rodarpalavra(palavra(f'atk de {sel.nome} aumentou'), batalha, janela)
                    sup2 += 1
                time.sleep(0.5)
                verturno = True
                janela.blit(fundo, (0, 0))
                janela.blit(imagens.molde3, (0, 384))
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra 1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
                nomecin2(janela, palavra(sel.nome), sel.nome)
                nivelcin1(janela, palavra(f'{escolhido.nivel}'))
                nivelcin2(janela, palavra(f'{sel.nivel}'))
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                if escolhido.hp <= 0:
                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    rodarpalavra(palavra(f'{escolhido.nome} desmaiou'), batalha, janela)
                    time.sleep(1.5)
                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    time.sleep(1)
                    fainted1(janela, fundo, escolhido, sel, variaveis.posx1 - 48, variaveis.posy1 - 48, imagens.altural * 1.3, selvagem, trainer, auxhp2, aux2)
                    time.sleep(1)
                    equipe.derrotados += 1
                    equipe.vivos -= 1
                    ################
                    if equipe.verificar():
                        rodarpalavra(palavra('voce ficou sem cinmons'), batalha, janela)
                        time.sleep(1)
                        player.visual = imagens.atras
                        batalha = False
                        verturno = True
                        selvagem = False
                        aleatorio = False
                        aviso = False
                    else:
                        morto = True
                        escolhendo = True
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
                if mov1 < len([n for n in equipe.lista if n != '']):
                    mov1 += 1
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            if temporizador < 1:
                seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                for n in range(len(equipe.lista)):
                    janela.blit(equipe.lista[n].mini, (64 + n * 128 * 1.5, 400))
            if (not morto):
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            if (not morto):
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(sel.nome), sel.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                segundo = escolhido
                auxhpc = auxhp1
                auxc = aux1
                marca = False
                if mov1 == 1 and temporizador == 2:
                    mov1 = mov2 = 1
                    if equipe.lista[0].hp > 0 and escolhido is not equipe.lista[0]:
                        escolhido = equipe.lista[0]
                        marca = True
                elif mov1 == 2 and temporizador == 2:
                    mov1 = mov2 = 1
                    if equipe.lista[1].hp > 0 and escolhido is not equipe.lista[1]:
                        escolhido = equipe.lista[1]
                        marca = True
                elif mov1 == 3 and temporizador == 2:
                    mov1 = mov2 = 1
                    if equipe.lista[2].hp > 0 and escolhido is not equipe.lista[2]:
                        escolhido = equipe.lista[2]
                        marca = True
                if temporizador == 2 and marca:
                    temporizador = 0
                    if (not morto):
                        verturno = False
                    aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                    auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                    rodarpalavra(palavra(f'Va {escolhido.nome}'), batalha, janela)
                    aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
                    auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
                    time.sleep(1.5)
                    comeco2(janela, fundo, selvagem, trainer, variaveis.posx1, variaveis.posy1, variaveis.posx2, variaveis.posy2, sel, escolhendo, escolhido, escolhido2,  segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto)
                    escolhendo = False
                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    morto = False
                    sup = 0
                elif temporizador == 2:
                    temporizador = 0

        elif bolsa:
            #ass = input()
            ataques = False
            if tecla[pygame.K_BACKSPACE] and escolhido.hp > 0:
                bolsa = False
                mov1 = 2
                mov2 = 1
            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:# or ass == 'a':
                if mov1 > 1:
                    mov1 -= 1
            elif tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:# or ass == 'd':
                if mov1 < vu:
                    mov1 += 1
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(sel.nome), sel.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            if temporizador < 1:
                seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                vu = 0
                for n in self.listaDeles:
                    if len([n for n in self.listaDeles]) > 0:
                        janela.blit(n, (64 + (vu * 128 * 1.5), 400))
                        vu += 1
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                if mov1 == 1 and temporizador == 2:
                    mov1 = mov2 = 1
                    temporizador = 0
                    if self.listaDeQtd[0] > 0 and equipe.quantidade < 3:
                        capturado, vezes = equipe.capturar(sel)
                        self.listaDeQtd[0] -= 1
                        animacao_captura(janela, fundo, sel, vezes, escolhido, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1)
                        time.sleep(0.5)
                        if capturado:
                            janela.blit(fundo, (0, 0))
                            janela.blit(imagens.crachabola, (variaveis.posx2 - imagens.largural + 63, variaveis.posy2 - imagens.altural + 124))
                            equipe.adicionar(sel)
                            som_nivel.play()
                            terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'Parabens {sel.nome} foi capturado'), batalha, janela)
                            time.sleep(1.5)
                            batalha = False
                            selvagem = False
                            aleatorio = False
                            aviso = False
                            bolsa = False
                        else:
                            animacao_escapou(janela, fundo, sel, escolhido, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1)
                            time.sleep(0.5)
                            terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'Poxa {sel.nome} nao foi capturado'), batalha, janela)
                            time.sleep(1)
                            verturno = False
                            bolsa = False
                    elif self.listaDeQtd[0] <= 0:
                        terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'Voce nao tem crachabolas'), batalha, janela)
                        time.sleep(1)
                    else:
                        terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'Voce ja tem 3 cinmons'), batalha, janela)
                        time.sleep(1)
                elif mov1 == 2 and temporizador == 2:
                    mov1 = mov2 = 1
                    temporizador = 0
                    if self.listaDeQtd[1] > 0:
                        if escolhido.hp < escolhido.hp_max:
                            for i in range(40):
                                if escolhido.hp < escolhido.hp_max:
                                    escolhido.hp += 0.25
                                    aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                                    auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                                    terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                    pygame.display.update()
                                    time.sleep(0.05)
                            self.listaDeQtd[1] -= 1
                            rodarpalavra(palavra(f'{escolhido.nome} recuperou hp'),batalha, janela)
                            verturno = False
                            bolsa = False
                        else:
                            terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'{escolhido.nome} hp cheio'),batalha, janela)
                            time.sleep(1)
                    else:
                        terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'{escolhido.nome} voce nao tem potions'),batalha, janela)
                        time.sleep(1)

        time.sleep(0.1)
        pygame.display.update()

    return batalha, selvagem, aleatorio, aviso, rodando


def animacao_ataque(janela, fundo, escolhido, sel, auxhp1, auxhp2, auxxp1, verturno, ataque, vidaAnterior1, vidaAnterior2, vidaDepois1, vidaDepois2):
    time.sleep(0.25)
    som_atk.play()
    for n in range(0, 16):
        janela.blit(fundo, (0, 0))
        janela.blit(imagens.molde3, (0, 384))
        if verturno:
            aux = 0
            for k in palavra(f'{escolhido.nome} usou {ataque.nome}'):
                if k != ' ':
                    janela.blit(k, (64 + aux, 400))
                    aux += 28
                else:
                    aux += 36
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            if n % 4 != 0:
                janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        else:
            aux = 0
            for k in palavra(f'{sel.nome} usou {ataque.nome}'):
                if k != ' ':
                    janela.blit(k, (64 + aux, 400))
                    aux += 28
                else:
                    aux += 36
            if n % 4 != 0:
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
        janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
        janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nomecin2(janela, palavra(sel.nome), sel.nome)
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nivelcin2(janela, palavra(f'{sel.nivel}'))
        pygame.display.update()
        time.sleep(0.03)
    if verturno:
        while vidaAnterior2 > vidaDepois2:
            vidaAnterior2 -= 0.25
            if vidaAnterior2 > 0:
                aux = int(150 * (vidaAnterior2 / sel.hp_max)//1)
            else:
                aux = 0
            auxhp = pygame.transform.scale(imagens.auxhp, (aux, 10))
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            janela.blit(auxhp, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            nomecin2(janela, palavra(sel.nome), sel.nome)
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            pygame.display.update()
            time.sleep(0.025 / (sel.hp_max/10))
    else:
        while vidaAnterior1 > vidaDepois1:
            vidaAnterior1 -= 0.25
            if vidaAnterior1 > 0:
                aux = int(150 * (vidaAnterior1 / escolhido.hp_max)//1)
            else:
                aux = 0
            auxhp = pygame.transform.scale(imagens.auxhp, (aux, 10))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(auxhp, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            pygame.display.update()
            time.sleep(0.025 / (escolhido.hp_max/10))

def nivel_dos_selvagens(cenario, sel):
    if cenario == imagens.cenario5:
        sel.xp = random.choice([0, 10])
        sel.subir_nivel()
        sel.hp = sel.hp_max
    elif cenario == imagens.cenario9:
        sel.xp = random.choice([10, 30])
        sel.subir_nivel()
        sel.hp = sel.hp_max

def selvagens_do_cenario(cenario):
    selvagens = []
    if cenario == imagens.cenario1:
        for n in range(4):
            selvagens.append(cimons.lupi)
        selvagens.append(cimons.rath)
        return selvagens
    elif cenario == imagens.cenario5:
        for n in range(2):
            for n in range(2):
                selvagens.append(cimons.goku)
                selvagens.append(cimons.lupi)
            selvagens.append(cimons.mclovin)
            selvagens.append(cimons.naruto)
        selvagens.append(cimons.mewtwo)
    elif cenario == imagens.cenario9:
        for n in range(4):
            selvagens.append(cimons.rath)
            for n in range(2):
                selvagens.append(cimons.goku)
        for _ in range(2):
            selvagens.append(cimons.mewtwo)
            selvagens.append(cimons.rayquaza)
        selvagens.append(cimons.homelander)
    return selvagens

def animacao_captura(janela, fundo, sel, vezes, escolhido, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1):
    janela.blit(fundo, (0, 0))
    janela.blit(imagens.molde3, (0, 384))
    janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
    janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
    janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
    janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
    janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
    janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
    janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
    nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
    nomecin2(janela, palavra(sel.nome), sel.nome)
    nivelcin1(janela, palavra(f'{escolhido.nivel}'))
    nivelcin2(janela, palavra(f'{sel.nivel}'))
    janela.blit(imagens.crachabola, (variaveis.posx2 - imagens.largural + 63, variaveis.posy2 - 32))
    pygame.display.update()
    time.sleep(1)
    auxy = 240  #0
    auxLy = variaveis.posx2 - imagens.largural - 32  #posx2 - largural + 88
    auxAy = variaveis.posy2 - imagens.altural - 32  #posy2
    while auxy > 0:
        janela.blit(fundo, (0, 0))
        janela.blit(imagens.molde3, (0, 384))
        janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
        janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
        janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nomecin2(janela, palavra(sel.nome), sel.nome)
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nivelcin2(janela, palavra(f'{sel.nivel}'))
        janela.blit(imagens.crachabola, (variaveis.posx2 - imagens.largural + 63, variaveis.posy2 - 32))        
        auxy -= 12
        auxLy += 6
        auxAy += 4
        save = pygame.transform.scale(sel.imagemf, (auxy, auxy))
        janela.blit(save, (auxLy, auxAy))
        time.sleep(0.03)
        pygame.display.update()
    
    auxy2 = variaveis.posy2 - 32    #posy2 - altural + 124
    while auxy2 < variaveis.posy2 - imagens.altural + 124:
        janela.blit(fundo, (0, 0))
        janela.blit(imagens.molde3, (0, 384))
        janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
        janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
        janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nomecin2(janela, palavra(sel.nome), sel.nome)      
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nivelcin2(janela, palavra(f'{sel.nivel}'))
        auxy -= 12
        auxy2 += 4
        janela.blit(imagens.crachabola, (variaveis.posx2 - imagens.largural + 63, auxy2))
        time.sleep(0.015)
        pygame.display.update()
    
    for n in range(vezes):
        auxy3 = variaveis.posx2 - imagens.largural + 63 #posx2 - largural + 37
        for k in range(13):
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(sel.nome), sel.nome)        
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            auxy -= 12
            auxy3 -= 2
            janela.blit(imagens.crachabola, (auxy3, variaveis.posy2 - imagens.altural + 124))
            time.sleep(0.02)
            pygame.display.update()
        auxy3 = variaveis.posx2 - imagens.largural + 37 #posx2 - largural + 63
        for k in range(13):
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(sel.nome), sel.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            auxy -= 12
            auxy3 += 2
            janela.blit(imagens.crachabola, (auxy3, variaveis.posy2 - imagens.altural + 124))
            time.sleep(0.02)
            pygame.display.update()
        auxy3 = variaveis.posx2 - imagens.largural + 63 #posx2 - largural + 89
        time.sleep(0.1)
        for k in range(13):
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(sel.nome), sel.nome)            
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            auxy -= 12
            auxy3 += 2
            janela.blit(imagens.crachabola, (auxy3, variaveis.posy2 - imagens.altural + 124))
            time.sleep(0.02)
            pygame.display.update()
        auxy3 = variaveis.posx2 - imagens.largural + 89
        for k in range(13):
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            aux = 0
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(sel.nome), sel.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{sel.nivel}'))
            auxy -= 12
            auxy3 -= 2
            janela.blit(imagens.crachabola, (auxy3, variaveis.posy2 - imagens.altural + 124))
            time.sleep(0.02)
            pygame.display.update()
        time.sleep(0.5)

def animacao_escapou(janela, fundo, sel, escolhido, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1):
    aux2c = 6
    auxL = variaveis.posx2 + 57.2 #posx2 - largural - 32
    auxA = variaveis.posy2 + 99.4 #posy2 - altural - 32
    while aux2c < imagens.padraoA * 1.5:
        janela.blit(fundo, (0, 0))
        janela.blit(imagens.molde3, (0, 384))
        janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
        janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
        janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nomecin2(janela, palavra(sel.nome), sel.nome)
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nivelcin2(janela, palavra(f'{sel.nivel}'))
        aux2c += 6
        auxL -= 2.8
        if abs(auxL - 608) < 1 + 2.8:
            auxL = 608
        auxA -= 4.6
        if abs(auxA - (-8)) < 1 + 4.6:
            auxA = -8
        save = pygame.transform.scale(sel.imagemf, (aux2c, aux2c))
        janela.blit(save, (auxL, auxA))
        pygame.display.update()

def animacao_xp(janela, fundo, escolhido, inimigo, auxhp1, aux1, aux1x, auxxp1, niveis, savenivel, savexp, savexp2):
    escolhidoaux = escolhido.clonar()
    escolhidoaux.nivel = savenivel
    savex1 = int(270 * (savexp / savenivel * 10)//1) 
    savexp1 = pygame.transform.scale(imagens.auxxp, (savex1, 10))
    while savexp > 0:
        savexp2 += 0.25
        savexp -= 0.25
        savex1 = int(270 * (savexp2 / (savenivel * 10))//1)
        savexp1 = pygame.transform.scale(imagens.auxxp, (savex1, 10))
        janela.blit(savexp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        pygame.display.update()
        if savexp2 >= savenivel * 10:
            savexp2 = 0
            savenivel += 1
            niveis -= 1
            savex1 = int(270 * (savexp2 / (savenivel * 10))//1)
            savexp1 = pygame.transform.scale(imagens.auxxp, (savex1, 10))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            escolhidoaux.nivel += 1
            escolhidoaux.xp = 0
            terminal(janela, escolhidoaux, fundo, inimigo, auxhp1, aux1, 0, 0, False, True, False, aux1x, savexp1)
        time.sleep(0.05 / savenivel)


def batalha_treinador(self, mochila, treinador, fundo, janela, equipe1, equipe2, selvagem, batalha, tecla, trainer, balao):
    aviso = False
    aviso2 = False
    sup = 0
    sup2 = 0
    while batalha:
        rodando = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                batalha = False
                rodando = False
        tecla = pygame.key.get_pressed()
        if (not aviso) or aviso2:
            escolhendo = False
            bolsa = False
            capturado = False
            ataques = False
            verturno = True
            morto = False
            segundo = ''
            auxhpc = 0
            auxc = 0
            mov1 = 1
            mov2 = 1
            if (not aviso2):
                escolhido = equipe1.lancar()
            escolhido2 = equipe2.lancar()
            sel = ''
            aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
            auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
            aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
            auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
            aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
            auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            if (not aviso):
                frase = f'{treinador.nome} esta te desafiando'
                frase = palavra(frase)
                rodarpalavra(frase, batalha, janela)
            time.sleep(1)
            terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
            rodarpalavra(palavra(f'{treinador.nome} escolheu {escolhido2.nome}'), batalha, janela)
            time.sleep(1)
            comeco1(janela, fundo, selvagem, variaveis.posx2, variaveis.posy2, escolhido2, aviso, aviso2, trainer, escolhido, escolhido2, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1)
            time.sleep(0.5)
            if (not aviso):
                rodarpalavra(palavra(f'Va {escolhido.nome}'), batalha, janela)
            time.sleep(0.5)
            aviso = True
            if (not aviso2):
                comeco2(janela, fundo, selvagem, trainer, variaveis.posx1, variaveis.posy1, variaveis.posx2, variaveis.posy2, sel, escolhendo, escolhido, escolhido2, segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto)
            time.sleep(0.5)
            aviso2 = False
        if (not escolhendo) and (not bolsa):
            temporizador = 0
            if escolhido.hp > 0:
                if tecla[pygame.K_SPACE]:# or auu == 'a':
                    time.sleep(0.2)
                    if (not ataques) and mov1 == 1 and mov2 == 1:
                        ataques = True
                    elif (not ataques) and mov1 == 2 and mov2 == 2:
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra('Voce nao pode fugir'), batalha, janela)
                        time.sleep(1)
                    elif (not ataques) and mov1 == 1 and mov2 == 2:
                        escolhendo = True
                    elif (not ataques) and mov1 == 2 and mov2 == 1:
                        bolsa = True
                        mov1 = 1
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
                        if escolhido.ataques[f'ataque{des}'].pp > 0:
                            escolhido.ataques[f'ataque{des}'].pp -= 1
                            terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'{escolhido.nome} usou {atk.nome}'), batalha, janela)
                            time.sleep(0.2)
                            if atk.efeito == 'dano':
                                dano = int((int(atk.dano * atk.efetivo(escolhido2)//1) + (sup * 0.5 * escolhido.nivel)//1) * escolhido.status//1)
                                animacao_ataque(janela, fundo, escolhido, escolhido2, auxhp1, auxhp2, auxxp1, verturno, atk, escolhido.hp, escolhido2.hp, escolhido.hp, escolhido2.hp - dano)
                                escolhido2.hp -= dano
                                if escolhido2.hp > 0:
                                    aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
                                else:
                                    aux2 = 0   
                                auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                                terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                if atk.efetivo(escolhido2) == 2:
                                    rodarpalavra(palavra(f'foi super efetivo'), batalha, janela)
                                elif atk.efetivo(escolhido2) == 0.5:
                                    rodarpalavra(palavra(f'nao foi muito efetivo'), batalha, janela)
                            else:
                                terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                rodarpalavra(palavra(f'atk de {escolhido.nome} aumentou'), batalha, janela)
                                sup += 1
                            time.sleep(0.5)

                                
                            verturno = False        #trocar o turno
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

            if verturno or escolhido2.hp <= 0:
                janela.blit(fundo, (0, 0))
                if (not ataques):
                    janela.blit(imagens.molde, (0, 384))
                    seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                else:
                    janela.blit(imagens.molde2, (0, 384))
                    seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                    golpes(escolhido, janela)

                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
                nomecin2(janela, palavra(escolhido2.nome), escolhido.nome)
                nivelcin1(janela, palavra(f'{escolhido.nivel}'))
                nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
                if escolhido2.hp <= 0:   
                    sup2 = 0      
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    rodarpalavra(palavra(f'{escolhido2.nome} desmaiou'), batalha, janela)
                    time.sleep(1)
                    escolhido2.hp_base = 0
                    fainted2(janela, fundo, escolhido, escolhido2, variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32, imagens.altural * 1.5, selvagem, trainer, auxhp1, aux1, aux1x, auxxp1)
                    time.sleep(1)
                    equipe2.derrotados += 1
                    equipe2.vivos -= 1
                    escolhido2.hp_base = 0
                    savexp1 = escolhido.xp
                    savenivel = escolhido.nivel
                    escolhido.xp += escolhido2.nivel * 10
                    savexp = escolhido.xp - savexp1
                    saveperso = escolhido
                    aprendido, niveis, escolhido = escolhido.subir_nivel()
                    equipe1.lista[equipe1.lista.index(saveperso)] = escolhido
                    aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
                    auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
                    animacao_xp(janela, fundo, escolhido, escolhido2, auxhp1, aux1, aux1x, auxxp1, niveis, savenivel, savexp, savexp1)
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    if saveperso != escolhido:
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'{saveperso.nome} evoluiu para {escolhido.nome}'), batalha, janela)
                        time.sleep(1)
                    if niveis > 0:
                        pygame.mixer.music.pause()
                        som_nivel.play()
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'{escolhido.nome} subiu de nivel'), batalha, janela)
                        time.sleep(1.5)
                        for nome in aprendido:
                            terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'{escolhido.nome} aprendeu {nome}'), batalha, janela)
                            time.sleep(1.5)
                        pygame.mixer.music.unpause()

                    
                    if equipe2.verificar():
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'Parabens voce venceu de {treinador.nome}'), batalha, janela)
                        dinheiro = 0
                        for j in range(len(equipe2.lista)):
                            dinheiro += equipe2.lista[j].nivel * 20
                        mochila.dinheiro += dinheiro
                        time.sleep(1)
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'voce ganhou {dinheiro} cinreais'), batalha, janela)
                        batalha = False
                        trainer = False
                        aviso = False
                    else:
                        escolhido2 = equipe2.lancar()
                        aviso2 = True
            else:
                atks = [escolhido2.ataques[n] for n in escolhido2.ataques]
                atq = random.choice(atks)
                fataque = f'{escolhido2.nome} usou {atq.nome}'
                terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                rodarpalavra(palavra(fataque), batalha, janela)
                time.sleep(0.2)
                if atq.efeito == 'dano':
                    dano = int(((int(atq.dano * atq.efetivo(escolhido)//1) + int(sup2 * 0.5 * escolhido2.nivel)//1) * escolhido2.status)//1)
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    animacao_ataque(janela, fundo, escolhido, escolhido2, auxhp1, auxhp2, auxxp1, verturno, atq, escolhido.hp, escolhido2.hp, escolhido.hp - dano, escolhido2.hp)
                    time.sleep(0.2)
                    escolhido.hp -= dano
                    if escolhido.hp > 0:
                        aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                    else:
                        aux1 = 0
                    auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                    if atq.efetivo(escolhido) == 2:
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra('foi super efetivo'), batalha, janela)
                    elif atq.efetivo(escolhido) == 0.5:
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra('nao foi muito efetivo'), batalha, janela) 
                else:
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    rodarpalavra(palavra(f'atk de {escolhido2.nome} aumentou'), batalha, janela)
                    sup2 += 1
                time.sleep(0.5)             
                verturno = True
                janela.blit(fundo, (0, 0))
                janela.blit(imagens.molde3, (0, 384))
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
                janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra 1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
                nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
                nivelcin1(janela, palavra(f'{escolhido.nivel}'))
                nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                aux2 = int(150 * (escolhido2.hp / escolhido2.hp_max)//1)
                auxhp2 = pygame.transform.scale(imagens.auxhp, (aux2, 10))
                janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                time.sleep(1)
                if escolhido.hp <= 0:
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    rodarpalavra(palavra(f'{escolhido.nome} desmaiou'), batalha, janela)
                    time.sleep(1.5)
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    time.sleep(1)
                    fainted1(janela, fundo, escolhido, escolhido2, variaveis.posx1 - 48, variaveis.posy1 - 48, imagens.altural * 1.3, selvagem, trainer, auxhp2, aux2)
                    time.sleep(1)
                    equipe1.derrotados += 1
                    equipe1.vivos -= 1
                    ################
                    if equipe1.verificar():
                        rodarpalavra(palavra('voce ficou sem cinmons'), batalha, janela)
                        equipe2.curar()
                        for j in range(len(equipe2.lista)):
                            equipe2.lista[j].hp_base += 1
                        time.sleep(1)
                        self.visual = imagens.atras
                        batalha = False
                        verturno = True
                        trainer = False
                        aviso = False
                    else:
                        morto = True
                        escolhendo = True
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
                if mov1 < len([n for n in equipe1.lista if n != '']):
                    mov1 += 1
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            if temporizador < 1:
                seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                for n in range(len(equipe1.lista)):
                    janela.blit(equipe1.lista[n].mini, (64 + n * 128 * 1.5, 400))
            if (not morto):
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            if (not morto):
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                segundo = escolhido
                auxhpc = auxhp1
                auxc = aux1
                marca = False
                if mov1 == 1 and temporizador == 2:
                    mov1 = mov2 = 1
                    if equipe1.lista[0].hp > 0 and escolhido is not equipe1.lista[0]:
                        escolhido = equipe1.lista[0]
                        marca = True
                elif mov1 == 2 and temporizador == 2:
                    mov1 = mov2 = 1
                    if equipe1.lista[1].hp > 0 and escolhido is not equipe1.lista[1]:
                        escolhido = equipe1.lista[1]
                        marca = True
                elif mov1 == 3 and temporizador == 2:
                    mov1 = mov2 = 1
                    if equipe1.lista[2].hp > 0 and escolhido is not equipe1.lista[2]:
                        escolhido = equipe1.lista[2]
                        marca = True
                if temporizador == 2 and marca:
                    temporizador = 0
                    if (not morto):
                        verturno = False
                    aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                    auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                    aux1x = int(270 * (escolhido.xp / (escolhido.nivel * 10))//1)
                    auxxp1 = pygame.transform.scale(imagens.auxxp, (aux1x, 10))
                    rodarpalavra(palavra(f'Va {escolhido.nome}'), batalha, janela)
                    time.sleep(1.5)
                    comeco2(janela, fundo, selvagem, trainer, variaveis.posx1, variaveis.posy1, variaveis.posx2, variaveis.posy2, sel, escolhendo, escolhido, escolhido2,  segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto)
                    escolhendo = False
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    morto = False
                    sup = 0
                elif temporizador == 2:
                    temporizador = 0
        elif bolsa:
            #ass = input()
            ataques = False
            if tecla[pygame.K_BACKSPACE] and escolhido.hp > 0:
                bolsa = False
                mov1 = 2
                mov2 = 1
            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:# or ass == 'a':
                if mov1 > 1:
                    mov1 -= 1
            elif tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:# or ass == 'd':
                if mov1 < vu:
                    mov1 += 1
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
            janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
            janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
            janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
            if temporizador < 1:
                seta(mov1, mov2, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
                vu = 0
                for n in mochila.listaDeles:
                    if len([n for n in mochila.listaDeles]) > 0:
                        janela.blit(n, (64 + (vu * 128 * 1.5), 400))
                        vu += 1
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                if mov1 == 1 and temporizador == 2:
                    mov1 = mov2 = 1
                    temporizador = 0
                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                    rodarpalavra(palavra('Voce nao pode fazer isso'), batalha, janela)
                    time.sleep(1)
                elif mov1 == 2 and temporizador == 2:
                    mov1 = mov2 = 1
                    temporizador = 0
                    if mochila.listaDeQtd[1] > 0:
                        if escolhido.hp < escolhido.hp_max:
                            for i in range(40):
                                if escolhido.hp < escolhido.hp_max:
                                    escolhido.hp += 0.25
                                    aux1 = int(150 * (escolhido.hp / escolhido.hp_max)//1)
                                    auxhp1 = pygame.transform.scale(imagens.auxhp, (aux1, 10))
                                    terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                                    pygame.display.update()
                                    time.sleep(0.05)
                            mochila.listaDeQtd[1] -= 1
                            rodarpalavra(palavra(f'{escolhido.nome} recuperou hp'),batalha, janela)
                            verturno = False
                            bolsa = False
                        else:
                            terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                            rodarpalavra(palavra(f'{escolhido.nome} hp cheio'),batalha, janela)
                            time.sleep(1)
                    else:
                        terminal(janela, escolhido, fundo, escolhido2, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1)
                        rodarpalavra(palavra(f'voce nao tem potions'),batalha, janela)
                        time.sleep(1)

        time.sleep(0.1)
        pygame.display.update()
    return batalha, trainer, aviso, rodando




def encontrarcin():
    chance = [1, 2, 3]
    aleatorio = random.choice(chance)
    if aleatorio == 1:
        return True, True
    else:
        return False, False
    

def encontrar_treinador(posx, posy, listaT, cenario):
    treinador = ''
    if cenario in listaT:
        if cenario == imagens.cenario5:
            if posx == 576 and 256 <= posy <= 448:
                treinador = 'treinador1'
                return treinador, True
            elif posx == 640 and 64 <= posy <= 128:
                treinador = 'treinador2'
                return treinador, True
        if cenario == imagens.cenario9:
            if posx == 384 and 64 <= posy <= 128:
                treinador = 'treinador3'
                return treinador, True
            elif posx == 512 and 64 <= posy <= 128:
                treinador = 'treinador4'
                return treinador, True
    return treinador, False

def avisoCombate(janela, treinador):
    limpar(janela, imagens.balaofala)
    batalha = False
    if treinador.nome == 'ewerton':
        rodarpalavra(palavra('sinta minha aura'), batalha, janela)
        time.sleep(1)
    elif treinador.nome == 'jl':
        rodarpalavra(palavra('nao grita'), batalha, janela)
        time.sleep(1)
    elif treinador.nome == 'daniel':
        rodarpalavra(palavra('voce nao tem aura mano'), batalha, janela)
        time.sleep(1)
    elif treinador.nome == 'jose':
        rodarpalavra(palavra('cabra da peste'), batalha, janela)
        time.sleep(1)

def menu(janela, equipe, balao, mov1a, escolhendo, bolsa, tecla, marca):
    time1 = False
    if balao:
        janela.blit(imagens.menu1, (848, 240))
        soun(palavra('time'), 'time', janela)
        soun(palavra('bolsa'), 'bolsa', janela)
        seta(1, mov1a, janela, imagens.setinha, False, escolhendo, bolsa, balao)
        if tecla[pygame.K_UP]:# or ass == 'a':
            if mov1a > 1:
                mov1a -= 1
        elif tecla[pygame.K_DOWN]:# or ass == 'b':
            if mov1a < 2:
                mov1a += 1 
        if mov1a == 1:
            if tecla[pygame.K_SPACE]:
                balao = False
                marca = True
                time1 = True
        elif mov1a == 2:
            if tecla[pygame.K_BACKSPACE]:
                balao = False
        if tecla[pygame.K_BACKSPACE]:
                balao = False
                marca = True
                time.sleep(0.1)
    if (not marca):
        balao = True
    else:
        marca = False
    return balao, mov1a, time1


def menu_time(janela, equipe, mov1, mov2, escolhendo, bolsa, balao):
    time.sleep(0.2)
    rodando = True
    temporizador  = 0
    escolhendo = True
    selecionado = ''
    selecao1 = False
    selecao2 = False
    mov1a = 1
    while rodando and escolhendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        tecla = pygame.key.get_pressed()
        janela.blit(imagens.molde3, (0, 384))
        seta(mov1, mov2, janela, imagens.setinha, False, True, bolsa, balao)
        if selecao1:
            janela.blit(imagens.menu1, (848, 240))
            soun(palavra('troca'), 'troca', janela)
            soun(palavra('sair'), 'sair', janela)
            seta(1, mov1a, janela, imagens.setinha, False, False, bolsa, True)
        if tecla[pygame.K_BACKSPACE]:
            escolhendo = False
            mov1 = 1
            mov2 = 2
        if (not selecao1) or selecao2:
            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]:# or ass == 'a':
                if mov1 > 1:
                    mov1 -= 1
            elif tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:# or ass == 'd':
                if mov1 < len([n for n in equipe.lista if n != '']):
                    mov1 += 1
        elif selecao1 and (not selecao2):
            if tecla[pygame.K_UP]:
                if mov1a > 1:
                    mov1a -= 1
            elif tecla[pygame.K_DOWN]:
                if mov1a < 2:
                    mov1a += 1
        for n in range(len(equipe.lista)):
            janela.blit(equipe.lista[n].mini, (64 + n * 128 * 1.5, 400))
        pygame.display.update()
        if (not selecao1) and (not selecao2):
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                marca = False
                if mov1 == 1 and temporizador == 2:
                    selecionado = equipe.lista[0]
                    marca = selecao1 = True
                elif mov1 == 2 and temporizador == 2:
                    selecionado = equipe.lista[1]
                    marca = selecao1 = True
                elif mov1 == 3 and temporizador == 2:
                    selecionado = equipe.lista[2]
                    marca = selecao1 = True
                if temporizador == 2 and marca:
                    temporizador = 0
                elif temporizador == 2:
                    temporizador = 0
                time.sleep(0.05)
        elif selecao1 and (not selecao2):
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                marca = False
                if mov1a == 1 and temporizador == 2:
                    if len(equipe.lista) > 1:
                        selecao2 = True
                        selecao1 = False
                elif mov1a == 2 and temporizador == 2:
                    selecionado = ''
                    selecao1 = False
                    escolhendo = False
                if temporizador == 2 and marca:
                    temporizador = 0
                elif temporizador == 2:
                    temporizador = 0
        elif selecao2:
            for n in range(len(equipe.lista)):
                janela.blit(equipe.lista[n].mini, (64 + n * 128 * 1.5, 400))
        pygame.display.update()
        if (not selecao1) and selecao2:
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                marca = False
                if mov1 == 1 and temporizador == 2:
                    mov1 = mov2 = 1
                    if selecionado is not equipe.lista[0]:
                        if selecionado is equipe.lista[1]:
                            equipe.lista[0], equipe.lista[1] = equipe.lista[1], equipe.lista[0]
                        elif len(equipe.lista) > 2  and selecionado is equipe.lista[2]:
                            equipe.lista[0], equipe.lista[2] = equipe.lista[2], equipe.lista[0]
                        escolhendo = False
                elif mov1 == 2 and temporizador == 2:
                    mov1 = mov2 = 1
                    if selecionado is not equipe.lista[1]:
                        if selecionado is equipe.lista[0]:
                            equipe.lista[0], equipe.lista[1] = equipe.lista[1], equipe.lista[0]
                        elif len(equipe.lista) > 2 and selecionado is equipe.lista[2]:
                            equipe.lista[1], equipe.lista[2] = equipe.lista[2], equipe.lista[1]
                        escolhendo = False
                elif mov1 == 3 and temporizador == 2:
                    mov1 = mov2 = 1
                    if selecionado is not equipe.lista[2]:
                        if selecionado is equipe.lista[0]:
                            equipe.lista[0], equipe.lista[2] = equipe.lista[2], equipe.lista[0]
                        elif len(equipe.lista) > 2 and selecionado is equipe.lista[1]:
                            equipe.lista[1], equipe.lista[2] = equipe.lista[2], equipe.lista[1]
                    escolhendo = False
                if temporizador == 2 and marca:
                    temporizador = 0
                elif temporizador == 2:
                    temporizador = 0

        time.sleep(0.1)
        

    return rodando, False





def palavra(palavra):
    global a, b, c, d, e, f, g, h, i, j, k, l, m, eni, o, p, q, r, s, t, u, v, x, y, z

    lista = []
    for no in palavra:
        if no.lower() == 'a':
            lista.append(imagens.a)
        elif no.lower() == 'b':
            lista.append(imagens.b)
        elif no.lower() == 'c':
            lista.append(imagens.c)
        elif no.lower() == 'd':
            lista.append(imagens.d)
        elif no.lower() == 'e':
            lista.append(imagens.e)
        elif no.lower() == 'f':
            lista.append(imagens.f)
        elif no.lower() == 'g':
            lista.append(imagens.g)
        elif no.lower() == 'h':
            lista.append(imagens.h)
        elif no.lower() == 'i':
            lista.append(imagens.i)
        elif no.lower() == 'j':
            lista.append(imagens.j)
        elif no.lower() == 'k':
            lista.append(imagens.k)
        elif no.lower() == 'l':
            lista.append(imagens.l)
        elif no.lower() == 'm':
            lista.append(imagens.m)
        elif no.lower() == 'n':
            lista.append(imagens.eni)
        elif no.lower() == 'o':
            lista.append(imagens.o)
        elif no.lower() == 'p':
            lista.append(imagens.p)
        elif no.lower() == 'q':
            lista.append(imagens.q)
        elif no.lower() == 'r':
            lista.append(imagens.r)
        elif no.lower() == 's':
            lista.append(imagens.s)
        elif no.lower() == 't':
            lista.append(imagens.t)
        elif no.lower() == 'u':
            lista.append(imagens.u)
        elif no.lower() == 'v':
            lista.append(imagens.v)
        elif no.lower() == 'w':
            lista.append(imagens.w)
        elif no.lower() == 'x':
            lista.append(imagens.x)
        elif no.lower() == 'y':
            lista.append(imagens.y)
        elif no.lower() == 'z':
            lista.append(imagens.z)
        elif no == ' ':
            lista.append(' ')
        elif no == '1':
            lista.append(imagens.um)
        elif no == '2':
            lista.append(imagens.dois)
        elif no == '3':
            lista.append(imagens.tres)
        elif no == '4':
            lista.append(imagens.quatro)
        elif no == '5':
            lista.append(imagens.cinco)
        elif no == '6':
            lista.append(imagens.seis)
        elif no == '7':
            lista.append(imagens.sete)
        elif no == '8':
            lista.append(imagens.oito)
        elif no == '9':
            lista.append(imagens.nove)
        elif no == '0':
            lista.append(imagens.zero)
    return lista

def rodarpalavra(lista, batalha, janela):
    if batalha:
        aux = 0
    else:
        aux = 8
    for n in lista:
        if n != ' ':
            janela.blit(n, (64 + aux, 400))
            aux += imagens.largural + 8
        else:
            aux += imagens.largural + 16
        pygame.display.update()
        time.sleep(0.05)


#funções da historia
def soun(lista, palavra, janela):
    aux = 0
    if palavra == 'sim' or palavra == 'time' or palavra == ('troca') or palavra == 'buy':
        for n in lista:
            if n != ' ':
                n = pygame.transform.scale(n, (imagens.largural / 2, imagens.altural / 2))
                janela.blit(n, (896 + aux, 256))
                aux += (imagens.largural/2) + 1
            else:
                aux += (imagens.largural/2) + 2
    elif palavra == 'nao' or palavra == 'bolsa' or palavra == 'sair':
        for n in lista:
            if n != ' ':
                n = pygame.transform.scale(n, (imagens.largural / 2, imagens.altural / 2))
                janela.blit(n, (896 + aux, 328))
                aux += (imagens.largural/2) + 1
            else:
                aux += (imagens.largural/2) + 2


def limpar(janela, balaofala):
    janela.blit(balaofala, (64, 384))
    pygame.display.update()


def falarcomioda(self, posx, posy):
    if (posx == 448 and posy == 64 and self.visual == imagens.atras) or (posx == 384 and posy == 0 and self.visual == imagens.direita) or (posx == 512 and posy == 0 and self.visual == imagens.esquerda):
        return True
    else:
        return False

def inicio(mov1a, ataques, escolhendo, bolsa, balao, janela, aviso, player1, player, batalha, cenario1, marca, tecla, escolhaioda):
    escolha = ''
    if (not aviso) and falarcomioda(player1, variaveis.posx, variaveis.posy):
        aviso = escolhaioda1(janela, variaveis.posx, variaveis.posy, batalha, variaveis.gramasatual, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.listatual, variaveis.posobjatual, imagens.player, imagens.balaofala)
    if variaveis.posy == variaveis.alturap:
        marcacao = False
        if (not balao):
            if variaveis.posx == 576:
                cin1(batalha, janela, variaveis.posx, variaveis.posy, variaveis.gramasatual, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.listatual, variaveis.posobjatual, player, imagens.balaofala)
                mov1a = 1
                marcacao = True
            elif variaveis.posx == 704:
                cin2(batalha, janela, variaveis.posx, variaveis.posy, variaveis.gramasatual, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.listatual, variaveis.posobjatual, player, imagens.balaofala)
                mov1a = 1
                marcacao = True
            elif variaveis.posx == 832:
                cin3(batalha, janela, variaveis.posx, variaveis.posy, variaveis.gramasatual, variaveis.gramasxatual, variaveis.gramasyatual, variaveis.listatual, variaveis.posobjatual, player, imagens.balaofala)
                mov1a = 1
                marcacao = True
        if balao:
            janela.blit(imagens.menu1, (848, 240))
            soun(palavra('sim'), 'sim', janela)
            soun(palavra('nao'), 'nao', janela)
            seta(1, mov1a, janela, imagens.setinha, ataques, escolhendo, bolsa, balao)
            if tecla[pygame.K_UP]:# or ass == 'a':
                if mov1a > 1:
                    mov1a -= 1
            elif tecla[pygame.K_DOWN]:# or ass == 'b':
                if mov1a < 2:
                    mov1a += 1 
            if mov1a == 1:
                if tecla[pygame.K_SPACE]:
                    escolhaioda = True
                    balao = False
                    if variaveis.posx == 576:
                        escolha = cimons.lupi
                        variaveis.lista4 = (imagens.ioda, imagens.mesa, imagens.crachabol, imagens.crachabol, imagens.player)
                        variaveis.posobj4 = ((448, 0), (576, 0), (715, 20), (843, 20))
                        variaveis.listaobj4 = (objetos.ioda4, objetos.mesa4, objetos.crachabol2_4, objetos.crachabol3_4)
                    elif variaveis.posx == 704:
                        escolha = cimons.rath
                        variaveis.lista4 = (imagens.ioda, imagens.mesa, imagens.crachabol, imagens.crachabol, imagens.player)
                        variaveis.posobj4 = ((448, 0), (576, 0), (587, 20),(843, 20))
                        variaveis.listaobj4 = (objetos.ioda4, objetos.mesa4, objetos.crachabol1_4, objetos.crachabol3_4)
                    elif variaveis.posx == 832:
                        escolha = cimons.goku
                        variaveis.lista4 = (imagens.ioda, imagens.mesa, imagens.crachabol, imagens.crachabol, imagens.player)
                        variaveis.posobj4 = ((448, 0), (576, 0), (587, 20),(715, 20))
                        variaveis.listaobj4 = (objetos.ioda4, objetos.mesa4, objetos.crachabol1_4, objetos.crachabol2_4)
                    variaveis.listatual = variaveis.lista4
                    variaveis.posobjatual = variaveis.posobj4
            elif mov1a == 2:
                if tecla[pygame.K_SPACE]:
                    balao = False
                    marca = True
                    time.sleep(0.1)
        if (not marca) and marcacao:
            balao = True
        else:
            marca = False
    return escolhaioda, escolha, balao, mov1a






def escolhaioda1(janela, posx, posy, batalha, gramasatual, gramasxatual, gramasyatual, listatual, posobjatual, player, balaofala):
    limpar(janela, balaofala)
    rodarpalavra(palavra('ola seja bem vindo'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('sou o professor ioda'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('esse e o laboratorio cin'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('onde a jornada dos cins comeca'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('o que'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('quer ser um cin'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('pois bem'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('darei a voce 2 crachabolas'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    rodarpalavra(palavra('e podera escolher seu cinmon'), batalha, janela)
    time.sleep(2)
    limpar(janela, balaofala)
    rodarpalavra(palavra('va e se torne um cin'), batalha, janela)
    time.sleep(1.5)
    limpar(janela, balaofala)
    return True

def cin1(batalha, janela, posx, posy, gramasatual, gramasxatual, gramasyatual, listatual, posobjatual, player, balaofala):
    limpar(janela, balaofala)
    rodarpalavra(palavra('esse e lupi'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('do tipo normal'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('deseja esse'), batalha, janela)

def cin2(batalha, janela, posx, posy, gramasatual, gramasxatual, gramasyatual, listatual, posobjatual, player, balaofala):
    limpar(janela, balaofala)
    rodarpalavra(palavra('esse e rath'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('do tipo escuridao'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('deseja esse'), batalha, janela)

def cin3(batalha, janela, posx, posy, gramasatual, gramasxatual, gramasyatual, listatual, posobjatual, player, balaofala):
    limpar(janela, balaofala)
    rodarpalavra(palavra('esse e goku'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('do tipo lutador'), batalha, janela)
    time.sleep(1)
    limpar(janela, balaofala)
    rodarpalavra(palavra('deseja esse'), batalha, janela)



#centro poke

def curarfala(janela, player, batalha, posx, posy):
    limpar(janela, imagens.balaofala)
    rodarpalavra(palavra('ola sou o enfermeiro jailson'), batalha, janela)
    time.sleep(1)
    limpar(janela, imagens.balaofala)
    rodarpalavra(palavra('irei curar seus cinmons'), batalha, janela)
    time.sleep(1)
    limpar(janela, imagens.balaofala)
    rodarpalavra(palavra('so um instante'), batalha, janela)
    time.sleep(2)
    limpar(janela, imagens.balaofala)
    rodarpalavra(palavra('pronto seus cinmons estao ok'), batalha, janela)
    time.sleep(1)

#loja
def lojafala(janela, batalha):
    limpar(janela, imagens.balaofala)
    rodarpalavra(palavra('ola sou o vendedor jailson'), batalha, janela)
    time.sleep(1)
    limpar(janela, imagens.balaofala)
    rodarpalavra(palavra('voce quer comprar aqui'), batalha, janela)
    time.sleep(1)

def sounloja(janela, balao, tecla, marca, mov1a):
    menuloja = False
    if balao:
        janela.blit(imagens.menu1, (848, 240))
        soun(palavra('sim'), 'sim', janela)
        soun(palavra('nao'), 'nao', janela)
        seta(1, mov1a, janela, imagens.setinha, False, False, False, balao)
        if tecla[pygame.K_UP]:# or ass == 'a':
            if mov1a > 1:
                mov1a -= 1
        elif tecla[pygame.K_DOWN]:# or ass == 'b':
            if mov1a < 2:
                mov1a += 1 
        if mov1a == 1:
            if tecla[pygame.K_SPACE]:
                menuloja = True
                balao = False
                marca = True
        elif mov1a == 2:
            if tecla[pygame.K_SPACE]:
                balao = False
                marca = True
                mov1a = 1
                time.sleep(0.1)
    if (not marca):
        balao = True
    else:
        marca = False 
    return balao, menuloja, mov1a

def menuloja(janela, mov1, menuloja, lista, mochila):
    time.sleep(0.2)
    rodando = True
    temporizador  = 0
    menuloja = True
    selecionado = ''
    selecao1 = False
    selecao2 = False
    mov1a = 1
    while rodando and menuloja:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        tecla = pygame.key.get_pressed()
        janela.blit(imagens.menuloja, (0, 0))
        aux = 0
        for t in range(len(palavra(f'{mochila.dinheiro}'))):
            numero = pygame.transform.scale(palavra(f'{mochila.dinheiro}')[t], (12, 37))
            janela.blit(numero, (40 + aux, 250))
            aux += imagens.largural + 1
        setaloja(mov1, janela, imagens.setinha)
        if selecao1:
            janela.blit(imagens.menu1, (848, 240))
            soun(palavra('buy'), 'buy', janela)
            soun(palavra('sair'), 'sair', janela)
            seta(1, mov1a, janela, imagens.setinha, False, False, False, True)
        if tecla[pygame.K_BACKSPACE]:
            menuloja = False
            mov1 = 1
        if (not selecao1):
            if tecla[pygame.K_UP] or tecla[pygame.K_a]:# or ass == 'a':
                if mov1 > 1:
                    mov1 -= 1
            elif tecla[pygame.K_DOWN] or tecla[pygame.K_d]:# or ass == 'd':
                if mov1 < 2:
                    mov1 += 1
        elif selecao1:
            if tecla[pygame.K_UP]:
                if mov1a > 1:
                    mov1a -= 1
            elif tecla[pygame.K_DOWN]:
                if mov1a < 2:
                    mov1a += 1
        for n in range(len(lista)):
            janela.blit(lista[n], (128, 16 + n * 64))
        pygame.display.update()
        if (not selecao1):
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                marca = False
                if mov1 == 1 and temporizador == 2:
                    selecionado = 'crachabola'
                    marca = selecao1 = True
                elif mov1 == 2 and temporizador == 2:
                    selecionado = 'potion'
                    marca = selecao1 = True
                if temporizador == 2 and marca:
                    temporizador = 0
                elif temporizador == 2:
                    temporizador = 0
        elif selecao1 and (not selecao2):
            if tecla[pygame.K_SPACE] or temporizador == 1:
                temporizador += 1
                marca = False
                if mov1a == 1 and temporizador == 2:
                    selecao2 = True
                elif mov1a == 2 and temporizador == 2:
                    menuloja = False
                if temporizador == 2 and marca:
                    temporizador = 0
                elif temporizador == 2:
                    temporizador = 0
        elif selecao1 and selecao2:
            comprou = mochila.comprar(selecionado)
            if comprou:
                limpar(janela, imagens.balaofala)
                rodarpalavra(palavra('volte sempre'), False, janela)
                time.sleep(1)
            else:
                limpar(janela, imagens.balaofala)
                rodarpalavra(palavra('nao tem dinheiro suficiente'), False, janela)
                time.sleep(1)
            menuloja = False
        pygame.display.update()

        time.sleep(0.1)
        

    return rodando, False

def setaloja(mov1, janela, setinha):
    posy = 32 + 64 * (mov1 - 1)
    posx = 16
    janela.blit(setinha, (posx, posy))

#funções de treinador


#funções de batalha

def nomecin1(janela, lista, nome):
    aux = 0
    for e, n in enumerate(lista):
        if n != ' ':
            n = pygame.transform.scale(n, (imagens.largural / 2, imagens.altural / 2))
            janela.blit(n, (variaveis.posx2 + variaveis.xb + aux/1.5 + 8, variaveis.posy1 + variaveis.yb/2 + 8 ))
            aux += imagens.largural + 1
        else:
            aux += imagens.largural + 2

def nomecin2(janela, lista, nome):
    aux = 0
    for e, n in enumerate(lista):
        if n != ' ':
            n = pygame.transform.scale(n, (imagens.largural / 2, imagens.altural / 2))
            janela.blit(n, (variaveis.posx1 - 40 + variaveis.xb + aux/1.5, variaveis.posy2 - 48 ))
            aux += imagens.largural + 1
        else:
            aux += imagens.largural + 2

def nivelcin1(janela, lista):
    aux = 0
    for n in lista:
        n = pygame.transform.scale(n, (imagens.largural / 2, imagens.altural / 2))
        janela.blit(n, (variaveis.posx2 + variaveis.xb * 30 + aux/1.5 + 8, variaveis.posy1 + variaveis.yb/2 + 12 ))
        aux += imagens.largural + 1

def nivelcin2(janela, lista):
    aux = 0
    for n in lista:
        n = pygame.transform.scale(n, (imagens.largural / 2, imagens.altural / 2))
        janela.blit(n, (variaveis.posx1 - 40 + variaveis.xb * 30 + aux/1.5, variaveis.posy2 - 44))
        aux += imagens.largural + 1


def terminal(janela, escolhido, fundo, sel, auxhp1, aux1, auxhp2, aux2, capturado, aviso, aviso2, aux1x, auxxp1):
    janela.blit(fundo, (0, 0))
    janela.blit(imagens.molde3, (0, 384))
    if aviso:
        janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
        if sel.hp_base > 0:
            if (not capturado):
                if (not aviso2):
                    janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            else:
                janela.blit(imagens.crachabola, (variaveis.posx2 - imagens.largural + 63, variaveis.posy2 - imagens.altural + 124))
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nomecin2(janela, palavra(sel.nome), sel.nome)
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nivelcin2(janela, palavra(f'{sel.nivel}'))
        if escolhido.hp > 0:
            janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
        if sel.hp > 0:
            janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
        janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        


def comeco1(janela, fundo, selvagem, posx2, posy2, sel, aviso, aviso2, trainer, escolhido, escolhido2, auxhp1, auxhp2, aux1, aux2, aux1x, auxxp1):
    if selvagem:
        aux2 = variaveis.largura + variaveis.padraoL * 1.5
        while aux2 >= posx2:
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            janela.blit(sel.imagemf, (aux2 - imagens.largural - 32, posy2 - imagens.altural - 32))
            aux2 -= 12
            time.sleep(0.025)
            pygame.display.update()

    elif trainer:
        auxz = 64
        auxLz = posx2 + 32  #posx2 + 64
        auxAz = posy2 + 72  #posy2 + 120
        janela.blit(imagens.crachabola, (auxLz, auxAz))
        pygame.display.update()
        time.sleep(0.5)

        while auxz > 0:
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            if aviso2:
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(imagens.barra, (posx2, variaveis.posy1 + 32))     #barra 1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, posy2 - 64))
                janela.blit(auxhp1, (posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxhp2, (variaveis.posx1 + 84, posy2 - 11))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
                nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
                nivelcin1(janela, palavra(f'{escolhido.nivel}'))
                nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
            auxz -= 4
            auxLz += 2
            auxAz += 3
            save = pygame.transform.scale(imagens.crachabola, (auxz * 0.75, auxz))
            janela.blit(save, (auxLz, auxAz))
            time.sleep(0.01)
            pygame.display.update()

        aux2c = 6
        auxL = variaveis.posx2 + 57.2 #posx2 - largural - 32
        auxA = variaveis.posy2 + 99.4 #posy2 - altural - 32
        while aux2c < imagens.padraoA * 1.5:
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            if aviso2:
                janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
                janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
                janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
                janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
                janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
                janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
                nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
                nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
                nivelcin1(janela, palavra(f'{escolhido.nivel}'))
                nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
            aux2c += 6
            auxL -= 2.8
            if abs(auxL - 608) < 1 + 2.8:
                auxL = 608
            auxA -= 4.6
            if abs(auxA - (-8)) < 1 + 4.6:
                auxA = -8
            save = pygame.transform.scale(escolhido2.imagemf, (aux2c, aux2c))
            janela.blit(save, (auxL, auxA))
            pygame.display.update()

def comeco2(janela, fundo, selvagem, trainer, posx1, posy1, posx2, posy2, sel, escolhendo, escolhido, escolhido2, segundo, auxhp1, auxhp2, aux1, aux2, auxhpc, auxc, morto):
    auxz = 64
    auxLz = variaveis.posx1 - 48 + (variaveis.padraoL * 0.6) - (variaveis.largurap//3) + 20
    auxAz = variaveis.posy1 + (variaveis.padraoL * 0.6) - (variaveis.alturap//3) + 8
    if escolhendo and (not morto):
        auxy = variaveis.padraoA * 1.5
        auxL = posx1 - 80 #
        auxA = posy1 - 80 #
        while auxy > 0:
            janela.blit(fundo, (0, 0))
            janela.blit(imagens.molde3, (0, 384))
            if escolhendo:
                janela.blit(imagens.barra, (posx2, posy1 + 32))     #barra 1
                janela.blit(imagens.barra, (posx1 - 48, posy2 - 64))
                janela.blit(auxhpc, (posx2 + 132, posy1 + 53 + 32))
                if selvagem:
                    janela.blit(auxhp2, (posx1 + 84, posy2 - 11))
                elif trainer:
                    janela.blit(auxhp2, (posx1 + 84, posy2 - 11))
                nomecin1(janela, palavra(segundo.nome), segundo.nome)
                nivelcin1(janela, palavra(f'{segundo.nivel}'))
                if selvagem:
                    nomecin2(janela, palavra(sel.nome), sel.nome)
                    nivelcin2(janela, palavra(f'{sel.nivel}'))
                elif trainer:
                    nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
                    nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
            if selvagem:
                janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            elif trainer:
                janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
            auxy -= 8
            auxL += 5.3
            if abs(auxL - 271) < 1:
                auxL = 271
            auxA += 7.03
            if abs(auxA - 355) < 1:
                auxA = 355
            save = pygame.transform.scale(segundo.imagemc, (auxy, auxy))
            janela.blit(save, (auxL, auxA))
            pygame.display.update()

            time.sleep(0.01)
            pygame.display.update()
    time.sleep(0.3)
    janela.blit(imagens.crachabola, (auxLz, auxAz))
    pygame.display.update()

    time.sleep(1)

    while auxz > 0:
        janela.blit(fundo, (0, 0))
        janela.blit(imagens.molde3, (0, 384))
        if selvagem:
                janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        elif trainer:
                janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        if escolhendo:
            janela.blit(imagens.barra, (posx2, posy1 + 32))     #barra 1
            janela.blit(imagens.barra, (posx1 - 48, posy2 - 64))
            janela.blit(auxhp1, (posx2 + 132, posy1 + 53 + 32))
            if selvagem:
                janela.blit(auxhp2, (posx1 + 84, posy2 - 11))
            elif trainer:
                janela.blit(auxhp2, (posx1 + 84, posy2 - 11))
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))
            if selvagem:
                nomecin2(janela, palavra(sel.nome), sel.nome)
                nivelcin2(janela, palavra(f'{sel.nivel}'))
            elif trainer:
                nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
                nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
        auxz -= 4
        auxLz += 2
        auxAz += 3

        save = pygame.transform.scale(imagens.crachabola, (auxz * 0.75, auxz))
        janela.blit(save, (auxLz, auxAz))
        pygame.display.update()

        time.sleep(0.005)
        pygame.display.update()
    
    auxy = 0
    auxL = 271 #posx1 - 80
    auxA = 355 #posy1 - 80
    while auxy < variaveis.padraoA * 1.5:
        janela.blit(fundo, (0, 0))
        janela.blit(imagens.molde3, (0, 384))
        if escolhendo:
            janela.blit(imagens.barra, (posx2, posy1 + 32))     #barra 1
            janela.blit(imagens.barra, (posx1 - 48, posy2 - 64))
            janela.blit(auxhp1, (posx2 + 132, posy1 + 53 + 32))
            if selvagem:
                janela.blit(auxhp2, (posx1 + 84, posy2 - 11))
            elif trainer:
                janela.blit(auxhp2, (posx1 + 84, posy2 - 11)) 
            nomecin1(janela, palavra(escolhido.nome), escolhido.nome)   
            nivelcin1(janela, palavra(f'{escolhido.nivel}'))   
            if selvagem:
                nomecin2(janela, palavra(sel.nome), sel.nome)
                nivelcin2(janela, palavra(f'{sel.nivel}'))
            elif trainer:
                nomecin2(janela, palavra(escolhido2.nome), escolhido2.nome)
                nivelcin2(janela, palavra(f'{escolhido2.nivel}'))
        if selvagem:
                janela.blit(sel.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        elif trainer:
                janela.blit(escolhido2.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        auxy += 8
        auxL -= 5.3
        if abs(auxL - (variaveis.posx1 - 80)) < 1:
            auxL = variaveis.posx1 - 80
        auxA -= 7.03
        if abs(auxA - (variaveis.posy1 - 80)) < 1:
            auxA = variaveis.posy1 - 80
        save = pygame.transform.scale(escolhido.imagemc, (auxy, auxy))
        janela.blit(save, (auxL, auxA))
        pygame.display.update()

        time.sleep(0.005)
        pygame.display.update()
    
def fainted2(janela, fundo, escolhido, inimigo, posx, posy, tamanho, selvagem, trainer, auxhp1, aux1, aux1x, auxxp1):
    aux = posy
    while aux <= variaveis.altura + tamanho:
        aux += 32
        janela.blit(fundo, (0, 0))
        janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, variaveis.posy1 - 80))
        janela.blit(inimigo.imagemf, (posx, aux))
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nomecin2(janela, palavra(inimigo.nome), inimigo.nome)
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nivelcin2(janela, palavra(f'{inimigo.nivel}'))
        janela.blit(auxhp1, (variaveis.posx2 + 132, variaveis.posy1 + 53 + 32))
        janela.blit(auxxp1, (variaveis.posx2 + 30, variaveis.posy1 + 116))
        janela.blit(imagens.molde3, (0, 384))
        pygame.display.update()

def fainted1(janela, fundo, escolhido, inimigo, posx, posy, tamanho, selvagem, trainer, auxhp2, aux2):
    aux = posy
    while aux <= variaveis.altura + tamanho:
        aux += 32
        janela.blit(fundo, (0, 0))
        janela.blit(inimigo.imagemf, (variaveis.posx2 - imagens.largural - 32, variaveis.posy2 - imagens.altural - 32))
        janela.blit(escolhido.imagemc, (variaveis.posx1 - 80, aux - 80))     
        janela.blit(imagens.barra, (variaveis.posx2, variaveis.posy1 + 32))     #barra1
        janela.blit(imagens.barra, (variaveis.posx1 - 48, variaveis.posy2 - 64))          #barra 2
        nomecin1(janela, palavra(escolhido.nome), escolhido.nome)
        nivelcin1(janela, palavra(f'{escolhido.nivel}'))
        nomecin2(janela, palavra(inimigo.nome), inimigo.nome)
        nivelcin2(janela, palavra(f'{inimigo.nivel}'))
        janela.blit(auxhp2, (variaveis.posx1 + 84, variaveis.posy2 - 11))
        janela.blit(imagens.molde3, (0, 384))
        pygame.display.update()

def seta(mov1, mov2, janela, setinha, ataques, escolhendo, bolsa, balao):
    if (not ataques) and (not escolhendo) and (not bolsa) and (not balao):
        if mov1 == 1:
            posx1 = 640
        elif mov1 == 2:
            posx1 = 816
        if mov2 == 1:
            posy1 = 400
        elif mov2 == 2:
            posy1 = 456
    elif ataques:
        if mov1 == 1:
            posx1 = 16
        elif mov1 == 2:
            posx1 = 318
        if mov2 == 1:
            posy1 = 400
        elif mov2 == 2:
            posy1 = 456
    elif bolsa or escolhendo:
        if mov1 == 1:
            posx1 = 16
        elif mov1 == 2:
            posx1 = 192
        elif mov1 == 3:
            posx1 = 368
        posy1 = 416
    elif balao:
        if mov2 == 1:
            posy1 = 248
        elif mov2 == 2:
            posy1 = 320
        posx1 = 856


    janela.blit(setinha, (posx1, posy1))

def golpes(escolhido, janela):
    n = [palavra(escolhido.ataques[f'ataque{j + 1}'].nome) for j in range(len(escolhido.ataques))]
    au = 0
    for ka in n:
        auxb = 0
        au += 1
        for ir in ka:
            if au <= 2:
                posy3 = 400
            else:
                posy3 = 456
            if au == 1 or au == 3:
                posx3 = 56
            else:
                posx3 = 368
            if ir != ' ':
                    janela.blit(ir, (posx3 + auxb, posy3))
                    auxb += imagens.largural + 8
            else:
                auxb += imagens.largural + 16



#funções de troca de cenario
def ircenario1(self, posobj1, posobjatual, fundo, gramasxatual, gramasyatual, gramas4_atual, gramas1, gramasx1, gramasy1, posy, listatual, listaobjatual, lista1, listaobj1, gramasatual, cenario2, cenario3):
    posobjatual = posobj1
    listatual = lista1
    gramasatual = gramas1
    gramasxatual = gramasx1
    gramasyatual = gramasy1
    gramas4_atual = []
    for n in range(len(gramasx1)):
        gramas4_atual.append(gramasatual[n].get_rect())
        gramas4_atual[n].x = gramasx1[n]
        gramas4_atual[n].y = gramasy1[n]
    listaobjatual = listaobj1

    if cenario2:
        self.visual = imagens.frente
        fundo = imagens.cenario3
        return fundo, posobjatual, listatual, gramasatual, gramasxatual, gramasyatual, gramas4_atual, listaobjatual, variaveis.posx, 256
    elif cenario3:
        self.visual = imagens.esquerda
        fundo = imagens. cenario3
        return fundo, posobjatual, listatual, gramasatual, gramasxatual, gramasyatual, gramas4_atual, listaobjatual, variaveis.largura - variaveis.largurap, posy

def ircenario2(self, posx, posy, posobjatual, posobj2, listatual, lista2, listaobjatual, listaobj2, fundo):
    posobjatual = posobj2
    listatual = lista2
    listaobjatual = listaobj2
    variaveis.gramasatual = ()
    variaveis.gramasxatual = ()
    variaveis.gramasyatual = ()
    variaveis.gramas4_atual = []
    self.visual = imagens.atras
    fundo = imagens.cenario2
    self.posicao = (posx, 448)
    return posobjatual, listatual, listaobjatual, fundo, posx, 448

def ircenario3(self, posx, posy, posobjatual, posobj3, listatual, lista3, listaobjatual, listaobj3, fundo):
    posobjatual = posobj3
    listatual = lista3
    listaobjatual = listaobj3
    variaveis.gramasatual = ()
    variaveis.gramasxatual = ()
    variaveis.gramasyatual = ()
    variaveis.gramas4_atual = []
    if fundo == imagens.cenario1:
        self.visual = imagens.direita
        fundo = imagens.cenario3
        self.posicao = (0, posy)
        return posobjatual, listatual, listaobjatual, fundo, 0, posy
    elif fundo == imagens.cenario4 or fundo == imagens.cenario5:
        self.visual = imagens.frente
        if fundo == imagens.cenario4:
            fundo = imagens.cenario3
            self.posicao = (posx, 320)
            return posobjatual, listatual, listaobjatual, fundo, posx, 320
        elif fundo == imagens.cenario5:
            fundo = imagens.cenario3
            self.posicao = (posx, 0)
            return posobjatual, listatual, listaobjatual, fundo, posx, 0

def ircenario4(self, posx, posy, posobjatual, posobj4, listatual, lista4, listaobjatual, listaobj4, fundo):
    posobjatual = posobj4
    listatual = lista4
    listaobjatual = listaobj4
    variaveis.gramasatual = ()
    variaveis.gramasxatual = ()
    variaveis.gramasyatual = ()
    variaveis.gramas4_atual = []
    self.visual = imagens.atras
    fundo = imagens.cenario4
    self.posicao = (posx, 0)
    return posobjatual, listatual, listaobjatual, fundo, posx, 448

def ircenario5(self, posobj5, posobjatual, fundo, posy, listatual, listaobjatual, lista5, listaobj5, cenario3, cenario6):
    posobjatual = posobj5
    listatual = lista5
    listaobjatual = listaobj5
    variaveis.gramasatual = variaveis.gramas5
    variaveis.gramasxatual = variaveis.gramasx5
    variaveis.gramasyatual = variaveis.gramasy5
    variaveis.gramas4_atual = []
    for n in range(len(variaveis.gramasx5)):
        variaveis.gramas4_atual.append(variaveis.gramasatual[n].get_rect())
        variaveis.gramas4_atual[n].x = variaveis.gramasx5[n]
        variaveis.gramas4_atual[n].y = variaveis.gramasy5[n]
    if fundo == imagens.cenario3:
        self.visual = imagens.atras
        fundo = imagens.cenario5
        self.posicao = (variaveis.posx, 448)
        return posobjatual, listatual, listaobjatual, fundo, variaveis.posx, 448
    elif fundo == imagens.cenario6:
        self.visual = imagens.esquerda
        fundo = imagens.cenario5
        self.posicao = (960, posy)
        return posobjatual, listatual, listaobjatual, fundo, 960, posy

def ircenario6(self, posx, posy, posobjatual, posobj6, listatual, lista6, listaobjatual, listaobj6, fundo, cenario5, centrocin, loja):
    posobjatual = posobj6
    listatual = lista6
    listaobjatual = listaobj6
    fundo = imagens.cenario6
    if cenario5:
        self.visual = imagens.direita
        return posobjatual, listatual, listaobjatual, fundo, 0, posy
    elif centrocin:
        self.visual = imagens.frente
        return posobjatual, listatual, listaobjatual, fundo, 832, 320
    elif loja:
        self.visual = imagens.frente
        return posobjatual, listatual, listaobjatual, fundo, 192, 320
    else:
        self.visual = imagens.frente
        return posobjatual, listatual, listaobjatual, fundo, posx, 0

def ircenario9(self, posobj, posobjatual, fundo, posy, listatual, listaobjatual, lista, listaobj):
    posobjatual = posobj
    listatual = lista
    listaobjatual = listaobj
    variaveis.gramasatual = variaveis.gramas9
    variaveis.gramasxatual = variaveis.gramasx9
    variaveis.gramasyatual = variaveis.gramasy9
    variaveis.gramas4_atual = []
    for n in range(len(variaveis.gramasx9)):
        variaveis.gramas4_atual.append(variaveis.gramasatual[n].get_rect())
        variaveis.gramas4_atual[n].x = variaveis.gramasx9[n]
        variaveis.gramas4_atual[n].y = variaveis.gramasy9[n]
    self.visual = imagens.atras
    fundo = imagens.cenario9
    self.posicao = (variaveis.posx, imagens.altura - imagens.alturap)
    return posobjatual, listatual, listaobjatual, fundo, variaveis.posx, imagens.altura - imagens.alturap


def ircentrocin(self, posx, posy, posobjatual, posobj7, listatual, lista7, listaobjatual, listaobj7, fundo):
    posobjatual = posobj7
    listatual = lista7
    listaobjatual = listaobj7
    self.visual = imagens.atras
    fundo = imagens.centrocin
    variaveis.gramasatual = ()
    variaveis.gramasxatual = ()
    variaveis.gramasyatual = ()
    variaveis.gramas4_atual = []
    return posobjatual, listatual, listaobjatual, fundo, 448, variaveis.altura - variaveis.alturap

def irloja(self, posx, posy, posobjatual, posobj8, listatual, lista8, listaobjatual, listaobj8, fundo):
    posobjatual = posobj8
    listatual = lista8
    listaobjatual = listaobj8
    self.visual = imagens.atras
    fundo = imagens.centrocin
    variaveis.gramasatual = ()
    variaveis.gramasxatual = ()
    variaveis.gramasyatual = ()
    variaveis.gramas4_atual = []
    return posobjatual, listatual, listaobjatual, fundo, 448, variaveis.altura - variaveis.alturap


def verificar4_3(posx, posy, direcao):
    if posx == 704 and posy == 448 and direcao:
        return True
    else:
        return False
    
def verificar3_4(self, objeto, posx, posy, direcao):
    save = self.rect.y
    self.rect.y -= 64
    if self.rect.colliderect(objeto):
        return True
    else:
        self.rect.y = save
        return False
    
def verificar3_1(posx, posy, direcao):
    if posx == 0 and direcao:
        return True
    else:
        return False

def verificar1_3(posx, posy, direcao):
    if posx == variaveis.largura - variaveis.largurap and direcao:
        return True
    else:
        return False

def verificar1_2(self, objeto):
    save = self.rect.y
    self.rect.y -= 64
    if self.rect.colliderect(objeto):
        return True
    else:
        self.rect.y = save
        return False

def verificar2_1(posx, posy, direcao):
    if posx == 192 and posy == 448 and direcao:
        return True
    else:
        return False
    

def verificar3_5(posx, posy, direcao):
    if posy == 0 and direcao:
        return True
    else:
        return False
    
def verificar5_3(posx, posy, direcao):
    if posy == 448 and direcao:
        return True
    else:
        return False
    
def verificar5_6(posx, posy, direcao):
    if posx == 960 and direcao:
        return True
    else:
        return False
    
def verificar6_5(posx, posy, direcao):
    if posx == 0 and direcao:
        return True
    else:
        return False
    
def verificar6_centrocin(self, objeto, posx, posy, direcao):
    save = self.rect.y
    self.rect.y -= 64
    if self.rect.colliderect(objeto):
        return True
    else:
        self.rect.y = save
        return False

def verificarcentrocin_6(posx, posy, direcao):
    if posx == 448 and posy == 448 and direcao:
        return True
    else:
        return False

def verificar6_loja(self, objeto, posx, posy, direcao):
    save = self.rect.y
    self.rect.y -= 64
    if self.rect.colliderect(objeto):
        return True
    else:
        self.rect.y = save
        return False

def verificar6_9(posx, posy, direcao):
    if posy == 0 and direcao:
        return True
    else:
        return False
    
def verificar9_6(posx, posy, direcao):
    if posy == imagens.altura - imagens.alturap and direcao:
        return True
    else:
        return False
