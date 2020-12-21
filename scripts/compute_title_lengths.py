import argparse
from hw5.jsonhelper import open_many_jsons
from hw5.calcavgt import *

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('sample', help='json file to compute')
	
	args = parser.parse_args()
	jlist=open_many_jsons(args.sample)
	calculateavgtitle(jlist)
	
if __name__=='__main__':
	main()

