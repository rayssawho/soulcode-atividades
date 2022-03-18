# +----------------------------------------------------+
# |  SoulCode Academy                                  |
# |  Atividade 14 - Herança e Polimorfismo             |
# |  Rayssa Alcântara Melo                             |
# +----------------------------------------------------+

from modules.pessoa import Pessoa
from modules.funcionario import Funcionario
from modules.aluno import Aluno
from modules.aluno_matematica import Aluno_mat
from modules.aluno_portugues import Aluno_port

if __name__ == "__main__":
    try:
        # Instanciando a classe Pessoa

        pessoa_1 = Pessoa("Rayssa", "6895412", "Rua L", "3453246752")
        print("Nome: ", pessoa_1.get_nome(), "\n"
              "RG:", pessoa_1.get_rg(), "\n"
              "Endereço: ", pessoa_1.get_endereco(), "\n"
              "Contato: ", pessoa_1.get_contato(), "\n")

        pessoa_2 = Pessoa("Marina", "7658901", "Rua M", "345621134")
        print("Nome: ", pessoa_2.get_nome(), "\n"
              "RG:", pessoa_2.get_rg(), "\n"
              "Endereço: ", pessoa_2.get_endereco(), "\n"
              "Contato: ", pessoa_2.get_contato(), "\n")

        pessoa_3 = Pessoa("Lucas", "8765343", "Rua A", "875435762")
        print("Nome: ", pessoa_3.get_nome(), "\n"
              "RG:", pessoa_3.get_rg(), "\n"
              "Endereço: ", pessoa_3.get_endereco(), "\n"
              "Contato: ", pessoa_3.get_contato(), "\n")

        pessoa_4 = Pessoa("Maria", "9874857", "Rua P", "345631114")
        print("Nome: ", pessoa_4.get_nome(), "\n"
              "RG:", pessoa_4.get_rg(), "\n"
              "Endereço: ", pessoa_4.get_endereco(), "\n"
              "Contato: ", pessoa_4.get_contato(), "\n")

        pessoa_5 = Pessoa("Paulo", "4598651", "Rua B", "958741365")
        print("Nome: ", pessoa_5.get_nome(), "\n"
              "RG:", pessoa_5.get_rg(), "\n"
              "Endereço: ", pessoa_5.get_endereco(), "\n"
              "Contato: ", pessoa_5.get_contato(), "\n")

        pessoa_6 = Pessoa("Vinicius", "1207644", "Rua C", "984575822")
        print("Nome: ", pessoa_6.get_nome(), "\n"
              "RG:", pessoa_6.get_rg(), "\n"
              "Endereço: ", pessoa_6.get_endereco(), "\n"
              "Contato: ", pessoa_6.get_contato(), "\n")

    except Exception as e:
        print(str(e))

    try:
        # Instanciando a classe Funcionário

        funcionario_1 = Funcionario("Gil", "23098765", "Rua O", "7687980965",
                                    "1", "Estagiário")
        print("Nome: ", funcionario_1.get_nome(), "\n"
              "RG:", funcionario_1.get_rg(), "\n"
              "Endereço: ", funcionario_1.get_endereco(), "\n"
              "Contato: ", funcionario_1.get_contato(), "\n"
              "ID: ", funcionario_1.get_id_func(), "\n"
              "Cargo: ", funcionario_1.get_cargo(), "\n")

        funcionario_2 = Funcionario("Lindon", "54678942", "Rua X",
                                    "0912354312", "2", "Cozinheiro")
        print("Nome: ", funcionario_2.get_nome(), "\n"
              "RG:", funcionario_2.get_rg(), "\n"
              "Endereço: ", funcionario_2.get_endereco(), "\n"
              "Contato: ", funcionario_2.get_contato(), "\n"
              "ID: ", funcionario_2.get_id_func(), "\n"
              "Cargo: ", funcionario_2.get_cargo(), "\n")

        funcionario_3 = Funcionario("Laís", "234543212", "Rua Z", "6584958423",
                                    "3", "Fotógrafa")
        print("Nome: ", funcionario_3.get_nome(), "\n"
              "RG:", funcionario_3.get_rg(), "\n"
              "Endereço: ", funcionario_3.get_endereco(), "\n"
              "Contato: ", funcionario_3.get_contato(), "\n"
              "ID: ", funcionario_3.get_id_func(), "\n"
              "Cargo: ", funcionario_3.get_cargo(), "\n")

        funcionario_4 = Funcionario("Dani", "456543235", "Rua S", "8764523462",
                                    "4", "Faxineira")
        print("Nome: ", funcionario_4.get_nome(), "\n"
              "RG:", funcionario_4.get_rg(), "\n"
              "Endereço: ", funcionario_4.get_endereco(), "\n"
              "Contato: ", funcionario_4.get_contato(), "\n"
              "ID: ", funcionario_4.get_id_func(), "\n"
              "Cargo: ", funcionario_4.get_cargo(), "\n")

        funcionario_5 = Funcionario("Junior", "45324687", "Rua D",
                                    "6763889642", "5", "Motorista")
        print("Nome: ", funcionario_5.get_nome(), "\n"
              "RG:", funcionario_5.get_rg(), "\n"
              "Endereço: ", funcionario_5.get_endereco(), "\n"
              "Contato: ", funcionario_5.get_contato(), "\n"
              "ID: ", funcionario_5.get_id_func(), "\n"
              "Cargo: ", funcionario_5.get_cargo(), "\n")

    except Exception as e:
        print(str(e))

    try:
        # Instanciando a classe Aluno

        aluno_1 = Aluno("Veronica", "9864123", "Rua N", "veronica@gmail.com",
                        "87456")
        print("Nome: ", aluno_1.get_nome(), "\n"
              "RG:", aluno_1.get_rg(), "\n"
              "Endereço: ", aluno_1.get_endereco(), "\n"
              "Contato: ", aluno_1.get_contato(), "\n"
              "Matrícula: ", aluno_1.get_matricula(), "\n")

        aluno_2 = Aluno("Thiago", "435689", "Rua T", "thiago@gmail.com",
                        "87452")
        print("Nome: ", aluno_2.get_nome(), "\n"
              "RG:", aluno_2.get_rg(), "\n"
              "Endereço: ", aluno_2.get_endereco(), "\n"
              "Contato: ", aluno_2.get_contato(), "\n"
              "Matrícula: ", aluno_2.get_matricula(), "\n")

        aluno_3 = Aluno("Dyego", "7889533", "Rua W", "878908653", "87445")
        print("Nome: ", aluno_3.get_nome(), "\n"
              "RG:", aluno_3.get_rg(), "\n"
              "Endereço: ", aluno_3.get_endereco(), "\n"
              "Contato: ", aluno_3.get_contato(), "\n"
              "Matrícula: ", aluno_3.get_matricula(), "\n")

        aluno_4 = Aluno("Sthefanny", "567997832", "Rua G", "567643232",
                        "87471")
        print("Nome: ", aluno_4.get_nome(), "\n"
              "RG:", aluno_4.get_rg(), "\n"
              "Endereço: ", aluno_4.get_endereco(), "\n"
              "Contato: ", aluno_4.get_contato(), "\n"
              "Matrícula: ", aluno_4.get_matricula(), "\n")

        aluno_5 = Aluno("Welida", "87790321", "Rua K", "9868907652", "87534")
        print("Nome: ", aluno_5.get_nome(), "\n"
              "RG:", aluno_5.get_rg(), "\n"
              "Endereço: ", aluno_5.get_endereco(), "\n"
              "Contato: ", aluno_5.get_contato(), "\n"
              "Matrícula: ", aluno_5.get_matricula(), "\n")

    except Exception as e:
        print(str(e))

    try:
        # Instanciando a classe Aluno_port

        aluno_pt_1 = Aluno_port("Greice", "6789043", "Rua Y", "8787876534",
                                "23543", "9.0")
        print("Nome: ", aluno_pt_1.get_nome(), "\n"
              "RG:", aluno_pt_1.get_rg(), "\n"
              "Endereço: ", aluno_pt_1.get_endereco(), "\n"
              "Contato: ", aluno_pt_1.get_contato(), "\n"
              "Matrícula: ", aluno_pt_1.get_matricula(), "\n"
              "Nota: ", aluno_pt_1.get_nota_port(), "\n")

        aluno_pt_2 = Aluno_port("Juliana", "3456534", "Rua E", "987862311",
                                "23545", "7.0")
        print("Nome: ", aluno_pt_2.get_nome(), "\n"
              "RG:", aluno_pt_2.get_rg(), "\n"
              "Endereço: ", aluno_pt_2.get_endereco(), "\n"
              "Contato: ", aluno_pt_2.get_contato(), "\n"
              "Matrícula: ", aluno_pt_2.get_matricula(), "\n"
              "Nota: ", aluno_pt_2.get_nota_port(), "\n")

        aluno_pt_3 = Aluno_port("Joana", "323214", "Rua P", "982345431",
                                "33548", "9.5")
        print("Nome: ", aluno_pt_3.get_nome(), "\n"
              "RG:", aluno_pt_3.get_rg(), "\n"
              "Endereço: ", aluno_pt_3.get_endereco(), "\n"
              "Contato: ", aluno_pt_3.get_contato(), "\n"
              "Matrícula: ", aluno_pt_3.get_matricula(), "\n"
              "Nota: ", aluno_pt_3.get_nota_port(), "\n")

        aluno_pt_4 = Aluno_port("Ana", "4987654", "Rua R", "912335141",
                                "44560", "9.8")
        print("Nome: ", aluno_pt_4.get_nome(), "\n"
              "RG:", aluno_pt_4.get_rg(), "\n"
              "Endereço: ", aluno_pt_4.get_endereco(), "\n"
              "Contato: ", aluno_pt_4.get_contato(), "\n"
              "Matrícula: ", aluno_pt_4.get_matricula(), "\n"
              "Nota: ", aluno_pt_4.get_nota_port(), "\n")

        aluno_pt_5 = Aluno_port("Rafael", "5120955", "Rua Q", "916754342",
                                "55568", "8.8")
        print("Nome: ", aluno_pt_5.get_nome(), "\n"
              "RG:", aluno_pt_5.get_rg(), "\n"
              "Endereço: ", aluno_pt_5.get_endereco(), "\n"
              "Contato: ", aluno_pt_5.get_contato(), "\n"
              "Matrícula: ", aluno_pt_5.get_matricula(), "\n"
              "Nota: ", aluno_pt_5.get_nota_port(), "\n")

    except Exception as e:
        print(str(e))

    try:
        # Instanciando a classe Aluno_mat

        aluno_mat_1 = Aluno_mat("Lafayette", "985647", "Rua Ç", "897845347",
                                "78451", "8.5")
        print("Nome: ", aluno_mat_1.get_nome(), "\n"
              "RG:", aluno_mat_1.get_rg(), "\n"
              "Endereço: ", aluno_mat_1.get_endereco(), "\n"
              "Contato: ", aluno_mat_1.get_contato(), "\n"
              "Matrícula: ", aluno_mat_1.get_matricula(), "\n"
              "Nota: ", aluno_mat_1.get_nota_mat(), "\n")

        aluno_mat_2 = Aluno_mat("Sandra", "3452344", "Rua V", "983442111",
                                "76543", "9.0")
        print("Nome: ", aluno_mat_2.get_nome(), "\n"
              "RG:", aluno_mat_2.get_rg(), "\n"
              "Endereço: ", aluno_mat_2.get_endereco(), "\n"
              "Contato: ", aluno_mat_2.get_contato(), "\n"
              "Matrícula: ", aluno_mat_2.get_matricula(), "\n"
              "Nota: ", aluno_mat_2.get_nota_mat(), "\n")

        aluno_mat_3 = Aluno_mat("Bianca", "3121209", "Rua N", "912098451",
                                "76512", "9.0")
        print("Nome: ", aluno_mat_3.get_nome(), "\n"
              "RG:", aluno_mat_3.get_rg(), "\n"
              "Endereço: ", aluno_mat_3.get_endereco(), "\n"
              "Contato: ", aluno_mat_3.get_contato(), "\n"
              "Matrícula: ", aluno_mat_3.get_matricula(), "\n"
              "Nota: ", aluno_mat_3.get_nota_mat(), "\n")

        aluno_mat_4 = Aluno_mat("Bertrand", "478956", "Rua J", "9127845963",
                                "24589", "8.0")
        print("Nome: ", aluno_mat_4.get_nome(), "\n"
              "RG:", aluno_mat_4.get_rg(), "\n"
              "Endereço: ", aluno_mat_4.get_endereco(), "\n"
              "Contato: ", aluno_mat_4.get_contato(), "\n"
              "Matrícula: ", aluno_mat_4.get_matricula(), "\n"
              "Nota: ", aluno_mat_4.get_nota_mat(), "\n")

        aluno_mat_5 = Aluno_mat("Renan", "6145265", "Rua U", "916458922",
                                "74589", "6.0")
        print("Nome: ", aluno_mat_5.get_nome(), "\n"
              "RG:", aluno_mat_5.get_rg(), "\n"
              "Endereço: ", aluno_mat_5.get_endereco(), "\n"
              "Contato: ", aluno_mat_5.get_contato(), "\n"
              "Matrícula: ", aluno_mat_5.get_matricula(), "\n"
              "Nota: ", aluno_mat_5.get_nota_mat(), "\n")

    except Exception as e:
        print(str(e))
