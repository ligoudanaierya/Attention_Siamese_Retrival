import os

#for i in range(1,11):
#    os.mkdir('sketch-features/'+str(i))
for i in os.listdir('./source_edge'):
    os.mkdir('score-np/'+i)
