def prog_se71():
    x = float(input("\ndigite valor de x: "))
    y = 1.0 if x <= 1.0 \
        else 2.0 if x <= 2.0 \
            else x**2.0 if x <= 3.0 \
                else x**3.0
    print(f"\nvalor de f(x): {y}")
    print("\n")
prog_se71()
