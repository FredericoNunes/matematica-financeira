from bizdays import Calendar
from anbima import holidays
cal = Calendar(holidays(), ['Sunday', 'Saturday'])



class Financeira(object):
    def __init__(self):
        self.taxa = 0
        self.capitalizacao =1
        self.tempo = 1
        self.fator = 1

    def Fator(self,taxa,tempo,capitalizacao=1,trunc=8):
        """
        :param taxa: <float>
        :param tempo: <int>
        :param capitalizacao:<int>
        :param trunc: <int>
        :return:
        """
        self.fator = Financeira.truncate((1+taxa/capitalizacao)**(capitalizacao*tempo),trunc)
        return self.fator

    def ValorPresente(self,valorFuturo,taxa,tempo,capitalizacao=1,trunc=8):
        """
        :param valorFuturo: <float>
        :param taxa: <float>
        :param tempo: <int>
        :param capitalizacao: <int>
        :param trunc: <int>
        :return:
        """
        fator = self.Fator(taxa,tempo,capitalizacao,trunc)
        valor_presente = Financeira.truncate(valorFuturo/fator,trunc)
        return valor_presente

    def ValorFuturo(self,valorPresente,taxa,tempo,capitalizacao=1,trunc=8):
        """
        :param valorPresente: <float>
        :param taxa: <float>
        :param tempo: <float>
        :param captalizacao: <int>
        :param trunc: <int>
        :return:
        """
        fator = self.Fator(taxa, tempo, capitalizacao, trunc)
        valor_futuro = Financeira.truncate(valorPresente*fator,trunc)
        return valor_futuro

    def TaxaEfetiva(self,taxa,tempo,capitalizacao=1,trunc=8):
        """
        :param taxa: <float>
        :param tempo: <int>
        :param capitalizacao:<int>
        :param trunc:<int>
        :return:
        """
        fator = self.Fator(taxa,tempo,capitalizacao,trunc)
        taxa_efetiva = Financeira.truncate(fator-1,trunc)
        return taxa_efetiva

    def Desconto(self,valorNominal,taxa,tempo):
        """
        :param valorNominal:
        :param taxa:
        :param tempo:
        :return:
        """
        fator = self.Fator(taxa,tempo)
        desconto_finaceiro = valorNominal*Financeira.truncate((fator-1)/fator,8)
        return desconto_finaceiro

    @staticmethod
    def truncate(f, n):
        '''Truncates/pads a float f to n decimal places without rounding'''
        '''stackover  answered Apr 23 '09 at 23:10 David Z'''
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return float('.'.join([i, (d+'0'*n)[:n]]))





