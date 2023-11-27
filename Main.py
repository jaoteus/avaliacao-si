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
        self.pergunta_1()

    def pergunta_1(self):
        print('Um sistema é um grupo de elementos inter-relacionados atuando juntos em direção a uma meta comum, recebendo insumos e produzindo resultados em um processo organizado de transformação.')
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
        print('Segundo Mattos (2005), um sistema de informação é um sistema especializado no processamento e na comunicação de dados (máquinas) ou de informações (organismos vivos), sendo constituído por um conjunto de módulos (objetos) de comunicação, de controle, de memórias e de processadores, interligados entre si, por meio de uma rede com protocolo comum.')
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
        print('Dados são sucessões de fatos brutos que não foram organizados, processados, relacionados, avaliados ou interpretados, representando apenas, partes isoladas de eventos, situações ou ocorrências. Constituem as unidades básicas, a partir das quais, informações poderão ser elaboradas ou obtidas (CORTÊZ, 2008).')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_4()
        else:
            print("Você errou :(")
            print('Dados são sucessões de fatos brutos que não foram organizados, processados, relacionados, avaliados ou interpretados, representando apenas, partes isoladas de eventos, situações ou ocorrências. Constituem as unidades básicas, a partir das quais, informações poderão ser elaboradas ou obtidas (CORTÊZ, 2008).')

            print("Esta frase é verdadeira")
            self.pergunta_4()

    def pergunta_4(self):
        print('Um banco de dados é uma entidade na qual é possível armazenar dados de maneira estruturada e com a menor redundância possível.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_5()
        else:
            print("Você errou :(")
            print('Um banco de dados é uma entidade na qual é possível armazenar dados de maneira estruturada e com a menor redundância possível.')
            print("Esta frase é verdadeira")
            self.pergunta_5()

    def pergunta_5(self):
        print('Data warehouse é o conjunto de hardware e software que possibilitam o acesso a dados estratificados e consolidados de forma consistente e rápida, a fim de evitar buscas redundantes e dispersivas pelos diversos repositórios genéricos existentes na organização.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_6()
        else:
            print("Você errou :(")
            print(
                'Data warehouse é o conjunto de hardware e software que possibilitam o acesso a dados estratificados e consolidados de forma consistente e rápida, a fim de evitar buscas redundantes e dispersivas pelos diversos repositórios genéricos existentes na organização.')

            print("Esta frase é verdadeira")
            self.pergunta_6()

    def pergunta_6(self):
        print('Sistemas de nível de conhecimento: Permitem à empresa integrar novos conhecimentos e controlar o fluxo de documentos, informação necessária para criação de novos projetos e geração de documentos oficiais.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_7()
        else:
            print("Você errou :(")
            print(
                'Sistemas de nível de conhecimento: Permitem à empresa integrar novos conhecimentos e controlar o fluxo de documentos, informação necessária para criação de novos projetos e geração de documentos oficiais.')

            print("Esta frase é verdadeira")
            self.pergunta_7()

    def pergunta_7(self):
        print('Sistemas de Automação de Escritório: São sistemas que servem as necessidades de informação ao nível de conhecimento da organização.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_8()
        else:
            print("Você errou :(")
            print(
                'Sistemas de Automação de Escritório: São sistemas que servem as necessidades de informação ao nível de conhecimento da organização.')

            print("Esta frase é verdadeira")
            self.pergunta_8()

    def pergunta_8(self):
        print('Sistemas de Suporte Executivo: O SSE não são projetados para resolver problemas específicos, eles fornecem uma generalizada capacidade de computação e telecomunicação que pode ser aplicada a problemas que se alteram.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_9()
        else:
            print("Você errou :(")
            print('Sistemas de Suporte Executivo: O SSE não são projetados para resolver problemas específicos, eles fornecem uma generalizada capacidade de computação e telecomunicação que pode ser aplicada a problemas que se alteram.')
            print("Esta frase é verdadeira")
            self.pergunta_9()

    def pergunta_9(self):
        print('O Instituto Nacional de Propriedade Intelectual (INPI) é o Órgão brasileiro responsável pelo controle das marcas, patentes, desenho industrial, transferência de tecnologia, indicação geográfica e programas de computador.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_10()
        else:
            print("Você errou :(")
            print('O Instituto Nacional de Propriedade Intelectual (INPI) é o Órgão brasileiro responsável pelo controle das marcas, patentes, desenho industrial, transferência de tecnologia, indicação geográfica e programas de computador.')
            print("Esta frase é verdadeira")
            self.pergunta_10()

    def pergunta_10(self):
        print('Os ERPs são uma plataforma de software desenvolvida para integrar os diversos departamentos de uma empresa, possibilitando a automação e armazenamento de todas as informações de negócios.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_11()
        else:
            print("Você errou :(")
            print('Os ERPs são uma plataforma de software desenvolvida para integrar os diversos departamentos de uma empresa, possibilitando a automação e armazenamento de todas as informações de negócios.')
            print("Esta frase é verdadeira")
            self.pergunta_11()

    def pergunta_11(self):
        print('Os processos empresariais têm como elementos: custo, prazos, qualidade de produção e satisfação do cliente')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_12()
        else:
            print("Você errou :(")
            print('Os processos empresariais têm como elementos: custo, prazos, qualidade de produção e satisfação do cliente')
            print("Esta frase é verdadeira")
            self.pergunta_12()

    def pergunta_12(self):
        print('Os sistemas de informação podem ajudar a melhorar o relacionamento com clientes por meio da personalização do atendimento, da oferta de serviços mais rápidos e eficientes e da coleta de feedback dos clientes.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_13()
        else:
            print("Você errou :(")
            print('Os sistemas de informação podem ajudar a melhorar o relacionamento com clientes por meio da personalização do atendimento, da oferta de serviços mais rápidos e eficientes e da coleta de feedback dos clientes.')
            print("Esta frase é verdadeira")
            self.pergunta_13()

    def pergunta_13(self):
        print('Um sistema de informação pode ajudar um hospital a fornecer atendimento médico de qualidade e seguro.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_14()
        else:
            print("Você errou :(")
            print('Um sistema de informação pode ajudar um hospital a fornecer atendimento médico de qualidade e seguro.')
            print("Esta frase é verdadeira")
            self.pergunta_14()

    def pergunta_14(self):
        print('Os sistemas de informação podem ser usados para melhorar a segurança e a privacidade.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_15()
        else:
            print("Você errou :(")
            print('Os sistemas de informação podem ser usados para melhorar a segurança e a privacidade.')
            print("Esta frase é verdadeira")
            self.pergunta_15()

    def pergunta_15(self):
        print('Os sistemas de informação podem ser usados para promover a sustentabilidade.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_16()
        else:
            print("Você errou :(")
            print('Os sistemas de informação podem ser usados para promover a sustentabilidade.')
            print("Esta frase é verdadeira")
            self.pergunta_16()
    def pergunta_16(self):
        print('Os sistemas de informação podem ser usados para transformar a maneira como as pessoas trabalham e vivem.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_17()
        else:
            print("Você errou :(")
            print('Os sistemas de informação podem ser usados para transformar a maneira como as pessoas trabalham e vivem.')
            print("Esta frase é verdadeira")
            self.pergunta_17()

    def pergunta_17(self):
        print('Os sistemas de informação podem ser usados para coletar, armazenar, processar e distribuir informações.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_18()
        else:
            print("Você errou :(")
            print('Os sistemas de informação podem ser usados para coletar, armazenar, processar e distribuir informações.')
            print("Esta frase é verdadeira")
            self.pergunta_18()

    def pergunta_18(self):
        print('Um sistema de informação pode ajudar uma organização a gerenciar seu estoque, rastrear suas vendas e cumprir os regulamentos governamentais.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_19()
        else:
            print("Você errou :(")
            print('Um sistema de informação pode ajudar uma organização a gerenciar seu estoque, rastrear suas vendas e cumprir os regulamentos governamentais.')
            print("Esta frase é verdadeira")
            self.pergunta_19()


    def pergunta_19(self):
        print('Os sistemas de informação podem ser integrados entre diferentes níveis organizacionais.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.pergunta_20()
        else:
            print("Você errou :(")
            print('Os sistemas de informação podem ser integrados entre diferentes níveis organizacionais.')
            print("Esta frase é verdadeira")
            self.pergunta_20()
    def pergunta_20(self):
        print('Os sistemas de informação devem ser gerenciados de forma eficaz para garantir seu sucesso.')
        self.resposta = input("Esta frase é verdadeira ou falsa ?")
        if self.resposta == 'V' or self.resposta == 'v':
            print("Você acertou!")
            self.pontuacao += 1
            self.mostrar_resultado()
        else:
            print("Você errou :(")
            print('Os sistemas de informação devem ser gerenciados de forma eficaz para garantir seu sucesso.')
            print("Esta frase é verdadeira")
            self.mostrar_resultado()



    def mostrar_resultado(self):
        pass


if __name__ == '__main__':
    App()
