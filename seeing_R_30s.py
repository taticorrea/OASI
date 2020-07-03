#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.time import Time
#%matplotlib.inline  
import IPython
from IPython import get_ipython
import statistics as std
#plt.style.use('classic')
get_ipython().run_line_magic('matplotlib', 'inline')


# <h1>ABRIL</h1>

# <h2>2019-04-05</h2>

# In[2]:


file = open('ABR/2019-04-05/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[3]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_5 = pd.read_csv('ABR/2019-04-05/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[4]:


df_5['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_5 = df_5[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[5]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_5['XBINNING']*df_5['FWHM']*df_5['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[6]:


df_5['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_5 = df_5[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_5


# <h2>2019-04-07</h2>

# In[7]:


file = open('ABR/2019-04-07/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[8]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_7 = pd.read_csv('ABR/2019-04-07/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[9]:


df_7['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_7 = df_7[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[10]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_7['XBINNING']*df_7['FWHM']*df_7['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[11]:


df_7['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_7 = df_7[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_7


# In[12]:


df_ABR = pd.concat([df_5,df_7],sort=False)
df_ABR.to_csv('seeing_30s_R_ABR.csv')
df_ABR


# <h1>JULHO</h1>

# <h2>2019-07-05</h2>

# In[13]:


file = open('JUL/2019-07-05/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[14]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_5 = pd.read_csv('JUL/2019-07-05/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[15]:


fwhm


# In[16]:


df_5['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm5
df_5 = df_5[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[17]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_5['XBINNING']*df_5['FWHM']*df_5['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[18]:


df_5['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_5 = df_5[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_5


# In[19]:


df_JUL = df_5
df_JUL.to_csv('seeing_30s_R_JUL.csv')
df_JUL


# <h1>AGOSTO</h1>

# <h2>2019-08-23</h2>

# In[20]:


file = open('AGO/2019-08-23/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[21]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_23 = pd.read_csv('AGO/2019-08-23/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[22]:


df_23['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_23 = df_23[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[23]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_23['XBINNING']*df_23['FWHM']*df_23['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[24]:


df_23['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_23 = df_23[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_23


# <h2>2019-08-24</h2>

# In[25]:


file = open('AGO/2019-08-24/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[26]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_24 = pd.read_csv('AGO/2019-08-24/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[27]:


df_24['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_24 = df_24[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[28]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_24['XBINNING']*df_24['FWHM']*df_24['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[29]:


df_24['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_24 = df_24[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_24


# <h2>2019-08-26</h2>

# In[30]:


file = open('AGO/2019-08-26/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[31]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_26 = pd.read_csv('AGO/2019-08-26/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[32]:


df_26['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_26 = df_26[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[33]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_26['XBINNING']*df_26['FWHM']*df_26['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[34]:


df_26['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_26 = df_26[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_26


# In[35]:


df_AGO = pd.concat([df_23,df_24,df_26],sort=False)
df_AGO.to_csv('seeing_30s_R_AGO.csv')
df_AGO


# <h1>SETEMBRO</h1>

# <h2>2019-09-01</h2>

# In[36]:


file = open('SET/2019-09-01/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[37]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_1 = pd.read_csv('SET/2019-09-01/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[38]:


df_1['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_1 = df_1[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[39]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_1['XBINNING']*df_1['FWHM']*df_1['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[40]:


df_1['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_1 = df_1[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_1


# <h2>2019-09-02</h2>

# In[41]:


file = open('SET/2019-09-02/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[42]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_2 = pd.read_csv('SET/2019-09-02/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[43]:


df_2['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_2 = df_2[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[44]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_2['XBINNING']*df_2['FWHM']*df_2['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[45]:


df_2['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_2 = df_2[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_2


# <h2>2019-09-03</h2>

# In[46]:


file = open('SET/2019-09-03/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[47]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_3 = pd.read_csv('SET/2019-09-03/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[48]:


df_3['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_3 = df_3[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[49]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_3['XBINNING']*df_3['FWHM']*df_3['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[50]:


df_3['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_3 = df_3[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_3


# <h2>2019-09-22</h2>

# In[51]:


file = open('SET/2019-09-22/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[52]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_22 = pd.read_csv('SET/2019-09-22/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[53]:


df_22['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_22 = df_22[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[54]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_22['XBINNING']*df_22['FWHM']*df_22['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[55]:


df_22['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_22 = df_22[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_22


# <h2>2019-09-24</h2>

# In[56]:


file = open('SET/2019-09-24/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[57]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_24 = pd.read_csv('SET/2019-09-24/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[58]:


df_24['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_24 = df_24[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[59]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_24['XBINNING']*df_24['FWHM']*df_24['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[60]:


df_24['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_24 = df_24[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_24


# <h2>2019-09-25</h2>

# In[61]:


file = open('SET/2019-09-25/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[62]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_25 = pd.read_csv('SET/2019-09-25/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[63]:


df_25['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_25 = df_25[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[64]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_25['XBINNING']*df_25['FWHM']*df_25['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[65]:


df_25['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_25 = df_25[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_25


# In[66]:


df_SET = pd.concat([df_1,df_2,df_3,df_22,df_24,df_25],sort=False)
df_SET.to_csv('seeing_30s_R_SET.csv')
df_SET


# <h1>OUTUBRO</h1>

# <h2>2019-10-28</h2>

# In[67]:


file = open('OUT/2019-10-28/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[68]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_28 = pd.read_csv('OUT/2019-10-28/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[69]:


df_28['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_28 = df_28[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[70]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_28['XBINNING']*df_28['FWHM']*df_28['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[71]:


df_28['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_28 = df_28[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_28


# In[72]:


df_OUT = df_25
df_OUT.to_csv('seeing_30s_R_OUT.csv')
df_OUT


# <h1>NOVEMBRO</h1>

# <h2>2019-11-04</h2>

# In[73]:


file = open('NOV/2019-11-04/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[74]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_4 = pd.read_csv('NOV/2019-11-04/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[75]:


df_4['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_4 = df_4[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[76]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_4['XBINNING']*df_4['FWHM']*df_4['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[77]:


df_4['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_4 = df_4[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_4


# <h2>2019-11-20</h2>

# In[78]:


file = open('NOV/2019-11-20/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[79]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_20 = pd.read_csv('NOV/2019-11-20/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[80]:


df_20['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_20 = df_20[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[81]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_20['XBINNING']*df_20['FWHM']*df_20['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[82]:


df_20['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_20 = df_20[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_20


# <h2>2019-11-21</h2>

# In[83]:


file = open('NOV/2019-11-21/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[84]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_21 = pd.read_csv('NOV/2019-11-21/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[85]:


df_21['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_21 = df_21[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[86]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_21['XBINNING']*df_21['FWHM']*df_21['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[87]:


df_21['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_21 = df_21[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_21


# <h2>2019-11-23</h2>

# In[88]:


file = open('NOV/2019-11-23/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[89]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_23 = pd.read_csv('NOV/2019-11-23/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[90]:


df_23['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_23 = df_23[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[91]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_23['XBINNING']*df_23['FWHM']*df_23['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[92]:


df_23['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_23 = df_23[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_23


# <h2>2019-11-30</h2>

# In[93]:


file = open('NOV/2019-11-30/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[94]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_30 = pd.read_csv('NOV/2019-11-30/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[95]:


df_30['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_30 = df_30[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[96]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_30['XBINNING']*df_30['FWHM']*df_30['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[97]:


df_30['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_30 = df_30[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_30


# In[98]:


df_NOV = pd.concat([df_4,df_20,df_21,df_23,df_30],sort=False)
df_NOV.to_csv('seeing_30s_R_NOV.csv')
df_NOV


# <h1>DEZEMBRO</h1>

# <h2>2019-12-02</h2>

# In[99]:


file = open('DEZ/2019-12-02/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[100]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_2 = pd.read_csv('DEZ/2019-12-02/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[101]:


df_2['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_2 = df_2[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[102]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_2['XBINNING']*df_2['FWHM']*df_2['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[103]:


df_2['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_2 = df_2[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_2


# <h2>2019-12-03</h2>

# In[104]:


file = open('DEZ/2019-12-03/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[105]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_3 = pd.read_csv('DEZ/2019-12-03/hselect_30s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[106]:


df_3['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_3 = df_3[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[107]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_3['XBINNING']*df_3['FWHM']*df_3['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[108]:


df_3['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_3 = df_3[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_3


# In[109]:


df_DEZ = pd.concat([df_2,df_3],sort=False)
df_DEZ.to_csv('seeing_30s_R_DEZ.csv')
df_DEZ


# In[110]:


df = pd.concat([df_ABR,df_AGO,df_DEZ,df_JUL,df_NOV,df_OUT,df_SET],sort=False)
df.to_csv('seeing_30s.csv')
df


# <h1>Seeing x Tempo </h1>

# In[111]:


it = ['2019-01-01T21:00:00']                             #Inicio das observaçoes
itime = Time(it, format = 'isot', scale = 'utc' )


# In[112]:


lista_tempos = Time(list(df['DATE-OBS']),format='isot',scale='utc')

dt = []
t = np.empty(len(df['DATE-OBS']))

for i in range(len(lista_tempos)):
    dt.append(lista_tempos[i] - itime)
    t[i] = (dt[i].value)/30


# In[113]:


estat = pd.DataFrame({'MÉDIA':[std.mean(df['SEEING'])],'MEDIANA':[std.median(df['SEEING'])],'MODA':[std.multimode(df['SEEING'])],'DESVPAD':[std.stdev(df['SEEING'])]})
estat.to_csv('estat_R_30s.dat')
estat


# In[ ]:


plt.figure(figsize=(10,5))
plt.hist(list(df['SEEING']),bins=20,label = r'$t_{exp} = 30s$',color='green',alpha=0.5,lw=1,edgecolor='black')
plt.ylabel('Frquência das imagens',size=15)
plt.xlabel('Seeing (")',size=15)
plt.xticks(np.arange(0,5,0.5))
plt.yticks(np.arange(0,22,2.5))
#plt.title('Seeing (1.48 $\pm$ 0.55) arcsec' + '      mediana 1.29 arcsec',size = 12,color='black')
plt.title('Média = 1.48 arcsec     Mediana = 1.29 arcsec     Moda =  arcsec     $\sigma$ = 0.55 arcsec',size=10)
plt.legend(prop={'size': 13})
plt.savefig('seeing_30s.png')
plt.show()

print('Seeing médio: ',std.mean(df['SEEING']),'\nMediana :',std.median(df['SEEING']),'\nModa: ',std.multimode(df['SEEING']),'Desvpad: ',std.stdev(df['SEEING']))


# In[ ]:




