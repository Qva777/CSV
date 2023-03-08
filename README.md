<h1>📍How to install: </h1>

<details><summary><h1>🧾Manual start:</h1></summary><br>
<h4>1 - Connect venv:</h4> 

```
python -m venv venv
```

<h4>2 - Activate it:</h4> 
<h5>For Windows</h5>

```
.\venv\Scripts\activate
```
<h5>For MacOS</h5>
```
source /venv/bin/activate
```


<h4>3 - Install libraries:</h4>

```
pip install -r requirements.txt
```

<h4>4 - Run the migration:</h4> 

```
python manage.py makemigrations
```

<h4>5 - Apply migration:</h4> 

```
python manage.py migrate
```

<h4>6 - Run server:</h4> 

```
python manage.py runserver
```

</details>
<details><summary><h1>🗂️How to install fixtures:</h1></summary><br/>

```
python manage.py loaddata My_fixtures/myfixture.json
```

</details>


[//]: # (<h1>Link to posted site:</h1>)
[//]: # (<a href="https://www.google.com/" target="_blank">Google</a>)