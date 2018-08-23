# we can do much when we put our mind to it, but for now let's practice KIS and start small
# Objective 1 To use python to create a new Apache2 virtualhost configuration file that accomplishes the following...
# 	* Accepts agrument variables for domain, platform and web root
# 	* Creates a new file, writes some content to this file, saves this file to the appropriate place (/etc/apache2/sites-available) and then closes it
#	* Instructs Apache2 via a command to "enable" the new site with 'sudo a2ensite'

from sys import argv
from os.path import exists
script, domain, platform, doc_root = argv

# test to see if we're storing the variables appropriately
# print("Great, so you said you wanted to create a new conf for " + domain + " with the platform " + platform + " and the web root " + root + ", right?")

# check and see if the file already exists and alert the user
print("Hold up, let's see if this file already exists (True or False)? \t> " + str(exists(domain)) + " <\n")
# print("If the answer was True, all hope abandon yee who hits RETURN here...")
# input("If the answer was True, all hope abandon yee who hits RETURN here...")

# prompt for an email address
print("Well, so maybe it exists and maybe it doesnt. \nWe could probably handle this better. \nI still need to know the email address you want to use for the ServerAdmin.\n")
admin_email = input("Please provide the admin e-mail address? ") # we will have a syntax error if we don't wrap our input with quotes, encapsulating this input with a str() didnt seem to help
# introduce some exception handling here to ask the user to try again but with quotes

# now let's attempt to open the new file
config_file = open(domain,'w')

# now let's write something to this file
config_file.write("<VirtualHost *:80>\n") # open the VirtualHost block
config_file.write("\tServerAdmin " + admin_email + "\n")
config_file.write("\tServerName " + domain + "\n")
config_file.write("\tDocumentRoot " + doc_root + "\n")
config_file.write("</VirtualHost>") # close the VirtualHost block

# let the user know we've completed this
print("Great, well I've written all this to the file so uh, goodbye for now I guess...")
# now close the file
config_file.close

# not sure if print(f"") is supported in the version of python on this machine
# print(f"Your said {platform} for the platform.")
# print(f"Your said {root} for the web root.")"