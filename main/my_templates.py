base_template1 = """
<!DOCTYPE HTML>
<html>
<head>
    <!-- Meta Data -->
    <meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0"/>
    <meta name="description" content="Online Python Editor With Live Syntax Checking">
    <meta name="keywords" content="Lint,Online,Editor,Python,Syntax-Checking">
    <meta name="author" content="Ed Brown">
    <title>COMP2005 Python Quiz</title>
    <!-- Favicon -->
</head>
<body>
<div id="intro">
    <h1>Python Online Quiz</h1>
</div>
<br>
<div>
<p>To save your code, enter your username, type your code, and click the 'Save' button.</p>
<p>To load your saved code, type in your username and click enter.</p>
<p>To revert back to the last version that was saved, click the 'Revert' button.</p>
</div>
<div>
    <form action="/lookup" method="POST">
        <input type = "text" name="username" id="username" placeholder="What is your username"/>
        <br>
        <button type="submit" id="executelookup">Enter</button>
    </form>
    <br/>
    <br />
    <form id= "mainForm" action="/run_code" method="POST">
        <input type="hidden" style="display: none;" name="userfound" value="usercode"/>
        <textarea name="codestuff" id="coding" rows="25" cols="80">ENTER CODE HERE</textarea>
        <br>
        <button type="button" id="run" name="run" onclick="Submit(this.id)">Run</button>
        <button type="button" id="save" name="save" onclick="Submit(this.id)">Save</button>
        <button type="button" id="revert" name="revert" onclick="Submit(this.id)">Revert</button>
    </form>
    <br>
    <div id="output">
        <pre><!-- OUTPUT PLACEHOLDER --></pre>
    </div>
    <br>
    <br>
    <form action="/numpy_prac" method="POST">
        <h4>Practice numpy codes:</h4>
        <br>
        <p>1. Write a NumPy program to test whether none of the elements of a given array is zero.</p>
        <p>2. Write a NumPy program to create a 3x3 identity matrix.</p>
        <p>3. Write a NumPy program to find the number of rows and columns of a given matrix.</p>
        <br>
        <button type="submit" id="solutions">Solutions</button>
    </form>
    <br>
</div>
<script>
function Submit(buttonId) {
    var button_element = document.getElementById(buttonId);
    var form = document.getElementById("mainForm")
    if (button_element.name == "run")
    {
        form.action = "/run_code";
        form.submit();
    }
    else if (button_element.name == "save")
    {
        form.action = "/save";
        form.submit();
    }
    else if (button_element.name == "revert")
    {
        form.action = "/revert";
        form.submit();
    }
}
</script>
</body>
</html>
"""

base_template2 = """
<!DOCTYPE HTML>
<html>
<head>
    <title>COMP2005 Python Quiz</title>
</head>
<body>
<div id="intro">
    <h1>Numpy Practice Code Solutions</h1>
</div>
<br>
<div>
    <h4>Solution to question 1:</h4>
    <p>import numpy as np</p>
    <p>// This has no zero</p>
    <p>x = np.array([1, 2, 3, 4, 5])</p>
    <p>print("Given array: ", x)</p>
    <p>print(np.all(x))</p>
    <p>// This has a zero</p>
    <p>y = np.array([0, 1, 2, 3, 4, 5])</p>
    <p>print("Given array: ", y)</p>
    <p>print(np.all(y))</p>
    <br>
    <br>
    <h4>Solution to question 2:</h4>
    <p>import numpy as np</p>
    <p>x = np.identity(3)</p>
    <p>print(x)</p>
    <br>
    <br>
    <h4>Solution to question 3:</h4>
    <p>import numpy as np</p>
    <p>// Setting up a matrix to test</p>
    <p>x = np.arrange(10,22).reshape((3, 4))</p>
    <p>print("Test matrix: ")</p>
    <p>print(x)</p>
    <p>print("Number of rows and columns of given matrix: ", x.shape)</p>
    <br>
</div>
</body>
</html>
"""
