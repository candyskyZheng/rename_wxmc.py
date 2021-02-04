import re
import os,sys

def rename_wxmc():
	old_names = os.listdir(path)
	for new_name_zuozhe in old_names:
		if new_name_zuozhe != sys.argv[0]:
			if ", SPE" in new_name_zuozhe:
				pattern = re.compile('\d+, (.+), SPE\d+')
				old_name_wxmc = str(pattern.findall(new_name_zuozhe))
				old_name_wxmc = str(old_name_wxmc.strip(''))
				new_name_wxmc = str(old_name_wxmc.replace("," , "_").replace("." , "_").replace("$" , "_").\
					replace("(" , "_").replace(")" , "_").replace("%" , "_").replace("-" , "_").\
					replace(":" , "_").replace(":" , "_").replace("#" , "_").replace("'" , "_").\
					replace('"' , "_").replace('&',"_"))
				new_name = new_name_zuozhe.replace(old_name_wxmc[2:-2], new_name_wxmc[2:-2])
				#new_name = name + " et al., " + new_name_wxmc[2:-2] + ", SPE" + new_name_zuozhe.split(', SPE')[1]
				os.rename(os.path.join(path,new_name_zuozhe),os.path.join(path,new_name))
				#print(old_name," >>> ", new_name)
				print("->"+new_name)

			elif ", OTC" in new_name_zuozhe:
				pattern = re.compile('\d+, (.+), OTC\d+')
				old_name_wxmc = str(pattern.findall(new_name_zuozhe))
				old_name_wxmc = str(old_name_wxmc.strip(''))
				new_name_wxmc = str(old_name_wxmc.replace("," , "_").replace("." , "_").replace("$" , "_").\
					replace("(" , "_").replace(")" , "_").replace("%" , "_").replace("-" , "_").\
					replace(":" , "_").replace(":" , "_").replace("#" , "_").replace("'" , "_").\
					replace('"' , "_").replace('&',"_"))
				new_name = new_name_zuozhe.replace(old_name_wxmc[2:-2], new_name_wxmc[2:-2])
				#new_name = name + " et al., " + new_name_wxmc[2:-2] + ", SPE" + new_name_zuozhe.split(', SPE')[1]
				os.rename(os.path.join(path,new_name_zuozhe),os.path.join(path,new_name))
				#print(old_name," >>> ", new_name)
				print("->"+new_name)

			elif ", IPTC" in new_name_zuozhe:
				pattern = re.compile('\d+, (.+), IPTC\d+')
				old_name_wxmc = str(pattern.findall(new_name_zuozhe))
				old_name_wxmc = str(old_name_wxmc.strip(''))
				new_name_wxmc = str(old_name_wxmc.replace("," , "_").replace("." , "_").replace("$" , "_").\
					replace("(" , "_").replace(")" , "_").replace("%" , "_").replace("-" , "_").\
					replace(":" , "_").replace(":" , "_").replace("#" , "_").replace("'" , "_").\
					replace('"' , "_").replace('&',"_"))
				new_name = new_name_zuozhe.replace(old_name_wxmc[2:-2], new_name_wxmc[2:-2])
				#new_name = name + " et al., " + new_name_wxmc[2:-2] + ", SPE" + new_name_zuozhe.split(', SPE')[1]
				os.rename(os.path.join(path,new_name_zuozhe),os.path.join(path,new_name))
				#print(old_name," >>> ", new_name)
				print("->"+new_name)

			else:
				pattern = re.compile('\d+, (.+).pdf')
				old_name_wxmc = str(pattern.findall(new_name_zuozhe))			
				new_name_wxmc = str(old_name_wxmc.replace("," , "_").replace("." , "_").replace("$" , "_").\
					replace("(" , "_").replace(")" , "_").replace("%" , "_").replace("-" , "_").replace(":" , "_").replace(";" , "_")\
					.replace("#" , "_").replace("'" , "_").replace('"' , "_"))
				new_name = new_name_zuozhe.replace(old_name_wxmc[2:-2], new_name_wxmc[2:-2])
				new_name = new_name + '.'
				os.rename(os.path.join(path,new_name_zuozhe),os.path.join(path,new_name))
				#print(old_name," >>> ", new_name)
				print("->"+new_name)

if __name__ == '__main__':
	path0 = r'D:\文件更新\Refer_Update0203'
	path1 = os.listdir(path0)
	for path2 in path1:
		path = r'D:\文件更新\Refer_Update0203\\A.J. Bermudez folder'
		path = path.replace(path.split("Refer_Update0203\\")[1] , path2)
		print(path)
		rename_wxmc()

