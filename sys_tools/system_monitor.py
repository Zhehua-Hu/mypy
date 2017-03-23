#!/usr/bin/python
# coding=utf-8
"""
Show CPU and Memory Information.
"""

from collections import OrderedDict


def cpu_info():
	''' Return the information in /proc/cpu_info
	as a dictionary in the following format:
	CPU_info['proc0']={...}
	CPU_info['proc1']={...}
	'''
	cpu_info=OrderedDict()
	procinfo=OrderedDict()

	nprocs = 0
	with open('/proc/cpuinfo') as f:
		for line in f:
			if not line.strip():
				# end of one processor
				cpu_info['proc%s' % nprocs] = procinfo
				nprocs=nprocs+1
				# Reset
				procinfo=OrderedDict()
			else:
				if len(line.split(':')) == 2:
					procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
				else:
					procinfo[line.split(':')[0].strip()] = ''

	return cpu_info

def mem_info():
	'''
	Return the information in /proc/meminfo
	as a dictionary
	'''
	meminfo=OrderedDict()

	with open('/proc/meminfo') as f:
		for line in f:
			meminfo[line.split(':')[0]] = line.split(':')[1].strip()
	return meminfo

def show_mem_info():
	print("meminfo___________________________")

	_mem_info = mem_info()
	print('Total memory: {0}'.format(_mem_info['MemTotal']))
	print('Free memory: {0}'.format(_mem_info['MemFree']))

	print("meminfo___________________________")

def show_cpu_info():
	print("cpu_info___________________________")

	_cpu_info = cpu_info()
	for processor in _cpu_info.keys():
		print(_cpu_info[processor]['model name'])

	print("cpu_info___________________________")


if __name__ == "__main__":

	show_mem_info()

	show_cpu_info()
