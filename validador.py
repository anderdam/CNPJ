"""
04.252.011/0001-10 // 40.688.134/0001-61 // 71.506.168/0001-11 // 12.544.992/0001-05
0  4  2  5  2  0  1  1  0  0  0  1  ?  ?
x  x  x  x  x  x  x  x  x  x  x  x
5  4  3  2  9  8  7  6  5  4  3  2
=  =  =  =  =  =  =  =  =  =  =  =
0 16  6 10 18  0  7  6  0  0  0  2  ==  65

Fórmula = 11 - (65 % 11) = 1 // Se o resultado for > 9, o dígito será 0
Primeiro dígito 1

0  4  2  5  2  0  1  1  0  0  0  1  1  ?
x  x  x  x  x  x  x  x  x  x  x  x  x
6  5  4  3  2  9  8  7  6  5  4  3  2
=  =  =  =  =  =  =  =  =  =  =  =  =
0 20  8 15  4  0  8  7  0  0  0  3  2 == 67

Fórmula = 11 - (67 % 11) = 11 // Se o resultado for > 9, o dígito será 0
Segundo dígito 0
"""
import funcoes

# cnpj = funcoes.valida(input('Digite um CNPJ: '))
cnpjs = ['04.252.011/0001-10',
         '40.688.134/0001-61',
         '71.506.168/0001-11',
         '12.544.992/0001-05',
         '11.111.111/1111-11',
         '123'
         ]

for cnpj in cnpjs:
    if funcoes.valida(cnpj):
        print(f'O CNPJ {cnpj} é válido')
    else:
        print(f'O CNPJ {cnpj} NÂO é válido')
