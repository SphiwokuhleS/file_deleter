#!/usr/bin/env python

# First get the path if the directory you want to delete files in
# Then get the particular file extension you want to delete
# Thn delete all files that have the files extension
import os
import optparse as op


def get_arguments():
	parser = op.OptionParser()

	parser.add_option("-p", "--path", dest="path", help="The directory you want to delete filees in")
	parser.add_option("-x", "--extension", dest="extension", help="Delete files with this extension")
	
	(options, arguments,)  = parser.parse_args()

	if not options.path:
		parser.error("Please specify a directory")
	return options

def get_dir(directory):
	return directory

def get_extension(extension):
	return extension

# def go_to_dir(dir):
# 	#check if dir exists, if it does go to that dir
# 	if os.path.isdir(dir) == 1:
# 		os.system("cd " + dir)
# 	else:
# 		print("Direcory does not exist...")

def delete_files(directory, extenstion):
	path = get_dir(directory)
	exten = get_extension(extension)
	dirlist = os.listdir(path)
	
	if os.path.isdir(path):
		for fil in dirlist:
			if fil.endswith(extension):
				os.remove(os.path.join(path, fil))
	else:
		print("The directory does not exist.")


options = get_arguments()

path = get_dir(options.path)

extension = get_extension(options.extension)
#go_to_dir(path)

delete_files(options.path, options.extension)

