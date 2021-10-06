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
        update_engress(dict_object)
        print(dict_object)
        # all_values = list(nested_dict_values_iterator(dict_object))
        # print(all_values)
        # print(dict_object)
        return dict_object
    except FileNotFoundError:
        print(file_path + " not found. ")

def update_engress(dict_object):
  engressValues = dict_object['resource']['aws_security_group_rule'].values()
  count = 0
  for v in engressValues:
    count += 1
  print(count)
  if count>0:
    new_engress_str = f'engress{count+1}'
    old_engress_str = f'engress{count}'
    dict_object['resource']['aws_security_group_rule'][new_engress_str]=dict_object['resource']['aws_security_group_rule'][old_engress_str]
    dict_object['resource']['aws_security_group_rule'][new_engress_str]['vpc-id']='xyz' 

def nested_dict_values_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all values of given dictionary
    for value in dict_obj.values():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for v in  nested_dict_values_iterator(value):
                yield v
        else:
            # If value is not dict type then yield the value
            yield value


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