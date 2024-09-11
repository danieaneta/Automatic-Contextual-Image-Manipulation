import numpy as np
import os
import cv2
import datetime as datetime


from image_tone_manipulation import Tone_Manipulation

Input_Directory = 'input_directory'

def test_Read_Store_Image_Array():
    #Successfully take np array and open in opencv:
    Image_List = os.listdir(Input_Directory)
    Tone_Manipulation(Input_Directory).Read_Store_Image_Array(Image_List)
    assert True

def test_Get_Image_Dimensions():
    Image_List = os.listdir(Input_Directory)
    Array_List = Tone_Manipulation(Input_Directory).Read_Store_Image_Array(Image_List)
    Tone_Manipulation(Input_Directory).Get_Image_Dimensions(Array_List)
    assert True

def test_Get_Index():
    Response_Result = 'Cold'
    Mood_List = ['Cold', 'Warm', 'Sunny', 'Gloomy', 'Neutral']

    Index = Tone_Manipulation(Input_Directory).Get_Index(Response_Result=Response_Result, Function_List=Mood_List)
    assert Index == 0

def test_Overlay_Values():
    Index = 1
    Selected_Value = Tone_Manipulation(Input_Directory).Get_Overlay_Values(Index_Number=Index)
    assert Selected_Value == [255,165,0]

def test_Make_Tone_Value_List():
    Tone_Value = [225,165,0]
    Directory_Length = 5
    Tone_List = Tone_Manipulation(Input_Directory).Make_Tone_Value_List(Tone_Value=Tone_Value, Directory_Length=Directory_Length)
    assert len(Tone_List) == Directory_Length

def test_Overlay_Values():
    Image_List = os.listdir(Input_Directory)
    Image_Arrays = Tone_Manipulation(Input_Directory).Read_Store_Image_Array(Image_List)
    Image_Shape_List = Tone_Manipulation(Input_Directory).Get_Image_Dimensions(Image_Arrays)
    Tone_List = [[225,165,0], [225,165,0], [225,165,0], [225,165,0]]
    Overlay_Image_Array_List = Tone_Manipulation(Input_Directory).Overlay_Image_Value(Image_Shape_List=Image_Shape_List, Tone_Value_List=Tone_List)

    assert type(Overlay_Image_Array_List) == list

def test_Merge_Image_Layers():
    Image_List = os.listdir(Input_Directory)
    Image_Arrays = Tone_Manipulation(Input_Directory).Read_Store_Image_Array(Image_List)
    Image_Shape_List = Tone_Manipulation(Input_Directory).Get_Image_Dimensions(Image_Arrays)
    Tone_List = [[225,165,0], [225,165,0], [225,165,0], [225,165,0]]
    Overlay_Image_Array_List = Tone_Manipulation(Input_Directory).Overlay_Image_Value(Image_Shape_List=Image_Shape_List, Tone_Value_List=Tone_List)
    Tone_Manipulation(Input_Directory).Merge_Image_Layers(Image_List=Image_Arrays, Overlay_List=Overlay_Image_Array_List)
    assert True

def test_Backup_Matrix():
    Image_List = os.listdir(Input_Directory)
    Image_Arrays = Tone_Manipulation(Input_Directory).Read_Store_Image_Array(Image_List)
    Image_Shape_List = Tone_Manipulation(Input_Directory).Get_Image_Dimensions(Image_Arrays)
    Tone_List = [[225,165,0], [225,165,0], [225,165,0], [225,165,0]]
    Overlay_Image_Array_List = Tone_Manipulation(Input_Directory).Overlay_Image_Value(Image_Shape_List=Image_Shape_List, Tone_Value_List=Tone_List)
    Output_Images = Tone_Manipulation(Input_Directory).Merge_Image_Layers(Image_List=Image_Arrays, Overlay_List=Overlay_Image_Array_List)
    Tone_Manipulation(Input_Directory).Backup_Matrix(Image_Name_List=Image_List, Output_Image_List=Output_Images)
    assert True
