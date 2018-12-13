#Get number of experiments in a specified Optimizely project

## Steps
If you have Python 3 downloaded and installed on your computer then begin with step 1, if not, download and install Python 3 on your computer [here](https://www.python.org/downloads/)

In your CLI
1. Clone this github repository
2. cd into the number_of_experiments_in_project directory
* Optional: Activate your virtual environment
3. Run
```
pip3 install requests
```
4. Generate your own [Optimizely v2 REST API Token](https://developers.optimizely.com/x/rest/getting-started/)
5. Run
```
python3 app.py <your project id> <your API token>
```
This script will print the number of experiments within the specified project to the CLI
