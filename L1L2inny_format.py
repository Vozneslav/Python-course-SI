#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sortowanie_babelkowe(lista):
  dlugosc = len(lista)
  for i in range(dlugosc):
    for j in range(dlugosc-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return


lista1 = [64, 34, 25, 12, 22, 11, 90]
sortowanie_babelkowe(lista1)
print(lista1)


# In[2]:


def sortowanie_przez_wstawianie(lista):
  dlugosc = len(lista)
  for i in range(1, dlugosc):
    wybrany_element = lista[i]
    j = i - 1
    while j >= 0 and wybrany_element < lista[j]:
      lista[j+1] = lista[j]
      j = j - 1
    lista[j + 1] = wybrany_element #swap?
  return


lista2 = [64, 34, 25, 12, 22, 11, 90]
sortowanie_przez_wstawianie(lista2)
print(lista2)


# In[3]:


def pierwsze_wartosci_babelkowo(lista, wart_progowa, ile = 3):
  pierwsze_trzy_wartosci = []
  el = 0
  while len(pierwsze_trzy_wartosci) < ile and el < len(lista):
    if lista[el] > wart_progowa:
      pierwsze_trzy_wartosci.append([el, lista[el]])
    el = el + 1

  for i in range(ile):
    for j in range(ile-i-1):
      if pierwsze_trzy_wartosci[j][1] < pierwsze_trzy_wartosci[j+1][1]:
        pierwsze_trzy_wartosci[j], pierwsze_trzy_wartosci[j+1] = pierwsze_trzy_wartosci[j+1], pierwsze_trzy_wartosci[j]
  return pierwsze_trzy_wartosci

pierwsze_wartosci_babelkowo([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)


# In[4]:


def pierwsze_wartosci_wstawianie(lista, wart_progowa, ile = 3):
  pierwsze_wartosci = []
  el = 0
  while len(pierwsze_wartosci) < ile and el < len(lista):
    if lista[el] > wart_progowa:
      pierwsze_wartosci.append([el, lista[el]])
    el = el + 1

  for i in range(1, ile):
    wybrany_element = pierwsze_wartosci[i]
    j = i - 1
    while j >= 0 and wybrany_element[1] > lista[j]:
      pierwsze_wartosci[j+1] = pierwsze_wartosci[j]
      j = j - 1
    pierwsze_wartosci[j + 1], wybrany_element = wybrany_element, pierwsze_wartosci[j + 1]
  
  return pierwsze_wartosci

pierwsze_wartosci_wstawianie([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)


# In[5]:


import time


start_b = time.time()
pierwsze_wartosci_babelkowo([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)
stop_b = time.time()

start_w = time.time()
pierwsze_wartosci_wstawianie([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)
stop_w = time.time()

czas_b = stop_b - start_b
czas_w = stop_w - start_w
print("Babelkowo zajelo %f sekundy\nWstawianie zajelo %f sekundy"%(czas_b, czas_w))


# In[ ]:




