from sys import argv
import pickle

filename = argv[1]
with open(filename, 'rb') as f:
    rooms = pickle.load(f)
print(rooms[1].description)
