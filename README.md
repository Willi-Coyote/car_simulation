# Installation

- Install Python 3.12 or higher (you can try with a lower version, but if you face any difficulties, install this
  version)
- Open a terminal and navigate to your project directory, e.g. ```C:/my_projects/car_simulation```
- Create a virtual env by executing ```python -m venv venv```
- Activate the Virtual Environment ```venv\Scripts\activate```
- Install Dependencies ```pip install -r requirements.txt```

# Setup IDE

- The recommended IDE is PyCharm
- Create the virtual env as described in installation and set this as local interpreter
- Use your IDE to run the tests and the application. It is much easier than in the command line. If you prefer the
  command line anyway please see the chapters below.

# Execute tests

- Navigate to the root directory of your project , e.g. ```C:/my_projects/car_simulation```
- Set the PYTHONPATH to src and tests. Please note, depending on your shell or os system this might be different. The
  example is for a Windows Command prompt ```$env:PYTHONPATH="src;tests"```
- Execute ```pytest```

# Run the application

- Make sure your virtual env is activated: ```venv\Scripts\activate```
- Set the PYTHONPATH: ```$env:PYTHONPATH="src;tests"```
- Run the main: ```python src/main.py```