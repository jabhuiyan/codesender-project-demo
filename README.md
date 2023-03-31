# codesender-project-demo
A simple online python interpreter using FLASK framework


[project by Fteam consisting of @jabhuiyan, @aneesh and @cwt837]
part of project for COMP 2005 by Prof. Ed Brown

(all updates and documentation can be observed from project_updates.txt file)
---------------------------------------------------
CodeServer is a simple server which can be used to practice python codes
---------------------------------------------------


-----------------------------------------------------
codeserver can be installed by going to codeserver directory from terminal and writing:

       pip install -e .

TO RUN THE FLASK APPLICATION SERVER:
with codeServer and flask installed, the flask server can be run by going to the directory of codeServer
and then setting up Flask environment variable with the following:

      $ export FLASK_APP=codeServer.py

(alternatively, for WINDOWS):
      
      >set FLASK_APP=codeServer.py

and then running:
       
       python -m flask run

TO RUN UNITTEST:
with pytest installed, go to the directory of codeServer and run

       python3 -m unittest
