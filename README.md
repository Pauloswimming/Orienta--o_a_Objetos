# Orientação_a_Objetos
 resultados de sua atividade livre


Como funciona o código:
Este programa em Python é usado para validar CPFs. Ele utiliza uma classe chamada CPFValidator para organizar e encapsular toda a lógica de validação, tornando o código mais limpo e modular.

Primeiramente, o programa solicita ao usuário que insira um CPF sem traços ou pontuação. Essa entrada é tratada pela classe, que remove qualquer caractere que não seja numérico. Em seguida, verifica-se se o CPF é composto por uma sequência repetitiva de números, como "11111111111", que é inválida.

A validação do CPF é feita através do cálculo dos dois dígitos verificadores. O primeiro dígito é calculado com base nos nove primeiros números, e o segundo dígito é calculado a partir dos

dez primeiros números (os nove iniciais mais o primeiro dígito verificador). O resultado é então comparado com o CPF fornecido pelo usuário. Se o CPF gerado pelo cálculo for igual ao inserido, ele é considerado válido; caso contrário, é inválido.

O programa também permite ao usuário validar múltiplos CPFs. Após cada validação, é perguntado se ele deseja continuar. Caso a resposta seja negativa, o programa exibe uma mensagem de encerramento e finaliza.

Para executar o programa, basta salvá-lo como um arquivo Python, como validador_cpf.py, e rodá-lo no terminal. Digite o comando python validador_cpf.py, insira os CPFs conforme solicitado e siga as instruções para validar outros CPFs ou encerrar.
