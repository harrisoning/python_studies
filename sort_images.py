import os, shutil

def create_dir(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)
        print(folder)

if __name__ == '__main__':      
    files = os.listdir()
    for i in files:
        if 'IMG' in i:
            year = i[4:8]
            month = i[8:10]
            y_m_path = year+'/'+month
            create_dir(y_m_path)
            try:
                shutil.move(i,year+'/'+month)
            except:
                print(i)
