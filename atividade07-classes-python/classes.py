# Crie uma classe em Python para modelar um objeto a sua escolha.
# Deve conter pelo menos 5 atributos, construtor e getters e setters
# conforme necessário


class Series:
    nome = ""
    genero = ""
    direcao = ""
    roteiro = ""
    canal = ""
    ano_lancamento = ""
    quant_temp = ""

    def __init__(
        self, nome, genero, direcao, roteiro, canal, ano_lancamento, quant_temp
    ):
        """Método Construtor da Classe Series

        Args:
            nome (string): Recebe um valor do tipo string com o nome da série
            genero (string): Recebe um valor do tipo string com o genero da série
            direcao (string): Recebe um valor do tipo string com o nome do diretor
            roteiro (string): Recebe um valor do tipo string com quem escreveu o roteiro
            canal (string): Recebe um valor do tipo string com o nome do canal que se passa a série
            ano_lancamento (string): Recebe um valor do tipo string com o ano de lançamento da serie
            quant_temp (string): Recebe um valor do tipo string com a quantidade de temporadas lançadas
        """
        self.nome = nome
        self.direcao = direcao
        self.roteiro = roteiro
        self.canal = canal
        self.ano_lancamento = ano_lancamento
        self.quant_temp = quant_temp

    # getters and setters da classe Series

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_genero(self, genero):
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_direcao(self, direcao):
        self.direcao = direcao

    def get_direcao(self):
        return self.direcao

    def set_roteiro(self, roteiro):
        self.roteiro = roteiro

    def get_roteiro(self):
        return self.roteiro

    def set_canal(self, canal):
        self.canal = canal

    def get_canal(self):
        return self.canal

    def set_ano_lancamento(self, ano_lancamento):
        self.ano_lancamento = ano_lancamento

    def get_ano_lancamento(self):
        return self.ano_lancamento

    def set_quant_temp(self, quant_temp):
        self.quant_temp = quant_temp

    def get_quant_temp(self):
        return self.quant_temp