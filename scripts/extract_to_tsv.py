import argparse
import json
import csv
import random

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('json_file', help='json file to process')
        parser.add_argument('num_posts_to_output', help='num of posts')
        parser.add_argument('-o', '--out_file', required=True, help='output tsv')
        args= parser.parse_args()

        jfile=args.json_file
        jlist=[]
        with open(jfile, 'r') as f:
                for line in f:
                        try: jline=json.loads(line)
                        except ValueError as e: continue
                        jlist.append(jline)

        #randomize, get name, title
        n=int(args.num_posts_to_output)
        randomized= jlist if n >= len(jlist) else random.sample(jlist, n)

        d=[]
        for r in randomized:
                d.append({'Name':(r['data']['name']).encode('ascii','ignore'), 'title': r['data']['title'].encode('ascii','ignore'),'coding':''})


        #write
        with open(args.out_file, 'w') as tsv_file:
                t=csv.DictWriter(tsv_file, fieldnames=['Name', 'title', 'coding'], delimiter='\t')
                t.writeheader()
                t.writerows(d)




if __name__=="__main__":
        main()
