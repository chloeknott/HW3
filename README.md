# Recipe-Maker-Web-Application
- Chloe Knott (chloeknott)
Instructions:

Prerequisites: 

Python 3x
    
pip 

Installation Steps:

1.Clone the Repository
    git clone https://github.com/chloeknott/HW3.git 
    cd Recipe-Maker-Web-Application

2.Install Required Libraries

`pip install -r requirements.txt`

3.Set up Virtual Environment

Create a new virtual environment folder

    python3 -m venv venv
Activate Virtual Environment 

    source venv/bin/activate

4.Set-up Database

    python3 setup-db.py

5.Run the Application (Launches the Flask Server)

    python3 run.py

6.Access the Application 
        Open your web browser and navigate to:

        Home page:
         http://127.0.0.1:5000/

        Login page:
         http://127.0.0.1:5000/login

        Registration page: 
        http://127.0.0.1:5000/registration 

        Recipe page: 
        http://127.0.0.1:5000/recipes 

        Create Recipe:
        http://127.0.0.1:5000/create-recipe 

        View more details for recipe:    http://127.0.0.1:5000/recipe/1 

