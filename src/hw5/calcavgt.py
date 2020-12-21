def calculateavgtitle(jlist):
	titles=list(map(lambda post: post['data']['title'], jlist))
	length=0
	for t in range(0, len(titles)-1):
		length=length+len(titles[t])
	print("Average post title length is: ", length/len(titles))
