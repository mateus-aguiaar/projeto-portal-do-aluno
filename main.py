import src.interface as ui
import csv
import os 
os.system("cls")

titulo = "\033[1;31mPORTAL DO ALUNO\033[m"
print(titulo.center(80))
print("-=-" * 25)

opcao_entrada = int(input(ui.MENU_INICIAL))

if opcao_entrada == 1:
    cadastro_professor = int(input(ui.MENU_OPCAO_ENTRADA))

    if cadastro_professor == 2:
        print(ui.CADASTRO_PROFESSOR)
        usuario_professor = str(input("Usuário: "))
        print("\nA sua senha deverá conter seis caracteres e um caracter especial")
        password_professor = str(input("\nDigite a sua senha: "))
        with open('dados-professor.csv', 'a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([usuario_professor,password_professor])
        print("\n\033[1;32mCadastro efetuado com sucesso!\033[m")
        
    elif cadastro_professor == 1:
        while True:
            login = input("\nDigite o usuário: ")
            password = input("\nDigite a sua senha: ")
            encontrado_professor = False
            try:
                with open("dados-professor.csv", "r", newline="", encoding="utf-8") as arquivo:
                    leitor = csv.reader(arquivo)

                    for linha in leitor:
                        if login == linha[0] and password == linha[1]:
                            encontrado_professor = True
                            break
                    
                    if encontrado_professor:
                        menu_professor = int(input(ui.MENU_PROFESSOR))
                        
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
                                    break
                                elif mais_de_uma_nota == 1:
                                    continue
                            break

                        elif menu_professor == 2:
                            materia_falta = str(input("Digite a respectiva matéria na qual o aluno faltou: "))
                            faltas = int(input('Digite a quantidade de faltas: '))
                            aluno_falta = str(input("Digite o nome e sobrenome do respectivo aluno: "))
                            with open("faltas.csv", "a", newline="", encoding="utf-8") as arquivo:
                                    escritor04 = csv.writer(arquivo)
                                    escritor04.writerow([materia_falta,faltas,aluno_falta])
                            print("\n\033[1;32mPresença/falta adicionada com sucesso!\033[m")  
                            break

                    else:
                        print("\n\033[1;31mUsuário ou senha incorretos.\033[m")
                        continue

            except FileNotFoundError:
                    print("\nNenhum cadastro encontrado ainda")

if opcao_entrada == 2:
    cadastro_aluno = int(input(ui.MENU_OPCAO_ENTRADA_ALUNO))
    
    if cadastro_aluno == 2:
        print(ui.CADASTRO_ALUNO)
        username = str(input('Digite o seu usuário: '))
        print('\nA sua senha deverá conter seis caracteres e um caracter especial')
        password = str(input('Digite a sua senha: '))
        with open('dados-aluno.csv', 'a', newline='') as arquivo:
            escritor02 = csv.writer(arquivo)
            escritor02.writerow([username,password])
        print('\n\033[1;32mCadastro efetuado com sucesso!\033[m')

    elif cadastro_aluno == 1:
            while True:  # WHILE DO LOGIN
                login = input('\nDigite o seu Usuário: ').strip()
                senha = input('\nDigite a sua senha: ').strip()
                encontrado_aluno = False
                try:
                    with open("dados-aluno.csv", "r", newline="", encoding="utf-8") as arquivo:
                        leitor = csv.reader(arquivo)

                        for linha in leitor:  # FOR DO CSV DE LOGIN
                            if login == linha[0] and senha == linha[1]:
                                encontrado_aluno = True
                                break  # sai do FOR do login

                    if encontrado_aluno:
                        menu_aluno = int(input(ui.MENU_ALUNO))

                        if menu_aluno == 1:
                            while True:  # WHILE DAS NOTAS
                                nome = input("\nPara acessar as suas notas, digite o seu nome e sobrenome: ").strip()
                                encontrado_nota = False

                                try:
                                    with open("boletim.csv", "r", newline="", encoding="utf-8") as arquivo:
                                        leitor = csv.reader(arquivo)

                                        for linha in leitor:  # FOR DO CSV DE NOTAS
                                            if len(linha) < 3:
                                                continue

                                        materia = linha[0].strip()
                                        nota = linha[1].strip()
                                        nome_csv = linha[2].strip()

                                        if nome.lower() == nome_csv.lower():
                                            print(f"{materia:<10}-----------> Nota: {nota}")
                                            encontrado_nota = True

                                    if encontrado_nota:
                                        break  # sai do WHILE DAS NOTAS
                                    else:
                                        print("\n\033[1;31mNome incorreto!\033[m")

                                except FileNotFoundError:
                                    print("\nArquivo do boletim não encontrado.")
                                    break

                        elif menu_aluno == 2:
                            print("\nPortal presença aluno ".center(60))

                            while True:
                                nome_falta = input("\nPara acessar as suas faltas, digite o seu nome e sobrenome: ").strip()
                                encontrado_falta = False

                                try:
                                    with open("faltas.csv", "r", newline="", encoding="utf-8") as arquivo2:
                                        leitor2 = csv.reader(arquivo2)

                                        for linha in leitor2:
                                            if len(linha) < 3:
                                                continue

                                            materia_falta = linha[0].strip()
                                            faltas = linha[1].strip()
                                            aluno_falta = linha[2].strip()

                                            if nome_falta.lower() == aluno_falta.lower():
                                                print(f"{materia_falta} -----------> faltas: {faltas}")
                                                encontrado_falta = True

                                    if encontrado_falta:
                                        break
                                    
                                    else:
                                        print("\n\033[1;31mNome incorreto!\033[m")

                                except FileNotFoundError:
                                    print("\n\033[1;31mArquivo de faltas não encontrado.\033[m")
                        break

                    else:
                        print("\n\033[1;31mUsuário ou senha incorretos!\033[m")

                except FileNotFoundError:
                    print("\n\033[1;31mArquivo de alunos não encontrado.\033[m")
                    break