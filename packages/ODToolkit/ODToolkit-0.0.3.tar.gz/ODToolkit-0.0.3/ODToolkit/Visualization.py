import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from typing import List, Tuple
import os
from ODToolkit.Analysis import get_fpfn


class BoxVisualizer:
    def __init__(self, 
                 img_h:int, 
                 img_w:int) -> None:
        self.h = img_h
        self.w = img_w
        self.area = self.h*self.w

    def show_boxes(self, 
                  labels: List[List], 
                  mode: List[str], 
                  figsize: List=[10,20])->None:

        assert len(labels) == len(mode), "labels and mode need to have same length, but got {} and {}".format(len(labels),
                                                                                                              len(mode))
        plt.figure(figsize=figsize)
        for idx, (data, name) in enumerate((zip(labels, mode))):
            area = []
            height, width = [], []
            aspect_ratio = []

            plt.subplot(4,len(labels),2*len(labels)+idx+1) # plot out the boxes
            plt.ylim(0,self.h)
            plt.xlim(0,self.w)

            # heatmap
            heat = np.zeros((self.h, self.w))

            for file in data:
                with open(file,'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        cls, xc, yc, w, h = line.split(' ')
                        xc, yc, h, w = float(xc), 1-float(yc), float(h), float(w) # 1-y because coordinate of y reverts
                        area.append(h*w*self.area)
                        height.append(h)
                        width.append(w)
                        aspect_ratio.append(h/w)

                        xc, yc, h, w = int(self.w*xc), int(self.h*yc), int(self.h*h), int(self.w*w)
                        rect = patches.Rectangle((xc-w//2, yc-h//2), 
                                                 width=w, height=h, 
                                                 linewidth=1, edgecolor='r', facecolor='none')
                        plt.gca().add_patch(rect)

                        # heatmap
                        heat[int(1-yc-h/2):int(1-yc+h/2), int(xc-w/2):int(xc+w/2)] += 1.

            plt.title('{}: box actual position'.format(name))

            area = np.array(area)
            msg = '{}: max area: {}, min area: {}, avg area: {}'.format(name, area.max(), area.min(), area.mean())
            plt.subplot(4,len(labels),idx+1)
            plt.hist(area, bins=100)
            plt.title('{}: histogram for box area'.format(name))

            plt.subplot(4,len(labels),1*len(labels)+idx+1)
            plt.scatter(width, height)
            plt.title('{}: width-height scatter plot'.format(name))

            plt.subplot(4,len(labels),3*len(labels)+idx+1)
            plt.imshow(heat)
            plt.title('{}: heatmap of boxes'.format(name))

            print('{}: max aspect_ratio:{}, min aspect_ratio:{}'.format(name, max(aspect_ratio), min(aspect_ratio)))
            
    def show_fpfn(self, 
                  FP:List, 
                  FN:List, 
                  correct:List, 
                  figsize=[15,20]):
        
        plt.figure(figsize=figsize)
        plt.subplot(2,3,1)
        plt.imshow(np.ones((self.h,self.w,3)))
        
        def read_box(box:List, color:str) -> List:
            temp = []
            for box in box:
                x1, y1, x2, y2 = box
                w, h = x2-x1, y2-y1
                rect = patches.Rectangle((x1, y1), 
                                         width=w, height=h,
                                         linewidth=1, edgecolor=color, facecolor='none')
                fpy.append(y1)
                plt.gca().add_patch(rect)
            return temp
        
        # spacial distribution
        fpy = read_box(FP, 'red')
        plt.title('FP boxes spatial distribution')

        plt.subplot(2,3,2)
        plt.imshow(np.ones((self.h,self.w,3)))
        fny = read_box(FN, 'blue')
        plt.title('FN boxes spatial distribution')

        plt.subplot(2,3,3)
        plt.imshow(np.ones((self.h,self.w,3)))
        cy = read_box(correct, 'green')
        plt.title('correct boxes spatial distribution')
        
        # y histogram
        plt.subplot(2,3,4)
        plt.hist(fpy, bins=100, orientation='horizontal')
        plt.ylim(0, self.h)
        plt.gca().invert_yaxis()
        plt.title('histogram of FP boxes along Y axis')

        plt.subplot(2,3,5)
        plt.hist(fny,bins=100, orientation='horizontal')
        plt.ylim(0, self.h)
        plt.gca().invert_yaxis()
        plt.title('histogram of FN boxes along Y axis')

        plt.subplot(2,3,6)
        plt.hist(cy,bins=100, orientation='horizontal')
        plt.ylim(0, self.h)
        plt.gca().invert_yaxis()
        plt.title('histogram of correct boxes along Y axis')