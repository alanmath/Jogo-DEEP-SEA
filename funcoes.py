from random import randint
def regras_do_jogo():
    regras = ''
    while regras != 's' and regras != 'n': 
        regras = input('Você deseja saber as regras do jogo? (s)sim ou (n)não :  ')
    if regras == 's':
        print("""
        O jogador é um mergulhador em busca de tesouros escondidos no fundo do mar. 
        Porém, o tanque de oxigênio não é grande o suficiente para possibilitar um mergulho tranquilo. 
        Com a fonte de oxigênio escassa, os mergulhadores precisam gerenciar bem o tempo debaixo da água.
        Quanto mais fundo o mergulhador for, maior é a chance de encontrar tesouros mais valiosos. 
        Além disso, a quantidade de tesouros que o mergulhador carrega afeta sua mobilidade.
        O objetivo do jogo é conseguir trazer para o submarino o maior valor em tesouros.""")
        print("""
        A cada rodada o jogo deve seguir os passos descritos a seguir:
        1.	Respirar: Jogo verifica se há a necessidade de reduzir o oxigênio. 
        O oxigênio deve ser reduzido de acordo com a quantidade de tesouros que o mergulhador estiver carregando. 
        Ou seja, se o jogador estiver carregando 2 tesouros o nível do oxigênio deve diminuir 2 níveis. 
        Se o mergulhador não estiver carregando nenhum tesouro então não há a necessidade de reduzir o oxigênio.
         Se o oxigênio alcançar o nível 0 ou menor, o jogador da vez termina a rodada e o jogo acaba.

        2.	Avançar ou Retroceder?: No início da partida o jogador começa dentro do submarino. 
        Depois de sair do submarino ele deve escolher continuar avançando para o fundo do mar ou voltar para o submarino.
        •	O mergulhador não pode voltar para o submarino sem tesouros.
        •	O mergulhador só pode voltar para o submarino uma única vez.
        •	Quando o mergulhador decidir retornar para o submarino ele não pode avançar de volta para o fundo do mar.
        •	Depois que o jogador decidir retroceder o jogador não precisa passar por este passo, pois a única opção agora será retroceder.

        3.	Nadar: Jogador rola dois dados d3 (Dado de três faces.) para verificar o avanço.
        A soma dos dois resultados do dado d3 representa a profundidade em que o mergulhador vai nadar.

        Se o jogador estiver carregando tesouros, então a quantidade de tesouros carregados deve ser subtraído do valor do avanço.
        (Exemplo: Se um dado sorteou o valor 1 e o outro dado sorteou o valor 3 e o jogador está carregando 3 tesouros, então o jogador vai avançar somente uma casa.) 
        Note que se o valor for negativo o jogador deve ficar parado. Esse passo se aplica tanto para avançar para o fundo do mar quanto para retornar para o submarino.

        4.	Caça ao tesouro: Neste passo o jogador pode fazer uma busca por tesouros ou decidir soltar um dos tesouros que ele carrega. 
        (Obs.: Este passo pode ser realizado independente da direção que o mergulhador estiver indo. Então se o mergulhador estiver retornando para o submarino ele pode vasculhar a área em busca de tesouros.)

        •	Se o mergulhador decidir soltar um tesouro, ele pode escolher qual tesouro deve ser descartado. Note que se o mergulhador estiver retornando ao submarino ele não pode soltar o tesouro se for o único que ele carrega.
        •	Se o mergulhador decidir vasculhar a área:
        •	O jogo deve informar o valor da recompensa. O valor da recompensa é um número aleatório que depende da profundidade do mar em que o mergulhar se encontra.
        •	O jogador decide se ele deseja ficar ou não com o tesouro. Note que o jogador só pode carregar no máximo 4 tesouros. Então se ele já estiver com 4 tesouros,
         o jogador escolhe qual tesouro deve ser descartado.
        O jogo acaba quando o mergulhador voltar para o submarino ou se o oxigênio do tanque se esgotar. 
        O mergulhador só receberá a recompensa dos tesouros se conseguir voltar para o submarino. Caso o oxigênio se esgote antes do mergulhador chegar ao submarino os tesouros serão perdidos e os pontos não são computados.
        
        Oxigênio
        O jogo começa com o oxigênio cheio, marcando o nível em 25. Conforme o jogo avança, o nível do oxigênio irá reduzindo conforme as ações do jogador. 
        Se o nível de oxigênio alcançar o valor 0 o jogador da vez termina a rodada e o jogo acaba.
        
        Profundidade
        A profundidade máxima que o mergulhador pode alcançar em direção ao fundo do mar é representada pelo valor 32. Onde a profundidade de nível 1 representa a profundidade
        mais próxima do submarino e a profundidade de nível 32 representa a profundidade mais distante do submarino.
        E a posição de valor 0 representa o submarino.
        """)
    
def jogadores(numero_de_jogadores):                 #Função inicial que nos diz o numero de jogadores
    diga_numero = 0                 #Fiz isso pra validar entrada
    while not diga_numero > 0  :
        qt = input('Diga quantos jogadores irão participar dessa aventura:  ')
        if qt.isnumeric():                                      
            diga_numero = int(qt)
        numero_de_jogadores = diga_numero
    return numero_de_jogadores

def soma_tesouros(lista):           #Função pra contar os tesouros no final do jogo
    contador = 0
    soma = 0
    while contador < len(lista):
        soma += lista[contador]
        contador+=1
    return soma

def avancar_ou_voltar(lista_de_tesouros, lista_de_posicoes, contador, lista_de_booleanos, lista_ta_subindo):    #Aqui decidimos se ele avança ou volta
    aperte_2 = 0
    valida_while = True
    while valida_while:
        if lista_ta_subindo[contador-1] == False:    #Aqui entra a função dessa lista, se ele ja tiver escolhido retornar, ele não poderá mais avançar, lá na frente eu faço essa variável se tornar falsa
            print('Amigo(a), você está subindo já, pode descer mais não!')
        resposta_de_avancar_ou_retroceder = input('Deseja avançar ou retroceder? (av)avançar ou (re)retroceder:  ')
        if resposta_de_avancar_ou_retroceder == 'av' and lista_ta_subindo[contador-1]:      #Coloquei a condição explicada acima, se ele ja ta subindo ou não!
            print(f'#####   DESCENDOOOOO JOGADOR {contador}, SE PREPARE !!!   #####\n')
            while aperte_2 != '':
                aperte_2 = input(f'aperte enter para DESCER jogador {contador}')
            if aperte_2 == '':
                dado1 = randint(1,3)
                dado2 = randint(1,3)
                print(f'OS DADOS FORAM ROLADOS E VOCÊ TIROU: DADO1 = {dado1} e DADO 2 = {dado2}, soma= {dado1+dado2}')
                if len(lista_de_tesouros[contador-1]) < (dado1+dado2):          #Condição de que ele possa andar!
                    lista_de_posicoes[contador-1][0] += (dado1+dado2-len(lista_de_tesouros[contador-1]))
                    print(f'você possui {len(lista_de_tesouros[contador-1])} tesouros então está andando {dado1+dado2-len(lista_de_tesouros[contador-1])} casas')
                    print(f'você, jogador {contador}, agora está na profundidade {lista_de_posicoes[contador-1]}')
                    novo_valida_while = False
                    if lista_de_posicoes[contador-1][0] > 32:       #Caso ele passe da casa 32, ele irá voltar
                        print("Aí você quer sair do jogo, vamos voltar você pra casa 32")
                        lista_de_posicoes[contador-1][0] = 32
                else:
                    print('e tu mora na vila olimpia é?')       #Ta carregando muito tesouro, então fica na mesma casa
                    print(f':( infelizmente você vai ficar na mesma casa. Pois carrega {len(lista_de_tesouros[contador-1])} tesouros e tirou {dado1+dado2}')
            valida_while =  False
            
        novo_valida_while = True        #Esse novo valida while será usado para o caso de ele não ter tesouro
        aperte_3 = 0
        while novo_valida_while:
            if resposta_de_avancar_ou_retroceder == 're':
                    valida_while = False            #Aqui para sair do while
                    print(f'SUBINDOOOOOOO JOGADOR {contador} a partir de agora você só pode subir !!!')
                    while aperte_3 != '':   #Validar entrada
                        aperte_3 = input('aperte enter para SUBIR')
                    if aperte_3 == '':
                        dado1 = randint(1,3)
                        dado2 = randint(1,3)
                        print(f'OS DADOS FORAM ROLADOS E VOCÊ TIROU: DADO1 = {dado1} e DADO 2 = {dado2}, soma = {dado1+dado2}')
                        if len(lista_de_tesouros[contador-1]) == 0:
                            print('Você não pode voltar sem tesouro, jogue novamente!')
                            novo_valida_while = False   
                        
                        
                        elif len(lista_de_tesouros[contador-1]) < (dado1+dado2):        #Caso ele entre em posições negativas
                            lista_de_posicoes[contador-1][0] -= (dado1+dado2-len(lista_de_tesouros[contador-1]))
                            if lista_de_posicoes[contador-1][0] <= 0:
                                lista_de_posicoes[contador-1][0] = 0
                                lista_de_booleanos[contador-1] = False      #A lista de booleanos se torna falso porque ele chegou no submarino
                                print(f'Você voltou para o SUBMARINO, parabens por não morrer haha, sua pontuação final é de {lista_de_tesouros[contador-1]}')
                                lista_de_booleanos[contador-1] = False  
                                valida_while =  False       
                            else:
                                print(f'você possui {len(lista_de_tesouros[contador-1])} tesouros então está voltando {dado1+dado2-len(lista_de_tesouros[contador-1])} casas')
                                print(f'você agora está na profundidade {lista_de_posicoes[contador-1]}')
                                lista_ta_subindo[contador-1] = False
                        else:
                            print('e tu mora na vila olimpia é')        #Caso ele fique sem conseguir andar pelo tanto de tesouro
                            print(f':( infelizmente você vai ficar na mesma casa. Pois carrega {len(lista_de_tesouros[contador-1])} tesouros e tirou {dado1+dado2}')
            
            novo_valida_while = False
                     
    lista_de_respostas = [lista_de_posicoes, lista_de_booleanos, lista_ta_subindo]  #Retornei uma lista para busca-las no programa principal
    return lista_de_respostas 
def pegar_ou_largar_tesouros(lista_de_booleanos, contador, lista_de_posicoes, lista_de_tesouros):       #Função na qual ele pega ou larga tesouros
    resposta = 0
    if lista_de_booleanos[contador-1]:  #Novamente, lista de booleanos vai analisar se o jogador ja chegou ou não no submarino
        resposta_soltar_ou_vasculhar = 0
        while resposta_soltar_ou_vasculhar != 's' and resposta_soltar_ou_vasculhar != 'v': 
            resposta_soltar_ou_vasculhar = input('você deseja soltar algum tesouro ou vasculhar o fundo do mar? (s) soltar ou v (vasculhar)? ')
        if resposta_soltar_ou_vasculhar == 'v':
            while resposta != '':
                resposta = input(f'aperte ENTER para continuar jogador {contador}')
            print ()
            valor_do_tesouro = transforma_casa_em_tamanho_do_tesouro(lista_de_posicoes, contador)   #Uso aqui a função transformar a casa em que ele estar no tesouro que vai encontrar
            print(f'Você vasculhou o fundo do mar e encontrou um tesouro que vale {valor_do_tesouro}')
            quer_ficar = 0
            while quer_ficar != 's' and quer_ficar != 'n': #Validar entrada
                quer_ficar = input('você quer esse tesouro? (s) sim ou (n) nao: ')
            if quer_ficar == 's':       #Aqui ele pode acabar estar voltando e escolher soltar, até mesmo ficar sem tesouro, mas aí ele não desce porque já estaria voltando, e também não sobe porque estaria sem tesouro, sendo forçado a pegar um tesouro pra subir!
                if len(lista_de_tesouros[contador-1]) < 4:
                    lista_de_tesouros[contador-1].append(valor_do_tesouro)  #adiciono o tesouro a lista de tesouros
                    print(f'jogador {contador}, seu tesouros agora são {lista_de_tesouros[contador-1]}' )   
                elif len(lista_de_tesouros[contador-1]) == 4:   #Caso ele ja esteja com excesso de tesouros
                    lista_de_tesouros[contador-1].append(valor_do_tesouro)
                    print(f'seus tesouros são:{lista_de_tesouros[contador-1]}')
                    largar = 1000
                    while not 1 <=largar <= 4: #Validar entrada
                        largar = int(input('Escolha qual vc deseja largar, da esquerda pra direita é 1,2,3...: '))
                        del lista_de_tesouros[contador-1][largar-1]
        if resposta_soltar_ou_vasculhar == 's':     #Caso ele deseja soltar o tesouro
            if len(lista_de_tesouros[contador-1]) == 0:
                print('Você não tem nenhum tesouro pra largar, vamo seguir em frente!')
            
            if len(lista_de_tesouros[contador-1]) > 0:      #Momento pra escolher qual largar
                largar_novamente = 10000
                print(f'seu tesouros são {lista_de_tesouros[contador-1]}')
                while (largar_novamente > len(lista_de_tesouros[contador-1])) or (largar_novamente < 0):
                    largar_novamente = int(input('qual você deseja largar agora, da esquerda pra direita é 1,2,3...?  '))
                del lista_de_tesouros[contador-1][largar_novamente-1]
    return lista_de_tesouros
        
def transforma_casa_em_tamanho_do_tesouro(lista_de_posicoes, contador):     #Nessa função ele transforma a casa do jogador no tesouro que ele vai encontrar
    tesouro_encontrado = 0
    if 1<=lista_de_posicoes[contador-1][0] <=8:
        tesouro_encontrado = randint (0,3)
    if 9<=lista_de_posicoes[contador-1][0] <=16:
        tesouro_encontrado = randint (4,7)
    if 17<=lista_de_posicoes[contador-1][0] <=24:
        tesouro_encontrado = randint (8,11)
    if 25<=lista_de_posicoes[contador-1][0] <=32:
        tesouro_encontrado = randint (12,15)
    return tesouro_encontrado


