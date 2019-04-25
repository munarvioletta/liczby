#! /usr/bin/env python3

def my_function():

  if lista_elem[0] > lista_elem[1]  and  lista_elem[2] > lista_elem[1]:
    najmniejsza = lista_elem[1]

  elif lista_elem[1] > lista_elem[0] and lista_elem[2] > lista_elem[0]:
    najmniejsza = lista_elem[0]

  else:
    najmniejsza = lista_elem[2]

  print(('najmniejsza liczba to: {}' ).format(najmniejsza))


odp = "t"
while  odp == "t":
  print (' Zadanie sprawdza ktora liczba jest najmniejsza')
  print (' wpisz 3 liczby po kolei')
  lista_elem = []
  try:
    n = int(input("Podaj ilosc liczb do porownania: "))

    if n == 0:
      print('brak liczb do porownania')
    elif n < 3:
      print('nie wystarczająca, wpisz 3 liczby do porownania')
    else:

      for i in range(n):

        while len(lista_elem) < n:

          try:
            x = float(input("Podaj liczbę: "))
            lista_elem.append(x)

          except:
            print('Wpisales znak lub liere, wpisz liczbe!')

      print(lista_elem)

      my_function()

  except:
    print('wprowadz liczbe calkowita')

  odp = input("Jeszcze raz (t/n)? ")

print('koniec')






