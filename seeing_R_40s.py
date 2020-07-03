#!/usr/bin/env python
# coding: utf-8

# In[153]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.time import Time
#plt.style.use('classic')
import statistics as std
#get_ipython().run_line_magic('matplotlib', 'inline')


# <h1>JANEIRO</h1>

# <h2>2019-01-08</h2>

# In[2]:


file = open('JAN/2019-01-08/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[3]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_8 = pd.read_csv('JAN/2019-01-08/hselect_R_40s.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[4]:


df_8['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_8 = df_8[['DATE-OBS', 
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
seeing.append(0.343*df_8['XBINNING']*df_8['FWHM']*df_8['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[6]:


df_8['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_8 = df_8[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_8


# <h2>2019-01-10</h2>

# In[7]:


file = open('JAN/2019-01-10/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 279 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[8]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_10 = pd.read_csv('JAN/2019-01-10/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[9]:


df_10['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_10 = df_10[['DATE-OBS', 
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
seeing.append(0.343*df_10['XBINNING']*df_10['FWHM']*df_10['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[11]:


df_10['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_10 = df_10[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_10


# <h2>2019-01-12</h2>

# In[12]:


file = open('JAN/2019-01-12/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[13]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_12 = pd.read_csv('JAN/2019-01-12/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[14]:


fwhm


# In[15]:


df_12['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_12 = df_12[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[16]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_12['XBINNING']*df_12['FWHM']*df_12['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[17]:


df_12['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_12 = df_12[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_12


# <h2>2019-01-13</h2>

# In[18]:


file = open('JAN/2019-01-13/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[19]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_13 = pd.read_csv('JAN/2019-01-13/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[20]:


df_13['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_13 = df_13[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[21]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_13['XBINNING']*df_13['FWHM']*df_13['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[22]:


df_13['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_13 = df_13[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_13


# In[23]:


df_JAN = pd.concat([df_8, df_10, df_12, df_13],sort=False)
df_JAN.to_csv('seeing_40s_R_JAN.csv')
df_JAN


# <h1>FEVEREIRO</h1>

# <h2>2019-02-27</h2>

# In[24]:


file = open('FEV/2019-02-27/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[25]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_27 = pd.read_csv('FEV/2019-02-27/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[26]:


df_27['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_27 = df_27[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[27]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_27['XBINNING']*df_27['FWHM']*df_27['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[28]:


df_27['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_27 = df_27[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_27


# <h2>2019-02-28</h2>

# In[29]:


file = open('FEV/2019-02-28/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[30]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_28 = pd.read_csv('FEV/2019-02-28/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[31]:


df_28['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_28 = df_28[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[32]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_28['XBINNING']*df_28['FWHM']*df_28['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[33]:


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


# In[34]:


df_FEV = pd.concat([df_27,df_28],sort=False)
df_FEV.to_csv('seeing_40s_R_FEV.csv')
df_FEV


# <h1>MARÇO</h1>

# <h2>2019-03-01</h2>

# In[35]:


file = open('MAR/2019-03-01/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[36]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_1 = pd.read_csv('MAR/2019-03-01/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[37]:


df_1['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_1 = df_1[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[38]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_1['XBINNING']*df_1['FWHM']*df_1['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[39]:


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


# <h2>2019-03-02</h2>

# In[40]:


file = open('MAR/2019-03-02/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[41]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_2 = pd.read_csv('MAR/2019-03-02/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[42]:


df_2['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_2 = df_2[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[43]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_2['XBINNING']*df_2['FWHM']*df_2['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[44]:


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


# <h2>2019-03-08</h2>

# In[45]:


file = open('MAR/2019-03-08/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[46]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_8 = pd.read_csv('MAR/2019-03-08/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[47]:


df_8['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_8 = df_8[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[48]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_8['XBINNING']*df_8['FWHM']*df_8['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[49]:


df_8['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_8 = df_8[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_8


# <h2>2019-03-29</h2>

# In[50]:


file = open('MAR/2019-03-29/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[51]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_29 = pd.read_csv('MAR/2019-03-29/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[52]:


df_29['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_29 = df_29[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[53]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_29['XBINNING']*df_29['FWHM']*df_29['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[54]:


df_29['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_29 = df_29[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_29


# <h2>2019-03-31</h2>

# In[55]:


file = open('MAR/2019-03-31/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[56]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_31 = pd.read_csv('MAR/2019-03-31/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[57]:


df_31['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_31 = df_31[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[58]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_31['XBINNING']*df_31['FWHM']*df_31['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[59]:


df_31['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_31 = df_31[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_31


# In[60]:


df_MAR = pd.concat([df_1,df_2,df_8,df_29,df_31],sort=False)
df_MAR.to_csv('seeing_40s_R_MAR.csv')
df_MAR


# <h1>ABRIL</h1>

# <h2>2019-04-02</h2>

# In[61]:


file = open('ABR/2019-04-02/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[62]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_2 = pd.read_csv('ABR/2019-04-02/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[63]:


df_2['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_2 = df_2[['DATE-OBS', 
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
seeing.append(0.343*df_2['XBINNING']*df_2['FWHM']*df_2['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[65]:


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


# <h2>2019-04-03</h2>

# In[66]:


file = open('ABR/2019-04-03/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[67]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_3 = pd.read_csv('ABR/2019-04-03/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[68]:


df_3['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_3 = df_3[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[69]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_3['XBINNING']*df_3['FWHM']*df_3['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[70]:


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


# <h2>2019-04-04</h2>

# In[71]:


file = open('ABR/2019-04-04/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[72]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_4 = pd.read_csv('ABR/2019-04-04/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[73]:


df_4['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_4 = df_4[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[74]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_4['XBINNING']*df_4['FWHM']*df_4['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[75]:


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


# <h2>2019-04-11</h2>

# In[76]:


file = open('ABR/2019-04-11/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[77]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_11 = pd.read_csv('ABR/2019-04-11/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[78]:


df_11['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_11 = df_11[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[79]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_11['XBINNING']*df_11['FWHM']*df_11['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[80]:


df_11['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_11 = df_11[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_11


# In[81]:


df_ABR = pd.concat([df_2,df_3,df_4,df_11],sort=False)
df_ABR.to_csv('seeing_40s_R_ABR.csv')
df_ABR


# <h1>MAIO</h1>

# <h2>2019-05-01</h2>

# In[82]:


file = open('MAI/2019-05-01/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[83]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_1 = pd.read_csv('MAI/2019-05-01/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[84]:


df_1['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_1 = df_1[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[85]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_1['XBINNING']*df_1['FWHM']*df_1['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[86]:


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


# In[87]:


df_MAI = df_1
df_MAI.to_csv('seeing_40s_R_MAI.csv')
df_MAI


# <h1>JUNHO</h1>

# <h2>2019-06-04</h2>

# In[88]:


file = open('JUN/2019-06-04/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[89]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_4 = pd.read_csv('JUN/2019-06-04/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[90]:


df_4['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_4 = df_4[['DATE-OBS', 
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
seeing.append(0.343*df_4['XBINNING']*df_4['FWHM']*df_4['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[92]:


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


# <h2>2019-06-05</h2>

# In[93]:


file = open('JUN/2019-06-05/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[94]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_5 = pd.read_csv('JUN/2019-06-05/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[95]:


df_5['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_5 = df_5[['DATE-OBS', 
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
seeing.append(0.343*df_5['XBINNING']*df_5['FWHM']*df_5['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[97]:


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


# In[98]:


df_JUN = pd.concat([df_4,df_5],sort=False)
df_JUN.to_csv('seeing_40s_R_JUN.csv')
df_JUN


# <h1>AGOSTO</h1>

# <h2>2019-08-27</h2>

# In[99]:


file = open('AGO/2019-08-27/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[100]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_27 = pd.read_csv('AGO/2019-08-27/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[101]:


df_27['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_27 = df_27[['DATE-OBS', 
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
seeing.append(0.343*df_27['XBINNING']*df_27['FWHM']*df_27['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[103]:


df_27['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_27 = df_27[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_27


# <h2>2019-08-28</h2>

# In[104]:


file = open('AGO/2019-08-28/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[105]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_28 = pd.read_csv('AGO/2019-08-28/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[106]:


df_28['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_28 = df_28[['DATE-OBS', 
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
seeing.append(0.343*df_28['XBINNING']*df_28['FWHM']*df_28['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[108]:


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


# <h2>2019-08-29</h2>

# In[109]:


file = open('AGO/2019-08-29/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[110]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_29 = pd.read_csv('AGO/2019-08-29/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[111]:


df_29['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_29 = df_29[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[112]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_29['XBINNING']*df_29['FWHM']*df_29['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[113]:


df_29['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_29 = df_29[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_29


# <h2>2019-08-30</h2>

# In[114]:


file = open('AGO/2019-08-30/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[115]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_30 = pd.read_csv('AGO/2019-08-30/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[116]:


df_30['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_30 = df_30[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[117]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_30['XBINNING']*df_30['FWHM']*df_30['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[118]:


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


# <h2>2019-08-31</h2>

# In[119]:


file = open('AGO/2019-08-31/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[120]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_31 = pd.read_csv('AGO/2019-08-31/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[121]:


df_31['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_31 = df_31[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[122]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_31['XBINNING']*df_31['FWHM']*df_31['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[123]:


df_31['SEEING'] = seeing                                        #Criando uma coluna com os valores do seeing

df_31 = df_31[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING',
         'SEEING',
         'IMAGE-NAME']]                                      #Mudando a ordem das colunas
df_31


# In[124]:


df_AGO = pd.concat([df_27,df_28,df_29,df_30,df_31],sort=False)
df_AGO.to_csv('seeing_40s_R_AGO.csv')
df_AGO


# <h1>SETEMBRO</h1>

# <h2>2019-09-04</h2>

# In[125]:


file = open('SET/2019-09-04/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[126]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_4 = pd.read_csv('SET/2019-09-04/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[127]:


df_4['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_4 = df_4[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[128]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_4['XBINNING']*df_4['FWHM']*df_4['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[129]:


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


# <h2>2019-09-05</h2>

# In[130]:


file = open('SET/2019-09-05/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[131]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_5 = pd.read_csv('SET/2019-09-05/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[132]:


df_5['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_5 = df_5[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[133]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_5['XBINNING']*df_5['FWHM']*df_5['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[134]:


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


# In[135]:


df_SET = pd.concat([df_4,df_5],sort=False)
df_SET.to_csv('seeing_40s_R_SET.csv')
df_SET


# <h1>OUTUBRO</h1>

# <h2>2019-10-25</h2>

# In[136]:


file = open('OUT/2019-10-25/logfile','r')                #Abrindo o arquivo onde estão os valores do fwhm

fwhm = []                                                #Inicializando a lista do fwhm

for indice, linha in enumerate(file):                    #Loop para ler as linhas apartir da 1930 e pegar o fwhm
    if indice  > 1:
        if linha[:47] == '  Average full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[47:]))
        elif linha[:39] == '  Full width at half maximum (FWHM) of ': 
            fwhm.append(float(linha[39:]))


# In[137]:


#Lendo o arquivo criado pelo hselect no IRAF que contém os dados do header
df_25 = pd.read_csv('OUT/2019-10-25/hselect_40s_R.dat',sep='\t',header=None,names=['DATE-OBS', 
                                                                               'FILTER',
                                                                               'EXP-TIME',
                                                                               'AIRMASS',
                                                                               'XBINNING',
                                                                               'IMAGE-NAME'])


# In[138]:


df_25['FWHM'] = fwhm                                         #Criando uma coluna com os valores do fwhm

df_25 = df_25[['DATE-OBS', 
         'FILTER',
         'EXP-TIME',
         'AIRMASS',
         'FWHM',
         'XBINNING', 
         'IMAGE-NAME']]                                   #Mudando a ordem das colunas


# In[139]:


'''
- Inicializando lista do seeing
- Calculando o seeing
- Transformando o primeiro elemento da lista (que contém todos os valores do seeing) em uma lista
'''
seeing = []
seeing.append(0.343*df_25['XBINNING']*df_25['FWHM']*df_25['AIRMASS']**(-0.6)*(6289/5000)**(-0.2))
seeing = seeing[0].values.tolist()


# In[140]:


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


# In[141]:


df_OUT = df_25
df_OUT.to_csv('seeing_40s_R_OUT.csv')
df_OUT


# <h1>Seeing x Tempo </h1>

# In[142]:


df_2019 = pd.concat([df_JAN,df_FEV,df_MAR,df_ABR,df_MAI,df_JUN,df_AGO,df_SET,df_OUT],sort=False)
df_2019.to_csv('seeing_40s.csv')
df_2019


# In[143]:


df_2019['SEEING'].max()


# In[144]:


it = ['2019-01-01T21:00:00']                             #Inicio das observaçoes
itime = Time(it, format = 'isot', scale = 'utc' )


# In[145]:


lista_tempos = Time(list(df_2019['DATE-OBS']),format='isot',scale='utc')

dt = []
t = np.empty(len(df_2019['DATE-OBS']))

for i in range(len(lista_tempos)):
    dt.append(lista_tempos[i] - itime)
    t[i] = (dt[i].value)/30


# In[162]:


estat = pd.DataFrame({'MÉDIA':[std.mean(df_2019['SEEING'])],'MEDIANA':[std.median(df_2019['SEEING'])],'MODA':[''],'DESVPAD':[std.stdev(df_2019['SEEING'])]})
estat.to_csv('estat_R_40s.dat')
estat
#std.multimode(df_2019['SEEING'])


# In[163]:


plt.figure(figsize=(10,5))
plt.hist(list(df_2019['SEEING']),bins=20,label = r'$t_{exp} = 40s$',color='blue',alpha=0.5,lw=1,edgecolor='black')
plt.ylabel('Frquência das imagens',size=15)
plt.xlabel('Seeing (")',size=15)
plt.xticks(np.arange(0,5,0.5))
plt.yticks(np.arange(0,22,2.5))
plt.title('Média = 1.36 arcsec     Mediana = 1.27 arcsec     Moda =  arcsec     $\sigma$ = 0.47 arcsec',size=10)
plt.legend(prop={'size': 13})
plt.savefig('seeing_40s.png')
plt.show()

print('Seeing médio: ',std.mean(df_2019['SEEING']),'\nMediana :',std.median(df_2019['SEEING']),'\nModa: ',std.multimode(df_2019['SEEING']),'Desvpad: ',std.stdev(df_2019['SEEING']))


# In[ ]:





# In[ ]:




