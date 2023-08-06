import os

import psutil

from webx.http.request import HttpRequest
from webx.config.settings import settings
from webx.http.response import JsonResponse


async def webx_monitor_stats(request: HttpRequest):
    print("HEADERS")
    print(request.headers)
    headers = request.headers
    auth = headers.get("Authorization")
    print(auth)
    monitor_settings = settings.get("WEBX_MONITORING")
    password = monitor_settings["password"] # no KeyError SHOULD be raised here, since all
    # checks are run before actually adding this view.

    if auth != password:
        response = JsonResponse({"message": "Invalid credentials"}, status=403) # Forbidden
        return response

    cpu_usage = psutil.cpu_percent()
    load_average = psutil.getloadavg()
    running_pid = os.getpid()

    payload = {
        "CPU_USAGE": cpu_usage,
        "LOAD_AVERAGE": load_average,
        "PID": running_pid
    }

    return JsonResponse(payload, status=200)
