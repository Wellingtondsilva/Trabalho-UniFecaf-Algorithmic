class Imovel:
    def __init__(self, tipo, quartos=1, garagem=False):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.valor_base = 0
        self.valor_final = 0
        self.desconto_aplicado = False

    def calcular_valor_base(self):
        pass

    def calcular_acrescimos(self):
        acrescimo_total = 0
        if self.tipo == "apartamento" and self.quartos > 1:
            acrescimo_total += 200 * (self.quartos - 1)
        elif self.tipo == "casa" and self.quartos > 1:
            acrescimo_total += 250 * (self.quartos - 1)
        if self.garagem and self.tipo in ["apartamento", "casa",]:
            acrescimo_total += 300
        return acrescimo_total
        