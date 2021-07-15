#!/usr/bin/python3
## includes


## define static vars such as ssh launch opts

## read file into array as menu item,mainopt,opt,opt,... - this stolen code is clearly not enough

import csv 

items = []

with open('file.csv') as csvfile:    
	csvReader = csv.reader(csvfile)    
	for row in csvReader:        
		items.append(row[0])        
print(items)


## create menu from array


## assemble and execute command defined above
