import glob
import math
import os
import shutil

# Start in the root folder
os.chdir('C:/Users/USER/Documents')

print("Current Directory:", os.getcwd())



def pwd():
    return os.getcwd()


def cd():
    if not args:
        return 'Specify the directory'
    path = args[0]
    try:
        os.chdir(path)
        return pwd().split(os.sep)[-1]
    except FileNotFoundError:
        return 'No such file or directory'


def humanize(size):
    unit = 1024
    power = min(int(math.log(size, unit)), 3)
    units = ['B', 'KB', 'MB', 'GB']
    return f'{size // pow(unit, power)}{units[power]}'


def get_size(st_size, is_file):
    if not args or not is_file:
        return ''
    commands = {'-l': str(st_size), '-lh': humanize(st_size)}
    return ' ' + commands.get(args[0], '')


def ls():
    files = sorted(os.scandir(), key=lambda x: not x.is_dir())
    return '\n'.join(
        file.name + get_size(file.stat().st_size, file.is_file())
        for file in files
    )


def get_files(ext):
    return [file for file in glob.glob(f'*{ext}') if os.path.isfile(file)]


def rm():
    if not args:
        return 'Specify the file or directory'

    target = args[0]

    # Handle file extension removal
    if target.startswith('.'):
        files = get_files(target)
        if not files:
            return f'File extension {target} not found in this directory'

        for f in files:
            os.remove(f)
        return

    target_path = os.path.abspath(target)

    if not os.path.exists(target_path):
        return 'No such file or directory'

    try:
        if os.path.isfile(target_path):
            os.remove(target_path)
        elif os.path.isdir(target_path):
            shutil.rmtree(target_path)
    except Exception as e:
        return str(e)


def mv():
    if not args:
        return 'Specify the current name of the file or directory and the new location and/or name'
    if len(args) != 2:
        return 'Specify the current name of the file or directory and the new location and/or name'

    fr, to = args

    # Handle moving by extension
    if fr.startswith('.'):
        files = get_files(fr)
        if not files:
            return f'File extension {fr} not found in this directory'

        for file in files:
            dest = os.path.join(to, os.path.basename(file))
            if os.path.exists(dest):
                while True:
                    choice = input(f'{os.path.basename(dest)} already exists in this directory. Replace? (y/n)\n')
                    if choice.lower() == 'y':
                        shutil.move(file, dest)
                        break
                    elif choice.lower() == 'n':
                        break
            else:
                shutil.move(file, dest)
        return

    old_path = os.path.abspath(fr)
    new_path = os.path.abspath(to)

    if not os.path.exists(old_path):
        return 'No such file or directory'

    if os.path.isdir(to):
        new_path = os.path.join(new_path, os.path.basename(fr))

    if os.path.exists(new_path):
        return 'The file or directory already exists'

    try:
        shutil.move(old_path, new_path)
    except Exception as e:
        return str(e)


def mkdir():
    if not args:
        return 'Specify the name of the directory to be made'
    dir_name = args[0]

    dir_path = os.path.abspath(dir_name)

    if os.path.exists(dir_path):
        return 'The directory already exists'

    try:
        os.makedirs(dir_path)
    except Exception as e:
        return str(e)


def cp():
    if not args:
        return 'Specify the file'
    if len(args) != 2:
        return 'Specify the current name of the file or directory and the new location and/or name'

    src, dest = args

    # Handle copying by extension
    if src.startswith('.'):
        files = get_files(src)
        if not files:
            return f'File extension {src} not found in this directory'

        for file in files:
            dest_path = os.path.join(dest, os.path.basename(file))
            if os.path.exists(dest_path):
                while True:
                    choice = input(f'{os.path.basename(dest_path)} already exists in this directory. Replace? (y/n)\n')
                    if choice.lower() == 'y':
                        shutil.copy(file, dest_path)
                        break
                    elif choice.lower() == 'n':
                        break
            else:
                shutil.copy(file, dest_path)
        return

    src_path = os.path.abspath(src)
    dest_path = os.path.abspath(dest)

    if not os.path.exists(src_path):
        return 'No such file or directory'

    if not os.path.isfile(src_path):
        return 'Specify the file'

    if os.path.isdir(dest):
        dest_path = os.path.join(dest_path, os.path.basename(src))

    if os.path.exists(dest_path):
        return f'{os.path.basename(dest_path)} already exists in this directory'

    try:
        shutil.copy(src_path, dest_path)
    except Exception as e:
        return str(e)


ACTIONS = {
    'pwd': pwd,
    'cd': cd,
    'ls': ls,
    'mv': mv,
    'rm': rm,
    'mkdir': mkdir,
    'cp': cp
}

while (command := input()) != 'quit':
    cmd, *args = command.split()
    if out := ACTIONS.get(cmd, lambda: 'Invalid command')():
        print(out)
