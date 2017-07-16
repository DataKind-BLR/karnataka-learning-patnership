Setup 
==========

Requirements
---------------

## Python
- Installation Guide: https://www.python.org/about/gettingstarted/

## Superset
- Installation & Configuration: https://superset.incubator.apache.org/installation.html
- Introduction Video: https://youtu.be/3Txm_nj_R7M

Making your own build
----------------------

## Preparing the Database
- Superset imports data from databases, thereby the data has to be consolidated to this form. 
- To do, this utilize the superset_data_generation.py script
- On the Commandline shift to the directory containing the script file
- Run the script using the following command structure
	python superset_data_generation.py </path/to/class4/csv> </path/to/class5/csv> </path/to/class6/csv> </path/to/community_feedback_data/csv> -o <output_file_name>.sqlite
- Note that `-o <output_file_name>` is an optional parameter, in the absence of which the output file defaults to `combined_data.sqlite`

## Configurations on Superset

### Run Superset
- Having installed and configured Superset execute the following command to run Superset:
	superset runserver -p <port_number>
- Note that `-p <port_number>` is an optional parameter, in the absence of which the web server defaults to the port 8088
- Open localhost:8088 to start using Superset

### Add a Database
- Having logged into Superset, in order to import a database select from the Menu tabs the Sources > Databases option.
- In the list of Database page that opens, click on the `+` (Add a new database) button to configure and import a new database.
- In the `Add Database` configuration page that opens. now make the following configurations:
	- Give the database a name in the `Database Name` field
	- Give the absolute path as `sqlite:////absolute/path/to/sqlite/database/file` in the `SQLAlchemy URI` field		- Click on the `Test Connection` button to verify that the database connection is secure, if not, verify that the `SQLAlchemy URI` is correct
	- Check the `Expose to SQL Lab` checkbox. This makes the database open to be queried and visualized in the SQL Lab feature of Superset
	- Click on the `Save` button to save changes
	- For other databases or further documentation, please refer: https://superset.incubator.apache.org/tutorial.html?highlight=dashboard#connecting-to-a-new-database

### Creating a Dashboard
https://superset.incubator.apache.org/tutorial.html?highlight=dashboard#creating-a-slice-and-dashboard

## Import Dashboard
- Having logged into Superset, in order to import a database select from the Menu tabs the Sources > Import Dashboards option.
- Click on the `Choose File` option and navigate and select to the directory containing the dashboard .pickle file.
- Click on the `Import` button to import the database.
