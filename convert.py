import os
import subprocess

source = 'Source'
directory = 'Result'
run_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), source)


def coping():
	if not os.path.exists(directory):
		os.makedirs(directory)

	print('Start programm')
	print('------------')
	for img in os.listdir(run_dir):
		process = subprocess.run(os.path.join(os.path.dirname(__file__), 'convert.exe') + ' %s' % os.path.join(run_dir, img))
		print('STDERR', process.stderr)
		print('STDOUT', process.stdout)
		print('ARGS', process.args)
		print('returncode', process.returncode)
	print('------------')
	print('End programm')


coping()