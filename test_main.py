import main

def test_unit_sum():
  # Arrange
  a = 2
  b = 3

  # Act
  actual = main.sum(a, b)

  # Assert
  assert actual == (a + b)

def test_unit_subtraction():
  # Arrange
  a = 2
  b = 3

  # Act
  actual = main.subtraction(a, b)

  # Assert
  assert actual == (a - b)

def test_unit_multiplication():
  # Arrange
  a = 2
  b = 3

  # Act
  actual = main.multiplication(a, b)

  # Assert
  assert actual == (a * b)

def test_unit_divide():
  # Arrange
  a = 2
  b = 3

  # Act
  actual = main.divide(a, b)

  # Assert
  assert actual == (a / b)

def test_unit_root():
  # Arrange
  a = 2
  b = 3

  # Act
  actual = main.root(a, b)

  # Assert
  assert actual == (a ** (1/b))

def test_unit_power():
  # Arrange
  a = 2
  b = 3

  # Act
  actual = main.power(a, b)

  # Assert
  assert actual == (a ** b)

def test_component_student():
  # Arrange
  a = 2
  b = 9
  c = 10

  # Act
  actual_s1, actual_s2 = main.stundent(a, b, c)

  # Assert
  assert actual_s1 == -2.5
  assert actual_s2 == -2
