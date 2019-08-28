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

data=np.random.randint(0, 2, (len(names), len(tags)))
sub_data=np.random.randint(0, 1, (len(names), len(sub_tags_elec)))

s_data=pd.DataFrame(data, columns=tags, index=names)
s_sub_data=pd.DataFrame(sub_data, columns=sub_tags_elec, index=names)

s_data=pd.concat([s_data, s_sub_data], axis=1)

s_data['plan']=np.random.randint(0, 2, (len(names), 1))
s_data['id']=[i for i in range(len(names))]


for i in range(len(s_data)):
	if s_data.electronic[i]!=0:
		s_data.techno[i]=np.random.randint(0, 2)
		s_data.electro_funky[i]=np.random.randint(0, 2)
		s_data.house[i]=np.random.randint(0, 2)
		s_data.minimal[i]=np.random.randint(0, 2)
		s_data.dubstep[i]=np.random.randint(0, 2)
		s_data.DandB[i]=np.random.randint(0, 2)



#  weighing

for e in tags:
	s_data[e]=s_data[e]*2/3

for e in sub_tags_elec:
	s_data[e]=s_data[e]*1/3
	
	


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
    
    
    
print('Rate r&b :')
rb = int(input())*2/3

print('Rate rock :')
rock = int(input())*2/3    
    
print('Rate jazz :')
jazz = int(input())*2/3

print('Rate electronic :')
electronic = int(input())*2/3  
  
if electronic!=0:
	 print('Rate techno :')
	 techno = int(input())*1/3
	 
	 print('Rate electro-funky :')
	 electro_funky = int(input())*1/3
	 
	 print('Rate house :')
	 house = int(input())*1/3
	 
	 print('Rate minimal :')
	 minimal = int(input())*1/3
	 
	 print('Rate dubstep :')
	 dubstep = int(input())*1/3
	 
	 print('Rate D&B :')
	 DandB = int(input())*1/3


else:
	 techno = 0
	 electro_funky = 0
	 house = 0
	 minimal = 0
	 dubstep = 0
	 DandB = 0



print('Rate pop from :')
pop = int(input())*2/3

print('Rate indie :')
indie = int(input())*2/3

print('Rate cinema :')
cinema = int(input())*2/3

print('Rate theater :')
theater = int(input())*2/3

print('Rate beers :')
beers = int(input())*2/3

print('Rate wine :')
wine = int(input())*2/3

print('Rate party :')
party = int(input())*2/3

print('Rate trips :')
trips = int(input())*2/3

print('Rate running :')
running = int(input())*2/3

print('Rate gym :')
gym = int(input())*2/3

print('Rate golf :')
golf = int(input())*2/3

print('Rate basket :')
basket = int(input())*2/3

print('Rate football :')
football = int(input())*2/3

print('Rate yoga :')
yoga = int(input())*2/3








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





