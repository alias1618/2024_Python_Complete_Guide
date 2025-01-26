import pickle

x = 10
y = 100
my_list = [1, 2, 3, 4, 5, 9]

def save_data():
    global x, y, my_list
    data = {'x': x, 'y': y, "my_list": my_list}

    with open("Chapter_5_I_O_in_Python/94_Pickle/my_pickle_file", 'wb') as pfile:
        pickle.dump(data, pfile)

save_data()