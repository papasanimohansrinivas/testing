import requests 

re=requests.get('https://api.github.com/repos/papasanimohansrinivas/KNN-implementation/git/refs/heads')


i = re.json()
hash_= i[0][u'object'][u'sha']

input_ ={
   "ref": "refs/heads/jayaprakash",
   "sha": hash_
}

headers_ = {
	'username':'papasani.mohansrinivas@gmail.com',
	'password':'Xmen@007'
}
body ={
  "content": "Content of the blob",
  "encoding": "utf-8"
}

USERNAME = headers_['username']
PASSWORD = headers_['password']


params = {
	'path':'ref/heads/jayaprakash',
	'ref':'jayaprakash'
}
response=requests.get('https://api.github.com/repos/papasanimohansrinivas/KNN-implementation/git/blobs',auth=(USERNAME, PASSWORD),params=params)

print response.json()
