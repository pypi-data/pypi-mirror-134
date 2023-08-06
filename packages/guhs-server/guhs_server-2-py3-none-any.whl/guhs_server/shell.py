import os.path
import subprocess


def read_file(path):
    path = shell_path(path)
    with open(path) as file:
        return file.read()


def write_file(path, contents):
    path = shell_path(path)
    with open(path, 'w') as file:
        return file.write(contents)


def file_exists(path):
    path = shell_path(path)
    return os.path.isfile(path)


def remove_file(path):
    path = shell_path(path)
    os.remove(path)


def files_in_path(path):
    path = shell_path(path)
    list_path = os.listdir(path)
    return [element for element in list_path if os.path.isfile(os.path.join(path, element))]


def execute_command(command):
    process = execute_background_command(command)
    stdout, stderr = [channel.decode() for channel in process.communicate()]

    return process.returncode, stdout, stderr


def execute_background_command(command):
    environment = os.environ.copy()

    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        env=environment
    )


def shell_path(path):
    return os.path.expanduser(path)
