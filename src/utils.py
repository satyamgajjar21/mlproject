import os
import sys

import numpy as np 
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
    
    
#     ✔ Creates folder if needed
# ✔ Saves Python object as binary
# ✔ Uses dill for serialization
# ✔ Used to save models & preprocessors
# ✔ Keeps project clean and modular