#!/usr/bin/python
# coding=utf-8
""" """
import time
import datetime
# from datetime import date

def WholeRunTime(run_fun):
	start = time.time()

	run_fun()

	end = time.time()
	print end-start

def PureRunTime(run_fun):
	start = time.clock()

	run_fun()

	end = time.clock()
	print end-start

def WholeAndPureRunTime(run_fun):
	Whole_start = time.time()
	Pure_start = time.clock()

	run_fun()

	Pure_end = time.clock()
	Whole_end = time.time()
	print("WholeTime:"+ ('%.2f'%(Piece_end-Piece_start)) + 's')
	print("PureTime:" + ('%.2f'%(Piece_end-Piece_start)) + 's')

def GetDate():
	return datetime.date.today()

def GetDateTime(format='%Y-%m-%d %H:%M:%S'):
	return datetime.datetime.now().strftime(format)

def main():
	def run_fun():
		index = 0
		for i in range(100):
			for j in range(200):
				for k in range(1000):
					index += 1
		x = raw_input("Input\n")
		print(x)
		return index


	# WholeRunTime(run_fun)
	# PureRunTime(run_fun)
	WholeAndPureRunTime(run_fun)

if __name__ == "__main__":
    main()