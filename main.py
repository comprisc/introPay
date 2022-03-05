

def print_hi(name):

    print(f'Oi, {name}')


def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado * 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range (fim): #repete o bloco de 0 até o fim
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        contador = numero + 1
        print(f'{contador} - {nome}')



#----------------Chamar a função---------



#estrutura de identificação / execução do script
if __name__ == '__main__':
   print_hi(f'Priscila')

   resultado = calcular_area_do_retangulo(3,4)
   print(f'A área do retangulo é de {resultado} m²')

   resultado = calcular_area_do_quadrado(5)
   print(f'A área do quadrado é de {resultado} m²')

   resultado = calcular_area_do_triangulo(2,5)
   print(f'A área do triangulo é de {resultado} m²')

   contagem_progressiva(11)

   #exibir o nome do candidato

   apoiar_candidato('Faker', 20)

