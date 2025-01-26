import pickle

with open("Chapter_5_I_O_in_Python/93_Serialization_and_Deserialization/pickle_file", "rb") as p_file:
    print(pickle.load(p_file))
    print(pickle.load(p_file))