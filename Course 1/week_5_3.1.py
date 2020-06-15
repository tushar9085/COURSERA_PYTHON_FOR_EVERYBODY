hrs = input("Enter Hours:")

rte = input("Enter Rate:")

try:
    hours = float(hrs)
    rate = float(rte)
except:
    print("Error")
    quit()

if hours > 40:
    pay = rate * 40 + (rate * 1.5) * (hours - 40)
    print(pay)

else:
    pay = hours * rate
    print(pay)
