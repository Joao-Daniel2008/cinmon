import socket
import threading
import cimons
import json
from time import sleep


def resolver_turno(idplayer, conexao):
    global cimons1, escolhas_turno, primeira, jogou, status1, status2, condicao_turno

    if idplayer != 1:
        with condicao_turno:
            while (not primeira):
                print('esperando outro jogador processar os dados do combate...')
                condicao_turno.wait()
                print('pronto! irei checar a condicao novamente.')

    for cimon in cimons.cimons:
        if cimons1[1]['nome'] == cimon.nome:
            cimon1 = cimon.clonar()
            cimon1.xp = sum(n * 10 for n in range(1, cimons1[1]['nivel']))
            cimon1.subir_nivel()
            cimon1.hp = cimons1[1]['hp']
    
    for cimon in cimons.cimons:
        if cimons1[2]['nome'] == cimon.nome:
            cimon2 = cimon.clonar()
            cimon2.xp = sum(n * 10 for n in range(1, cimons1[2]['nivel']))
            cimon2.subir_nivel()
            cimon2.hp = cimons1[2]['hp']

    for ataque in cimons.ataques:
        if escolhas_turno[1] == ataque.nome:
            golpe_p1 = ataque

    for ataque in cimons.ataques:
        if escolhas_turno[2] == ataque.nome:
            golpe_p2 = ataque

    hpAnterior1 = cimons1[1]['hp']
    hpAnterior2 = cimons1[2]['hp']


    if (not primeira):
        cimons1[2]['hp'] -= int(((int(golpe_p1.dano * golpe_p1.efetivo(cimon2)//1)) * cimon1.status)//1)
        
        if cimons1[2]['hp'] > 0:
            cimons1[1]['hp'] -= int(((int(golpe_p2.dano * golpe_p2.efetivo(cimon1)//1)) * cimon2.status)//1)
        
        if cimons1[1]['hp'] <= 0:
            cimons1[1]['qtd'] -= 1
            if cimons1[1]['qtd'] <= 0:
                status1 = 'perdeu'
            else:
                status1 = 'batalha'
        else:
            status1 = 'batalha'
        
        if cimons1[2]['hp'] <= 0:
            cimons1[2]['qtd'] -= 1
            if cimons1[2]['qtd'] <= 0:
                status2 = 'perdeu'
            else:
                status2 = 'batalha'
        else:
            status2 = 'batalha'




    resultado_p1 = {
        'evento': "RESULTADO_TURNO",
        'novo_hp1': cimons1[1]['hp'],
        'novo_hp2': cimons1[2]['hp'],
        'hp_anterior1': hpAnterior1,
        'hp_anterior2': hpAnterior2,
        'golpe_tomado': golpe_p2.nome,
        'ID': 1,
        'status': status2
    }

    resultado_p2 = {
        'evento': "RESULTADO_TURNO",
        'novo_hp1': cimons1[2]['hp'],
        'novo_hp2': cimons1[1]['hp'],
        'hp_anterior1': hpAnterior2,
        'hp_anterior2': hpAnterior1,
        'golpe_tomado': golpe_p1.nome,
        'ID': 2,
        'status': status1
    }



    if golpe_p1.efetivo(cimon2) == 2:
        resultado_p1['efetivo_dado'] = "super efetivo"
        resultado_p2['efetivo_tomado'] = "super efetivo"
    elif golpe_p1.efetivo(cimon2) == 1:
        resultado_p1['efetivo_dado'] = "normal"
        resultado_p2['efetivo_tomado'] = "normal"
    elif golpe_p1.efetivo(cimon2) == 0.5:
        resultado_p1['efetivo_dado'] = "pouco efetivo"
        resultado_p2['efetivo_tomado'] = "pouco efetivo"

    if golpe_p2.efetivo(cimon1) == 2:
        resultado_p1['efetivo_tomado'] = "super efetivo"
        resultado_p2['efetivo_dado'] = "super efetivo"
    elif golpe_p2.efetivo(cimon1) == 1:
        resultado_p1['efetivo_tomado'] = "normal"
        resultado_p2['efetivo_dado'] = "normal"
    elif golpe_p2.efetivo(cimon1) == 0.5:
        resultado_p1['efetivo_tomado'] = "pouco efetivo"
        resultado_p2['efetivo_dado'] = "pouco efetivo"

    conexao.sendall(json.dumps(resultado_p1).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(resultado_p2).encode('utf-8'))
    
    with condicao_turno:
        if (not primeira):
            primeira = True
            condicao_turno.notify()

        elif primeira:
            primeira = False
            escolhas_turno.clear()

    

def minha_troca_seu_ataque(idplayer, conexao):
    global escolhas_turno, cimons1, primeira, jogou, status1, status2, condicao_turno

    if idplayer != 1:
        with condicao_turno:
            while (not primeira):
                print('esperando outro jogador processar os dados do combate...')
                condicao_turno.wait()
                print('pronto! irei checar a condicao novamente.')

    if idplayer == 1:
        for ataque in cimons.ataques:
            if escolhas_turno[2] == ataque.nome:
                golpe_p2 = ataque
    elif idplayer == 2:
        for ataque in cimons.ataques:
            if escolhas_turno[1] == ataque.nome:
                golpe_p1 = ataque

    for cimon in cimons.cimons:
        if cimons1[1]['nome'] == cimon.nome:
            cimon1 = cimon.clonar()
            cimon1.xp = sum(n * 10 for n in range(1, cimons1[1]['nivel']))
            cimon1.subir_nivel()
            cimon1.hp = cimons1[1]['hp']
    
    for cimon in cimons.cimons:
        if cimons1[2]['nome'] == cimon.nome:
            cimon2 = cimon.clonar()
            cimon2.xp = sum(n * 10 for n in range(1, cimons1[2]['nivel']))
            cimon2.subir_nivel()
            cimon2.hp = cimons1[2]['hp']
    
    hpAnterior1 = cimons1[1]['hp']
    hpAnterior2 = cimons1[2]['hp']
    

    if idplayer == 1 and (not primeira):
        cimons1[1]['hp'] -= int(((int(golpe_p2.dano * golpe_p2.efetivo(cimon1)//1)) * cimon2.status)//1)
        
        if cimons1[1]['hp'] <= 0:
            cimons1[1]['qtd'] -= 1
            if cimons1[1]['qtd'] <= 0:
                status1 = 'perdeu'
            else:
                status1 = 'batalha'
        else:
            status1 = 'batalha'
        if cimons1[2]['hp'] <= 0:
            cimons1[2]['qtd'] -= 1
            if cimons1[2]['qtd'] <= 0:
                status2 = 'perdeu'
            else:
                status2 = 'batalha'
        else:
            status2 = 'batalha'

    elif idplayer == 2 and (not primeira):
        cimons1[2]['hp'] -= int(((int(golpe_p1.dano * golpe_p1.efetivo(cimon2)//1)) * cimon1.status)//1)
        
        if cimons1[1]['hp'] <= 0:
            cimons1[1]['qtd'] -= 1
            if cimons1[1]['qtd'] <= 0:
                status1 = 'perdeu'
            else:
                status1 = 'batalha'
        else:
            status1 = 'batalha'
        if cimons1[2]['hp'] <= 0:
            cimons1[2]['qtd'] -= 1
            if cimons1[2]['qtd'] <= 0:
                status2 = 'perdeu'
            else:
                status2 = 'batalha'
        else:
            status2 = 'batalha'

    if idplayer == 1:
        golpe_tomado1 = golpe_p2.nome
    else:
        golpe_tomado1 = ''

    if idplayer == 2:
        golpe_tomado2 = golpe_p1.nome
    else:
        golpe_tomado2 = ''
    
    resultado_p1 = {
        'evento': "RESULTADO_TURNO",
        'novo_hp1': cimons1[1]['hp'],
        'novo_hp2': cimons1[2]['hp'],
        'hp_anterior1': hpAnterior1,
        'hp_anterior2': hpAnterior2,
        'golpe_tomado': golpe_tomado1,
        'ID': 1,
        'status': status2
        }
    
    resultado_p2 = {
        'evento': "RESULTADO_TURNO",
        'novo_hp1': cimons1[2]['hp'],
        'novo_hp2': cimons1[1]['hp'],
        'hp_anterior1': hpAnterior2,
        'hp_anterior2': hpAnterior1,
        'golpe_tomado': golpe_tomado2,
        'ID': 2,
        'status': status1
        }
    
    if idplayer == 1:    
        if golpe_p2.efetivo(cimon1) == 2:
            resultado_p1['efetivo_tomado'] = "super efetivo"
            resultado_p2['efetivo_dado'] = "super efetivo"
        elif golpe_p2.efetivo(cimon1) == 1:
            resultado_p1['efetivo_tomado'] = "normal"
            resultado_p2['efetivo_dado'] = "normal"
        elif golpe_p2.efetivo(cimon1) == 0.5:
            resultado_p1['efetivo_tomado'] = "pouco efetivo"
            resultado_p2['efetivo_dado'] = "pouco efetivo"

    elif idplayer == 2:
        if golpe_p1.efetivo(cimon2) == 2:
            resultado_p1['efetivo_dado'] = "super efetivo"
            resultado_p2['efetivo_tomado'] = "super efetivo"
        elif golpe_p1.efetivo(cimon2) == 1:
            resultado_p1['efetivo_dado'] = "normal"
            resultado_p2['efetivo_tomado'] = "normal"
        elif golpe_p1.efetivo(cimon2) == 0.5:
            resultado_p1['efetivo_dado'] = "pouco efetivo"
            resultado_p2['efetivo_tomado'] = "pouco efetivo"
    

    conexao.sendall(json.dumps(resultado_p1).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(resultado_p2).encode('utf-8'))
    
    with condicao_turno:
        if (not primeira):
            primeira = True
            condicao_turno.notify()

        elif primeira:
            primeira = False
            escolhas_turno.clear()

def meu_ataque_sua_troca(idplayer, conexao):
    global escolhas_turno, cimons1, primeira, jogou, status1, status2, condicao_turno

    if idplayer != 1:
        with condicao_turno:
            while (not primeira):
                print('esperando outro jogador processar os dados do combate...')
                condicao_turno.wait()
                print('pronto! irei checar a condicao novamente.')


    for cimon in cimons.cimons:
        if cimons1[1]['nome'] == cimon.nome:
            cimon1 = cimon.clonar()
            cimon1.xp = sum(n * 10 for n in range(1, cimons1[1]['nivel']))
            cimon1.subir_nivel()
            cimon1.hp = cimons1[1]['hp']
    
    for cimon in cimons.cimons:
        if cimons1[2]['nome'] == cimon.nome:
            cimon2 = cimon.clonar()
            cimon2.xp = sum(n * 10 for n in range(1, cimons1[2]['nivel']))
            cimon2.subir_nivel()
            cimon2.hp = cimons1[2]['hp']

    if idplayer == 1:
        for ataque in cimons.ataques:
            if escolhas_turno[1] == ataque.nome:
                golpe_p1 = ataque
    elif idplayer == 2:
        for ataque in cimons.ataques:
            if escolhas_turno[2] == ataque.nome:
                golpe_p2 = ataque

    hpAnterior1 = cimons1[1]['hp']
    hpAnterior2 = cimons1[2]['hp']
    

    if idplayer == 1 and (not primeira):
        cimons1[2]['hp'] -= int(((int(golpe_p1.dano * golpe_p1.efetivo(cimon2)//1)) * cimon1.status)//1)
    
        if cimons1[1]['hp'] <= 0:
            cimons1[1]['qtd'] -= 1
            if cimons1[1]['qtd'] <= 0:
                status1 = 'perdeu'
            else:
                status1 = 'batalha'
        else:
            status1 = 'batalha'

        if cimons1[2]['hp'] <= 0:
            cimons1[2]['qtd'] -= 1
            if cimons1[2]['qtd'] <= 0:
                status2 = 'perdeu'
            else:
                status2 = 'batalha'
        else:
            status2 = 'batalha'

    elif idplayer == 2 and (not primeira):
        cimons1[1]['hp'] -= int(((int(golpe_p2.dano * golpe_p2.efetivo(cimon1)//1)) * cimon2.status)//1)
        
        if cimons1[1]['hp'] <= 0:
            cimons1[1]['qtd'] -= 1
            if cimons1[1]['qtd'] <= 0:
                status1 = 'perdeu'
            else:
                status1 = 'batalha'
        else:
            status1 = 'batalha'

        if cimons1[2]['hp'] <= 0:
            cimons1[2]['qtd'] -= 1
            if cimons1[2]['qtd'] <= 0:
                status2 = 'perdeu'
            else:
                status2 = 'batalha'
        else:
            status2 = 'batalha'


    if idplayer == 1:
        golpe_tomado1 = ''
    else:
        golpe_tomado1 = golpe_p2.nome

    if idplayer == 2:
        golpe_tomado2 = ''
    else:
        golpe_tomado2 = golpe_p1.nome

    resultado_p1 = {
        'evento': "TROCA",
        'novo_hp1': cimons1[1]['hp'],
        'novo_hp2': cimons1[2]['hp'],
        'hp_anterior1': hpAnterior1,
        'hp_anterior2': hpAnterior2,
        'golpe_tomado': golpe_tomado1,
        'ID': 1,
        'status': status2,
        'nome': cimons1[2]['nome'],
        'nivel': cimons1[2]['nivel'],
        'hp': cimons1[2]['hp']
        }
    
    resultado_p2 = {
        'evento': "TROCA",
        'novo_hp1': cimons1[2]['hp'],
        'novo_hp2': cimons1[1]['hp'],
        'hp_anterior1': hpAnterior2,
        'hp_anterior2': hpAnterior1,
        'golpe_tomado': golpe_tomado2,
        'ID': 2,
        'status': status1,
        'nome': cimons1[1]['nome'],
        'nivel': cimons1[1]['nivel'],
        'hp': cimons1[1]['hp']
    }
        
    if idplayer == 1:
        if golpe_p1.efetivo(cimon2) == 2:
            resultado_p1['efetivo_dado'] = "super efetivo"
            resultado_p2['efetivo_tomado'] = "super efetivo"
        elif golpe_p1.efetivo(cimon2) == 1:
            resultado_p1['efetivo_dado'] = "normal"
            resultado_p2['efetivo_tomado'] = "normal"
        elif golpe_p1.efetivo(cimon2) == 0.5:
            resultado_p1['efetivo_dado'] = "pouco efetivo"
            resultado_p2['efetivo_tomado'] = "pouco efetivo"


    elif idplayer == 2:
        if golpe_p2.efetivo(cimon1) == 2:
            resultado_p1['efetivo_tomado'] = "super efetivo"
            resultado_p2['efetivo_dado'] = "super efetivo"
        elif golpe_p2.efetivo(cimon1) == 1:
            resultado_p1['efetivo_tomado'] = "normal"
            resultado_p2['efetivo_dado'] = "normal"
        elif golpe_p2.efetivo(cimon1) == 0.5:
            resultado_p1['efetivo_tomado'] = "pouco efetivo"
            resultado_p2['efetivo_dado'] = "pouco efetivo"

    conexao.sendall(json.dumps(resultado_p1).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(resultado_p2).encode('utf-8'))

    with condicao_turno:
        if (not primeira):
            primeira = True
            condicao_turno.notify()

        elif primeira:
            primeira = False
            escolhas_turno.clear()


def troca_dupla(idplayer, conexao):
    global escolhas_turno, cimons1, primeira, jogou

    resultado_p1 = {
        'evento': 'TROCA_DUPLA',
        'nome': cimons1[2]['nome'],
        'nivel': cimons1[2]['nivel'],
        'hp': cimons1[2]['hp']
        }
    
    resultado_p2 = {
        'evento': 'TROCA_DUPLA',
        'nome': cimons1[1]['nome'],
        'nivel': cimons1[1]['nivel'],
        'hp': cimons1[1]['hp']
    }

    conexao.sendall(json.dumps(resultado_p1).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(resultado_p2).encode('utf-8'))
    
    if primeira:
        primeira = False
    escolhas_turno.clear()



def gerenciar_clientes(conexao, endereco, idplayer):
    global cimons, escolhas_turno, outra_decisao, cimons1, condicao_turno, comeco1, comeco2, vivo, status1, status2, jogadores, primeira


    print(f'NOVA CONEXAO: {endereco}')

    while True:
        try:
            dados = conexao.recv(2048).decode('utf-8')

            if not dados:
                print(f'CONEXAO PERDIDA COM: {endereco}')
                conexao.close()
                break

            decisao = json.loads(dados)

            outra_decisao[idplayer] = decisao['evento']

            if 'COMECO' in decisao['evento'] or decisao['evento'] == 'TROCA':
                cimons1[idplayer]['nome'] = decisao['nome']
                cimons1[idplayer]['nivel'] = decisao['nivel']
                cimons1[idplayer]['hp'] = decisao['hp']
                if decisao['evento'] == 'TROCA' or comeco1 or comeco2:
                    with condicao_turno:
                        escolhas_turno[idplayer] = 'TROCA' if decisao['evento'] == 'TROCA' else ''
                        if len(escolhas_turno) < 2:
                            condicao_turno.wait()
                        else:
                            condicao_turno.notify()
                            if comeco1 or comeco2:
                                escolhas_turno.clear()
                if decisao['evento'] == 'TROCA':
                    cimons1['evento'] = 'TROCA'
                elif comeco1 or comeco2:
                    if idplayer == 1:
                        comeco1 = False
                    elif idplayer == 2:
                        comeco2 = False
                    cimons1[idplayer]['qtd'] = decisao['qtd']
                if decisao['evento'] == 'COMECO2':
                    with condicao_turno:
                        vivo = True
                        condicao_turno.notify()
                decisao2 = outra_decisao[1] if idplayer == 2 else outra_decisao[2]
                if decisao['evento'] == 'COMECO':
                    conexao.sendall(json.dumps(cimons1[2]).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(cimons1[1]).encode('utf-8'))
                if decisao['evento'] == 'TROCA' and decisao2 == 'ESCOLHA_GOLPE':
                    minha_troca_seu_ataque(idplayer, conexao)
                elif decisao['evento'] == 'TROCA' and decisao2 == 'TROCA':
                    troca_dupla(idplayer, conexao)

            elif decisao['evento'] == 'AGUARDANDO_REPOSICAO':
                with condicao_turno:
                    while (not vivo):
                        print('aguardando reposição...')
                        condicao_turno.wait()
                        print('pronto, verificando condição novamente...')
                vivo = False
                conexao.sendall(json.dumps(cimons1[2]).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(cimons1[1]).encode('utf-8'))

            elif decisao['evento'] == 'ESCOLHA_GOLPE':
                with condicao_turno:
                    escolhas_turno[idplayer] = decisao['golpe']
                    condicao_turno.wait_for(lambda: len(escolhas_turno) == 2)
                    condicao_turno.notify_all()
                decisao2 = outra_decisao[1] if idplayer == 2 else outra_decisao[2]
                if decisao2 == 'ESCOLHA_GOLPE':
                    resolver_turno(idplayer, conexao)
                elif decisao2 == 'TROCA':
                    meu_ataque_sua_troca(idplayer, conexao)
                
        except:
            print(f'ERROOOOO')
            conexao.close()
            vivo = False
            escolhas_turno = {}
            cimons1 = {1: {}, 2: {}}
            jogou = 0
            outra_decisao = {1: '', 2: ''}
            primeira = False
            status1 = ''
            status2 = ''
            jogadores = 1
            break







comeco1 = True
comeco2 = True
HOST='0.0.0.0'
PORTA=5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('CRIANDO SERVIDOR...')
try:
    server.bind((HOST, PORTA))
except:
    print('CRIACAO ERRO')


print('ABRINDO PORTAS...')
server.listen()
print('AGUARDANDO CLIENTES...')
status1 = ''
status2 = ''
jogadores = 1
condicao_turno = threading.Condition()
vivo = False
escolhas_turno = {}
cimons1 = {1: {}, 2: {}}
jogou = 0
outra_decisao = {1: '', 2: ''}
primeira = False

while True:
    conexao, endereco = server.accept()
    thread = threading.Thread(target=(gerenciar_clientes), args=(conexao, endereco, jogadores), daemon=True)
    thread.start()
    jogadores += 1
    if jogadores == 3:
        jogadores = 1