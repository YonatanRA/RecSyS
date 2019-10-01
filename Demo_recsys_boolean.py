# Demo recsys boolean (0-1)



# import libraries

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform





# names and tags

names=['id__'+str(i) for i in range(3000)]

tags=['r&b', 'rock', 'jazz', 'techno', 'pop', 'indie',
      'cinema', 'theater', 'beers', 'wine', 'party', 'trips',
      'running', 'gym', 'golf', 'basket', 'football', 'yoga']





# synth data

data=np.random.randint(0, 2, (len(names), len(tags)))
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
             party, trips, running, gym, golf, basket, football, yoga]

    
    n_user={k:v for k, v in list(zip(tags, rating))}
    n_user['id']='id__'+str(len(s_data.id)+1)
    n_user['plan']=0
    
    names=list(df.index)
    df=df.append(n_user, ignore_index=True)
    names.append(n_user['id'])
    df.index=names
    
    
    similar = pd.DataFrame(1/(1 + squareform(pdist(df.iloc[:, :-2], metric))), 
                         index=df.index, columns=df.index)

    similarities = similar[n_user['id']].sort_values(ascending=False)
    
    closer_users=[]
    for e in similarities.index:
        if df.ix[e].plan==1:
            closer_users.append(e)
    
    return df.ix[closer_users[:10]]
    
    
    
print('Rate r&b :')
rb = int(input())

print('Rate rock :')
rock = int(input())    
    
print('Rate jazz :')
jazz = int(input())

print('Rate techno :')
techno = int(input())  
    
print('Rate pop from :')
pop = int(input())

print('Rate indie :')
indie = int(input())

print('Rate cinema :')
cinema = int(input())

print('Rate theater :')
theater = int(input())

print('Rate beers :')
beers = int(input())

print('Rate wine :')
wine = int(input())

print('Rate party :')
party = int(input())

print('Rate trips :')
trips = int(input())

print('Rate running :')
running = int(input())

print('Rate gym :')
gym = int(input())

print('Rate golf :')
golf = int(input())

print('Rate basket :')
basket = int(input())

print('Rate football :')
football = int(input())

print('Rate yoga :')
yoga = int(input())








# metrics for squareform

'''
'euclidean', 'minkowski', 'cityblock', 'seuclidean', 'sqeuclidean', 'cosine', 'correlation'

'hamming', 'jaccard', 'chebyshev', 'canberra', 'braycurtis', 'mahalanobis', 'yule'

'matching', 'dice', 'kulsinski', 'rogerstanimoto', 'russellrao', 'sokalmichener'

'sokalsneath', 'wminkowski'
'''


metric='cosine' 




# plans (users)

plans=new_user(s_data, rb, rock, jazz, techno, pop, indie, cinema, theater, beers, wine,
               party, trips, running, gym, golf, basket, football, yoga, metric)



print (plans)




