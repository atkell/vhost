# vhost
Exploration of how to programmatically add and or edit an apache virtualhost configuration file via scripting

## objectives
To use python to create a new Apache2 virtualhost configuration file that accomplishes the following...
* Accepts agrument variables for domain, platform and web root
 * Creates a new file, writes some content to this file, saves this file to the appropriate place (/etc/apache2/sites-available) and then closes it
* Instructs Apache2 via a command to "enable" the new site with 'sudo a2ensite'
