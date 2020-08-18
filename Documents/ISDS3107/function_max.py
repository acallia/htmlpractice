





def main():
  fam = [40, 55, 62, 72, 65]
  tallest = max(fam)
  print("The tallest is ", tallest)

def max(l):
  m = l[0]
  for h in l:
    if h > m:
      m = h
  return m

main()
