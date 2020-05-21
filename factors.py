integer = int(input('Please enter an integer: '))
for index in range(integer, 0, -1):
  if integer % index == 0:
    if index % 2 == 0:
      print('Even!')
    else:
      print('Odd!')
    print(index, end = ' ')
