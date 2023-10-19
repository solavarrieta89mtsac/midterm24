# get the user input
import sys
import os

file_name = input("What is the name of the file (without .html)?")
out_file = file_name.lower() + ".html"

body_h1 = input("What is the character's name?")
body_h1 = "<h1>" + body_h1 + "</h1>\n"

body_h2 = input("Wwho is the actor?")
body_h2 = "<h2>Played by " + body_h2 + "</h2>\n"

body_description = input("Please describe your character:")
body_description = "<p>" + body_description + "</p>\n"

body_img = input("Link to the character photo:")
body_img = '<img src="' + body_img + '" alt="' + file_name + '">\n'

body_quo = input("Character quote:")
body_quo = "<p>" + body_quo + "</p>\n"

body_link = input("Youtube Link:")
body_link = "<p>" + body_link + "</p>\n"

combined_body = body_h1 + body_h2 + body_description + body_img + body_quo + body_link
#define the template pages
page_head = "assets/page-head.txt"
page_footer = "assets/page-footer.txt"

if os.path.isfile(page_head):
    f = open(page_head, "r")
    combined_head = ''.join(f.readlines())
    f.close()
else:
    print("No {} present.".format(page_head))
    sys.exit()

if os.path.isfile(page_footer):
    f = open(page_footer, "r")
    combined_footer = ''.join(f.readlines())
    f.close()
else:
    print("No {} present.".format(page_footer))
    sys.exit()
combined_page = combined_head + combined_body + combined_footer

# Write the HTML file
f = open(out_file, "w")
f.write(combined_page)
f.close()
print("created {}".format(out_file))