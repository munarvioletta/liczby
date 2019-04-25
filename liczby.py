#! /usr/bin/env python3

def my_function():

  if lista_elem[0] > lista_elem[1]  and  lista_elem[2] > lista_elem[1]:
    najmniejsza = lista_elem[1]

  elif lista_elem[1] > lista_elem[0] and lista_elem[2] > lista_elem[0]:
    najmniejsza = lista_elem[0]

  else:
    najmniejsza = lista_elem[2]

  print(('najmniejsza liczba to {}:' ).format(najmniejsza))    


odp = "t"
while  odp == "t":
  print (' Zadanie sprawdza ktora liczba jest najmniejsza')
  print (' wpisz 3 liczby po kolei')
  lista_elem = []
  print(lista_elem)
  
  for i in range(0,5):   

    while len(lista_elem) <= 2:
      print('nie wystarczająca, wpisz 3 liczby do porownania')
      try: 
        x = int(input("Podaj liczbę: "))
        lista_elem.append(x)
        
      except:
        print('Wpisales znak lub liere, wpisz liczbe!')
   
  print(lista_elem)

  my_function()   

  odp = input("Jeszcze raz (t/n)? ")

print('koniec')






