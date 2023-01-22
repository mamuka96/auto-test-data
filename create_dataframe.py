import os
import pathlib
import pandas as pd
from config import *

list_of_file_names = sorted(os.listdir(folder_path_))
list_of_needed_file_names = [f for f in list_of_file_names if file_name_ in f]

for f in list_of_needed_file_names:
    file_ext = pathlib.Path(f).suffix
    if file_ext == ".csv":
        df = pd.read_csv(f'{folder_path_}/{file_name_}{file_ext}')
    elif file_ext == ".xlsx":
        df = pd.read_excel(f'{folder_path_}/{file_name_}{file_ext}')