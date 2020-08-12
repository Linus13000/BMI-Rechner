m = input("Gewicht in Kg? ")
s = input("Größe in cm? ")
s = float(s) / 100

def rechner(m, s):
    s2 = s ** 2
    bmi = float(m) / s2
    return bmi

bmi = round(rechner(m, s), 2)

if bmi < 16:
    print(bmi, "Dies entspricht starkem Untergewicht.")
elif bmi < 17:
    print(bmi, "Dies entspricht maßigem Untergewicht.")
elif bmi < 18.5:
    print(bmi, "Dies entspricht leichtem Untergewicht.")
elif bmi < 25:
    print(bmi, "Dies entspricht dem Normalgewicht.")
elif bmi < 30:
    print(bmi, "Dies entspricht einer Präadipositas.")
elif bmi < 35:
    print(bmi, "Dies entspricht einer Adipositas Grad I.")
elif bmi < 40:
    print(bmi, "Dies entspricht einer Adipositas Grad II.")
elif bmi >= 40:
    print(bmi, "Dies entspricht einer Adipositas Grad III.")
