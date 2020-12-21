import requests
from .jsonhelper import dump_many_jsons

def get_posts(subreddit_name, num_posts):
	data=requests.get(f'http://api.reddit.com/r/{subreddit_name}/new?limit={num_posts}', headers={'User-Agent': 'windows:requests (by /u/alisa)'})
	content=data.json()['data']
	posts= content['children']
	return posts

def sample (fname, sub_reddits):
	l=[];
	for sr in sub_reddits:
		l.extend(get_posts(sr,100))
	dump_many_jsons(l, fname)
	
