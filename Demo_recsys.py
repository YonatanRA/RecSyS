# Demo recsys



# import libraries

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform




# names and tags

names=['id__'+str(i) for i in range(2000)]

tags=['r&b', 'rock', 'jazz', 'techno', 'pop', 'indie',
      'cinema', 'theater', 'beers', 'wine', 'party', 'trips',
      'running', 'gym', 'golf', 'basket', 'football', 'yoga']





# synth data

data=np.random.randint(0, 6, (len(names), len(tags)))
s_data=pd.DataFrame(data, columns=tags, index=names)
s_data['plan']=np.random.randint(0, 2, (len(names), 1))
s_data['id']=[i for i in range(len(names))]





# new user function


def new_user(df, rb, rock, jazz, techno, pop, indie, cinema, theater, beers, wine,
             party, trips, running, gym, golf, basket, football, yoga, metric):
    
    
    tags=['r&b', 'rock', 'jazz', 'techno', 'pop', 'indie',
          'cinema', 'theater', 'beers', 'wine', 'party', 'trips',
          'running', 'gym', 'golf', 'basket', 'football', 'yoga']
    
    
    rating=[rb, rock, jazz, techno, pop, indie, cinema, theater, beers, wine,
             party, trips, running, gym, golf, basket, football, yoga, metric]
    
    
    n_user={k:v for k, v in list(zip(tags, n_rating[0]))}
    n_user['id']='id__'+str(len(s_data.id)+1)
    n_user['plan']=0
    
    names=list(df.index)
    df=df.append(n_user, ignore_index=True)
    names.append(n_user['id'])
    df.index=names
    
    similar = pd.DataFrame(1/(1 + squareform(pdist(df.iloc[:, :-1], metric))), 
                         index=df.index, columns=df.index)

    similarities = similar[n_user['id']].sort_values(ascending=False)
    
    closer_users=[]
    for e in similarities.index:
        if df.ix[e].plan==1:
            closer_users.append(e)
    
    return df.ix[closer_users[:10]]
    
    
    
    
print('Rate r&b from 0 to 5:')
rb = int(input())

print('Rate rock from 0 to 5:')
rock = int(input())    
    
print('Rate jazz from 0 to 5:')
jazz = int(input())

print('Rate techno from 0 to 5:')
techno = int(input())  
    
print('Rate pop from 0 to 5:')
pop = int(input())

print('Rate indie from 0 to 5:')
indie = int(input())

print('Rate cinema from 0 to 5:')
cinema = int(input())

print('Rate theater from 0 to 5:')
theater = int(input())

print('Rate beers from 0 to 5:')
beers = int(input())

print('Rate wine from 0 to 5:')
wine = int(input())

print('Rate party from 0 to 5:')
party = int(input())





















