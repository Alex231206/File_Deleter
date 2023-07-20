import os, shutil, send2trash, pprint
from datetime import datetime

annotation: str = open('annotation.txt', 'r', encoding = 'utf-8').read()
#history_of_requests = open('history_of_requests.txt', 'a')

while True:
    print(annotation)

    user_choice: str = input('Enter your command: ')

    if user_choice == '0':
        print('The program was finished. See you later')

    elif user_choice == '1':
        path: str = input('Enter absolute path to folder: ')

        if os.path.isabs(path):
            try:
                max_size: float = float(input('Enter maximum size of files (in Megabytes) to delete: '))

            except ValueError:
                print('Incorect data!\n')
                continue

            else:
                files_list: list = []

                for foldername, subfolders, files in os.walk(path):
                    for file in files:
                        file_location = f'{foldername}\\{file}'
                        file_extension = file[file.rfind('.')+1:]
                        file_size = os.path.getsize(file_location) / 1024 / 1024

                        if file_size > max_size:
                            each_file_dict: dict = {
                                'FileName': '',
                                'Location': '',
                                'Size (in Megabytes)': '',
                            }

                            each_file_dict['FileName'] = file
                            each_file_dict['Location'] = file_location
                            each_file_dict['Size (in Megabytes)'] = file_size

                            files_list.append(each_file_dict)

                            send2trash.send2trash(file_location)

                pprint.pprint(files_list)
                print()

                history_of_requests = open('history_of_requests.txt', 'a')

                history_of_requests.write(f"""
                
                Date: {datetime.today()}
""")
                pprint.pprint(files_list, stream = history_of_requests)


        else:
            print(f"The path {path} doesn't exist\n")
            continue

    else:
        print(f"The program {user_choice} doesn't exist\n")
        continue






