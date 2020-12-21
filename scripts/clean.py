
import argparse
from hw5.cleanfix import *
from hw5.jsonhelper import *


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', required=True, help="input json file")
	parser.add_argument('-o','--output', required=True, help='name of output file')
	
	args = parser.parse_args()
	iname=args.input
	oname=args.output
	
	jlist=open_many_jsons(iname)
	
	o=fixtitle(jlist)
	o=fixtime(o)
	
	dump_many_jsons(o, oname)
			
	
if __name__=='__main__':
	main()
