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
        self.regras()
    def regras(self):
        print(
            f'{self.nome_usuario}, estas são as regras de como jogar:\n'
            f'O jogo é composto por 20 perguntas, em cada pergunta você terá que escolher Verdadeiro (v) ou Falso (F)\n'
            f'Se você acertar, ganhará um ponto, se errar, não ganhará nada.\n'
        )
        while self.autenticado == None:
            self.cont = input("Deseja continuar ? \n Sim - S\n Não - N\nDigite: ")
            if self.cont == 's' or self.cont == 'S':
                self.pergunta_1()

    def pergunta_1(self):
        print(
            'Um sistema é um grupo de elementos inter-relacionados atuando juntos em direção a uma meta comum, recebendo insumos e produzindo resultados em um processo organizado de transformação.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_2()
        else:
            print("Você errou :(")
            print("Um sistema é um grupo de elementos inter-relacionados atuando juntos em direção a uma meta comum, recebendo insumos e produzindo resultados em um processo organizado de transformação.")
            print("Esta frase é verdadeira")
            self.pergunta_2()
    def pergunta_2(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_3()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_3()
    def pergunta_3(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_4(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_5()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_5()

    def pergunta_5(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_6(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_7(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_8(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_9(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_10(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_11(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_12(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_13(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_14(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_15(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()
    def pergunta_16(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_17(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_18(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()


    def pergunta_19(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()
    def pergunta_20(self):
        print(
            'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
        )
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print(
                'Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.'
            )
            print("Esta frase é verdadeira")
            self.pergunta_4()





    def mostrar_resultado(self):
        pass


if __name__ == '__main__':
    App()
