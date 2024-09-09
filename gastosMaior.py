gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 300, 500, 700]

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")