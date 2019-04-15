
def sum(x):
  if x < 0:
      return 0
  print(x)
  sum(x - 1)
  print(x)








if __name__ == '__main__':
    sum(9)