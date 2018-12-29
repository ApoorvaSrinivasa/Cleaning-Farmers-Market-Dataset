# Data-cleaning
CS-513, Theory and Practice of Data Cleaning, Fall 2018

## The Data
The dataset chosen for the final project is a U.S Farmer’s Market dataset. A Farmer’s market is a business run by the farmers themselves, wherein, they sell their produce directly to the customers. 
The dataset consists of information about various farmer's markets throughout the U.S, such as the location of the market, its social networking accounts, active months, mode of payment, goods sold etc.

## The Process
### Overview and initial assessment
Description of the structure and content of the dataset and quality issues that are apparent from an initial inspection. Also, describe a (hypothetical or real) use case of the dataset and derive from it some data cleaning goals that can achieve the desired fitness for use. In addition: Are their use cases for which the dataset is already clean enough? 

### Data cleaning with OpenRefine
In this hands-on part of the project, OpenRefine is used to clean the chosen dataset — as much as needed for the use case and a little more to remove major data discrepancies.  A documentation of the data cleaning process is created, both in narrative form and with supplemental information (e.g., which columns were cleaned and what changes were made?). Further, the results are quantified along with provenance information from OpenRefine.

### Data cleaning/manipulation using Python
An additional step, in which Python is used for cleaning tasks that couldn't be completed by OpenRefine.

### Developing a relational database schema
Logical integrity constraints (ICs) are identified after loading the data into a SQLite database with a target schema. Further, SQL queries are used to profile the dataset and to check the ICs that we have identified.

### Creating a workflow model
YesWorkflow is used to create a workflow model for the entire project. The following questions can be answered using the workflow: what are the key inputs and outputs of workflow? What are the dependencies? A visual version of the workflow is also created using the YesWorkflow tool.


Source for the data : https://www.ams.usda.gov/local-food-directories/farmersmarkets
