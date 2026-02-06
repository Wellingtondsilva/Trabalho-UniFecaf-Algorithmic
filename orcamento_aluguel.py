class Imovel:
# Classe que representa um imóvel, contém atributos e métodos comuns a todos os tipos de imóveis.
    def __init__(self, tipo, quartos=1, garagem=False):
        self.tipo = tipo                  # Tipo do imóvel
        self.quartos = quartos            # Números de quartos
        self.garagem = garagem            # Possui garagem?
        self.valor_base = 0               # Valor base do aluguel
        self.valor_final = 0              # Valor final calculado
        self.desconto_aplicado = False    # Desconto aplicado
############################################################################################################

# Para calcular o valor base do aluguel
    def calcular_valor_base(self):
        pass                           
############################################################################################################

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
############################################################################################################

        