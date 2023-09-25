def prog_se62():
    peso = float(input("\ndigite peso: "))
    altura = float(input("\ndigite altura: "))
    imc = peso / (altura**2.0)
    if imc < 20.0:
        print("\nabaixo do peso")
    elif imc <= 25.0:
        print("\nnormal")
    elif imc <= 30.0:
        print("\nexcesso de peso")
    elif imc <= 35.0:
        print("\nobesidade")
    else:
        print("\nobesidade mórbida")
    print("\n")

prog_se62()