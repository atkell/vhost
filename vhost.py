# we can do much when we put our mind to it, but for now let's practice KIS and start small
from sys import argv
from os.path import exists
script, domain, platform, doc_root = argv

# check and see if the file already exists and alert the user
print("Hold up, let's see if this file already exists (True or False)? \t> " + str(exists(domain)) + " <\n")

# prompt for an email address
print("Well, so maybe it exists and maybe it doesnt. \nWe could probably handle this better. \nI still need to know the email address you want to use for the ServerAdmin.\n")
admin_email = input("Please provide the admin e-mail address? ") # we will have a syntax error if we don't wrap our input with quotes, encapsulating this input with a str() didnt seem to help
# introduce some exception handling here to ask the user to try again but with quotes

# now let's attempt to open the new file
config_file = open(domain,'w')

# now let's write something to this file
# we could do this without so many lines, I'm sure
config_file.write("<VirtualHost *:80>\n") # open the VirtualHost block
config_file.write("\tServerAdmin " + admin_email + "\n")
config_file.write("\tServerName " + domain + "\n")
config_file.write("\tDocumentRoot " + doc_root + "\n")
config_file.write("</VirtualHost>") # close the VirtualHost block

# let the user know we've completed this
print("Great, well I've written all this to the file so uh, goodbye for now I guess...")

# now close the file
config_file.close