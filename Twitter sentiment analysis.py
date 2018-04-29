
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().system('pip install tweepy')


# In[3]:


get_ipython().system('pip install textblob')


# In[10]:


import tweepy


# In[8]:


import nltk
nltk.download('punkt')


# In[10]:


nltk.download('averaged_perceptron_tagger')


# In[2]:


from textblob import TextBlob


# In[3]:


w=TextBlob('Prithvi is a thin guy and his life revolves on Sarcasm')


# In[4]:


w


# In[11]:


w.tags


# In[5]:


w.words


# In[6]:


w.sentiment.polarity


# In[7]:


consumer_key= 'uScSMZyGyKLL1QS0IZn6LwhmR'
consumer_secret= 'NFnSxuL0tP2NR13Iw8bIMoWDDW5sgUWHDyTYKtvqimtfBI7QDl'


# In[8]:


access_token='93947520-tMImwLjyqYj0wrkwjszxCoZIVmIZao0ZA6kmwCWl8'
access_token_secret='ClvWkfVPG4AxMRU6btSNLEOI3AmCpbQwQCmdsqPO5bfUZ'


# In[11]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


# In[12]:


auth.set_access_token(access_token, access_token_secret)


# In[13]:


api = tweepy.API(auth)


# In[14]:


sachin_tweets=api.search('Sachin Tendulkar')


# In[15]:


l=[]
for tweets in sachin_tweets:
    a=TextBlob(tweets.text)
    l.append(a.polarity)


# In[16]:


np.mean(l)
#Indicating positive sentiment when Sachin Tendulkar is mentioned in tweets


# In[119]:


chester_tweets=api.search('Chester Bennington')


# In[120]:


l2=[]
for tweets in chester_tweets:
    a=TextBlob(tweets.text)
    l2.append(a.polarity)


# In[121]:


np.mean(l2)
#Indicating negative sentiment due to recent death of Chester Bennington


# In[111]:


a_tweets=api.search('Avicii')


# In[112]:


l3=[]
for tweets in a_tweets:
    a=TextBlob(tweets.text)
    l3.append(a.polarity)


# In[113]:


np.mean(l3)
#Indicating negative sentiment due to recent death of Avicii


# In[122]:


l4=[]
l5=[]
for tweets in chester_tweets:
    a=TextBlob(tweets.text)
    l4.append(tweets.text)
    l5.append(a.polarity)


# In[123]:


df=pd.DataFrame({'Tweets':l4,'Polarity':l5})


# In[124]:


df['Label']=df.Polarity.map({(-1):'Negative Sentiment',0:'Neutral Sentiment',(1):'Positive Sentiment'})


# In[125]:


df.Label[df.Polarity>0]='Positive'
df.Label[df.Polarity<0]='Negative'
df.Label[df.Polarity==0]='Neutral'


# In[126]:


df


# In[127]:


plt.plot(df.Polarity)
plt.axhline(df.Polarity.mean())
#Average sentiment is negative due to Chester's recent death.

