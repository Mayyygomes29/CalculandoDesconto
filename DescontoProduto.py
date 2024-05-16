#Calcular um programa que calcule o desconto do produto
p = float(input("Digite o valor do produto : "))

print("1 - Dinheiro/ Cheque ")
print("2 - À Vista no cartão ")
print("3 - 2x no cartão ")
print("4 - 3x ou mais no cartão ")

op = int(input("Escolha uma opção: "))

if op == 1:
    des = (p * 10)/100 
    total = p - des
    print("Valor com desconto fica R${:.2f}".format(total))
elif op == 2:
    des = (p * 2)/100
    total = p - des
    print("Valor com desconto fica R${:.2f}".format(total))
elif op == 3:
      print("R${:.2f}".format(p))    
elif op == 4:
     juros = (p * 20) /100
     total = p + juros
     print("Valor com juros fica R${:.2f}".format(total))
else:
     print("Nenhuma opção disponível!")     
