import argparse
import requests
import json

def get_posts(subreddit_name, aftern):
        data=requests.get(f'http://api.reddit.com{subreddit_name}/hot?limit=100&after={aftern}', headers={'User-Agent': 'windows:requests (by /u/alisa)'})
        
        content=data.json()['data']
        lastfullname=content['after']
        posts= content['children']
        return lastfullname, posts


def get500 (sname):
        l=[]
        after=''
        for i in range(0,5):
                after, posts = get_posts(sname, after)
                l.extend(posts)
        return l[:500]
        


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('subreddit', help="input subreddit")
        parser.add_argument('-o','--output', required=True, help='name of output file')

        args = parser.parse_args()
        iname=args.subreddit
        oname=args.output

        o=get500(iname)

        with open(oname, 'w') as f:
                for line in o:
                        print(json.dumps(line), file=f)

if __name__=='__main__':
        main()
