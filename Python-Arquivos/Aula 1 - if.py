preco = float(input("Preço do produto: "))
qtd = int(input("Quantidade: "))
total = preco * qtd
if total > 200.00:
    opcao = input("Desconto [D] ou Parcelamento [P]: ")
    if opcao == "D":
        desc = total * 0.05
        total -= desc
        print("O desconto é de R$: %.2f" % desc)
    else:
        p = int(input("Escolha a quantidade de parcelas: "))
        print("%d parcelas de R$ %.2f" % (p, total/p))    
print("Total: R$ %.2f" % total)


        
