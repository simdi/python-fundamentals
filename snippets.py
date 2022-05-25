# Using the zip function to create something like a merger of multiple sequences
"""Using zip function"""
names = ['Amanda', 'Chime', 'Chimamanda', 'Daborah']
grades = [3.5, 4.5, 3.45, 2.95]

for name, grade in zip(names, grades):
  print(f'Name: {name}, grade: {grade}')
# Output
# Name: Amanda, grade: 3.5
# Name: Chime, grade: 4.5
# Name: Chimamanda, grade: 3.45
# Name: Daborah, grade: 2.95

