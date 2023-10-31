from django.shortcuts import render 
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def near_hundred (request: HttpRequest, n:int) -> HttpResponse:
    if abs(n - 100) <= 10 or abs (n - 200) <= 10:  
        return HttpResponse (True)
    else:
        return HttpResponse (False)
    
def String_Splosion(request: HttpRequest, string:str) -> HttpResponse:
    word = ""
    for i in range(len(string)):
        word += string[:i + 1]
        # word += "\n"
    return HttpResponse(word)

def cat_dog(request: HttpRequest, x:bool) -> HttpResponse:
    num_cat = x.count("cat")
    num_dog = x.count("dog")
    if num_cat == num_dog:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
def lone_sum(request: HttpRequest, a:int, b:int, c:int) -> HttpResponse:
    total = 0
    if a == b == c:
        return HttpResponse(total)
    elif a == b:
        return HttpResponse(c)
    elif b == c:
        return HttpResponse(a)
    elif a == c:
        return HttpResponse(b)

    elif a != b and b != c and a != c:
        return HttpResponse(a + b + c)