from time import sleep

#FUNÇÃO (facilitar no código final do menu, colocando apenas o menu_p())
dados = [] #Lista vazia, para adicionar os dados do veículo registrado
cont = 1 #Aqui é para salvar os carros no input de entrada (ex: Carro 1, Moto 2)
def pedir_inp(msg): #função para pedir hora e min de saída
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Digite apenas números.')
def menu_p(): #while True pra criar loop e possibilitar a  volta para o menu principal
    hora = 0
    minuto = 0
    global cont, tipo #gambiarra q achei :|

    while True:                        #Aqui é a "estética" do menu. Fiz
        try:
            print()
            print('\033[1;97m—*—\033[m'*18)
            print('\033[1;34mMENU PRINCIPAL\033[m'.center(60))
            print('\033[1;97m—*—\033[m'*18)
            print()
            print('\033[1;97mOPÇÕES\033[m'.center(60))
            print('————————————'.center(50))
            print('\033[1;97m1. Entrada de veículos \n2. Saída de Veículos \n3. Verificar Quantidade de Veículos \n4. Encerrar Sistema ')
            print()
            choice = int(input('Selecione uma opção: '))
            print('——'*12)
        except ValueError:
            print('Digite uma opção válida')
            continue

        while True:
            if choice == 1:                                                               #Aqui se a escolha for o 1 (Entrada de veículos), o menu de entrada aparecerá
                print()
                while True:                                                              #Input do usuário, da hora e minuto de entrada no UniCesumar Parking
                    try:
                        hora = int(input('Digite a hora de entrada: '))
                        minuto = int(input('Digite o minuto de entrada: '))
                    except ValueError:
                        print('\033[1;31mErro. Digite um horário\033[m')
                        continue
                                                                                    #Aqui, se a (hora de entrada * 60) + o minuto forem menores que 480 (8h em minutos), o horário será inválido. Mesma coisa com às 18h | Multiplicando, fazemos horas -> minutos
                    if (hora * 60) + minuto < 480 or (hora * 60) + minuto > 1080:
                        print()
                        print('Horário \033[1;31minválido\033[m. |HORÁRIO DE FUNCIONAMENTO DAS 08:00 às 18:00|'.center(60))
                        print()
                        continue #Se o input for inválido, o loop continuará até o usuário digitar um valor dentro do horário de funcionamento
                    else:
                        break #Se o input for válido, sairá do loop (acima da variavel hora) e irá para o regsitro de placa
                print()
                print('——'*20)
                print('Selecione o TIPO de veículo \n—————————————————————————— \n1. Motocicleta \n2. Carro \n3. Caminhão')
                print()

                tipo = input('Digite uma opção: ')

                #Aqui é pra converter o número para o tipo de veíuclo.
                if tipo == '1':
                    int(tipo)
                    tipo = 'Motocicleta'
                elif tipo == '2':
                    int(tipo)
                    tipo = 'Carro'
                elif tipo == '3':
                    int(tipo)
                    tipo = 'Caminhão'

                #Aqui é para aparecer a hora e o minuto formatados (Ajudar na visualização do usuário)

                placa = input('Digite a placa do veículo: ')
                print('Veículo \033[1;92mREGISTRDADO\033[m.')

                save = {'Tipo': tipo,      #aqui eu coloco as 4 informações inputadas acima, dentro de save, fazendo um mapeamento das informações, atribuindo os inputs às infos.
                        'Placa': placa,
                        'hora_entrada': hora,
                        'min_entrada': minuto
                }

                dados.append(save)                           #Aqui, eu adiciono os dados registrados acima, dentro da lista "dados", criada acima da função.
                cont += 1

                novo = input('Deseja registrar outro veículo? (S/N): ').upper().strip()#Aqui é para o usuario escolher registrar outro veículo ou não

                if novo.startswith('S'):                 #aqui se o input de "novo" for "S", ele volta para o início do registro de entrada
                    continue
                elif novo.startswith('N'):               #aqui se o input de "novo" for "N", ele volta para o menu principal
                 break

             #Aqui é para inputar a saída dos veículos, e o if not é pro caso de não ter registro de veículos
            elif choice == 2:
                if not dados:
                    print('———'*12)
                    print('Não há VEÍCULOS REGISTRADOS no momento.')
                    print('———'*12)
                    sleep(0.8)
                    print('Voltando ao \033[1;34mMENU PRINCIPAL.\033[m')
                    sleep(0.8)
                    for c in range(3, 0, -1):
                        c = '.'
                        sleep(0.2)
                        print (c)
                    sleep(1)
                    break

                else:
                    for i, save in enumerate(dados):
                        print(f'[{i+1}] {save['Tipo']} | Placa: {save['Placa']} | Entrada: {save['hora_entrada']}:{save['min_entrada']}')
                    try:
                        print()
                        sure = input('Quer registrar uma saída? (S/N): ').upper().strip() #Para caso o usuário decida não registrar a saída.
                        if sure.startswith('S'):
                            print()
                            print()
                            selecao = pedir_inp('Selecione o veículo: ')
                            if selecao < 1 or selecao > len(dados):
                                print()
                                print('|Veículo Inválido|')
                                print()
                                continue
                            print()
                            save = dados[selecao-1] #Aqui o menos é pq no python, começa a lista no 0, e o usuario vera 1, 2 e 3, e se ele inputar 1, será o segundo dalista, por isso -1
                            hora_saida = pedir_inp('Hora de saída : ')
                            min_saida = pedir_inp('Minuto de saída: ')
                            entrada_t = save ['hora_entrada'] *60 + save ['min_entrada']
                            saida_t = hora_saida * 60 + min_saida
                            tempo = saida_t - entrada_t

                            if tempo <= 15:
                                print('Veículo \033[1;32mISENTO\033[m.')

                            elif 16 <= tempo <=59:
                                print('——'*12)
                                print('Veículo sujeito a cobrança de \033[1;32mR$1,50\033[m.')
                                print('——'*12)
                            else:
                                horas = tempo/60 *1
                                print('——'*12)
                                print('Veículo sujeito a cobrança de \033[1;32mR$1,00\033[m por hora.')
                                print('——'*12)
                                print(f'\033[1mValor a pagar\033[m: \033[1;92mR$\033[m{horas:.2f}')

                            dados.pop(selecao-1) #aqui, quando o usuário inputar a saída do veículo, ele será removido da lista.

                            print('Deseja registrar outra saída? (S/N): ')
                            nova_s = input('> ').strip().upper()
                            if nova_s .startswith('S'):
                                continue
                            else:
                                break
                        elif sure.startswith('N'):
                            print('——'*12)
                            print('Voltando ao \033[1;34mMENU PRINCIPAL\033[m')
                            print('——'*12)
                            for c in range (3, 0, -1):
                                c = '*'
                                print(c)
                                sleep(0.8)
                            break
                        else:
                            print()
                            print('Erro. Digite \033[1;34mS\033[m ou \033[1;31mN\033[m.')

                    except ValueError:
                        print('—'*10)
                        print('\033[1;31mVeículo inválido\033[m')
                        print('—'*10)

                        #Aqui é para checar quantos veículos estão estacionados
            elif choice == 3:
                if not dados:    #Se não houver veículos, o usuário é enviado par ao menu principal.
                    print('——'*12)
                    print('Não há VEÍCULOS REGISTRADOS no momento.')
                    print('——'*12)
                    sleep(0.8)
                    print('Voltando ao \033[1;34mMENU PRINCIPAL.\033[m')
                    for c in range (3, 0, -1):
                        c = '*'
                        sleep(0.2)
                        print(c)
                    break
                elif dados:
                    print(f'{len(dados)} veículos estacionados.') #Lê quantos "Dados" estão na lista 'dados', que no caso, são os carros, colocados dentro da lista 'Save'
                    back = input('Deseja voltar ao menu? (S/N): ').upper().strip()
                    if back.startswith('S'):
                        print()
                        sleep(0.5)
                        print('Voltando ao \033[1;34mMENU PRINCIPAL.\033[m')
                        for c in range (3, 0, -1):
                            c = '*'
                            print(c)
                            sleep(0.8)
                        break
                    else:
                        print()
                        print('Ok')
                        print()
                        continue

            elif choice == 4:
                print()
                print('Encerrando sistema')
                sleep(1)
                for c in range (3, 0, -1):
                    c = '.'
                    print(c)
                    sleep(0.8)
                exit()
                    #FUNÇÃO

            else:
                if not choice in [1, 2, 3, 4]:
                    print()
                    print('\033[1;97mDigite uma OPÇÃO VÁLIDA\033[m')
                    break

            #Menu#
print('\033[1;97m—*—\033[m'*18)
print('|\033[1;94mUNICESUMAR PARKING\033[m|'.center(60))
print('\033[1;97mSISTEMA DE GERENCIAMENTO\033[m'.center(60))
print('\033[1;97m—*—\033[m'*18)
print('HORÁRIO DE FUNCIONAMENTO - \033[1;97m08:00 às 18:00\033[m'.center(55))
print()
while True:
    try:
        user_select = str(input('\033[1mDeseja acessar o sistema?\033[m(\033[1;92mS\033[m/\033[1;31mN\033[m): ').upper().strip())
        if not user_select.isalpha():
            print('Digite apenas \033[1;97m\'S\'\033[m ou \033[1;97m\'N\'\033[m.')

        if user_select.startswith('S'):
            print('Entrando no sistema...')
            sleep(1)
            menu_p()
            break


        elif user_select.startswith('N'):
            print('Finalizando...')
            for _ in range (3, 0, -1):
                _ = '*'
                print(_)
                sleep(0.8)
            break

    except ValueError:
        print('Digite apenas \033[1;97m\'S\'\033[m ou \033[1;97m\'N\'\033[m.')