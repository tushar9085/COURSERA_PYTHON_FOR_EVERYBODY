n = input("Enter a score:")
score = float(n)

if score >= 0.0 :
    if score < 0.6  :
        print("F")
    elif score < 0.7 :
        print("D")
    elif score < 0.8 :
        print("C")
    elif score < 0.9 :
        print("B")
    elif score <= 1.0 :
        print("A")

if score > 1.0 :
    print("Error")
