import csv, sys
sys.stdout = open('test.txt' , 'w')

#Add each category to a dictionary key and links to the value for that key
links_dict = {}
for row in csv.reader(open('big-list.csv'),delimiter=","):
	category = row[3]

	#################### TOP CENTER COLUMN ####################
	#APPLE
	if category == "Apple":
		key = "Apple"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' ' + row[1] + '</a>')

	###################### FIRST COLUMN #######################
	#TECH REVIEW
	elif category == "Tech Review":
		key = "Tech Review"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	#NEWS REVIEW
	elif category == "News Review":
		key = "News Review"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	###################### SECOND COLUMN ######################
	#VIDEO REVIEW
	elif category == "Video":
		key = "Video"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	#GENERAL REVIEW
	elif category == "General Review":
		key = "General Review"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	###################### THIRD COLUMN ######################
	#COMPARISON
	elif category == "Comparison":
		key = "Comparison"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	#UNBOXING LINKS
	elif category == "Unboxing":
		key = "Unboxing"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	#FOLLOW UP LINKS
	elif category == "Follow Up":
		key = "Follow Up"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')

	#REDDIT LINKS
	elif category == "Reddit":
		key = "Reddit"
		links_dict.setdefault(key, [])
		links_dict[key].append("<a href=" + '"' + row[2] + '"' + " class=\"link-text\">" + row[0] + ' - ' + row[1] + '</a>')


#Create HTML tags for headers and links

#APPLE
print("<!------------------------------------->")
print("<!----------TOP CENTER COLUMN---------->")
print("<!-------------APPLE LINKS------------->")
print("<!------------------------------------->")
print('<h2 class="category-text">Apple Links</h2>')
for key, links in links_dict.items():
	if key == 'Apple':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

#TECH REVIEW
print("<!------------------------------------->")
print("<!------------FIRST COLUMN------------->")
print("<!----------TECH REVIEW LINKS---------->")
print("<!------------------------------------->")
print('<h2 class="category-text">Tech Reviews</h2>')
for key, links in links_dict.items():
	if key == 'Tech Review':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

#NEWS REVIEW
print("<!------------------------------------->")
print("<!----------NEWS REVIEW LINKS---------->")
print("<!------------------------------------->")
print('<h2 class="category-text">News Reviews</h2>')
for key, links in links_dict.items():
	if key == 'News Review':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

#COMPARISON REVIEW
print("<!------------------------------------->")
print("<!------------THIRD COLUMN------------->")
print("<!-------COMPARISON REVIEW LINKS------->")
print("<!------------------------------------->")
print('<h2 class="category-text">Comparison</h2>')
for key, links in links_dict.items():
	if key == 'Comparison':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

#UNBOXING REVIEW
print("<!------------------------------------->")
print("<!-----------UNBOXING LINKS------------>")
print("<!------------------------------------->")
print('<h2 class="category-text">Unboxing</h2>')
for key, links in links_dict.items():
	if key == 'Unboxing':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

#FOLLOW UP REVIEW
print("<!------------------------------------->")
print("<!-----------FOLLOW UP LINKS----------->")
print("<!------------------------------------->")
print('<h2 class="category-text">Follow Up</h2>')
for key, links in links_dict.items():
	if key == 'Follow Up':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

#REDDIT REVIEW
print("<!------------------------------------->")
print("<!------------REDDIT LINKS------------->")
print("<!------------------------------------->")
print('<h2 class="category-text">Reddit</h2>')
for key, links in links_dict.items():
	if key == 'Reddit':
			for a_tag in links:
				print(a_tag)
print("<!------------------------------------->")
print("\n")

sys.stdout.close()
