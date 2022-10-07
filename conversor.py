def poli (c):
  a = c*0.3937
  file = open('conversor.txt', 'w+')
  file.write('a conversão é {}.'.format(a))
  file.seek(0,0)
  file.read()
  file.seek(0,0)
  file.close()