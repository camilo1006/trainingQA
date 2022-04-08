def sum(a, b):
  return a + b

def subtraction(a, b):
  return a - b

def divide(a, b):
  return a/b

def multiplication(a, b):
  return a*b

def root(a, b = 2):
  return (a ** (1/b))

def power(a, b):
  return (a ** b)

def stundent(a, b, c):
  value_a = root(subtraction(power(b, 2), multiplication(multiplication(4, a), c)))
  o1 = divide(subtraction(-b, value_a), multiplication(2, a))
  o2 = divide(sum(-b, value_a), multiplication(2, a))

  return o1, o2

print(stundent(4, -12, 9))
