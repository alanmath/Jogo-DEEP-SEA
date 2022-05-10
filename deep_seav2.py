from random import randint
from funcoes import *
from funcoes import avancar_ou_voltar
from funcoes import transforma_casa_em_tamanho_do_tesouro

reiniciar_jogo = True
while reiniciar_jogo:       #COLOQUEI O JOGO DENTRO DO WHILE REINICIAR, PARA TER A OPÇÃO NO FINAL
    # INICIO DO JOGO
    print("""\033[0;34m
                 ________________________________________
                |                                        |
                |    BEM VINDO AO AVENTURA EM AUTO MAR   |
                |________________________________________|      
                                        %%%%%%%%%%                
                %%%                   %%%%%%%%%%%%%               
                %%%     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%* 
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
                %%*      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
                %%%                                               
    \033[m""")
    regras_do_jogo()
    print()
    enter_iniciar = 0
    while enter_iniciar != '':              #CONDIÇÕES INICIAIS, criando todas as variáveis que serão necessárias!
        enter_iniciar = input('aperte ENTER para iniciar!')
    oxigenio_atual = 25
    resposta_de_avancar_ou_retroceder = 'av'
    valida_while = True
    ta_subindo = []
    aperte_2 = 0
    aperte_3 = 0
    tesouro_a_ser_adicionado = 0
    resposta_soltar_ou_vasculhar = 0
    quer_ficar = 0
    numero_de_jogadores = 0
    numero_de_jogadores = jogadores(numero_de_jogadores)
    contador = 1
    valida_oxigenio = True
    lista_de_tesouros = []
    lista_de_posicoes = []
    lista_de_jogadores = []
    lista_de_booleanos = []
    lista_ta_subindo = []
    contador_criador = 1
    while contador_criador <= numero_de_jogadores:   #CRIANDO A LISTA DE TESOUROS DE CADA JOGADOR
        lista_de_tesouros.append([])
        contador_criador += 1
    contador_criador = 1
    while contador_criador <= numero_de_jogadores:   #CRIANDO A LISTA DE POSIÇÕES DE CADA JOGADOR
        lista_de_posicoes.append([0])
        contador_criador += 1
    contador_criador = 1
    while contador_criador <= numero_de_jogadores:     #ESSA LISTA DE BOOLEANOS SERVIRÁ PRA QUE O JOGADOR APÓS CHEGAR NO SUBMARINO ELE NÃO JOGUE MAIS, O SEU BOOLEANO SE TORNARÁ FALSO!
        lista_de_booleanos.append(True)
        contador_criador+= 1  
    contador_criador = 1
    while contador_criador <= numero_de_jogadores:  #ESSA É PRA BARRAR UM JOGADOR QUE JÁ ESTÁ VOLTANDO PRO SUBMARINO A NÃO AVANÇAR NOVAMENTE
        lista_ta_subindo.append(True)
        contador_criador += 1  


    while valida_while:  #ESSE WHILE CARREGA O JOGO INTEIRO, TODAS AS FUNCIONALIDADES CONTAM AQUI DENTRO!
        contador = 1       #REINICIA O JOGADOR
        while contador <= numero_de_jogadores and valida_oxigenio:      
            continua_jogo = True    
            while lista_de_booleanos[contador-1] and continua_jogo:     #SE A LISTA DE BOOLEANOS FOR FALSA ELE NÃO ENTRA NO WHILE
                print('#################################\n NOVA FASE: RESPIRAR \n#################################')
                aperte = 0
                while aperte != '':
                    aperte = input(f'JOGADOR {contador}, aperte ENTER para RESPIRAR: ')
                    print ()
                if aperte == '' :
                    print(f'jogador {contador} seu nivel de oxigênio atual é de {oxigenio_atual}')
                    oxigenio_atual -= len(lista_de_tesouros[contador-1])
                    print(f'você consumiu {len(lista_de_tesouros[contador-1])} nesta rodada e seu oxigênio agora é de {oxigenio_atual}')
                    if oxigenio_atual <= 0:                                 
                        valida_while = False
                        valida_oxigenio = False          #O valida oxigênio é para caso o oxigenio chegue a 0, ai ele irá encerrar o jogo
                        
                        
                if oxigenio_atual >0:                   #Se o oxigênio zerar o jogo acaba
                    lista_de_av_ou_vol = avancar_ou_voltar(lista_de_tesouros, lista_de_posicoes, contador, lista_de_booleanos, lista_ta_subindo)   #Opção de avançar ou nadar
                    lista_de_posicoes = lista_de_av_ou_vol[0]           #EU CRIEI UMA LISTA PRA SER RETORNADA NA FUNÇÃO avançar_ou_voltar, retornando todos esses valores
                    lista_de_booleanos = lista_de_av_ou_vol[1]
                    lista_ta_subindo = lista_de_av_ou_vol[2]
                    lista_de_tesouros = pegar_ou_largar_tesouros(lista_de_booleanos, contador, lista_de_posicoes, lista_de_tesouros)
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')       #Panorama Geral final do jogador
                print('           PANORAMA GERAL')
                print(f"""
                Casa do jogador {contador}: {lista_de_posicoes[contador-1]}
                Seus tesouros: {lista_de_tesouros[contador-1]}
                Oxigênio geral: {oxigenio_atual}""")
                continua_jogo = False
            contador_finalizador = 0
            while contador_finalizador < numero_de_jogadores:           #Nessa parte, eu fiz toda a lógica pra que quando todos os jogadores cheguem no submarino o jogo acabe
                variavel = True and lista_de_booleanos[contador_finalizador]
                if variavel == True:
                    contador_finalizador += 100000
                contador_finalizador += 1
            if variavel ==False:
                valida_while = False
            contador += 1
    print('ACABOU O JOGO!!!!!!!!')
    print('')
    print('A pontuação dos jogadores foram:')
    pontuacao = 1
    while pontuacao <= numero_de_jogadores :            #AQUI DAREMOS A PONTUAÇÃO DO JOGADOR E SE ELE TIVER FINALIZADO!
        if lista_de_booleanos[pontuacao-1] == False:
            print(f'Jogador {pontuacao} : {soma_tesouros(lista_de_tesouros[pontuacao-1])}')
        elif lista_de_booleanos[pontuacao- 1] == True:
            print(f'jogador {pontuacao} morreu antes do tempo')
        pontuacao+= 1
    
    deseja_reiniciar = 0                                #DOU A OPÇÃO DE REINICIAR O JOGO!
    while deseja_reiniciar != 's' and deseja_reiniciar != 'n':
        deseja_reiniciar = input('Você quer reiniciar o jogo? (s)sim ou (n)não ')
    if deseja_reiniciar == 's':
        reiniciar_jogo = True
    elif deseja_reiniciar == 'n':
        reiniciar_jogo = False