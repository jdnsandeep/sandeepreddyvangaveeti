from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
  
<body>
    <h2>Welcome To ShinChanWorld</h2>
    <marquee> Lets Move this text.</marquee>
    <marquee direction="right" 
        behavior="alternate" 
        style="border:BLACK 2px SOLID">
        PathallapallivamsiKrishna
    </marquee>
</body>
  
</html>

                        """)