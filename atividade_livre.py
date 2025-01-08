'''
Criando um validor de CPFs com nosso algoritmo e Python
Nome:Paulo Henrique Rodrigues Nogueira 
Matricula:232005989 
'''
import re
import sys

class CPFValidator:
    def __init__(self, entrada):
        self.entrada = entrada
        self.cpf_enviado_ao_usuario = self._remover_pontuacao(self.entrada)

    @staticmethod
    def _remover_pontuacao(cpf):
        return re.sub(r'[^0-9]', '', cpf)

    def _is_sequencial(self):
        return self.cpf_enviado_ao_usuario == self.cpf_enviado_ao_usuario[0] * len(self.cpf_enviado_ao_usuario)

    @staticmethod
    def _calcular_digito(cpf_parcial, contador_inicial):
        soma = 0
        for digito in cpf_parcial:
            soma += int(digito) * contador_inicial
            contador_inicial -= 1
        digito = (soma * 10) % 11
        return digito if digito <= 9 else 0

    def validar(self):
        if self._is_sequencial():
            print('Você enviou dados sequenciais.')
            return

        nove_digitos = self.cpf_enviado_ao_usuario[:9]
        digito_1 = self._calcular_digito(nove_digitos, 10)
        dez_digitos = nove_digitos + str(digito_1)
        digito_2 = self._calcular_digito(dez_digitos, 11)

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        if self.cpf_enviado_ao_usuario == cpf_gerado_pelo_calculo:
            print(f'{self.cpf_enviado_ao_usuario} é válido')
        else:
            print('CPF inválido')

if __name__ == "__main__":
    while True:
        entrada = input('Digite o CPF sem traços ou pontuação: ')
        validador = CPFValidator(entrada)
        validador.validar()
        continuar = input('Deseja validar outro CPF? (s/n): ').strip().lower()
        if continuar != 's':
            print('Encerrando o programa.')
            break
