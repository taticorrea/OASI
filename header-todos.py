#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import pandas as pd
import statistics as std


# <h1>JANEIRO</h1>

# In[2]:


dia_5_raw = pd.read_csv('JAN/2019-01-05/2019-01-05_raw.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_5_calib = pd.read_csv('JAN/2019-01-05/2019-01-05_calib.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_8_raw = pd.read_csv('JAN/2019-01-08/2019-01-08_raw.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_8_calib = pd.read_csv('JAN/2019-01-08/2019-01-08_calib.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_10 = pd.read_csv('JAN/2019-01-10/2019-01-10.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_11 = pd.read_csv('JAN/2019-01-11/2019-01-11.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_12 = pd.read_csv('JAN/2019-01-12/2019-01-12.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_13 = pd.read_csv('JAN/2019-01-13/2019-01-13.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('JAN/2019-01-28/2019-01-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('JAN/2019-01-29/2019-01-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_30 = pd.read_csv('JAN/2019-01-30/2019-01-30.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_31 = pd.read_csv('JAN/2019-01-31/2019-01-31.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[3]:


JAN = pd.concat([dia_5_raw,dia_8_raw,dia_10,dia_11,dia_12,dia_13,dia_28,dia_29,dia_30,dia_31], sort=False)
JAN.to_csv('JAN_dados.csv')
JAN


# <h1>FEVEREIRO</h1>

# In[4]:


dia_1 = pd.read_csv('FEV/2019-02-01/2019-02-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('FEV/2019-02-03/2019-02-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('FEV/2019-02-04/2019-02-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('FEV/2019-02-05/2019-02-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_7 = pd.read_csv('FEV/2019-02-07/2019-02-07.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_8 = pd.read_csv('FEV/2019-02-08/2019-02-08.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_9 = pd.read_csv('FEV/2019-02-09/2019-02-09.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_10 = pd.read_csv('FEV/2019-02-10/2019-02-10.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_11 = pd.read_csv('FEV/2019-02-11/2019-02-11.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('FEV/2019-02-27/2019-02-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('FEV/2019-02-28/2019-02-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[5]:


FEV = pd.concat([dia_1,dia_3,dia_4,dia_5,dia_7,dia_8,dia_9,dia_10,dia_11,dia_27,dia_28], sort=False)
FEV.to_csv('FEV_dados.csv')
FEV


# <h1>MARÇO</h1>

# In[6]:


dia_1 = pd.read_csv('MAR/2019-03-01/2019-03-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('MAR/2019-03-02/2019-03-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('MAR/2019-03-05/2019-03-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_6 = pd.read_csv('MAR/2019-03-06/2019-03-06.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_8 = pd.read_csv('MAR/2019-03-08/2019-03-08.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_9 = pd.read_csv('MAR/2019-03-09/2019-03-09.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_10 = pd.read_csv('MAR/2019-03-10/2019-03-10.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_11 = pd.read_csv('MAR/2019-03-11/2019-03-11.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_12 = pd.read_csv('MAR/2019-03-12/2019-03-12.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('MAR/2019-03-29/2019-03-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_31 = pd.read_csv('MAR/2019-03-31/2019-03-31.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[7]:


MAR = pd.concat([dia_1,dia_2,dia_5,dia_6,dia_8,dia_9,dia_10,dia_11,dia_12,dia_29,dia_31], sort=False)
MAR.to_csv('MAR_dados.csv')
MAR


# <h1>ABRIL</h1>

# In[8]:


dia_1 = pd.read_csv('ABR/2019-04-01/2019-04-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('ABR/2019-04-02/2019-04-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('ABR/2019-04-03/2019-04-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('ABR/2019-04-04/2019-04-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('ABR/2019-04-05/2019-04-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_7 = pd.read_csv('ABR/2019-04-07/2019-04-07.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_9 = pd.read_csv('ABR/2019-04-09/2019-04-09.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_10 = pd.read_csv('ABR/2019-04-10/2019-04-10.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_11 = pd.read_csv('ABR/2019-04-11/2019-04-11.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_12 = pd.read_csv('ABR/2019-04-12/2019-04-12.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('ABR/2019-04-27/2019-04-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('ABR/2019-04-29/2019-04-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[9]:


ABR = pd.concat([dia_1,dia_2,dia_3,dia_4,dia_5,dia_7,dia_9,dia_10,dia_11,dia_12,dia_27,dia_29], sort=False)
ABR.to_csv('ABR_dados.csv')
ABR


# <h1>MAIO</h1>

# In[10]:


#dia_5 = pd.read_csv('/JAN/2019-01-05/.csv')
dia_1 = pd.read_csv('MAI/2019-05-01/2019-05-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('MAI/2019-05-02/2019-05-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('MAI/2019-05-03/2019-05-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('MAI/2019-05-04/2019-05-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('MAI/2019-05-05/2019-05-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_6 = pd.read_csv('MAI/2019-05-06/2019-05-06.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_9 = pd.read_csv('MAI/2019-05-09/2019-05-09.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_10 = pd.read_csv('MAI/2019-05-10/2019-05-10.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_11 = pd.read_csv('MAI/2019-05-11/2019-05-11.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('MAI/2019-05-27/2019-05-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('MAI/2019-05-28/2019-05-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('MAI/2019-05-29/2019-05-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_30 = pd.read_csv('MAI/2019-05-30/2019-05-30.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('MAI/2019-05-31/2019-05-31.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[11]:


MAI = pd.concat([dia_1,dia_3,dia_4,dia_5,dia_6,dia_8,dia_9,dia_10,dia_11,dia_27,dia_28,dia_29,dia_30,dia_31], sort=False)
MAI.to_csv('MAI_dados.csv')
MAI


# <h1>JUNHO</h1>

# In[12]:


dia_1 = pd.read_csv('JUN/2019-06-01/2019-06-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('JUN/2019-06-02/2019-06-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('JUN/2019-06-03/2019-06-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_4 = pd.read_csv('JUN/2019-06-04/2019-06-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('JUN/2019-06-05/2019-06-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_6 = pd.read_csv('JUN/2019-06-06/2019-06-06.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_7 = pd.read_csv('JUN/2019-06-07/2019-06-07.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_8 = pd.read_csv('JUN/2019-06-08/2019-06-08.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_9 = pd.read_csv('JUN/2019-06-09/2019-06-09.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_10 = pd.read_csv('JUN/2019-06-10/2019-06-10.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_16 = pd.read_csv('JUN/2019-06-16/2019-06-16.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_25 = pd.read_csv('JUN/2019-06-25/2019-06-25.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_26 = pd.read_csv('JUN/2019-06-26/2019-06-26.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_28 = pd.read_csv('JUN/2019-06-28/2019-06-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_29 = pd.read_csv('JUN/2019-06-29/2019-06-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[13]:


JUN = pd.concat([dia_1,dia_2,dia_3,dia_5,dia_6,dia_7,dia_8,dia_9,dia_10,dia_16,dia_25], sort=False)
JUN.to_csv('JUN_dados.csv')
JUN


# <h1>JULHO</h1>

# In[14]:


#dia_1 = pd.read_csv('JUL/2019-07-01/2019-07-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('JUL/2019-07-02/2019-07-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('JUL/2019-07-03/2019-07-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('JUL/2019-07-04/2019-07-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('JUL/2019-07-05/2019-07-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_6 = pd.read_csv('JUL/2019-07-06/2019-07-06.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_7 = pd.read_csv('JUL/2019-07-07/2019-07-07.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_8 = pd.read_csv('JUL/2019-07-08/2019-07-08.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_9 = pd.read_csv('JUL/2019-07-09/2019-07-09.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_26 = pd.read_csv('JUL/2019-07-26/2019-07-26.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('JUL/2019-07-27/2019-07-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('JUL/2019-07-28/2019-07-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('JUL/2019-07-29/2019-07-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_30 = pd.read_csv('JUL/2019-07-30/2019-07-30.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_31 = pd.read_csv('JUL/2019-07-31/2019-07-31.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[15]:


JUL = pd.concat([dia_2,dia_3,dia_4,dia_5,dia_6,dia_7,dia_26,dia_29,dia_31,dia_27,dia_28], sort=False)
JUL.to_csv('JUL_dados.csv')
JUL


# <h1>AGOSTO</h1>

# In[16]:


dia_1 = pd.read_csv('AGO/2019-08-01/2019-08-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('AGO/2019-08-02/2019-08-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('AGO/2019-08-03/2019-08-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('AGO/2019-08-04/2019-08-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_6 = pd.read_csv('AGO/2019-08-06/2019-08-06.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_7 = pd.read_csv('AGO/2019-08-07/2019-08-07.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_23 = pd.read_csv('AGO/2019-08-23/2019-08-23.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_24 = pd.read_csv('AGO/2019-08-24/2019-08-24.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_25 = pd.read_csv('AGO/2019-08-25/2019-08-25.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_26 = pd.read_csv('AGO/2019-08-26/2019-08-26.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('AGO/2019-08-27/2019-08-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('AGO/2019-08-28/2019-08-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('AGO/2019-08-29/2019-08-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_30 = pd.read_csv('AGO/2019-08-30/2019-08-30.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_31 = pd.read_csv('AGO/2019-08-31/2019-08-31.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[17]:


AGO = pd.concat([dia_1,dia_2,dia_3,dia_4,dia_7,dia_23,dia_24,dia_25,dia_26,dia_27,dia_28,dia_29,dia_30,dia_31], sort=False)
AGO.to_csv('AGO_dados.csv')
AGO


# <h1>SETEMBRO</h1>

# In[18]:


dia_1 = pd.read_csv('SET/2019-09-01/2019-09-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('SET/2019-09-02/2019-09-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('SET/2019-09-03/2019-09-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('SET/2019-09-04/2019-09-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_5 = pd.read_csv('SET/2019-09-05/2019-09-05.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_6 = pd.read_csv('SET/2019-09-06/2019-09-06.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_21 = pd.read_csv('SET/2019-09-21/2019-09-21.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_22 = pd.read_csv('SET/2019-09-22/2019-09-22.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_23 = pd.read_csv('SET/2019-09-23/2019-09-23.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_24 = pd.read_csv('SET/2019-09-24/2019-09-24.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_25 = pd.read_csv('SET/2019-09-25/2019-09-25.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[19]:


SET = pd.concat([dia_1,dia_2,dia_3,dia_4,dia_5,dia_22,dia_24,dia_25], sort=False)
SET.to_csv('SET_dados.csv')
SET


# <h1>OUTUBRO</h1>

# In[20]:


dia_23 = pd.read_csv('OUT/2019-10-23/2019-10-23.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_24 = pd.read_csv('OUT/2019-10-24/2019-10-24.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_25 = pd.read_csv('OUT/2019-10-25/2019-10-25.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_26 = pd.read_csv('OUT/2019-10-26/2019-10-26.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('OUT/2019-10-27/2019-10-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('OUT/2019-10-28/2019-10-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('OUT/2019-10-29/2019-10-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_30 = pd.read_csv('OUT/2019-10-30/2019-10-30.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_31 = pd.read_csv('OUT/2019-10-31/2019-10-31.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[21]:


OUT = pd.concat([dia_23,dia_24,dia_25,dia_26,dia_27,dia_28,dia_29,dia_30,dia_31], sort=False)
OUT.to_csv('OUT_dados.csv')
OUT


# <h1>NOVEMBRO</h1>

# In[22]:


#dia_1 = pd.read_csv('NOV/2019-11-01/2019-11-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_2 = pd.read_csv('NOV/2019-11-02/2019-11-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('NOV/2019-11-03/2019-11-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_4 = pd.read_csv('NOV/2019-11-04/2019-11-04.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_19 = pd.read_csv('NOV/2019-11-19/2019-11-19.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_20 = pd.read_csv('NOV/2019-11-20/2019-11-20.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_21 = pd.read_csv('NOV/2019-11-21/2019-11-21.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_22 = pd.read_csv('NOV/2019-11-22/2019-11-22.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_23 = pd.read_csv('NOV/2019-11-23/2019-11-23.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_24 = pd.read_csv('NOV/2019-11-24/2019-11-24.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
#dia_25 = pd.read_csv('NOV/2019-11-25/2019-11-25.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_26 = pd.read_csv('NOV/2019-11-26/2019-11-26.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_27 = pd.read_csv('NOV/2019-11-27/2019-11-27.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_28 = pd.read_csv('NOV/2019-11-28/2019-11-28.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_29 = pd.read_csv('NOV/2019-11-29/2019-11-29.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_30 = pd.read_csv('NOV/2019-11-30/2019-11-30.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[23]:


NOV = pd.concat([dia_3,dia_4,dia_19,dia_20,dia_21,dia_22,dia_23,dia_26,dia_27,dia_28,dia_29,dia_30,dia_31], sort=False)
NOV.to_csv('NOV_dados.csv')
NOV


# <h1>DEZEMBRO</h1>

# In[24]:


dia_1 = pd.read_csv('DEZ/2019-12-01/2019-12-01.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_2 = pd.read_csv('DEZ/2019-12-02/2019-12-02.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_3 = pd.read_csv('DEZ/2019-12-03/2019-12-03.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_18 = pd.read_csv('DEZ/2019-12-18/2019-12-18.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_19 = pd.read_csv('DEZ/2019-12-19/2019-12-19.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_20 = pd.read_csv('DEZ/2019-12-20/2019-12-20.dat',sep='\t',names=['EXP-TIME', 'FILTER'])
dia_21 = pd.read_csv('DEZ/2019-12-21/2019-12-21.dat',sep='\t',names=['EXP-TIME', 'FILTER'])


# In[25]:


DEZ = pd.concat([dia_1,dia_2,dia_3,dia_18,dia_19,dia_20,dia_21], sort=False)
DEZ.to_csv('DEZ_dados.csv')
DEZ


# <h1>2019</h1>

# In[26]:


year = pd.concat([JAN,FEV,MAR,ABR,MAI,JUN,JUL,AGO,SET,OUT,NOV,DEZ], sort=False)
year.to_csv('2019_dados.csv')
year


# In[27]:


grupos = year.groupby(['FILTER'])                       #Agrupando por filtros
count = pd.DataFrame(grupos.count())                    #Criando dataFrame com o número de imagens por filtro
count


# In[28]:


eixo_x = ['B','Clear','I','No Filter','R','U','V','g','i','r','u','z']                #Plotando o número de imagens por filtro
plt.figure(figsize=(12,7))
plt.bar(eixo_x,count['EXP-TIME'],facecolor='darkred', alpha = 0.5, lw=1)
plt.title('Número de imagens por filtro',size=15)
plt.ylabel('Número de imagens',size=12)
plt.savefig('imagens_filtro.png')
plt.show()


# In[29]:


'''
eixo_x = ['B','Clear','I','No Filter','R','U','V','g','i','r','u','z']                #Plotando o número de imagens por filtro
'''


# In[30]:


filtro_B = grupos.get_group('B')         
filtro_I = grupos.get_group('I')         
filtro_U = grupos.get_group('U')      
filtro_V = grupos.get_group('V')      
filtro_u = grupos.get_group('u')        
filtro_r = grupos.get_group('r')       
filtro_R = grupos.get_group('R')
filtro_g = grupos.get_group('g')
filtro_z = grupos.get_group('z')
filtro_i = grupos.get_group('i')
filtro_NF = grupos.get_group('No Filter')
filtro_clear = grupos.get_group('Clear')          


# <h1>Histogramas por filtro</h1>

# <h2>Filtro Clear</h2>

# In[31]:


plt.figure(figsize=(12,7))
plt.hist(filtro_clear['EXP-TIME'],label='Filtro Clear',bins=10,facecolor='brown', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_Clear.png')
plt.show()


# In[32]:


mean_exp_time_clear = std.mean(filtro_clear['EXP-TIME'])
median_exp_time_clear = std.median(filtro_clear['EXP-TIME'])
#desvpad_exp_time_clear = std.stdev(filtro_clear['EXP-TIME'])
moda_exp_time_clear = std.mode(filtro_clear['EXP-TIME'])

print('FILTRO Clear')
print('moda:',moda_exp_time_clear,'s')
print('média: ',mean_exp_time_clear,'s')
print('mediana: ',median_exp_time_clear,'s')
#print('desvio padrão: ',desvpad_exp_time_clear,'s')


# <h2>Filtro u</h2>

# In[33]:


plt.figure(figsize=(12,7))
plt.hist(filtro_u['EXP-TIME'],label='Filtro u',bins=7,facecolor='darkgreen', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_u.png')
plt.show()


# In[34]:


mean_exp_time_u = std.mean(filtro_u['EXP-TIME'])
median_exp_time_u = std.median(filtro_u['EXP-TIME'])
desvpad_exp_time_u = std.stdev(filtro_u['EXP-TIME'])
#moda_exp_time_u = std.mode(filtro_u['EXP-TIME'])

print('FILTRO u')
#print('moda:',moda_exp_time_u,'s')
print('média: ',mean_exp_time_u,'s')
print('mediana: ',median_exp_time_u,'s')
print('desvio padrão: ',desvpad_exp_time_u,'s')


# <h2>Filtro z</h2>

# In[35]:


plt.figure(figsize=(12,7))
plt.hist(filtro_z['EXP-TIME'],label='Filtro z',bins=7,facecolor='pink', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_z.png')
plt.show()


# In[36]:


mean_exp_time_z = std.mean(filtro_z['EXP-TIME'])
median_exp_time_z = std.median(filtro_z['EXP-TIME'])
desvpad_exp_time_z = std.stdev(filtro_z['EXP-TIME'])
moda_exp_time_z = std.mode(filtro_z['EXP-TIME'])

print('FILTRO z')
print('moda:',moda_exp_time_z,'s')
print('média: ',mean_exp_time_z,'s')
print('mediana: ',median_exp_time_z,'s')
print('desvio padrão: ',desvpad_exp_time_z,'s')


# <h2>Filtro V</h2>

# In[37]:


plt.figure(figsize=(12,7))
plt.hist(filtro_V['EXP-TIME'],label='Filtro V',bins=7,facecolor='black', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_V.png')
plt.show()


# In[38]:


mean_exp_time_V = std.mean(filtro_V['EXP-TIME'])
median_exp_time_V = std.median(filtro_V['EXP-TIME'])
desvpad_exp_time_V = std.stdev(filtro_V['EXP-TIME'])
moda_exp_time_V = std.mode(filtro_V['EXP-TIME'])

print('FILTRO V')
print('moda:',moda_exp_time_V,'s')
print('média: ',mean_exp_time_V,'s')
print('mediana: ',median_exp_time_V,'s')
print('desvio padrão: ',desvpad_exp_time_V,'s')


# <h2>Filtro U</h2>

# In[39]:


plt.figure(figsize=(12,7))
plt.hist(filtro_U['EXP-TIME'],label='Filtro U',bins=7,facecolor='yellow', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_U.png')
plt.show()


# In[40]:


mean_exp_time_U = std.mean(filtro_U['EXP-TIME'])
median_exp_time_U = std.median(filtro_U['EXP-TIME'])
desvpad_exp_time_U = std.stdev(filtro_U['EXP-TIME'])
moda_exp_time_U = std.mode(filtro_U['EXP-TIME'])

print('FILTRO B')
print('moda:',moda_exp_time_U,'s')
print('média: ',mean_exp_time_U,'s')
print('mediana: ',median_exp_time_U,'s')
print('desvio padrão: ',desvpad_exp_time_U,'s')


# <h2>Filtro I</h2>

# In[41]:


plt.figure(figsize=(12,7))
plt.hist(filtro_I['EXP-TIME'],label='Filtro I',bins=15,facecolor='green', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_I.png')
plt.show()


# In[42]:


mean_exp_time_I = std.mean(filtro_I['EXP-TIME'])
median_exp_time_I = std.median(filtro_I['EXP-TIME'])
desvpad_exp_time_I = std.stdev(filtro_I['EXP-TIME'])
moda_exp_time_I = std.mode(filtro_I['EXP-TIME'])

print('FILTRO I')
print('moda:',moda_exp_time_I,'s')
print('média: ',mean_exp_time_I,'s')
print('mediana: ',median_exp_time_I,'s')
print('desvio padrão: ',desvpad_exp_time_I,'s')


# <h2>Filtro B</h2>

# In[43]:


plt.figure(figsize=(12,7))
plt.hist(filtro_B['EXP-TIME'],label='Filtro B',bins=7,facecolor='red', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_B.png')
plt.show()


# In[44]:


mean_exp_time_B = std.mean(filtro_B['EXP-TIME'])
median_exp_time_B = std.median(filtro_B['EXP-TIME'])
desvpad_exp_time_B = std.stdev(filtro_B['EXP-TIME'])
moda_exp_time_B = std.mode(filtro_B['EXP-TIME'])

print('FILTRO B')
print('moda:',moda_exp_time_B,'s')
print('média: ',mean_exp_time_B,'s')
print('mediana: ',median_exp_time_B,'s')
print('desvio padrão: ',desvpad_exp_time_B,'s')


# <h2>Filtro r</h2>

# In[45]:


plt.figure(figsize=(12,7))
plt.hist(filtro_r['EXP-TIME'],label='Filtro r',bins=14,facecolor='purple', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_r.png')
plt.show()


# In[46]:


mean_exp_time_r = std.mean(filtro_r['EXP-TIME'])
median_exp_time_r = std.median(filtro_r['EXP-TIME'])
desvpad_exp_time_r = std.stdev(filtro_r['EXP-TIME'])
moda_exp_time_r = std.mode(filtro_r['EXP-TIME'])

print('FILTRO r')
print('moda:',moda_exp_time_r,'s')
print('média: ',mean_exp_time_r,'s')
print('mediana: ',median_exp_time_r,'s')
print('desvio padrão: ',desvpad_exp_time_r,'s')


# <h2>Filtro R</h2>

# In[47]:


plt.figure(figsize=(12,7))
plt.hist(filtro_R['EXP-TIME'],label='Filtro R',bins=13,facecolor='darkorange', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_R.png')
plt.show()


# In[48]:


mean_exp_time_R = std.mean(filtro_R['EXP-TIME'])
median_exp_time_R = std.median(filtro_R['EXP-TIME'])
desvpad_exp_time_R = std.stdev(filtro_R['EXP-TIME'])
moda_exp_time_R = std.mode(filtro_R['EXP-TIME'])

print('FILTRO R')
print('moda:',moda_exp_time_R,'s')
print('média: ',mean_exp_time_R,'s')
print('mediana: ',median_exp_time_R,'s')
print('desvio padrão: ',desvpad_exp_time_R,'s')


# <h2>Filtro g</h2>

# In[49]:


plt.figure(figsize=(12,7))
plt.hist(filtro_g['EXP-TIME'],label='Filtro g',bins=10,color='darkgrey', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_g.png')
plt.show()


# In[50]:


mean_exp_time_g = std.mean(filtro_g['EXP-TIME'])
median_exp_time_g = std.median(filtro_g['EXP-TIME'])
desvpad_exp_time_g = std.stdev(filtro_g['EXP-TIME'])
moda_exp_time_g = std.mode(filtro_g['EXP-TIME'])

print('FILTRO g')
print('moda:',moda_exp_time_g,'s')
print('média: ',mean_exp_time_g,'s')
print('mediana: ',median_exp_time_g,'s')
print('desvio padrão: ',desvpad_exp_time_g,'s')


# <h2>Filtro z</h2>

# In[51]:


plt.figure(figsize=(12,7))
plt.hist(filtro_z['EXP-TIME'],label='Filtro z',bins=13,color='darkred', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_z.png')
plt.show()


# In[52]:


mean_exp_time_z = std.mean(filtro_z['EXP-TIME'])
median_exp_time_z = std.median(filtro_z['EXP-TIME'])
desvpad_exp_time_z = std.stdev(filtro_z['EXP-TIME'])
moda_exp_time_z = std.mode(filtro_z['EXP-TIME'])

print('FILTRO z')
print('moda:',moda_exp_time_z,'s')
print('média: ',mean_exp_time_z,'s')
print('mediana: ',median_exp_time_z,'s')
print('desvio padrão: ',desvpad_exp_time_z,'s')


# <h2>Filtro i</h2>

# In[53]:


plt.figure(figsize=(12,7))
plt.hist(filtro_i['EXP-TIME'],label='Filtro i',bins=10,color='darkblue', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_i.png')
plt.show()


# In[54]:


mean_exp_time_i = std.mean(filtro_i['EXP-TIME'])
median_exp_time_i = std.median(filtro_i['EXP-TIME'])
desvpad_exp_time_i = std.stdev(filtro_i['EXP-TIME'])
moda_exp_time_i = std.mode(filtro_i['EXP-TIME'])

print('FILTRO i')
print('moda:',moda_exp_time_i,'s')
print('média: ',mean_exp_time_i,'s')
print('mediana: ',median_exp_time_i,'s')
print('desvio padrão: ',desvpad_exp_time_i,'s')


# <h2>Sem Filtro </h2>

# In[55]:


plt.figure(figsize=(12,7))
plt.hist(filtro_NF['EXP-TIME'],label='Sem Filtro',bins=13,color='darkgreen', alpha = 0.5, lw=1, edgecolor='black')
plt.title('Tempo de exposição no ano de 2019',size=20)
plt.ylabel('Frequência de ocorrência',size=15)
plt.xlabel('Tempo de exposição (segundos)',size=15)
plt.legend()
plt.savefig('exptime-hist_NF.png')
plt.show()


# In[56]:


mean_exp_time_NF = std.mean(filtro_NF['EXP-TIME'])
median_exp_time_NF = std.median(filtro_NF['EXP-TIME'])
desvpad_exp_time_NF = std.stdev(filtro_NF['EXP-TIME'])
moda_exp_time_NF = std.stdev(filtro_NF['EXP-TIME'])

print('SEM FILTRO')
print('moda:',moda_exp_time_NF,'s')
print('média: ',mean_exp_time_NF,'s')
print('mediana: ',median_exp_time_NF,'s')
print('desvio padrão: ',desvpad_exp_time_NF,'s')


# <h1>Tabela Estatística</h1>

# In[57]:


#estatistica = pd.DataFrame({'FILTRO':['z','i'],'MODA':[moda_exp_time_z,moda_exp_time_i],'MEDIA':[mean_exp_time_r,mean_exp_time_R,mean_exp_time_G,mean_exp_time_z,mean_exp_time_i],'MEDIANA':[mean_exp_time_r,mean_exp_time_R,mean_exp_time_G,mean_exp_time_z,mean_exp_time_i]})

estatistica = pd.DataFrame({'FILTRO':['U','u','r','R','g','z','i','Sem Filtro','V','B','I','Clear'],
                            'MODA':['',moda_exp_time_U,moda_exp_time_r,moda_exp_time_V,moda_exp_time_B,moda_exp_time_I,moda_exp_time_clear,moda_exp_time_R,moda_exp_time_g,moda_exp_time_z,moda_exp_time_i,moda_exp_time_NF],
                            'MEDIA':[mean_exp_time_u,mean_exp_time_U,mean_exp_time_r,mean_exp_time_V,mean_exp_time_B,mean_exp_time_I,mean_exp_time_clear,mean_exp_time_R,mean_exp_time_g,mean_exp_time_z,mean_exp_time_i,mean_exp_time_NF],
                            'MEDIANA':[median_exp_time_u,median_exp_time_U,median_exp_time_r,median_exp_time_V,median_exp_time_B,median_exp_time_I,median_exp_time_clear,median_exp_time_R,median_exp_time_g,median_exp_time_z,median_exp_time_i,median_exp_time_NF]})

estatistica.to_csv('estatistica.csv')
estatistica

