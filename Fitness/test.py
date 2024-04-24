import pandas as pd
import pickle
def save_object(obj,filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
file = pd.read_csv('Fitness.csv',encoding='UTF-8')
res = {file['name'][i]:file['translation'][i] for i in range(len(file['name']))}
save_object(res,'FitnessNamesObject')