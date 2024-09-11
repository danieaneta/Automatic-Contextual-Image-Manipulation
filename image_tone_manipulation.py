import numpy as np
import os
import cv2
import datetime as datetime
from LLM_Input import LLM_Model


class Tone_Manipulation():
    def __init__(self, input_directory):
        self.input_directory = input_directory
        self.working_directory = os.getcwd()

        current_time = datetime.datetime.now()
        self.current_time = current_time.strftime("%Y-%m-%d-%H-%M-%S")


    def Read_Store_Image_Array(self, image_list):
        Array_List = []
        for Array in image_list:
            ND_Array = cv2.imread(f"{self.working_directory}/{self.input_directory}/{Array}")
            Array_List.append(ND_Array)
        return Array_List
    

    def Get_Image_Dimensions(self, array_list):
        Dimension_List = []
        for Array in array_list:
            Orig_Dimension = Array.shape
            Dimension_List.append(Orig_Dimension)
        return Dimension_List


    def Get_Index(self, Response_Result, Function_List):
        Tone_Index = None
        for Tone in Function_List:
            if Response_Result == Tone: 
                Tone_Index = Function_List.index(Response_Result)
            else:
                pass
        return Tone_Index
    

    def Get_Overlay_Values(self, Index_Number):
        """
        [[Blue (0,0,255)], [Orange (255, 165,0)], [Yellow (255, 266,0)], [Gray (128,128,128)], [White (255,255,255)]]
        """
        Value_Matrices = [[0,0,255], [255,165,0], [255,255,0], [128,128,128], [255,255,255]]
        Selected_Value = Value_Matrices[Index_Number]
        return Selected_Value
    

    def Make_Tone_Value_List(self, Tone_Value, Directory_Length):
        Tone_List = []
        for i in range(Directory_Length):
            Tone_List.append(Tone_Value)
        return Tone_List


    def Overlay_Image_Value(self, Image_Shape_List, Tone_Value_List):
        Overlay_Image_Array_List = []
        for i in range(len(Image_Shape_List)):
            Overlay_Image_Matrix = np.full(Image_Shape_List[i], Tone_Value_List[i], dtype=np.uint8)
            Overlay_Image_Array_List.append(Overlay_Image_Matrix)
        return Overlay_Image_Array_List
    

    def Merge_Image_Layers(self, Image_List, Overlay_List):
        Output_Images = []
        for i in range(len(Image_List)):
            Output = Image_List[i] * 0.7 + Overlay_List[i] * 0.3
            Output_Images.append(Output)
        return Output_Images
    

    def Backup_Matrix(self, Image_Name_List, Output_Image_List):
        Backup_Dictionary = {'ImageName' : [],
                             'Output_Image' : []}
        
        for i in range(len(Output_Image_List)):
            Backup_Dictionary["ImageName"] = Image_Name_List[i]
            Backup_Dictionary["Output_Image"] = Output_Image_List[i]
        
        with open(f'backups/{self.current_time}.py', 'w') as file:
            file.write(str(Backup_Dictionary))
            file.close()


    def Create_New_Project(self):
        Current_Time = self.current_time
        os.mkdir(f"projects/{Current_Time}")
        return Current_Time


    def Save_New_Project(self, Image_Name_List, Output_Image_List):
        Current_Time = self.Create_New_Project()
        for i in range(len(Output_Image_List)):
            Output_Dir = f'projects/{Current_Time}/{Image_Name_List[i]}'
            cv2.imwrite(f'{Output_Dir}', Output_Image_List[i])


    def Initiate_Process(self): 
        #Receive prompt here 
        Mood_List = ['Cold', 'Warm', 'Sunny', 'Gloomy', 'Neutral']
        response_result = LLM_Model(input('Input Prompt Here: ')).Initiate_Response()
        print('Response Result: ', response_result)

        #Tone Manipulation Prep
        Image_Directory_List = os.listdir(self.input_directory)
        ND_Array_List = self.Read_Store_Image_Array(Image_Directory_List)
        Dimension_List = self.Get_Image_Dimensions(ND_Array_List)

        #Tone Manipulation
        Tone_Index = self.Get_Index(Response_Result=response_result, Function_List=Mood_List)
        Tone_Matrix = self.Get_Overlay_Values(Index_Number=Tone_Index)

        Total_Directory_Length = int(len(ND_Array_List))
        Tone_List = self.Make_Tone_Value_List(Tone_Matrix, Total_Directory_Length)
        Overlay_Image_List = self.Overlay_Image_Value(Image_Shape_List=Dimension_List, Tone_Value_List=Tone_List)

        #Tonal Overlay
        Output_Image_List = self.Merge_Image_Layers(Image_List=ND_Array_List, Overlay_List=Overlay_Image_List)

        #Saving and Backups
        self.Backup_Matrix(Image_Name_List=Image_Directory_List, Output_Image_List=Output_Image_List)
        self.Save_New_Project(Image_Name_List=Image_Directory_List, Output_Image_List=Output_Image_List) 


if __name__ == "__main__":
    Tone_Manipulation(input_directory='input_directory').Initiate_Process()