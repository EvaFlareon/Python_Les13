import os
import subprocess

source = 'Source'
directory = 'Result'
run_dir = os.path.join(os.path.dirname(__file__), source)


def coping():
    if not os.path.exists(directory):
        os.makedirs(directory)

    print('Start program')
    print('------------')
    for img in os.listdir(run_dir):
        process = subprocess.run(
            'convert ' + os.path.join(run_dir, img) + ' -resize 200 ' + os.path.join(os.path.dirname(__file__),
                                                                                     directory, img))
        print('STDERR', process.stderr)
        print('STDOUT', process.stdout)
        print('ARGS', process.args)
        print('returncode', process.returncode)
    print('------------')
    print('End program')


coping()
