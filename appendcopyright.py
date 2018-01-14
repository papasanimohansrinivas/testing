def app_copy_right(path_name=None,file_name=None,file_object=None):


	### status 1 succesfully appended 
	### status 2 

	### writes log file 

	logfile = open('log1.txt','a')
	failed_files = open('failed_files.txt','a')




	if path_name==None:
		path_name=''

	#### import fileextensions from copyright_filetype module

	from copyright_filetype import fileextensions	

	### import get_file_type to get the file types 


	from file_type_checker import get_file_type,check_extension

	extension=get_file_type(file_name)

	### check extensions if extensions are whether java/go/shell scripts or something


	extension_type = check_extension(extension)

	## extension_type 1 means they are source files 

	if extension_type==1:
		print(file_name+' is source code file and  checking for Copyright\n ')
		
		logfile.write(file_name+' is source code file and  checking for Copyright\n ')

		ibm_copyright=fileextensions[extension]

		with open(path_name+file_name,'r') as file_:
			source_code=file_.read()
			file_.close()

		

		### checks 'copyright' word in file then takes action depending on the if word is present or not



		if 'copyright' not in source_code.lower():
			print('file : '+file_name+"   hasn't got got IBM Copyright\n")

			with open(path_name+file_name,'w') as fil :
				fil.write(ibm_copyright.rstrip('\r\n')+'\n'+source_code)
				fil.close()
				### if file has sucesfully appended copyright then status is 1 
				logfile.write('path_name : '+path_name+'file_name : '+file_name+'status : '+str(1))
		else:
			logfile.write('path_name : '+path_name+'file_name : '+file_name+'status : '+str(1))
			print('file : '+file_name+"   has already got IBM Copyright\n")

	### extension code 2 means configurarion files .

	## we are going to leave configuration file aside 

	elif extension_type==2:
		logfile.write(file_name+'  is configuration file and not going to  prepend Copyright')
		print(file_name+' is configuration file and not  going to  prepend Copyright')


	### if extension is 3 we show allowed formats and log the failed files names 
	elif extension_type==3:
		logfile.write('path_name : '+path_name+'file_name : '+file_name+'status : '+str(0))
		failed_files.write('path_name : '+path_name+'file_name : '+file_name+'status : '+str(0))
		print('sorry this program can handle following file types only \n'+'\n'.join(r.upper() for r in fileextensions.keys())+
			'\ncheck failed files for status')
	logfile.close()
	failed_files.close()

# app_copy_right(file_name='Test1.java')