print ('Zadanie 1')
Piekarnia = ['chleb', 'bułki', 'ciastka']
Warzywniak = ['pietruszka', 'marchewka', 'ziemniaki']
for i in Piekarnia:
    print ('W Piekarni kupuję', i)
for j in Warzywniak:
    print ('W Warzywniaku kupuję', j)
print ('W Piekarni kupuję', Piekarnia)
print ('W Warzywniaku kupuję', Warzywniak)
x = len(Piekarnia) + len(Warzywniak)
print ('W sumie kupuję', (x), 'produktów')

print ('Zadanie 2')
divis = []
for i in range (1,101):
  if i % 5 == 0:
    divis.append (i)
print (divis)
cubes = [divi ** 3 for divi in divis]
print (cubes)

print ("Hiszpańska inkwizycja")

print ("lubie cię")

print ("karate")
