import pickle

from syncmymoodle.filetree import Node

with open(".cache/asdf.pkl", "rb") as f:
    root: Node = pickle.load(f)

root.remove_children_nameclashes()

for path in root.list_files():
    print(path)
