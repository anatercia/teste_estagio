# Código para contagem da letra "a" em um texto
print("Bem-vindo(a) a sessão de verificação da letra 'a' em um texto!")

while True:
    try:
        contagem = str(input("\nDigite um texto: ")).lower().count("a")

        if contagem == 0:
            print("\nA letra 'a' não aparece no texto.")
            
        else:
            print(f"\nA letra 'a' aparece no texto {contagem} vez(es).")
        
    except ValueError:
        print("Texto inválido!")

    while True:
        resposta = input("\nDeseja continuar? (s/n) ").lower()
        
        if resposta in ['s', 'n']:
            break  # Sai do loop se a resposta for válida
        
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")

    if resposta == "n":
        print("\nSessão encerrada!")
        break

