import sys

RATE = 5
if len(sys.argv) == 2:
    units = float(sys.argv[1])
else:
    print("No input given - using default units")
    units = 100  

bill_amount = units * RATE

print("Units Consumed:", units)
print("Rate per Unit: ", RATE)
print("Total Bill Amount: ", bill_amount)
