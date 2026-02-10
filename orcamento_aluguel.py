import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

import csv

# Classe que representa um imóvel, contém atributos e métodos comuns a todos os tipos de imóveis.
class Imovel:
    def __init__(self, tipo, quartos=1, garagem=False):
        self.tipo = tipo                  # Tipo do imóvel
        self.quartos = quartos            # Números de quartos
        self.garagem = garagem            # Possui garagem?
        self.valor_base = 0               # Valor base do aluguel
        self.valor_final = 0              # Valor final calculado
        self.desconto_aplicado = False    # Desconto aplicado

# Para calcular o valor base do aluguel
    def calcular_valor_base(self):
        pass

# Calcula os acréscimos no valor do aluguel baseado nas características.
    def calcular_acrescimos(self):
        acrescimo_total = 0
# Verifica acréscimo por quartos extras
        if self.tipo == "apartamento" and self.quartos > 1:
            acrescimo_total += 200 * (self.quartos - 1)     # R$200 por quarto extra
        elif self.tipo == "casa" and self.quartos > 1:
            acrescimo_total += 250 * (self.quartos - 1)     # R$250 por quarto extra
# Verifica acréscimo por garagem            
        if self.garagem and self.tipo in ["apartamento", "casa",]:
            acrescimo_total += 300                         # R$300 por vaga de garagem       
        return acrescimo_total

# Aplica desconto de 5% para apartamento sem crianças.
    def aplica_desconto(self, tem_criancas):
        if self.tipo == "apartamento" and not tem_criancas:
            desconto = self.valor_final * 0.05                # Calcula 5% de desconto
            self.valor_final -= desconto                      # Subtrai o desconto
            self.desconto_aplicado = True                     # Marca que o desconto foi aplicado
            return desconto
        return 0

# Calcula o valor final do aluguel com todos os ajustes.
    def calcular_valor_final(self, tem_criancas=False):
        self.calcular_valor_base()                           # Calcula valor base
        acrescimos = self.calcular_acrescimos()              # Calcula acréscimos
        self.valor_final = self.valor_base + acrescimos      # Soma base = acréscimos
        self.aplica_desconto(tem_criancas)                  # Aplica desconto se aplicável
        return self.valor_final

# Exibe na tela o orçamento formatado.
    def exibir_orcamento(self):
        print("\n" + "="*100)
        print(" "*30 + "ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M")
        print("\n" + "="*100)
        print(f"Tipo do imóvel: {self.tipo.upper()}")
        print(f"Quantidade de quartos: {self.quartos}")
        print(f"Vaga de garagem: {'SIM' if self.garagem else 'NÃO'}")
        print(f"Valor base do aluguel: R$ {self.valor_base:.2f}")
        print(f"Valor final mensal: R$ {self.valor_final:.2f}")
        if self.desconto_aplicado:
            print("Desconto aplicado: 5% (sem crianças)")
        print("\n" + "="*100)
############################################################################################################

# Classe para apartamento.
class Apartamento(Imovel):
    def __init__(self, quartos=1, garagem=False):
        super().__init__("apartamento", quartos, garagem)     # Chama o construtor da classe

    def calcular_valor_base(self):
        self.valor_base = 700.00                              # Valor base para apartamento
############################################################################################################

# Classe para casa.
class Casa(Imovel):
    def __init__(self, quartos=1, garagem=False):
        super().__init__("casa", quartos, garagem)            # Chama o construtor da classe

    def calcular_valor_base(self):
        self.valor_base = 900.00                              # Valor base para casa
############################################################################################################

# Classe para estúdio.
class Estudio(Imovel):
    def __init__(self, vagas_estacionamento=0):
        super().__init__("estúdio", quartos=0)                # Estúdio não possui quartos
        self.vagas_estacionamento = vagas_estacionamento      # Vagas de estacionamento
        self.garagem = False                                  # Não possui 
        
    def calcular_valor_base(self):
        self.valor_base = 1200.00                             # Valor base estúdio
        
    def calcular_acrescimos(self):
        acrescimo_total = 0
# Lógica específica para estacionamento de estúdio.
        if self.vagas_estacionamento > 0:
            if self.vagas_estacionamento <= 2:                # Até 2 vagas: R$250,00 valor fixo
                acrescimo_total += 250
            else:                                             # Primeiras 2 vagas + R$ 250,00
                acrescimo_total += 250
# Vagas adicionais: R$ 60,00 cada
                vagas_extras = self.vagas_estacionamento - 2
                acrescimo_total += vagas_extras * 60
        return acrescimo_total
    
# Sobrescreve o método de exibição para incluir vagas de estacionamento.
    def exibir_orcamento(self):
        super().exibir_orcamento()                           # Chama método da classe
        if self.vagas_estacionamento > 0:
            print(f"Vagas de estacionamento: {self.vagas_estacionamento}")
############################################################################################################

# Classe que gerencia o orçamento completo, incluindo contrato e parcelas.
class OrcamentoCompleto:
    def __init__(self, imovel, tem_criancas=False, parcelas_contrato=1):
        self.imovel = imovel                                                           # Objeto do imóvel
        self.tem_criancas = tem_criancas                                               # Possui crianças?
        self.parcelas_contrato = min(max(1, parcelas_contrato), 5)                     # Garante parcelas entre 1 e 5
        self.valor_mensal = 0                                                          # Valor mensal do aluguel
        self.valor_contrato = 2000.00                                                  # Valor fixo do contrato
        self.valor_parcelas_contrato = 0                                               # Valor de cada parcela do contrato
        self.calcular_orcamento()                                                      # Calcula o orçamento ao criar o objeto

# Calcula todos os valores do orçamento.
    def calcular_orcamento(self):
        self.valor_mensal = self.imovel.calcular_valor_final(self.tem_criancas)        # Calcula valor mensal do aluguel
        self.valor_parcelas_contrato = self.valor_contrato / self.parcelas_contrato    # Calcula valor da parcela do contrato

# Exibe um resumo completo do orçamento.
    def exibir_orcamento(self):
        self.imovel.exibir_orcamento()                                                 # Exibe orçamento do imóvel
        total_12_meses = self.valor_mensal * 12

        print("\n" + "-"*100)
        print(" "*30 + "DETALHES DO CONTRATO E FINANCEIRO")
        print("-"*100 + "\n")
        print(f"Valor total do contrato: R$ {self.valor_contrato:.2f}")
        print(F"Parcelas do contrato: {self.parcelas_contrato} x R$ {self.valor_parcelas_contrato:.2f}")
        print(f"Possui crianças: {'SIM' if self.tem_criancas else 'NÃO'}")
        print("\n" + "-"*100)
        print(" "*30 + "PROJEÇÃO DE 12 MESES DE ALUGUEL")
        print("-"*100 + "\n")
        print(f"Total em 12 meses: R$ {total_12_meses:.2f}")
        print(f"Média mensal: R$ {self.valor_mensal:.2f}")

# Gera um arquivo CSV com a projeção de 12 meses.
    def gerar_csv_12_meses(self, nome_arquivo="orcamento_12_meses.csv"):
        try:
            dados = []
            for mes in range(1, 13):
                dados.append({
                    'Mes': f'Mês {mes}',
                    'Valor_Aluguel': self.valor_mensal,
                    'Descricao': f'Aluguel {self.imovel.tipo} - Mês {mes}'
                })

# Escreve no CSV.
            with open(nome_arquivo, 'w', newline='', encoding= 'utf-8') as arquivo:
                campos = ['Mes', 'Valor_Aluguel', 'Descricao']
                escritor = csv.DictWriter(arquivo, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(dados)
            print(f"\nArquivo CSV gerado com sucesso: {nome_arquivo}")
            return nome_arquivo
        except Exception as e:
            print(f"\nErro ao gerar arquivo CSV: {e}")
            return None
########################################################################################################################

# Função: Menu Principal
def menu_principal():
    print("\n" + "-"*100)
    print(" "*30 + "SISTEMA DE ORÇAMENTO - IMOBILIÁRIA R.M")
    print("-"*100 + "\n")
    while True:
        print(" "*30 + "MENU PRINCIPAL:")
        print("1. Criar orçamento para Apartamento")
        print("2. Criar orçamento para Casa")
        print("3. Criar orçamento para Estúdio")
        print("4. Sair")
        try:
            opcao = int(input("\nEscolha uma opção: "))
            limpar_tela()
            if opcao == 1:
                criar_orcamento_apartamento()
            elif opcao == 2:
                criar_orcamento_casa()
            elif opcao == 3:
                criar_orcamento_estudio()
            elif opcao == 4:
                print("\nObrigado por usar o sistema da Imobiliária R.M")
                print("Encerrando programa...")
                break
            else:
                print("\nOpção inválida! Escolha entre 1 e 4.")
        except ValueError:
            print("\nEntrada inválida! Digite um número.")
#######################################################################################################################

# Cria um orçamento específico para apartamento.
def criar_orcamento_apartamento():
    print("\n" + "-"*100)
    print(" "*30 + "ORÇAMENTO PARA APARTAMENTO")
    print("-"*100 + "\n")
    try:
# Solicita dados do apartamento.
        quartos = int(input("Quatidade de quartos: ") or "1")
        garagem = input("Incluir vaga de garagem? (S/N): ").upper() == "S"
        tem_criancas = input("Possui crianças? (S/N): ").upper() == "S"
# Solicita Parcalamento do contrato.        
        parcelas = int(input("Número de parcelas para o contrato (1-5, padrão: 1): ") or "1")
        parcelas = min(max(1, parcelas), 5)                                 # Garante entre 1-5
# Cria objeto do apartamento.
        apartamento = Apartamento(quartos=quartos, garagem=garagem)
# Cria orçamento completo.
        orcamento = OrcamentoCompleto(
            imovel=apartamento,
            tem_criancas=tem_criancas,
            parcelas_contrato=parcelas
        )
# Exibe resumo.
        orcamento.exibir_orcamento()
# Oferece opção de gerar CSV.
        gerar_csv = input("\nDeseja gerar arquivo CSV com projeção de 12 meses? (S/N): ").upper() == "S"
        if gerar_csv:
            orcamento.gerar_csv_12_meses()
    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")
######################################################################################################################

# Função cria orçamento específico para casa.
def criar_orcamento_casa():
    print("\n" + "-"*100)
    print(" "*30 + "ORÇAMENTO PARA CASA")
    print("-"*100 + "\n")
    try:
# Solicita dados para casa
        quartos = int(input("Quatidade de quartos: ") or "1")
        garagem = input("Incluir vaga de garagem? (S/N): ").upper() == "S"
        tem_criancas = input("Possui crianças? (S/N): ").upper() == "S"
# Solicita Parcalamento do contrato.        
        parcelas = int(input("Número de parcelas para o contrato (1-5, padrão: 1): ") or "1")
        parcelas = min(max(1, parcelas), 5)                                 # Garante entre 1-5
# Cria objeto casa
        casa = Casa(quartos=quartos, garagem=garagem)
# Cria orçamento completo
        orcamento = OrcamentoCompleto(
            imovel=casa,
            tem_criancas=tem_criancas,
            parcelas_contrato=parcelas
        )
# Exibe resumo
        orcamento.exibir_orcamento()
# Oferece opção de gerar CSV
        gera_csv = input("\nDeseja gerar arquivo CSV com projeção de 12 meses? (S/N): ").upper() == "S"
        if gera_csv:
            orcamento.gerar_csv_12_meses()
    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")
#########################################################################################################################

# Cria um orçamento específico para estúdio.
def criar_orcamento_estudio():
    print("\n" + "-"*100)
    print(" "*30 + "ORÇAMENTO PARA ESTÚDIO")
    print("-"*100 + "\n")
    try:
# Solicita dados do estúdio
        vagas = int(input("Quantidade de vagas de estacionamento (0-10, padrão: 0): ") or "0")
        vagas = min(max(0, vagas), 10)                          # Garante entre 0 e 10
# Estúdio não tem desconto por crianças
        tem_criancas = False
# Solicita parcelamento do contrato
        parcelas = int(input("Número de parcelas para o contrato (1-5, padrão: 1): ") or "1")
        parcelas = min(max(1, parcelas), 5)                      # Garante entre 1-5
# Cria objeto estúdio
        estudio = Estudio(vagas_estacionamento=vagas)
# Cria orçamento completo
        orcamento = OrcamentoCompleto(
            imovel=estudio,
            tem_criancas=tem_criancas,
            parcelas_contrato=parcelas
        )
# Exibe resumo
        orcamento.exibir_orcamento()
# Oferece opção de gerar CSV
        gera_csv = input("\nDeseja gerar arquivo CSV com projeção de 12 meses? (S/N): ").upper() == "S"
        if gera_csv:
            orcamento.gerar_csv_12_meses()
    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")
########################################################################################################################################

# Função com exemplos de uso para testes.
def exemplos_uso():
    print("\n" + "-"*100)
    print(" "*30 + "EXEMPLOS DE USO DO SISTEMA")
    print("-"*100 + "\n")
# Exemplo 1: Apartamento básico
    print("\nEXEMPLO 1: Apartamento básico (1 quarto, sem garagem)")
    apt1 = Apartamento(quartos=1, garagem=False)
    orc1 = OrcamentoCompleto(apt1, tem_criancas=False, parcelas_contrato=3)
    orc1.exibir_orcamento()
# Exemplo 2: Casa com extras
    print("-"*100 + "\n")
    print("\nEXEMPLO 2: Casa com 3 quartos e garagem")
    casa1 = Casa(quartos=3, garagem=True)
    orc2 = OrcamentoCompleto(casa1, tem_criancas=True, parcelas_contrato=5)
    orc2.exibir_orcamento()
# Exemplo 3: Estúdio com estacionamento
    print("-"*100 + "\n")
    print("\nEXEMPLO 3: Estúdio com 4 vagas de estacionamento")
    est1 = Estudio(vagas_estacionamento=4)
    orc3 = OrcamentoCompleto(est1, parcelas_contrato=2)
    orc3.exibir_orcamento()
# Gera CSV para um dos exemplos
    print("-"*100 + "\n")
    print("\nGerando arquivo CSV para o Exemplo 1...")
    orc1.gerar_csv_12_meses("exemplo_apartamento.csv")
##########################################################################################################

# Função Principal que inicia o sistema.
def main():
    print("\n" + "-"*100)
    print(" "*20 + "Bem - vindo ao Sistema de Orçamento da Imobiliária R.M!")
    print(" "*23 + "Este sistema gera orçamento mensais de aluguel.")
    print("-"*100 + "\n")
    while True:
        print("\n" + "*"*100)
        print(" "*40 + "OPÇÕES:")
        print("*"*100 + "\n")
        print("1. Usar Sistema interativo")
        print("2. Ver exemplos de uso")
        print("3. Sair")
        try:
            escolha = int(input("\nEscolha uma opção (1-3): "))
            if escolha == 1:
                menu_principal()
            elif escolha == 2:
                exemplos_uso()
            elif escolha == 3:
                print("\nObrigado por usar nosso sistema!")
                break
            else:
                print("\nOpção inválida!")
        except ValueError:
            print("\nEntrada inválida! Digite um número.")
#########################################################################################################

# Execução do programa.
if __name__ == "__main__":
    main()
    