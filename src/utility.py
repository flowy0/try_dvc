# utility 


import os 

def create_folders(folder_list):
    '''
    create folders based on the input list
    params: folder_list 
    '''
    for i in folder_list:
        if not os.path.exists(i):
            os.makedirs(i)
            print("folder is created: " + i)
        else:
            print("folder already exists: " + i)