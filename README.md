# Tensor_Test

This repository contains test task solution

# Requirements

* Python 3.9.X
* pip and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Installation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/tensor_test/".
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/conftest.py" file

# Results

To check the report, open the "/results/report.html" file once the execution has finished.