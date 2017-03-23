#!/usr/bin/python
# coding=utf-8
""" """

from collections import OrderedDict
import pprint

def CPUinfo():
	''' Return the information in /proc/CPUinfo
	as a dictionary in the following format:
	CPU_info['proc0']={...}
	CPU_info['proc1']={...}
	'''
	CPUinfo=OrderedDict()
	procinfo=OrderedDict()

	nprocs = 0
	with open('/proc/cpuinfo') as f:
		for line in f:
			if not line.strip():
				# end of one processor
				CPUinfo['proc%s' % nprocs] = procinfo
				nprocs=nprocs+1
				# Reset
				procinfo=OrderedDict()
			else:
				if len(line.split(':')) == 2:
					procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
				else:
					procinfo[line.split(':')[0].strip()] = ''

	return CPUinfo


def meminfo():
	'''
	Return the information in /proc/meminfo
	as a dictionary
	'''
	meminfo=OrderedDict()

	with open('/proc/meminfo') as f:
		for line in f:
			meminfo[line.split(':')[0]] = line.split(':')[1].strip()
	return meminfo


def show_meminfo():
	print("meminfo___________________________")

	mem_info = meminfo()
	print('Total memory: {0}'.format(mem_info['MemTotal']))
	print('Free memory: {0}'.format(mem_info['MemFree']))

	print("meminfo___________________________")


def show_cpuinfo():
	print("cpuinfo___________________________")

	cpu_info = CPUinfo()
	for processor in cpu_info.keys():
		print(cpu_info[processor]['model name'])

	print("cpuinfo___________________________")


if __name__ == "__main__":
	show_meminfo()
	show_cpuinfo()