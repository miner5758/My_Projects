import os

#create folder in "python os folder", example: create_folder('h','Default')
#cretae folder in different directory, example: create_folder('e','Downloads')
# if you want to create a folder inside a folder, example create_folder('e','Downloads\\e')
def create_folder(folder_name,folder_location):
    if folder_location == 'Default':
        d = '/'
        directory = folder_name
        parent_dir = r"Python OS Folder"
        path = os.path.join(parent_dir, directory)
        if path.count(d) == 0:
            os.mkdir(path)
            print("Directory '%s' created" %directory)
        elif path.count(d) >= 1:
             os.makedirs(path)
             print("Directory '%s' created" %directory)
    elif folder_location != 'Default':
        try:
            t = '\\'
            s = '/'
            directory = folder_name
            parent_dir = r"User"
            parent_dir = parent_dir + t + folder_location
            path = os.path.join(parent_dir, directory)
            if path.count(s) == 0:
                os.mkdir(path)
                print("Directory '%s' created" %directory)
            elif path.count(s) >= 1:
                os.makedirs(path)
                print("Directory '%s' created" %directory)
        except FileNotFoundError:
            print(folder_location,"isn't a place in your computer!")
    else:
        print('Something has gone extremley wrong if you are seeing this!')
