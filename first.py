# (C) Copyright ${year} Nuxeo (http://nuxeo.com/) and others.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# 
# distributed under the License is distributed on an "AS IS" BASIS,
# 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# 
# See the License for the specific language governing permissions and
# 
# limitations under the License.
# 
# Contributors:


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
