class App:
    def __init__(self):
        self.pontuacao = 0
        self.descobrir_nome()

    def descobrir_nome(self):
        self.autenticado = None
        while self.autenticado == None:
            self.nome_usuario = input("Digite seu nome: ")
            if '1' in self.nome_usuario or '2' in self.nome_usuario or '3' in self.nome_usuario or '4' in self.nome_usuario or '5' in self.nome_usuario or '6' in self.nome_usuario or '7' in self.nome_usuario or '8' in self.nome_usuario or '9' in self.nome_usuario or '0' in self.nome_usuario:
                print('Seu nome não pode conter número, digite novamente')
            else:
                self.autenticado = True
                print(f"Bem-Vindo ao jogo, {self.nome_usuario}")
    def regras(self):
        print(
            f''



        )


    def pergunta_1(self):
        self.pergunta_2()
        pass
    def pergunta_2(self):
        self.pergunta_3()
        pass
    def pergunta_3(self):
        self.pergunta_4()
        pass
    def pergunta_4(self):
        self.pergunta_5()
        pass
    def pergunta_5(self):
        self.pergunta_6()
        pass
    def pergunta_6(self):
        self.pergunta_7()
        pass
    def pergunta_7(self):
        self.pergunta_8()
        pass
    def pergunta_8(self):
        self.pergunta_9()
        pass
    def pergunta_9(self):
        self.pergunta_10()
        pass
    def pergunta_10(self):
        self.pergunta_11()
        pass
    def pergunta_11(self):
        self.pergunta_12()
        pass
    def pergunta_12(self):
        self.pergunta_13()
        pass
    def pergunta_13(self):
        self.pergunta_14()
        pass
    def pergunta_14(self):
        self.pergunta_15()
        pass
    def pergunta_15(self):
        self.pergunta_16()
        pass
    def pergunta_16(self):
        self.pergunta_17()
        pass
    def pergunta_17(self):
        self.pergunta_18()
        pass
    def pergunta_18(self):
        self.pergunta_19()
        pass
    def pergunta_19(self):
        self.pergunta_20()
        pass
    def pergunta_20(self):
        self.mostrar_resultado()
        pass
    def mostrar_resultado(self):
        pass


if __name__ == '__main__':
    App()
