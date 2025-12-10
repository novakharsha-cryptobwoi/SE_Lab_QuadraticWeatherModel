def predict_temperature(a, b, c, t):
    return a*t*t + b*t + c

# Hardcoded inputs
a = 0.3
b = -1.2
c = 25
t = 6

result = predict_temperature(a, b, c, t)
print("Predicted temperature:", result)
