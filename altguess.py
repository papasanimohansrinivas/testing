
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
import magic

# print(magic.from_file(".\guessit.py"))

f = magic.Magic(mime=True, uncompress=True)

# print(f.from_file('.\\Test1.java'))

fp = open('Test1.java','r')

import os

# print(os.fstat(fp.fileno()))

import sh