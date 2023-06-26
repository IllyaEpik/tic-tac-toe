import os
def find_file(name_file):
    file = __file__.split("\\")
    del file[-1]
    del file[-1]
    file = "/".join(file) 
    return os.path.join(file, name_file)