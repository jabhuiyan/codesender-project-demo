# Python 3 server example
"""codeServer is a simple server which can be used to practice
Python code.
Attributions:
1. by <Jubaer Ahmed, Aneesh Raghupathy, Carson Thorne>,<November 18th, 2022>
2. https://pylint.pycqa.org/en/v2.13.9/user_guide/run.html#
3. https://flask.palletsprojects.com/en/1.1.x/quickstart/
"""
import os
from io import StringIO
from subprocess import PIPE, STDOUT, run
from flask import Flask, request
from pylint.lint import Run
from pylint.reporters.text import TextReporter
import my_templates
import log_data

app = Flask(__name__)

base_template = my_templates.base_template1


# ---------------------
# persisting code written in server


def check_code(file):
    file = f"{file}.txt"
    if file == ".txt":
        file = "usercode.txt"
    if not os.path.exists(file):
        f = open(file, "w")
        f.close()
    contents = open(file)
    code = [line for line in contents]
    contents.close()
    if len(code) > 0:
        return "".join(code)
    else:
        return "ENTER CODE HERE"


def writefile(file, data):
    file = f"{file}.txt"
    if file == ".txt":
        file = "usercode.txt"
    f = open(file, "w")
    f.write(data.replace('\r', ""))
    f.close()


# -----------------------


def pylint_output(module_name):
    """
    pylint_output(module_name)
    Takes the name of a module and runs pylint on its code.
    :param module_name: the name of the module to be linted.
    :return: a string of pylint's feedback-output
    """
    pylnt_output = StringIO()  # Custom open stream
    reporter = TextReporter(pylnt_output)
    Run([module_name], reporter=reporter, do_exit=False)
    pylnt_txt = str(pylnt_output.getvalue())  # Retrieve the text report and cast as str
    return pylnt_txt


@app.route('/')
def do_get():
    """
    GET method that loads up the webpage and
    retrieves input from client.
    :return: webpage of the server
    """
    writefile("usercode", "")
    return base_template


@app.route('/run_code', methods=['POST'])
def do_post():
    """
    POST method that display output to client.
    :return: webpage with the output of code.
    """
    code = request.form['codestuff']
    username = request.form['userfound']
    log_data.log_event(username, 'RUN', code)
    my_prgm = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
    output = my_prgm.stdout
    pylnt_txt = pylint_output("codeServer.py")
    outp_w_pylint = output + "\nPylint output: \n" + pylnt_txt
    page = base_template.replace('<!-- OUTPUT PLACEHOLDER -->', str(outp_w_pylint))

    return page.replace("usercode", username)


@app.route('/lookup', methods=['POST'])
def lookup():
    """
    LOOKUP method to retrieve stored code by username.
    :return: webpage with username's written code
    """
    username = request.form['username']
    log_data.log_event(username, 'LOOKUP')
    page = base_template.replace("ENTER CODE HERE", check_code(username))

    return page.replace("usercode", username)


@app.route('/save', methods=['POST'])
def save():
    username = request.form['userfound']
    code = request.form['codestuff']
    log_data.log_event(username, 'SAVE', code)
    writefile(username, code)
    page = base_template.replace("ENTER CODE HERE", check_code(username))

    return page.replace("usercode", username)


@app.route('/revert', methods=['POST'])
def revert():
    username = request.form['userfound']
    log_data.log_event(username, 'REVERT')
    page = base_template.replace("ENTER CODE HERE", check_code(username))
    return page.replace("usercode", username)


@app.route('/numpy_prac', methods=['GET', 'POST'])
def numpy_solve():
    """
    NUMPY_SOLVE method to show solutions to the numpy practice problems
    :return: webpage with the practice problem solutions
    """
    return my_templates.base_template2
