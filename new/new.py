from classTEST import First as fst
fst1 = fst()
from classTEST import Second as Snd
Snd1 = Snd()
from classTEST import Third as Trd
Trd1 = Trd()
from classTEST import Third2 as Trdw
Trdw1 = Trdw()



import pickle
pickle.dump( Trdw1, open( "./SJHw3.pkl", "wb" ) )
print('dump pickle')
Trdw1_pkl = pickle.load( open( "./SJHw3.pkl", "rb" ) )
print('load pickle')