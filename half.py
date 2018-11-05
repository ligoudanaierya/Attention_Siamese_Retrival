import numpy as np
import os 

for i in os.listdir('source-edge-train'):
	count = 0
	del_count = 0
	dir = os.path.join('source-edge-train',i)
	for j in os.listdir(dir):
		count += 1
	print(dir,count)
	'''for m in os.listdir(dir):
		os.remove(os.path.join(dir,m))
		del_count += 1
		if del_count >= count/2:
			break
		'''
