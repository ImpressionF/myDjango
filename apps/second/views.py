from django.shortcuts import render


# Create your views here.


def goSecond(requeset):
    # content = 'aa'
    # return render(requeset, 'goSecond.html', content)
    name = 'bro'
    nums = [1, 2, 3, 4]
    return render(requeset, 'goSecond.html', {'name': name, 'nums': nums});
