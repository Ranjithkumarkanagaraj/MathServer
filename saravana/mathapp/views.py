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