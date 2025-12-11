def predict_temperature(a, b, c, t):
    return a*t*t + b*t + c

with open("input.txt") as f:
    a = float(f.readline())
    b = float(f.readline())
    c = float(f.readline())
    t = float(f.readline())

result = predict_temperature(a, b, c, t)
print("Predicted temperature:", result)
