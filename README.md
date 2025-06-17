# install
pip install fastapi uvicorn sqlalchemy pymysql

<h1>Package install commands</h1>
<ol>
<li>python -m venv venv  # Creates a folder named "venv" (windows)</li>
<li>
    <ul>
    <li>source venv/bin/activate</li>
    <li>source venv/Scripts/activate (windows/bash)</li>
    </ul>
</li>
<li>pip install fastapi uvicorn </li>
<li>pip freeze > requirements.txt</li>
<li>uvicorn main:app --reload</li>
</ol>

### sqlalchemy
<p>
SQLAlchemy is basically referred to as the toolkit of Python SQL that provides developers with the flexibility of using the SQL database. The benefit of using this particular library is to allow Python developers to work with the language's own objects, and not write separate SQL queries. They can basically use Python to access and work with databases. 

SQLAlchemy is also an Object Relational Mapper which is a technique used to convert data between databases or OOP languages such as Python.
</p>