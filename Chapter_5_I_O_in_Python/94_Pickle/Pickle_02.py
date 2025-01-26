import pickle

x = None
y = None
my_list = None

def restore_data():
    global x, y, my_list
    with open("Chapter_5_I_O_in_Python/94_Pickle/my_pickle_file", "rb") as pfile:
        data = pickle.load(pfile)
        x = data['x']
        y = data['y']
        my_list = data['my_list']

restore_data()
print(x, y, my_list)

