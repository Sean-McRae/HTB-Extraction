import os

cookie = raw_input('Cookie: ')

cook2string = str(cookie)

htb = 0
for num in range(172):
	stringify = str(htb)
	cmd = 'curl -s -b '+'"'+cook2string+'"'+' https://www.hackthebox.eu/home/machines/profile/'+stringify+' | grep -o -P "(?<=statusCheck).+(?=#serverStatus)"'
	cmd2 = 'curl -s -b '+'"'+cook2string+'"'+' https://www.hackthebox.eu/home/machines/profile/'+stringify+' | grep -o -P "(?<=IP:).+(?=</td>)"'
	htb = htb+1
	print ("Now Grabbing HTB #:"+stringify)
	os.system(cmd)
	os.system(cmd2)



