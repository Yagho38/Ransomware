import os


def discover(initial_path):
    
    extensions = [
        'docx', 'doc', 'ppt', 'txt',
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absopath = os.path.abspath(os.path.join(dirpath, _file))
            ext = absopath.split('.')[-1]
            if ext in extensions:
                yield absopath


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)