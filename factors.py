integer = int(input('Please enter an integer: '))
for index in range(integer, 0, -1):
  if integer % index == 0:
    print(index, end = ' ')
