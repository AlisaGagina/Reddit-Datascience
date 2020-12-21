
from hw5.collect import sample

def main():
	
	sub_reddits_1=['funny', 'AskReddit', 'gaming', 'aww', 'pics', 'Music', 'science', 'worldnews', 'videos', 'todayilearned']	
	sub_reddits_2=['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends', 'unpopularopinion']
	
	sample('../data/sample1.json', sub_reddits_1)
	sample('../data/sample2.json', sub_reddits_2)
		

	
if __name__=='__main__':
	main()

