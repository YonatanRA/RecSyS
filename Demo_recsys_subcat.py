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

tags=['r&b', 'rock', 'jazz', 'electronic', 'pop', 'indie',
      'cinema', 'theater', 'beers', 'wine', 'party', 'trips',
      'running', 'gym', 'golf', 'basket', 'football', 'yoga']


sub_tags_elec=['techno', 'electro_funky', 'house', 'minimal', 'dubstep', 'DandB']



# synth data

data=np.random.randint(0, 6, (len(names), len(tags)))
sub_data=np.random.randint(0, 1, (len(names), len(sub_tags_elec)))

s_data=pd.DataFrame(data, columns=tags, index=names)
s_sub_data=pd.DataFrame(sub_data, columns=sub_tags_elec, index=names)

s_data=pd.concat([s_data, s_sub_data], axis=1)

s_data['plan']=np.random.randint(0, 2, (len(names), 1))
s_data['id']=[i for i in range(len(names))]


for i in range(len(s_data)):
	if s_data.electronic[i]==1:
		s_data.techno[i]=np.random.randint(0, 6)
		s_data.electro_funky[i]=np.random.randint(0, 6)
		s_data.house[i]=np.random.randint(0, 6)
		s_data.minimal[i]=np.random.randint(0, 6)
		s_data.dubstep[i]=np.random.randint(0, 6)
		s_data.DandB[i]=np.random.randint(0, 6)





# new user function


def new_user(df, rb, rock, jazz, electronic, pop, indie, cinema, theater, beers, wine,
             party, trips, running, gym, golf, basket, football, yoga,
             techno, electro_funky, house, minimal, dubstep, DandB, metric):
    
    
    tags=['r&b', 'rock', 'jazz', 'electronic', 'pop', 'indie',
          'cinema', 'theater', 'beers', 'wine', 'party', 'trips',
          'running', 'gym', 'golf', 'basket', 'football', 'yoga',
          'techno', 'electro_funky', 'house', 'minimal', 'dubstep', 'DandB']
    
    
    
    rating=[rb, rock, jazz, electronic, pop, indie, cinema, theater, beers, wine,
            party, trips, running, gym, golf, basket, football, yoga, 
            techno, electro_funky, house, minimal, dubstep, DandB]
    
    
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
    
    
    
print('Rate r&b from 0 to 5:')
rb = int(input())

print('Rate rock from 0 to 5:')
rock = int(input())    
    
print('Rate jazz from 0 to 5:')
jazz = int(input())

print('Rate electronic from 0 to 5:')
electronic = int(input())  
  
if electronic!=0:
	 print('Rate techno from 0 to 5:')
	 techno = int(input())
	 
	 print('Rate electro-funky from 0 to 5:')
	 electro_funky = int(input())
	 
	 print('Rate house from 0 to 5:')
	 house = int(input())
	 
	 print('Rate minimal from 0 to 5:')
	 minimal = int(input())
	 
	 print('Rate dubstep from 0 to 5:')
	 dubstep = int(input())
	 
	 print('Rate D&B from 0 to 5:')
	 DandB = int(input())


else:
	 techno = 0
	 electro_funky = 0
	 house = 0
	 minimal = 0
	 dubstep = 0
	 DandB = 0



print('Rate pop from from 0 to 5:')
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

print('Rate trips from 0 to 5:')
trips = int(input())

print('Rate running from 0 to 5:')
running = int(input())

print('Rate gym from 0 to 5:')
gym = int(input())

print('Rate golf from 0 to 5:')
golf = int(input())

print('Rate basket from 0 to 5:')
basket = int(input())

print('Rate football from 0 to 5:')
football = int(input())

print('Rate yoga from 0 to 5:')
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

plans=new_user(s_data, rb, rock, jazz, electronic, pop, indie, cinema, theater, beers, wine,
               party, trips, running, gym, golf, basket, football, yoga, 
               techno, electro_funky, house, minimal, dubstep, DandB, metric)



print (plans)


0


