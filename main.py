from datetime import datetime
from src.models.cliente import Cliente
from src.models.usuario import Usuario
from src.models.animal import Animal
from src.models.funcionarios import Funcionario, Aplicador
from src.models.vacina import Vacina,AplicacaoVacina
from src.utilities.gerencia_csv import Gerencia_csv
from src.models.estoque_vacina import Agenda
import csv


#Objetos definidos
agenda_sistema = Agenda()
aplicador_obj = Aplicador("Fernanda Biquinho", "12/02/1833", "21 32333212", "132.132.333-22", "Doutura")
aplicacao_vacina_obj = AplicacaoVacina(0,"")



opcao = 0
while opcao != 3:
    print("Olá, Bem vindo ao Sistema de Vacinação de Pets")
    print("1 - Cliente")
    print("2 - Funcionário")
    print("3 - Sair")
    opcao = int(input("Digite sua opção: "))

    match opcao:
        case 1:
            
            print("1 - Já é Cliente")
            print("2 - Ainda não é Cliente")
            opcao2 = int(input("Digite sua opção: "))
            
            match opcao2:
                case 1:
                    
                    login = input("Informe seu login:")
                    senha = input("Informe senha:")
                    verificacao = Cliente.autentica_usuario(Cliente, 'src\Database\Banco_Cliente.csv', login, senha)
                    if (verificacao == True):
                        #Caso cliente seja autenticado, cria-se um objeto a partir dos dados armazenados
                        cliente_obj = ''
                        with open ("src\Database\Banco_Cliente.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter=',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[4] == login:
                                        cliente_obj = Cliente(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6])
                        opcao3 = 0
                        
                        while opcao3 != 5:
                            print("1 - Cadastrar Pet")
                            print("2 - Agendar Vacina")
                            print("3 - Aplicar Vacina")
                            print("4 - Verificar Pets")
                            print("5 - Sair")
                            opcao3 = int(input("Digite sua opção: "))
                            match opcao3:
                                case 1:
                                    #os inputs estao dentro do metodo que o objeto chama, e ele retorna o animla
                                    cliente_obj.Cadastrar_pet()
                                
                                case 2:
                                    
                                    Gerencia_csv.ler_arquivo('src\Database\Banco_Datas.csv')
                                    
                                    data = str(input("Informe uma data: "))
                                    vacina = str(input("Informe o nome da vacina: "))

                                    vacina_obj = ''
                                    try:
                                        with open ("src\Database\Banco_Vacinas.csv", mode ='r') as arq:
                                            leitor_csv = csv.reader(arq, delimiter =',')
                                            next(leitor_csv)
                                            for atributo in leitor_csv:
                                                if atributo[0] == vacina:
                                                    vacina_obj = Vacina(atributo[0],atributo[1],atributo[2],atributo[3])
                                    except:
                                        print("Não existe uma vacina com esse nome")
                                        break
                        
                        
                                    animal = str(input("Informe o nome do animal: "))
                        
                                    try:
                                        with open ("src\Database\Banco_Animais.csv", mode ='r') as arq:
                                            leitor_csv = csv.reader(arq, delimiter =',')
                                            next(leitor_csv)
                                            for atributo in leitor_csv:
                                                if atributo[0] == animal:
                                                    if atributo[5] == cliente_obj.nome_completo:
                                                        animal_obj = Animal(atributo[0],atributo[1],atributo[3],atributo[4],atributo[5])
                                    except:
                                        print("Não foi possivel achar o animal")
                                    cliente_obj.Agendar_vacina(data, animal_obj, cliente_obj, agenda_sistema, vacina_obj.nome)
                                
                                case 3:
                                    
                                    nome_pet = input("Digite o nome do animal: ")
                                    animal_obj,cliente_obj = agenda_sistema.verificar_agendamentos(cliente_obj.nome_completo,nome_pet)
                                    cliente_obj.Aplicar_vacina(vacina_obj,animal_obj,aplicador_obj,aplicacao_vacina_obj)
                                
                                case 4:

                                    cliente_obj.Visualizar_pets()

                                case 5:
                                    break
                    else:
                        print("Não foi possivel encontrar seu cadastro")

                case 2:

                    nome = input("Informe seu nome: ")
                    data = str(input("Informe uma data: "))
                    formato = "%d/%m/%Y"
                    data = datetime.strptime(data, formato)
                    data = data.date()
                    telefone = str(input("Informe seu telefone: "))
                    cpf = str(input("Informe seu cpf: "))
                    login = str(input("Crie um login: "))
                    senha = str(input("Crie uma senha: "))
                    email =str(input("Informe seu email: "))

                    cliente_objeto = Cliente(nome, data, telefone, cpf, login, senha, email)
                    dados = [[nome, data, telefone, cpf, login, senha, email]]
                    Gerencia_csv.escrever_arquivo(Gerencia_csv,"src\Database\Banco_Cliente.csv", dados)

                    
        case 2:

            print("TELA DO FUNCIONÁRIO")
            #autenticando funcionario
            login = input("Informe o login: ")
            senha = input("Informe a senha: ")
            verificacao = Funcionario.autentica_funcionario(Funcionario,"src\Database\Banco_Funcionarios.csv",login, senha)
            if (verificacao == True):
                #Caso funcionario seja autenticado, cria-se um objeto a partir dos dados armazenados
                funcionario_obj = ''
                with open ("src\Database\Banco_Funcionarios.csv", mode ='r') as arq:
                        leitor_csv = csv.reader(arq, delimiter =',')
                        next(leitor_csv)
                        for atributo in leitor_csv:
                            if atributo[6] == login:
                                funcionario_obj = Funcionario(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6], atributo[7], atributo[8])
    
            print("1- Cadastrar um novo cliente")
            print("2 - Cadastrar um animal")
            print("3 - Verificar datas de vacinações disponíveis")
            print("4 - Verificar vacinas disponíveis")
            print("5 - Agendar uma vacincação")
            print("6 - Aplicar uma vacina")
            print("7 - Sair")
            opcao4 = 0

            while opcao4 !=7:
                
                opcao4 = int(input("Digite sua opção: "))
                
                match (opcao4):
                    
                    case 1:
                        #funcionario pega os dados do cliente e adiciona no banco de dados
                        funcionario_obj.Cadastrar_Cliente()
                    
                    case 2:
                        
                        nome_cli = input("Informe o nome do cliente: ")

                        cliente_obj1 = ''
                        try:
                            with open ("src/Database/Banco_Cliente.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter =',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[0] == nome_cli:
                                        cliente_obj1 = Cliente(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6])
                            cliente_obj1.Cadastrar_pet()
                        except:
                            print("Não foi possivel achar um cliente com esse nome")
                    
                    case 3:
                        
                        Gerencia_csv.ler_arquivo('src\Database\Banco_Datas.csv')
                    
                    case 4:
                        
                        Gerencia_csv.ler_arquivo('src\Database\Banco_Vacinas.csv')
                    
                    case 5:
                        
                        Gerencia_csv.ler_arquivo('src\Database\Banco_Datas.csv')
                        
                        data = str(input("Informe uma data: "))
                        vacina = input("Informe o nome da vacina: ")
                        
                        vacina_obj = ''
                        try:
                            with open ("src\Database\Banco_Vacinas.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter =',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[0] == vacina:
                                        vacina_obj = Vacina(atributo[0],atributo[1],atributo[2],atributo[3])
                        except:
                            print("Não existe uma vacina com esse nome")
                            break
                        nome_cli = input("Digite o nome do cliente: ")
                        
                        cliente_obj1 = ''
                        
                        try:
                            with open ("src/Database/Banco_Cliente.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter =',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[0] == nome_cli:
                                        cliente_obj1 = Cliente(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6])
                        except:
                            print("Não foi possivel achar o cliente")
                        
                        animal = str(input("Informe o nome do animal: "))
                        
                        try:
                            with open ("src\Database\Banco_Animais.csv", mode ='r') as arq:
                                leitor_csv = csv.reader(arq, delimiter =',')
                                next(leitor_csv)
                                for atributo in leitor_csv:
                                    if atributo[0] == animal:
                                        if atributo[5] == cliente_obj1.nome_completo:
                                            animal_obj = Animal(atributo[0],atributo[1],atributo[3],atributo[4],atributo[5])
                        except:
                            print("Não foi possivel achar o animal")
                        cliente_obj1.Agendar_vacina(data, animal_obj, cliente_obj1, agenda_sistema, vacina_obj.nome)
                    case 6:
                        nome_cli = input("Digite o nome do cliente: ")
                        nome_pet = input("Digite o nome do animal: ")
                        animal_obj,cliente_obj = agenda_sistema.verificar_agendamentos(nome_cli,nome_pet)
                        cliente_obj.Aplicar_vacina(vacina_obj,animal_obj,aplicador_obj,aplicacao_vacina_obj)
                    
                    case 7:
                        break
        case 3:
            break

