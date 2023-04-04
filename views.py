from django.shortcuts import render
import datetime
# Create your views here.
def christmas(request):
    now = datetime.datetime.now()
    return render(request, "christmas.html", {
        "new": now.month == 4 and now.day == 4
    })




