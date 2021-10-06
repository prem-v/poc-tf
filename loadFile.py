import os 
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
# call listdir() method
# path is a directory of which you want to list
directories = os.listdir( dir_path )
 
def main():
   # This would print all the files and directories
    for file in directories:
      if file == "eg.tf.json":
        print(file)
        file_path = dir_path+'/eg.tf.json'
        new_file_path = dir_path+'/update.json'
        print(file_path)
        dict_object = python_json_file_to_dict(file_path)
        python_dict_to_json_file(new_file_path, dict_object)

def python_json_file_to_dict(file_path):
    try:
    # Get a file object with write permission.
        file_object = open(file_path, 'r')
        # Load JSON file data to a python dict object.
        dict_object = json.load(file_object)
        print(dict_object)
        dict_object['hello'] = 'world2'
        print(dict_object)
        return dict_object
    except FileNotFoundError:
        print(file_path + " not found. ") 
def python_dict_to_json_file(file_path, dict_object):
    try:
        # Get a file object with write permission.
        file_object = open(file_path, 'w')
        # Save dict data into the JSON file.
        json.dump(dict_object, file_object)
        print(file_path + " created. ")    
    except FileNotFoundError:
        print(file_path + " not found. ")

if __name__ == '__main__':
    main()