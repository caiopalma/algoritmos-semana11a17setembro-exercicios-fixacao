def prog_se55():
    saldomedio = float(input("\ndigite saldo medio: "))
    if saldomedio < 501.0:
        credito = 0.0
    elif saldomedio < 1001.0:
        credito = saldomedio * 0.3
    elif saldomedio < 3001.0:
        credito = saldomedio * 0.4
    else: 
        credito = saldomedio * 0.5
    if credito != 0.0:
        print(f"\nComo seu saldo era de {saldomedio} "
              f"seu credito sera de {credito}")
    else:
        print(f"Como seu saldo era de {saldomedio} "
              f"voce nao tera nenhum credito")
    print("\n")

prog_se55()