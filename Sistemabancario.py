menu ='''

--- Bom dia! O que deseja ? ---
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--------------------------------
'''

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
saque_valor = []    # Lista com valores de saque
deposito_valor = [] # Lista com valores depositados

while True:

    opcao = input(menu)
    
    if opcao == "d":
        depositar = float(input("Quanto deseja depositar? "))
        if depositar < 0:
            print('Não é possível fazer esse depósito.')
        else:
            saldo += depositar
            deposito_valor.append('R$ ' + str(depositar))
            print('Deposito realizado com sucesso!')
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Já foi realizado os 3 saques diários permitidos")
        elif saldo == 0:
            print("Não é possível fazer saque pois não existe saldo na conta")
        else:
            saque = float(input("Quanto deseja sacar?"))
            if saque > limite:
                print("É permitido no máximo R$ 500,00")
            
            elif saque < 0 :
                print('Não é possível fazer esse saque.')

            else:
                saque_valor.append('R$ ' + str(saque))
                print('Saque realizado com sucesso')
                saldo -= saque
                numero_saques += 1
    elif opcao == "e":
        
        saldo_final = 'R$ ' + str(saldo)

        print(f'============== EXTRATO ==============\n\nDepositos: {deposito_valor}\nSaques: {saque_valor}\n\nSaldo: {saldo_final}.\n\n=====================================')

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a opração desejada.")

