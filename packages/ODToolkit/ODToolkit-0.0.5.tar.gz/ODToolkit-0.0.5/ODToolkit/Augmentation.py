import glob
import numpy as np
from PIL import Image
import os
import cv2
from typing import List, Tuple


def valid_x(x_target, x1, x2):
    '''
    x1-x2 represents width or height
    thus, for a valid x proposal, we just want to make sure there is no overlapping
    '''
    
    diff = x2-x1
    if (x_target+diff) < x1 or x_target > x2:
        return True
    else:
        return False
    
    
def copy_paste_augmentation(train_img: List[str], 
                            train_lbl: List[str], 
                            K:int, 
                            savepath_img:str, 
                            savepath_lbl:str, 
                            R: int=1,
                            width:int,
                            height:int,
                            area_threshold:float,
                            mask_percentage:float,
                            mask_top=True,
                            quit: int=100):

    THRESHOLD_AREA = int(area_threshold*width*height)
    margin = int(mask_percentage*height)
    area = width*height

    with open(train_lbl[K], 'r') as f:
        lines = f.readlines()

    # some quick return algorithm
    # 1. if no label, then directly return
    # 2. if all small boxes, directly return
    if lines == []:
        return
    big_box = 0
    for line in lines:
        cls, xc, yc, w, h = line.split(' ')
        xc, yc, h, w = float(xc), float(yc), float(h), float(w)
        xc, yc, h, w = int(width*xc), int(height*yc), int(height*h), int(width*w)
        
        if h*w <= THRESHOLD_AREA:
            continue
        else:
            big_box+=1
    if big_box == 0:
        return
    
    # if there are some big boxes in the image, process it and create aug files
    image = np.array(Image.open(train_img[K]))
    new_im = image.copy()

    occ = [] # put all boxes in to this list
    with open(savepath_lbl, 'w') as f:
        f.write('')
        
    for line in lines:
        with open(savepath_lbl, 'a') as f:
            f.write(line)
            
        cls, xc, yc, w, h = line.split(' ')

        xc, yc, h, w = float(xc), float(yc), float(h), float(w)
        xc, yc, h, w = int(width*xc), int(height*yc), int(height*h), int(width*w)

        y1 = max(0, yc - h/2)
        x1 = max(0, xc - w/2)
        y2 = min(height, y1+h)
        x2 = min(width, x1+w)
        
        if h*w <= THRESHOLD_AREA:
            continue
        else:
            occ.append([cls, x1, y1, x2, y2]) # x1y1x2y2
            
    # now we make sure in occ and occ_new, all are big boxes
    occ_new = occ.copy()
    if len(occ) > 3: # if too many boxes, we don't copy-paste that much
        R = 1
    for _ in range(R):
        for box in occ:
            _, x1, y1, x2, y2 = box
            h, w = y2-y1, x2-x1
            
            valid = False
            val_cnt = 0 # check if while loop is a endless loop
            while not valid: # keep finding valid position to place the fake box
                dx = np.random.randint(0, width-w)
                if mask_top:
                    dy = np.random.randint(margin, height-h)
                else:
                    dy = np.random.randint(0, margin-h)
                    
                res = []
                val_cnt+=1
                if val_cnt > quit: # if bad-luck, we give up this box
                    break 
                    
                for boxn in occ_new:
                    cls, x1n, y1n, x2n, y2n = boxn
                    hn, wn = y2n-y1n, x2n-x1n
                    
                    res.append(valid_x(dx, x1n, x2n) or valid_x(dy, y1n, y2n))

                if np.all(np.array(res, dtype=bool)):
                    valid = True
                    with open(savepath_lbl, 'a') as f:
                        # cls, xc, yc, w, h
                        line = ' '.join([str(i) for i in [cls, (dx+w/2)/width, (dy+h/2)/height, w/width, h/height]])
                        f.write(line+'\n')
                

            if val_cnt <=quit: # if lucky, we move to new round, if not, we give up this box
                patch = image[int(y1):int(y1+h), int(x1):int(x1+w), :]
                
                if np.random.rand() < 0.5: # vertical random flip
                    patch = patch[::-1, :, :]
                if np.random.rand() < 0.5: # horizontal random flip
                    patch = patch[:, ::-1, :]
                    
                new_im[int(dy):int(dy+h), int(dx):int(dx+w), :] = patch

                # update occ_new in x1y1x2y2
                occ_new.append([cls, dx, dy, dx+w, dy+h])
    
    image_ready = Image.fromarray(new_im)
    image_ready.save(savepath_img)
    
    return image_ready