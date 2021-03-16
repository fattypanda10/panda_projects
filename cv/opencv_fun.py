'''
************ COMPUTER VISION PROJECT - ASSIGNMENT 1 ************
************ AUTHOR - RAJAT SHARMA (r0846712) (MAI (ECS)) **********

How the main video (single file) was made:
    
    - Main method of approach was to have a single code file with which I could 
    generate multiple video files depending on various operations that were asked
    
    - For this, the following code was written where the video was captured 
    using the webcam of the laptop, which is a 2014 MacBook Pro with 8 gigs
    of RAM and a 2.8 GHz Dual-Core i5 processor
    
    - Procedure
    
        * There is a general live feed from the webcam that is enabled the moment
        the code is run. Thereafter for enabling a specific operation or feature(s), 
        a key is pressed and to quit from that feature-specific video, the key 'q'
        is pressed
        
        * Each feature specific video is then written to a particular video file and
        then towards the end, all the videos are stiched or concatenated into one
        
        * The videos do have text, nonetheless, for better understanding and convience,
        below the time stamps have been given
        
        * After writing different video files for individual operations, they were
        combined into one using the package MoviePy (the code for this is at the end
        of this file for your persual)
        
        * Thereafter the video was compressed using an online video compressor
        
        * An audio track, which was downloaded without any copyright infringment
        (freely available online), was added to the compressed video file
        
    - Outline of the operations performed in the Video (In the same order as in Video)
        * Conversion to HSV colorspace
        * Conversion to Grayscale 
        * Gaussian Blur (Kernel = 3)
        * Gaussion Blur (Kernel = 7) 
        * Gaussion Blur (Kernel = 5)
        * Gaussion Blur (Kernel = 13)
        * Bilateral Blur
        * Conversion to RGB colorspace 
        * Thresholding | Morphological Operations
        * Sobel Edge Detection (with white edges) (Scale 5, Delta 0)
        * Sobel Edge Detection (with white edges) (Scale 1, Delta 10)
        * Hough Circular Transform
        * Hough Circular Transform (Param1 100, Param2 30) 
        * Hough Circular Transform (Param1 200, Param2 20)
        * Template Matching/Object Detection & Tracking using Template Matching
        * Drawing Flashing Rectangle around Object/Region of Interest
        * Increasing Noise Addition
        * Sobel Edge Detection (BGR Colorspace)
        * Masking (of blue color object)
        * Contour Plotting
 
'''

############################ MAIN CODE #######################################

import cv2
import numpy as np

#############################################################################

# Uncomment for the Code for Combining all Video Files into One Video

# from moviepy.editor import VideoFileClip, concatenate_videoclips
# import os
# from natsort import natsorted

#############################################################################

### Colorspace Change for the Video Frame
def frameProcess(frame, colorCode:str):
        if colorCode.lower() == 'hsv':
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        elif colorCode.lower() == 'gray':
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame
    
### Output Video for Colored & Grayscale Frames
def output(color_or_gray: int):
    # Colored Frame = 1 | Grayscale = 0
    out = cv2.VideoWriter('video_out.mp4', codec, 10, (vidW, vidH), color_or_gray)
    return out 

### Check Colorspace of Frame - Colored or Grayscale
def shape(frame:np.array):
    return 1 if len(frame.shape) == 3 else 0

#############################################################################

### Main
vidW = 1280
vidH = 720
vid = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'mp4v')
# out2 = cv2.VideoWriter('video_out.mp4', codec, 10, (vidW, vidH), 1)
while vid.isOpened():
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video', (vidW, vidH))
    
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(frame,
    #             'Color',
    #             (50, 50),
    #             font, 
    #             1, 
    #             (255, 0, 0), 
    #             3, 
    #             cv2.LINE_4)
    
    # out2.write(frame)
    cv2.imshow('Video', frame)
    
    key = cv2.waitKey(1)
    # Quit (q)
    if key == ord('q'):
        # out2.release()
        break
    
#############################################################################

    # HSV (a)
    elif key == ord('a'):
        out = None
        while vid.isOpened():
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)            
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################
            
    # Grayscale (s)
    elif key == ord('s'):
        out = None
        while vid.isOpened():
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Grayscale',
                (50, 50),
                font, 
                1, 
                (255, 0, 0), 
                3, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################

    # RGB (d)
    elif key == ord('d'):
        out = None
        while vid.isOpened():
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'RGB Colorspace:',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################

    ## Noise Addition (f)
    elif key == ord('f'):
        out = None
        i = 0
        mu = (75, 75, 75)
        var =(100, 100, 100)
        sigma = np.sqrt(var).astype(np.uint8)
        while vid.isOpened():
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)            
            var =(i, i, i)
            sigma = np.sqrt(var).astype(np.uint8)
            noise = np.zeros(frame.shape).astype(frame.dtype)
            cv2.randn(noise, mu, sigma)
            frame += noise
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Making the Video Stream Noisier with Gaussian Noise',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            i += 1000
            if key == ord('q'):
                out.release()
                break

#############################################################################

    ## Gaussian Blur (g)
    elif key == ord('g'):
        out = None
        mu = (50, 50, 50)
        var =(500, 500, 500)
        sigma = np.sqrt(var).astype(np.uint8)
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            
            # Noise Added
            noise = np.zeros(frame.shape).astype(frame.dtype)
            cv2.randn(noise, mu, sigma)
            frame += noise
            
            # Gaussian Blur
            gaussianBlur = cv2.GaussianBlur(frame, (13, 13), 0)
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Smoothing | Gaussian Filter (Kernel Size: 13):',
                (50, 50),
                font, 
                1, 
                (255, 0, 0), 
                3, 
                cv2.LINE_4)
            cv2.putText(frame,
                'Effective in removing Gaussian noise using Gaussian Kernel',
                (50, 80),
                font, 
                1, 
                (255, 0, 0), 
                3, 
                cv2.LINE_4)
           
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################
           
    # Bilateral Filter (h)
    elif key == ord('h'):
        out = None
        mu = (50, 50, 50)
        var =(500, 500, 500)
        sigma = np.sqrt(var).astype(np.uint8)
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            
            # Noise Added
            noise = np.zeros(frame.shape).astype(frame.dtype)
            cv2.randn(noise, mu, sigma)
            frame += noise
            
            # Bilateral Blur
            frame = cv2.bilateralFilter(frame, 9, 75, 75)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Smoothing | Bilateral Filter:',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            cv2.putText(frame,
                'highly effective in noise removal while keeping edges sharp',
                (50, 80),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            cv2.putText(frame,
                'But the operation is slower',
                (50, 110),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            cv2.putText(frame,
                'takes a Gaussian filter in space, but one more Gaussian filter which is a function of pixel difference.',
                (50, 140),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            
            
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
    
#############################################################################

    # Thresholding (j)
    elif key == ord('j'):
        out = None
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1) 
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Basic Thresholding Types
            # ret,thresh1 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
            ret,thresh2 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY_INV)
            # ret,thresh3 = cv2.threshold(frame, 127, 255, cv2.THRESH_TRUNC) 
            # ret,thresh4 = cv2.threshold(frame, 127, 255, cv2.THRESH_TOZERO)
            # ret,thresh5 = cv2.threshold(frame, 127, 255, cv2.THRESH_TOZERO_INV)
            
            # # Adaptive Thresholding
            # th2 = cv2.adaptiveThreshold(frame, 
            #                             255,
            #                             cv2.ADAPTIVE_THRESH_MEAN_C,
            #                             cv2.THRESH_BINARY,11,2)
            
            # th3 = cv2.adaptiveThreshold(frame, 
            #                             255,
            #                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            #                             cv2.THRESH_BINARY,11,2)
            
            # # Otsu Threshold
            # ret2,th4 = cv2.threshold(frame,
            #                          0,
            #                          255,
            #                          cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            
            # # Gaussian Blur + Otsu Threshold
            # blurry = cv2.GaussianBlur(frame,(5,5),0)
            # ret3,th5 = cv2.threshold(blurry,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            
            # Morpho Ops
            # Erosion
            kernel = np.ones((5,5),np.uint8)
            erosion = cv2.erode(thresh2, kernel, iterations = 1)
            
            # Dilation
            dilation = cv2.dilate(thresh2, kernel, iterations = 1)
            
            # Opening
            opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
            
            # Closing
            closing = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel)
            
            # Morphological Gradient
            gradient = cv2.morphologyEx(thresh2, cv2.MORPH_GRADIENT, kernel)
            
            # Top Hat
            tophat = cv2.morphologyEx(thresh2, cv2.MORPH_TOPHAT, kernel)
            
            # Black Hat
            blackhat = cv2.morphologyEx(thresh2, cv2.MORPH_BLACKHAT, kernel)

            # Thresholded Image
            threshA = cv2.cvtColor(opening, cv2.COLOR_GRAY2BGR)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(thresh2,
                'Thresholding | Morphological Operations',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(thresh2))
            out.write(thresh2)
            cv2.imshow('Video', thresh2)    
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################

    # Sobel Edge Detection - with White Edges (k)
    elif key == ord('k'):
        out = None
        scale = 1
        delta = 10
        ddepth = cv2.CV_16S
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.GaussianBlur(frame, (9, 9), 0)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)            
            # Sobel
            grad_x = cv2.Sobel(frame, 
                               ddepth, 
                               1, 
                               0, 
                               ksize=-1, 
                               scale=scale, 
                               delta=delta, 
                               borderType=cv2.BORDER_DEFAULT)
            grad_y = cv2.Sobel(frame, 
                               ddepth, 
                               0, 
                               1, 
                               ksize=-1, 
                               scale=scale, 
                               delta=delta, 
                               borderType=cv2.BORDER_DEFAULT)

            # Scharr
            # grad_x = cv2.Scharr(frame,ddepth,1,0)
            # grad_y = cv2.Scharr(frame,ddepth,0,1)
            
            abs_grad_x = cv2.convertScaleAbs(grad_x)
            abs_grad_y = cv2.convertScaleAbs(grad_y)
        
            grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(grad,
                'Sobel Edge Detection with white edges: Scale 1, Delta 10',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(grad))
            out.write(grad)
            cv2.imshow('Video', grad)    
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
##############################################################################
  
    # Sobel with coloured edge (BGR) detection (l)
    elif key == ord('l'):
        out = None
        scale = 1
        delta = 0
        ddepth = cv2.CV_16S
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            fb, fg, fr = cv2.split(frame)
            channels = [fb, fg, fr]
            comb = []
            for i in channels:
                frame = i
                frame = cv2.flip(frame, 1)
                frame = cv2.GaussianBlur(frame, (9, 9), 0)
            
                # Sobel
                grad_x = cv2.Sobel(frame, ddepth, 1, 0, ksize=-1, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
                grad_y = cv2.Sobel(frame, ddepth, 0, 1, ksize=-1, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

                # Scharr
                # grad_x = cv2.Scharr(frame,ddepth,1,0)
                # grad_y = cv2.Scharr(frame,ddepth,0,1)
                
                abs_grad_x = cv2.convertScaleAbs(grad_x)
                abs_grad_y = cv2.convertScaleAbs(grad_y)
            
                grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
                comb.append(grad)
                
            result = cv2.merge((comb[0], comb[1], comb[2]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(grad,
                'Sobel Edge Detection in BGR Colorspace',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(result))
            out.write(result)
            cv2.imshow('Video', result)    
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break        
    
#############################################################################
    
    # Hough Circular Transform (z)
    elif key == ord('z'):
        out = None
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.medianBlur(frame, 5)
            # frame = cv2.GaussianBlur(frame, (7, 7), 0)
            rows = frame.shape[0]
            # _, contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cv2.drawContours(frame, contours, -1, (0,255,0), 3)
            circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                        param1=200, param2=30,
                                        minRadius=40, maxRadius=125)
            # circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1.2, 200)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR).astype(np.uint8)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    center = (i[0], i[1])
                    radius = i[2]
                    
                    # circle center
                    cv2.circle(frame, 
                               center,
                               1, 
                               (255, 0, 0), 
                               5)
                    
                    # circle outline
                    cv2.circle(frame, 
                               center,
                               radius,
                               (0, 0, 255), 
                               5)
                    cv2.rectangle(frame, 
                                (center[0] - radius, center[1] - radius),
                                (center[0] + radius, center[1] + radius),
                                (0,255,0), 
                                5)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Hough Circular Transform',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)      
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################

    # Contour Plotting (x)
    elif key == ord('x'):
        out = None
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(frame, 127, 255, 0)
            _, contours, _ = cv2.findContours(thresh, 
                                              cv2.RETR_TREE, 
                                              cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame, contours, -1, (0,255,0), 3)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Contours in the Video Frame (Contour Drawing)',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)    
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
#############################################################################   

    # Drawing FLashing Shape around the Object/Region of Interest (c)
    elif key == ord('c'):
        out = None
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            vid.set(cv2.CAP_PROP_BUFFERSIZE, 3)
            ret, frame = vid.read()
            frame = cv2.flip(frame, 1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(frame, (800,50),(1200, 500),(255,0,0), 5)
            cv2.putText(frame,
                'Flashing Rectangle around Region of Interest',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            
            key1 = cv2.waitKey(1)
            
            cv2.rectangle(frame, (800,50),(1200,500),(0,0,255), 5)
            cv2.putText(frame,
                'Flashing Rectangle around Region of Interest',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            
            key2 = cv2.waitKey(1)
            
            cv2.rectangle(frame, (800,50),(1200,500),(0,255,0), 5)            
            cv2.putText(frame,
                'Flashing Rectangle around Region of Interest',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            
            key3 = cv2.waitKey(1)
            if (key1 == ord('q')) or (key2 == ord('q')) or (key3 == ord('q')):
                out.release()
                break
            
#############################################################################
           
    # Template Matching | Object Tracking using Template Matching (v)
    elif key == ord('v'):
        out = None
        while vid.isOpened():
            temp = cv2.imread('temp.jpg', cv2.IMREAD_GRAYSCALE)
            temp = cv2.GaussianBlur(temp, (5, 5), 0)
            vid = cv2.VideoCapture(0)
            vid.set(cv2.CAP_PROP_BUFFERSIZE, 3)
            ret, frame = vid.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.GaussianBlur(frame, (11, 11), 0)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            temp = cv2.resize(temp,(400, 400), interpolation = cv2.INTER_CUBIC)
            w, h = temp.shape[::-1]            
            # All the 6 methods for comparison in a list
            methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                        'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
            method = eval(methods[1])
            res = cv2.matchTemplate(frame, temp, method)
            res = cv2.normalize(res, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            
            # For looping through all methods 
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            #     top_left = min_loc
            # else:
            #     top_left = max_loc
            
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR).astype(np.uint8)
            cv2.rectangle(frame, top_left, bottom_right, (0, 255 ,0), 5)
            
            # res = likelihood map based on intensity
            res = cv2.resize(res,(frame.shape[1], frame.shape[0]), interpolation = cv2.INTER_CUBIC)
            # cv2.namedWindow('Temp', cv2.WINDOW_NORMAL)
            # cv2.resizeWindow('Temp', (vidW, vidH))
    
            # cv2.imshow('Temp', res)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                'Template/Feature Matching & Tracking (Round Object) with Rectangle',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(frame))
            out.write(frame)
            cv2.imshow('Video', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
    
#############################################################################
   
    # Masking - For Blue Coloured Object only (b)
    elif key == ord('b'):
        out = None
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1) 
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
            # define range of blue color in HSV
            # Original 110, 50, 50 | 130, 255, 255
            lower_blue = np.array([80,20,20])
            upper_blue = np.array([130,255,255])
           
            # Threshold for blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
            # Bitwise-AND Masking
            res = cv2.bitwise_and(frame,frame, mask= mask)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(res,
                'Masking for a Blue Color Object',
                (50, 50),
                font, 
                0.5, 
                (255, 0, 0), 
                2, 
                cv2.LINE_4)
            if out is None:
                out = output(shape(res))
            out.write(res)
            cv2.imshow('Video', res)    
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
            
##############################################################################
    
    # 2D Filtering/Convolving (n)
    elif key == ord('n'):
        out = None
        kernel = np.array([
                        [5, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]], np.float32)
        
        while vid.isOpened():
            vid = cv2.VideoCapture(0)
            _, frame = vid.read()
            frame = cv2.flip(frame, 1) 
            frame = cv2.filter2D(frame, -1, kernel)
            if out is None:
                out = output(shape(frame))
            out.write(frame)            
            cv2.imshow('Video', frame)    
            key = cv2.waitKey(1)
            if key == ord('q'):
                out.release()
                break
    
vid.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


##############################################################################

### Code for Combining all the video files into a single video file using Moviepy

# CURRENT_PATH = os.getcwd()
# videos = np.array([i for i in os.listdir(CURRENT_PATH) if ((not i.startswith('.')) and (i.endswith(".mp4")))])
# videos = natsorted(videos)
# videoclips = [VideoFileClip(i) for i in videos]
# combined = concatenate_videoclips(videoclips)
# combined.write_videofile("all.mp4")
