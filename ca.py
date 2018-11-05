import os
import numpy as np
import cv2
num = 0
for root, dir, f in os.walk('sketch_edge'):
    for name in f:
        path =os.path.join(root,name)
        cat = path.split("/")[2].split('.')[0]
        img = cv2.imread(path)
        if cat == '1':
            cv2.imwrite('sketch-category/moon/'+path.replace('/',''),img)
        if cat == '10':
            cv2.imwrite('sketch-category/koeln_dom/'+path.replace('/',''),img)
        if cat == '11':
            cv2.imwrite('sketch-category/China_tower/'+path.replace('/',''),img)
        if cat == '2':
            cv2.imwrite('sketch-category/notre_dame_paris/'+path.replace('/',''),img)
        if cat == '12':
            cv2.imwrite('sketch-category/sunflower/'+path.replace('/',''),img)
        if cat=='13':
            cv2.imwrite('sketch-category/big_ben/'+path.replace('/',''),img)
        if cat=='14':
            cv2.imwrite('sketch-category/horse/'+path.replace('/',''),img)
        if cat=='15':
            cv2.imwrite('sketch-category/Arc_de_Triomphe/'+path.replace('/',''),img)
        if cat=='16':
            cv2.imwrite('sketch-category/tower_bridge/'+path.replace('/',''),img)
        if cat=='17':
            cv2.imwrite('sketch-category/Taj_Mahal/'+path.replace('/',''),img)
        if cat=='18':
            cv2.imwrite('sketch-category/Venice_bridge/'+path.replace('/',''),img)
        if cat == '19':
            cv2.imwrite('sketch-category/duck_swan/'+path.replace('/',''),img)
        if cat =='20':
            cv2.imwrite('sketch-category/heart_shape/'+path.replace('/',''),img)
        if cat =='21':
            cv2.imwrite('sketch-category/Temple_of_Heaven_beijing/'+path.replace('/',''),img)
        if cat == '22':
            cv2.imwrite('sketch-category/Shanghai_TV_tower/'+path.replace('/',''),img)
        if cat =='23':
            cv2.imwrite('sketch-category/butterfly/'+path.replace('/',''),img)
        if cat == '24':
            cv2.imwrite('sketch-category/Colosseum/'+path.replace('/',''),img)
        if cat =='25':
            cv2.imwrite('sketch-category/sunset_sunrise/'+path.replace('/',''),img)
        if cat == '26':
            cv2.imwrite('sketch-category/bird/'+path.replace('/',''),img)
        if cat == '27':
            cv2.imwrite('sketch-category/Rome_antica/'+path.replace('/',''),img)
        if cat == '28':
            cv2.imwrite('sketch-category/rock_mountain/'+path.replace('/',''),img)
        if cat == '29':
            cv2.imwrite('sketch-category/tree/'+path.replace('/',''),img)
        if cat =='30':
            cv2.imwrite('sketch-category/Sydney_bridge/'+path.replace('/',''),img)
        if cat =='3':
            cv2.imwrite('sketch-category/Egypt_pyramid/'+path.replace('/',''),img)
        if cat =='31':
            cv2.imwrite('sketch-category/Sydney_Opera/'+path.replace('/',''),img)
        if cat =='32':
            cv2.imwrite('sketch-category/To-ji_temple/'+path.replace('/',''),img)
        if cat =='33':
            cv2.imwrite('sketch-category/Pisa_tower/'+path.replace('/',''),img)
        if cat =='4':
            cv2.imwrite('sketch-category/starfish/'+path.replace('/',''),img)
        if cat =='5':
            cv2.imwrite('sketch-category/Pantheon/'+path.replace('/',''),img)
        if cat == '6':
            cv2.imwrite('sketch-category/bicycle/'+path.replace('/',''),img)
        if cat =='7':
            cv2.imwrite('sketch-category/Burj_Al_Arab/'+path.replace('/',''),img)
        if cat=='8':
            cv2.imwrite('sketch-category/eiffel_tower/'+path.replace('/',''),img)
        if cat =='9':
            cv2.imwrite('sketch-category/airplane/'+path.replace('/',''),img)
