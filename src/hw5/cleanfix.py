from datetime import datetime

def fixtitle (l):
	cleanl=[] 
	for obj in l: 
		obj2={}  
		for k in obj:
			if k=='title_text':
				obj2['title']=obj['title_text'] 
			else:
				obj2[k]=obj[k] 
		if 'title' in obj2:
			cleanl.append(obj2)
	return cleanl 

def fixtime(l):
	cleanl=[]
	for obj in l:
		if 'createdAt' in obj:
			try:
				orig_dt = datetime.strptime(obj['createdAt'], "%Y-%m-%dT%H:%M:%S%z")
			except:
				continue
			utc_time_value = orig_dt - orig_dt.utcoffset()
			utc_dt = utc_time_value.replace(tzinfo=None)
			obj['createdAt']=utc_dt.astimezone().strftime( "%Y-%m-%dT%H:%M:%S%z")
		cleanl.append(obj)
	return cleanl 

 
