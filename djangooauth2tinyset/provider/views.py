
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json


@login_required
def APIbasicinfoView(request):
    return HttpResponse(json.dumps({"id":request.user.pk,"email":request.user.email,"nickname":request.user.first_name}))
