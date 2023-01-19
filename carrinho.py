from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja está comendo!')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        if self.falando:
            print(f'{self.nom} não pode comer enquanto fala!')
            return
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo agora.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come')
            return
        if self.falando:
            print(f'{self.nome} ja está falando sobre {assunto}')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        print(f'{self.nome} parou de falar!')
        self.falando = False

    def ano_nascimento(self):
        print(self.ano_atual - self.idade)