import os, time, exifread, re
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from hachoir.core import config

def rename_file(file, c_time):
    c_time = re.sub('-|:', '', c_time).replace(' ', '_')
    file_type = file.split('.')[-1]
    new_name = f'IMG_{c_time}.{file_type}'
    if os.path.exists(new_name):
        print('File exists')
        now = str(time.time())[-5:]
        final_name = f'IMG_{c_time}_{now}.{file_type}'
    else:
        final_name = new_name
    # os.rename(file, final_name)
    print(f'{file} --> {final_name}')
    return final_name

def rename_bmtime(file, t='m'):
    if t == 'b':
        t_stamp = os.stat(file).st_birthtime
    else:
        t_stamp = os.path.getmtime(file)
    c_time = time.strftime('%Y%m%d_%H%M%S',time.localtime(t_stamp))
    new_name = rename_file(file, c_time)

def rename_img(file):
    try:
        with open(file, 'rb') as f:
            tags = exifread.process_file(f)
            c_time = str(tags['EXIF DateTimeOriginal'])
            new_name = rename_file(file, c_time)
    except KeyError:
            rename_bmtime(file, 'b')
    except:
            return file

def rename_vid(file):
    try:
        c_time = extractMetadata(createParser(file)).exportDictionary()['Metadata']['Creation date']
        if c_time[:4] != '1904':
            new_name = rename_file(file, c_time)
    except AttributeError:
            print(f'No Creation Time: {file}')
            rename_bmtime(file)
            print('-'*50)
    except:
            return file

if __name__ == '__main__':
    config.quiet = True
    files = os.listdir()
    errors, others = [], []
    for file in files:
        # images
        if re.search('HEIC|JPG|JPEG|PNG', file, re.IGNORECASE):
            errors.append(rename_img(file))
                
        # videos and others   
        elif re.search('MOV|MP4|M4V', file, re.IGNORECASE):
            errors.append(rename_vid(file))

        else:
            others.append(file)

    errors = list(filter(None, errors))
    print()
    print(f'Files: {len(files)}')
    print(f'Errors: {len(errors)}', errors)
    print(f'Others: {len(others)}', others)