from django.shortcuts import render

# Create your views here.

def set(request):
    request.session['username'] = 'Dharmendra'
    request.session['age'] = '23'
    request.session['city'] = 'Bhopal'
    return render(request, 'set.html')  

def get(request):
    if 'username' in request.session:
        request.session.modified = True 
        username = request.session.get('username')
        age = request.session.get('age')
        city = request.session.get('city')
        return render(request, 'get.html', {'username': username ,'age': age, 'city': city})
    else:
        return render(request, 'get.html', {'error': 'No session data found.'})

def delete(request):
    if 'username' in request.session:
        del request.session['username']
        return render(request, 'delete.html')
    return render(request, 'delete.html')