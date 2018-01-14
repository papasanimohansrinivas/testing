
# 
# 	(C) Copyright ${year} Nuxeo (http://nuxeo.com/) and others.
# 	
# 	Licensed under the Apache License, Version 2.0 (the "License");
# 	you may not use this file except in compliance with the License.
# 	You may obtain a copy of the License at
# 	
# 	    http://www.apache.org/licenses/LICENSE-2.0
# 	
# 	Unless required by applicable law or agreed to in writing, software
# 	distributed under the License is distributed on an "AS IS" BASIS,
# 	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# 	See the License for the specific language governing permissions and
# 	limitations under the License.
# 	
# 	Contributors:
# 
# 
def tarfile_extractor(path,file_name):
	import tarfile
	import os
	import sys

	file = None

	try:
		assert tarfile.is_tarfile(path+file_name)
		file = path+file_name
	except AssertionError:
		print  file_name+'is not tar _file.'
		return 'code 100'

	folder = tarfile.open(file,'r')

	for names in folder.getnames():
		if '.py' in names:
			print names
			# with open(names,'r') as dd:
				# print dd.read()




tarfile_extractor('C:\Users\mohanSrinivas\Downloads','\mohantesting.tar.gz')