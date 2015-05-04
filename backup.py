#!/usr/bin/python

import os
import time

DBSERVER = 'localhost'
DBUSER = 'root'
DBPASSWORD = 'root'
DBNAME = 'miranda'

filename = 'home/coder/backup/data/backup.'+str(int(time.time()))+'.sql'
os.system('mysqldump -u' + DBUSER + ' -p' + DBPASSWORD + ' ' + DBNAME + ' > ' + filename)
# os.system('cp ' + filename)