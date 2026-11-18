# Ex.03 Design a Website for Server Side Processing
## Date:11.11.2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
math.html

<html>
<head>
     <title>My sample web page</title>
</head>
<body>
    <h1 align="center">Calculate churn Rate</h1>
    <h2 align="center">Ranjithkumar(26017811)</h2>
     <form method="POST">
    {% csrf_token %}

    <label>InitCust:</label>
    <input type="text" name="Initcust" value="{{I}}"><br><br>

    <label>CustLost:</label>
    <input type="text" name="Custlost" value="{{C}}"><br><br>

    <input type="submit" value="Calculate"><br><br>

    <label>Churn Rate:</label>
    <input type="text" value="{{rate}}"><br><br>
</form>
</body>
</html>

views.py

from django.shortcuts import render
0
def churn_rate(request):

    I = float(request.POST.get('Initcust', '0'))
    C = float(request.POST.get('Custlost', '0'))

    rate = (C / I) * 100 if request.method == 'POST' and I != 0 else 0

    print("Initcust =", I)
    print("Custlost =", C)
    print("Churn rate =", rate)

    return render(request, 'mathapp/math.html', {
        'I': I,
        'C': C,
        'rate': rate
    })

    urls.py

    from django.contrib import admin
    from django.urls import path
    from mathapp import views

    urlpatterns = [path('', views.churn_rate, name='churn_rate'),]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (163).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (162).png>)
## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
