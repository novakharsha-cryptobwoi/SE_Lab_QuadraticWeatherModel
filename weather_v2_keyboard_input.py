def predict_temperature(a, b, c, t):
    return a*t*t + b*t + c

print("Enter values for a, b, c and t:")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
t = float(input("t: "))

result = predict_temperature(a, b, c, t)
print("Predicted temperature:", result)
