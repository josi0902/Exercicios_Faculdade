print('-----Calculadora de media-----')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: ')) 
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) // 3

print('A média das notas é: ', media)

if media >= 7:
    print('### Aluno aprovado! ###')
else:
    print('### Aluno reprovado!###')   

if media >= 7:
        print('***Parabéns!***')
else:
        print('***Estude mais da próxima vez!***')    


