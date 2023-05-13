## Frappe QR Code

Frappe QR Code built by Upeosoft Limited

#### License

MIT

## Dependencies

This module depends on qrcode, base64 and BytesIO. If any of them is not installed in your environment, you will need to install it as shown below for the case of qrcode.

<pre><code> ./env/bin/pip3 install qrcode </code></pre>

This command is to be run from your bench directory.


## How to Install

On your instance terminal, run the below command to grab the code from GitHub to your instance: <pre><code> bench get-app https://github.com/Upeosoft-Limited/Frappe-QR-Code.git </code></pre>

Once the command has completed the execution, you will need to install the app in every site where you want toe app to run. You can install this app with the below command: <pre><code> bench --site [SITE_NAME] install-app frappe_qrcode </code></pre>

When this command completes, the application is installed in your site. You will however need to run the migrate command, which ensures that all changes to the database have been effected to your site's database. If your site is in development mode, ensure that bench is running. If you are on production, supervisor will take care of this. The command to effect the migrations is as below: <pre><code> bench --site [SITE_NAME] migrate </code></pre>

At this point, your app is fully installed and database changes migrated. All you need to do is restart your instance. The commands to do that are below:

#### Development Environment 
<pre><code> bench start </code></pre>

If you receive a warning that bench is already running, run the below command:
<pre><code> bench restart </code></pre>

#### Production Environment
<pre><code> sudo supervisorctl restart all </code></pre>

<b>Please note that these commands can be run from any directory, as long as you are inside the bench directory.</b>

## How to Pull Changes
When you need to get the most recent update from this repo, you need to do the following:
+ Navigate to the **frappe_qrcode** app in your bench directory (*Ensure you are inside the **frappe_qrcode** app directory*)
+ Run the below command:
<pre><code> git pull </code></pre>
+ Once that has completed getting the changes, run the below command:
<pre><code> bench migrate </code></pre>

## How to Push Changes
**NOTE:** *Any time you need to push changes, you first need to pull just to make sure you have the latest changes to avoid trouble with GitHub.*

Customizations done to the system need to be exported to be accessed when you install this application to other instances. Below I will break down the two ways you can customize doctypes, and how to handle the changes.

#### Customization done on the DocTypes
These are customizations where you go to the doctype or the doctype list and click on <b>customize</b>. After you are done customizing the ductype, always remember to click on the <b>Actions</b> button, then click on <b>Export Customizations</b>. If you cannot see the Export Customizations button on your intance, it is because your instance is not in developer mode. You can enable developer mode by any of the following methods:

##### Running a bench Command
<pre><code> bench set-config developer_mode 1 </code></pre>

##### Manual Editing
Go to the <b>site_config.json</b> file of your instance and check for the presence of this key-value pair
<pre><code> developer_mode: 0 </code></pre>
If this exists, change the 0 to 1 and restart your bench. If it does not exist, add it, being careful to ensure your json is well formatted to avoid errors.

#### Customization done on the Custom Field DocType
When you customize the system using this feature, your changes can be tracked easily by <b>exporting fixtures</b>. This is what we discuss next.

At this point, if you check the changes with the <b>git status</b> command, none of the customizations done on the documents will be shown. To track them, we will need to export them as fixtures by running the following command:
<pre><code> bench export-fixtures </code></pre>

This will gather all changes from all documents and create json files with required changes to inform the system what it needs to take care of when the app is installed in another instance.


## Print Formats
When you have custom print formats, you will need to ensure that you have selected the right module, which in our case is the <b>Frappe-QR-Code</b> app. Once this is done, the <b>bench export-fixtures</b> command will take care of the rest.
