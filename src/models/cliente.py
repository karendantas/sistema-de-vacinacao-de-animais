from src.models.usuario import Pessoa, Usuario
from src.models.animal import Animal
from src.utilities.gerencia_csv import Gerencia_csv
from datetime import datetime

class Cliente(Pessoa, Usuario, Gerencia_csv):
    def __init__(self, nome_completo, data_nascimento, telefone, cpf, login, senha, email):
        Pessoa.__init__(self, nome_completo, data_nascimento, telefone, cpf)
        Usuario.__init__(self,login, senha, email)
        self.animais = []

    def Cadastrar_pet(self):
        '''
            O método 'Cadastrar_pet' está na classe 'Usuario', por isso
            está sendo chamada pela classe Pai. O retorno da classe gera um objeto de animal
            que sera armazenado na variavel 'animal'

            Depois que a variavel conter de certeza um objeto de animal, ele sera adiconado
            a lista de animais do cliente e os dados do objeto serao enviados para o arquivo
            'Banco_Animais'
        
        '''
        nome_pet = input("Informe o nome do animal: ")
        data_pet = str(input("Informe a data de nascimento do animal:"))
        formato = "%d/%m/%Y"
        data_pet = datetime.strptime(data_pet, formato)
        data_pet = data_pet.date()
        raça_pet = input("Informe a reaça do animal: ")
        sexo_pet = input("Informe o sexo do animal: ")
        especie_pet = input("Informe a especie do animal:")

        animal = Animal(nome_pet, raça_pet, especie_pet, data_pet,sexo_pet )
        self.animais.append(animal)

        dados = [[nome_pet, raça_pet, especie_pet, data_pet, sexo_pet]]
        Gerencia_csv().escrever_arquivo("src\Database\Banco_Animais.csv", dados)

            
    def Agendar_vacina(self, data, Animal, Cliente, Agenda, Vacina):
        '''
           Esse metodo irá receber os args e irá alocar em um dict. 
           Esse dict irá ser alocado na classe Agenda por meio do metódo set_agendamentos

            Args:
            data: uma string no formato datetime
            animal: (object) uma instancia da classe Animal
            cliente: (object) uma instancia da classe Cliente
            agenda: (object) uma instancia da classe Agenda
            vacina: (object) uma instancia da classe Vacina
        '''

        if Gerencia_csv.verificar_datas(Gerencia_csv,data):
            agendamento = {}
            agendamento = {"Cliente: ": Cliente,"Animal: ": Animal,"Data: ": data,"Vacina: ": Vacina}
            Agenda.set_agendamentos(agendamento)
        else:
            print("Data informada inválida")
    
    def Aplicar_vacina(self,vacina, animal,aplicador,aplicacao_vacina):
        '''
        
        Simula a hora que o cliente leva o animal para receber a vacina, adicionando ao 
        histórico do animal a vacina recebida.

        Args:
        vacina: (Object) Uma instancia da Vacina a ser utilizada
        animal: (Object) Uma instancia de Animal
        aplicador: (Object) Uma instancia de Aplicador
        aplicacao_vacina: (Object) Uma instancia de Aplicacao_Vacina
        
        '''

        if aplicador is None:
            print("Não foi possível efetuar a vacinação")
        else:
            aplicacao_vacina.data_aplicacao = datetime.today()
            animal.setHistoricoVacinas("Vacina: {}\nAplicador: {}\nData aplicação Vacina: {}".format(vacina.nome,
            aplicador.nome_completo,aplicacao_vacina.data_aplicacao))


    def Visualizar_pets(self):
        for i in self.animais:
            print("Nome: {}\nEspécie: {}\nRaça: {}\nData de Nascimento: {}".format(i.nome,i.especie,i.raca,i.data_nascimento))