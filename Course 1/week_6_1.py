def computepay( hours, rate):
    if hours > 40:
        pay = rate * 40 + (rate * 1.5)*(hours-40)
    else:
        pay= hours * rate

    return pay


hrs = input("Enter hours:")
rte = input("Enter rate")

try:
    hours = float(hrs)
    rate = float(rte)

except:
    print("Error")
    quit()

pay = computepay(hours, rate)

print("Pay", pay)
