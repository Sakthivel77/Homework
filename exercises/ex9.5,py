import csv
def isValid(a):
  b = [10 if x == 'X' else int(x) for x in a if x not in '- ']
  if len(b) ==10:
    total = 0
    for i in range(len(b)):
        total+= (len(a)-i)*b[i]
    return (total/11).is_integer()
  elif len(b) == 13:
      total = 0
      for i in range(len(b)):
          if i%2 == 0:
              total += b[i]
          else:
              total +=b[i]*3

      return (total/10).is_integer()
  else:
      return False
with open('ISBN_EXERCISE.txt') as f:
  reader = csv.reader(f,delimiter = ':')
  count = 0
  for row in reader:
    if isValid(row[1]):
      count +=1
      print(row)
  print(f'{count} valid ISBN')
      
