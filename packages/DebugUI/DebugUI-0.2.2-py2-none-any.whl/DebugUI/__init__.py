#!/usr/bin/python
# -*- coding: UTF-8 -*-

import streamlit as st
from PIL import Image, ImageDraw
import os
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')


selectedImage = None
multiSelect = False
image_datas = []

image_previews = []

def open(open_type='image', num=1):
    if open_type == 'image':
        global multiSelect
        global image_datas

        multiSelect = False
        # 异步回调
        uploaded_file = st.file_uploader("选择一张图片：", type=['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])
        if uploaded_file is not None:
            
            imageData, format, width, height = _processSelectPhoto(uploaded_file)

            st.image(imageData, use_column_width=True)

            base_module = __import__("debug_ui_base_class")
            clz = getattr(base_module, 'DebugUIBaseClass')
            method = getattr(clz, '__pg_process__')

            if method is not None:
               
                data = {}
                data["_image"] = imageData
                data["_format"] = format
                data["_width"] = width
                data["_height"] = height
                data["_debug_ui_component_type"] = "image" # image
                data["_debug_ui_component_id"] = "0"
                image_datas.append(data)

                method(data)

            else:
                raise Exception, "Playground should have debug_ui_base_class.py!"
        else:
            print("please choose a photo")

    elif open_type == 'images':
        multiSelect = True

        uploaded_file = st.file_uploader("选择 "+str(num)+" 张图片：", type=['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])
        global image_datas

        # 继续选择清除原来选择
        if len(image_datas)==num:
            image_datas=[]
            image_previews = []
            

        if uploaded_file is not None:    
            imageData, format, width, height = _processSelectPhoto(uploaded_file)

            img_data = {}
            img_data["_image"] = imageData
            img_data["_format"] = format
            img_data["_width"] = width
            img_data["_height"] = height
            image_datas.append(img_data)

            # 显示多张
            global image_previews
            image_previews.append(imageData)
            st.image(image_previews, use_column_width=True)

            if len(image_datas)!=num:
                st.info('请选择第'+str(len(image_datas)+1)+"张图片")
                return
        else:
            print("please choose a photo")
            return

        base_module = __import__("debug_ui_base_class")
        clz = getattr(base_module, 'DebugUIBaseClass')
        method = getattr(clz, '__pg_process__')

        if method is not None:
           
            data = {}
            data["_images"] = image_datas
            data["_debug_ui_component_type"] = "images" # images
            data["_debug_ui_component_id"] = "0"

            method(data)
        else:
            raise Exception, "Playground should have debug_ui_base_class.py!"

    elif open_type == 'camera':
        raise Exception, "Camera Not Support Now!"

def _processSelectPhoto(imagePath):
    image = Image.open(imagePath)

    # print(type(sss))
    width, height = image.size
    format = _toMNNImageFormat(image)
    imageData = _toMNNData(image)
    return imageData, format, width, height

def _toMNNData(image):
    return np.array(image)

def _toMNNImageFormat(image):
        format = image.mode
        if format == 'RGBA':
            return 0
        elif format == 'RGB':
            return 1
        elif format == 'BGR':
            return 2
        elif format == 'GRAY':
            return 3
        elif format == 'BGRA':
            return 4
        return 0


# <type 'numpy.ndarray'>
def drawImage(data):

    # ndata = np.array(data)
    # print type(ndata)

    img = Image.fromarray(np.uint8(data))
    st.image(img, caption='', use_column_width=True)


def _selectedImage(index=0):
    global selectedImage
    global image_datas
    global multiSelect

    nimage = None
    if multiSelect:
        if image_datas is not None and len(image_datas)>index:
            image_data = image_datas[index]
            nimage = image_data["_image"]
    else:
        if image_datas is not None and len(image_datas)>0:
            image_data = image_datas[0]
            nimage = image_data["_image"]
        
    return nimage


def drawPoints(points, color='red', width=4, index=0):
    nimage = _selectedImage(index)
    if type(nimage).__name__!='ndarray':
        raise Exception, "found no match image, or index out of bound"

    # image = Image.open(simage)
    image = Image.fromarray(nimage)
    idraw = ImageDraw.Draw(image)

    if width <= 1:
        idraw.point(points, fill=color)
    else:
        for x in range(0, len(points)):
            point = points[x]
            idraw.rectangle(
                [
                    (point[0] - width/2, point[1] - width/2),
                    (point[0] + width/2, point[1] + width/2)
                ],
                fill=color)
    st.image(image, caption='', use_column_width=True)


def drawRects(coordList, texts, lineColor='red', lineWidth=2, index=0):
    nimage = _selectedImage(index)
    if type(nimage).__name__!='ndarray':
        raise Exception, "found no match image, or index out of bound"

    if coordList is None or texts is None:
        raise Exception(
            "drawRects input error, coordList or texts is None")
    if len(coordList) != len(texts):
        raise Exception("drawRects input error, coordList length is " +
                        str(len(coordList)) + " but texts length is " + str(len(texts)))

    # image = Image.open(simage)

    print type(nimage)

    image = Image.fromarray(nimage)
    idraw = ImageDraw.Draw(image)



    if lineColor == None:
        lineColor = 'red'

    if lineWidth == None:
        lineWidth = 2

    for x in range(0, len(coordList)):
        coord = coordList[x]
        text = texts[x]

        x = coord[0]
        y = coord[1]
        w = coord[2]
        h = coord[3]

        idraw.polygon([
            (x, y),
            (x+w, y),
            (x + w, y + h),
            (x, y+h)
        ], outline=lineColor)

        idraw.text((coord[0]+2, coord[1]+2), text, fill=lineColor)
    st.image(image, caption='', use_column_width=True)

def setLabel(index, text, config=None):
    st.text(text)


def getEnvVars():
    envs = os.environ
    if os.environ.get('workPath') == None:
        envs['workPath'] = './'
    return envs



    
