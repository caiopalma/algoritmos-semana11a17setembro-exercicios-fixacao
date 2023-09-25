def prog_se59():
    op = int(input("Digite:"
                   "\n1-Regiao Norte"
                   "\n2-Regiao Nordeste"
                   "\n3-Regiao Centro-Oeste"
                   "\n4-Regiao Sul"
                   "\n"
                   ))
    iv = int(input("Digite:"
                   "\n1-Ida"
                   "\n2-Ida-Volta"))
    match (op, iv):
        case (1,1):
            print("\nO valor da passagem de ida para R.Norte R$500.00")
        case (1,2):
            print("\nO valor da passagem de ida-volta para R.Norte: R$950.00")
        case (2,1):
            print("\nO valor da passagem de ida para R.Nordeste: R$350.00")
        case (2,2):
            print("\nO valor da passagem de ida-volta para R.Nordeste: R$650.00")
        case (3,1):
            print("\nO valor da passagem de ida para R.C.Oeste: R$350.00")
        case (3,2):
            print("\nO valor da passagem de ida-volta para R.C.Oeste: R$600,00")
        case (4,1):
            print("\nO valor da passagem de ida para R.Sul: R$300.00")
        case (4,2):
            print("\nO valor da passagem de ida-volta para R.Sul: R$550.00")
        case _:
            print("\nOpcao Inexistente")

prog_se59()