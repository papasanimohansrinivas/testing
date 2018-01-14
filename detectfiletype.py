
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
def get_filetype(file_path=None,file_name=None):
	relative_path = file_path
	import os

	# from subprocess import call

	# os.system('file '+os.getcwd()+'\Test1.java')

	# print(os.getcwd())
	# # check_call('file '+os.getcwd()+'\Test1.java')

	import subprocess as sp
	cmd = 'ls -lrt'

	# output = sp.check_output ('ls')

	# from fabric import api


# import pip
# installed_packages = pip.get_installed_distributions()
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      # for i in installed_packages])

# for u in installed_packages_list:
	# print(u)
# get_filetype()

import subprocess

p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line)
retval = p.wait()