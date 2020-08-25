# -*- coding: utf-8 -*-

import cv2 
import numpy as np



class AnalisadorDeImagem:
    
    def __init__(self, img_path):
        self.img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
        self.img_gray = cv2.cvtColor(self.img_color, cv2.COLOR_BGR2GRAY)
        
    def __pre_precessamento_de_imagem(self, img):
        # apply GuassianBlur to reduce noise. medianBlur is also added for smoothening, reducing noise.
        gray = cv2.GaussianBlur(img,(5,5),0, 2)
        gray = cv2.medianBlur(gray,5)
        	        
        
        return gray
    
    def localizaCirculos(self):
        
        
        #preprocess image
        gray_blurred = self.__pre_precessamento_de_imagem(self.img_gray)
        cv2.imshow("bluerred", gray_blurred)
        cv2.waitKey(0)
        
        
        #detecta os circulos com HoughCircles
        detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, gray_blurred.shape[0]/8, param1 = 30, 
               param2 = 50, minRadius = 1, maxRadius = 60)
        
        return detected_circles
    
    def informacoesSobreCirculos(self, detected_circles):
        if detected_circles is None:
            return 0
        else: 
            return len(detected_circles[0, :])
    
    def desenhaCirculosNaImagem(self, detected_circles):
        if detected_circles is not None:
            self.img_color_circle = self.img_color.copy()
            # Convert the circle parameters     a, b and r to integers. 
            detected_circles = np.uint16(np.around(detected_circles)) 
          
            for pt in detected_circles[0, :]: 
                a, b, r = pt[0], pt[1], pt[2] 
          
                # Draw the circumference of the circle. 
                cv2.circle(self.img_color_circle, (a, b), r, (0, 255, 0), 2) 
          
                # Draw a small circle (of radius 1) to show the center. 
                cv2.circle(self.img_color_circle, (a, b), 1, (0, 0, 255), 3)
            
            return self.img_color_circle
    
    def imprimeImagem(self, img):
        cv2.imshow("Detected Circle", img) 
        cv2.waitKey(0)
            