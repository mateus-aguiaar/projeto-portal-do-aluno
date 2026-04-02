import csv
import os 
os.system('cls')

titulo = "PORTAL DO ALUNO"
print(titulo.center(60))
print('-=-' * 20)


print('\n[1] - Professor \n[2] - Aluno')

opcao_entrada = int(input("\n------> 1 ou 2: "))

if opcao_entrada == 1:
    print('\n[1] - Já tenho cadastro\n[2] - Não tenho cadastro')
    cadastro_professor = int(input('\nDigite a sua opção de entrada: '))

    if cadastro_professor == 2:
        print('\nFaça o seu cadastro no Portal professor: ')
        print('-' * 45)
        print('O nome de usuário deverá conter 8 caracteres, pelo menos um maiusculo e um minusculo e um caracter especial.\n')
        usuario_professor = str(input('Username: '))
        print('\nA sua senha deverá conter seis caracteres e um caracter especial')
        password_professor = str(input('\nDigite a sua senha: '))
        with open('dados-professor.csv', 'a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([usuario_professor,password_professor])
        print('\n\033[1;32mCadastro efetuado com sucesso!\033[m')
        
    elif cadastro_professor == 1:
        while True:
            login = input('\nDigite o usuário: ')
            password = input('\nDigite a sua senha: ')
            encontrado_professor = False
            try:
                with open("dados-professor.csv", "r", newline="", encoding="utf-8") as arquivo:
                    leitor = csv.reader(arquivo)

                    for linha in leitor:
                        if login == linha[0] and password == linha[1]:
                            encontrado_professor = True
                            break
                    
                    if encontrado_professor:
                        print('\n\033[1;32mLogin realizado com sucesso!\033[m')
                        print("\n[1] - Boletim \n[2] - Presença")
                        menu_professor = int(input("\n------> 1 ou 2: "))
                        
                        if menu_professor == 1:
                            while True:
                                print("\nAdicionar notas, deve-se digitar a matéria, a nota, e o nome do Aluno: ")
                                materia = str(input("\nDigite a matéria que deseja adicionar a nota: "))
                                nota = float(input("\nDigite a nota da respectiva matéria: "))
                                aluno = str(input("\nDigite o aluno, nome e sobrenome: "))
                                with open("boletim.csv", "a", newline = "", encoding="utf-8" ) as arquivo:
                                    escritor03 = csv.writer(arquivo)
                                    escritor03.writerow([materia,nota,aluno])
                                print("\n\033[1;32mNota adicionada com sucesso!\033[m")
                                mais_de_uma_nota = int(input("Digite [1] para adicionar mais notas e [2] finalizar: "))
                                if mais_de_uma_nota == 2:
                                    print("Fim")
                                    break
                                elif mais_de_uma_nota == 1:
                                    print('\nDigite novamente: ')
                                    continue
                            break

                        elif menu_professor == 2:
                            print("Adicione faltas e presenças, digitando 1 para presença e 2 para falta, em seguida o nome do aluno: ")
                            break

                    else:
                        print("\n\033[1;31mUsuário ou senha incorretos.\033[m")
                        continue

            except FileNotFoundError:
                    print("\nNenhum cadastro encontrado ainda")

if opcao_entrada == 2:
    print('\n[1]- Já tenho cadastro\n[2]- Não tenho cadastro')
    cadastro_aluno = int(input('\nDigite a sua opção de entrada: '))
    
    if cadastro_aluno == 2:
        print('\nFaça o seu cadastro do Aluno: ')
        print('-' * 45)
        print('O nome de usuário deverá conter 8 caracteres, pelo menos um maiusculo e um minusculo e um caracter especial.\n')
        username = str(input('Digite o seu usuário: '))
        print('\nA sua senha deverá conter seis caracteres e um caracter especial')
        password = str(input('Digite a sua senha: '))
        with open('dados-aluno.csv', 'a', newline='') as arquivo:
            escritor02 = csv.writer(arquivo)
            escritor02.writerow([username,password])
        print('\n\033[1;32mCadastro efetuado com sucesso!\033[m')

    elif cadastro_aluno == 1:
         while True:
            login = str(input('\nDigite o seu Usuário: '))
            senha = str(input('\nDigite a sua senha: '))
            encontrado_aluno = False
            try:
                with open("dados-aluno.csv", "r", newline="", encoding="utf-8") as arquivo:
                    leitor = csv.reader(arquivo)
                    for linha in leitor:
                        if login == linha [0] and senha == linha [1]:
                            encontrado_aluno = True
                            break

                    if encontrado_aluno:
                        print("\n\033[1;32mLogin realizado com sucesso!\033[m")
                        print("\nBem vindo(a)")
                        menu_aluno = int(input("\n[1]-Boletim\n\n[2]-Presença\n--------> 1 ou 2 "))
                        if menu_aluno == 1:
                            print("-=-" * 30)
                            while True:
                                nome = str(input("\nPara acessar as suas notas, digite o seu nome e sobrenome: "))
                                encontrado_nota = False
                                try:
                                    with open("boletim.csv", 'r', newline='', encoding='utf-8') as arquivo:
                                        leitor = csv.reader(arquivo)
                                        
                                        for linha in leitor:
                                                if len(linha) < 3:
                                                        continue
                                                
                                                materia = linha[0].strip()
                                                nota = linha[1].strip()
                                                nome_csv = linha[2].strip()

                                                if nome == nome_csv:
                                                    print(f"{materia:<10} Nota: {nota}")
                                                    encontrado_nota = True          
                                        if encontrado_nota:
                                            break
                                        else:
                                            print("\n\033[1;31mNome incorreto!\033[m")

                                except FileNotFoundError:
                                    print("\nArquivo do boletim não encontrado.")

                        elif menu_aluno == 2:
                            print("\nPortal presença aluno ".center(60))
                        break
                        
                    else:
                        print("\n\033[1;31mUsuário ou senha incorretos.\033[m")
                        
            except FileNotFoundError:
                print("\n\033[1;31Nenhum cadastro encontrado ainda\033[m")