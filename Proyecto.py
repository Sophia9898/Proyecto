#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import requests
respuesta=requests.get("https://api.sbif.cl/api-sbifv3/recursos_api/balances/2009/instituciones/012?apikey=1b5cb2b5b03228678bedcc37be0becc267456dc9&formato=json")
res=respuesta.json()
print(res)
                       


# In[48]:


print("Moneda Reajustable Por IPC:", res["CodigosBalances"][0]["DescripcionCuenta"])


# In[2]:


import requests
ipc=requests.get("https://api.sbif.cl/api-sbifv3/recursos_api/ipc/2010?apikey=1b5cb2b5b03228678bedcc37be0becc267456dc9&formato=json")
res2=ipc.json()
print(res2)
#Primero obtuvimos los valores en formato json de la api de bancos, donde obtuvimos los valores del ipc para cada mes del año 2010.
            


# In[3]:


n=12
i=0
b=[]
while i<n:
    a=res2["IPCs"][i]["Valor"]
    i=i+1
    b.append(a)
print(b)
len(b)
#luego tomamos los valores del ipc y generamos una lista con ellos.


# In[4]:


def enteros(lista):
    i2=0
    enteross=[]
    while len(lista)>i2:
        p=lista[i2].split(",")
        i=0
        numero=""
        while len(p)>i:
            numero=numero+p[i]
            if i == len(p)-1:
                pass
            else:
                numero=numero+"."
            i=i+1
        enteross.append(numero)
        i2=i2+1
    return(enteross)
     
lista_valores = enteros(b)
print(lista_valores)
#Luego generamos una nueva lista con los valores de los ipcs en la cual borramos la comas con el comando .split y reemplazamos
#comas por puntos debido a que el programa no permitía trabajar matematicamente los números como float utilizando las comas.


# In[5]:


i3 = 0
while len(lista_valores) > i3:
    lista_valores[i3] = float(lista_valores[i3])
    i3 = i3 + 1
print(lista_valores)
#Luego transformamos la lista que anteriormente era de string a una lista de números con el comando float.


# In[6]:


n = 12
i4 = 0
c = []
while i4 < n:
    a = res2["IPCs"][i4]["Fecha"]
    i4 = i4 + 1
    c.append(a)
print(c)
len(c)
#Luego creamos una lista c con las fechas.


# In[7]:


i5 = 0
fechas = []
while len(c) > i5:
    f = c[i5].split("-")
    m = int(f[1])
    fechas.append(m)
    i5 = i5 + 1
print(fechas)
#Luego creamos una nueva lista y borramos los -, los reemplazamos por comas, tomamos solamente el valor de los meses y los pasamos
# con el comando int a numeros enteros.


# In[8]:


import matplotlib.pyplot as plt
plt.plot(fechas,lista_valores,'g--d')
plt.title('IPC AÑO 2010')
plt.ylabel('IPC')
plt.xlabel('Meses 2010')
plt.show()
#Luego graficamos los datos recaudados de la api para el posterior analisis de ellos.


# In[ ]:


#podemos notar por el grafico que el ipc no tiene un comportamiento lineal expecto los meses de de Octubre,Noviembre y Diciembre
#donde podemos notar que su comportamiento es una línea recta esto quiere decir que el valor se mantuvo contanste durante estos 
#meses, en cambio los meses anteriores podriamos decir que se asemeja a un comportamiento sinusoidal con amplitud variable el cual
# probablemente pueda ser descrito por una aproximación hecha por Series de Fourier, esto nos dice que los niveles de inflación.
#sufrieron abruptos cambios, lo cual puede deberse a diversos factores.

