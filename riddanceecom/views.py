from django.shortcuts import render


def handler404(request, *args, **argv):
    return render(request, 'errors/404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception, *args):
    return render(request, 'errors/403.html', status=403)


def handler400(request, exception, *args):
    return render(request, 'errors/400.html', status=400)


"""
        Error handlers for the respective erros.
"""

