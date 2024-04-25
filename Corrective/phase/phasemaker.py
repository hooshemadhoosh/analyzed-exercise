import pandas as pd
from tkinter import filedialog as fd
import pickle
def save_object(obj,filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
filename = fd.askopenfilename(title='Open files')
if filename!='' and filename.endswith('.xlsx'):
    file = pd.read_excel(filename)
    data = {file['name'][i]:{name:file[name][i] for name in file.columns} for i in range(len(file['name']))}
    save_object(data,filename.replace('.xlsx',''))
