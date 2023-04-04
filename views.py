from django.shortcuts import render
import datetime
# Create your views here.
def christmas(request):
    now = datetime.datetime
    return render(request, "christmas.html", {
        "new": now.month == 25 and now.day == 6
    })




