import pickle

x = 10

y = [1, 2, 3, 4]

with open("Chapter_5_I_O_in_Python/93_Serialization_and_Deserialization/pickle_file", "wb") as p_file:
    pickle.dump(x, p_file)
    pickle.dump(y, p_file)