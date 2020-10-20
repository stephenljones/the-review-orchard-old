import csv, sys
sys.stdout = open('formatted-links.txt' , 'w')
for row in csv.reader(open('ipad8links.csv'),delimiter=","):
	print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
sys.stdout.close()
