def prog_se70():
    x = float(input("digite valor de x: "))
    if(x > 4.0 or x < -4.0):
        fx = (5 * x + 3) / ( (x**2) - 16)**0.5
        print(f"\nf(x)= {fx}")
    else:
        print(f"\nNAO PODE SER FEITA")
    print(f"\n")

prog_se70()