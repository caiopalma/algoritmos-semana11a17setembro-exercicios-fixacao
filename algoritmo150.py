import math

def prog_se61():
    ang = float(input("\ndigite angulo em graus: "))
    rang = ang * math.pi / 180.0
    if (rang > math.pi/2.0 and rang <= math.pi) \
        or (rang > 3.0*math.pi/2.0 and rang <= 2.0*math.pi):
        print(f"\nseno: {math.sin(rang)}")
    else:
        print(f"\nco-seno: {math.cos(rang)}")
    print("\n")

prog_se61()