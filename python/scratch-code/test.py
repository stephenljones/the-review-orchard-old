import csv, sys
sys.stdout = open('test.txt' , 'w')
for row in csv.reader(open('big-list.csv'),delimiter=","):
	category = row[3]
	if category == "Apple":
		print("--Apple Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Comparison":
		print("--Comparison Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Individual Review":
		print("--Individual Review Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "General Review":
		print("--General Review Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Membership Site":
		print("--Membership Site Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "News Review":
		print("--News Review Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Podcast":
		print("--Podcast Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Reddit":
		print("--Reddit Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Set Up":
		print("--Set Up Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Tech Review":
		print("--Tech Review Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Unboxing":
		print("--Unboxing Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "User Manual":
		print("--User Manual Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "User Manual For Purchase":
		print("--User Manual For Purchase Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Video":
		print("--Video Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Specs":
		print("--Specs Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
	elif category == "Follow Up":
		print("--Follow Up Link--")
		print("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')
sys.stdout.close()
