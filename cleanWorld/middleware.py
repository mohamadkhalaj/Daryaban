import time

from .models import visitor


def vistorsMiddleware(get_response):
    def middleware(request):
        request_start = time.time()
        IGNORED_PATH = [
            "/admin/jsi18n/",
            "/admin/api/visitor/",
            "/favicon.ico",
        ]

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        userAgent = request.META.get("HTTP_USER_AGENT")
        path = request.META.get("PATH_INFO")

        if path not in IGNORED_PATH:
            obj = visitor(ip_address=ip, userAgent=userAgent, path=path)
            if path.startswith("/admin/") and request.user.is_authenticated:
                obj.isAdminPanel = True

        response = get_response(request)

        request_end = time.time()
        try:
            obj.responseTime = request_end - request_start
            obj.save()
        except:
            pass

        return response

    return middleware
