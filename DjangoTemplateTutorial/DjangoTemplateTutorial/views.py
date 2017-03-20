from django.http import HttpResponse

from django.template import loader

def index(request):
    template = loader.get_template( 'index.html')

    context = {
        'name': 'Belal Khan',
        'fname': 'Azad Khan',
        'course': 'Python Django Framework',
        'address': 'Kanke, Ranchi, India',
    }
    return HttpResponse(template.render(context,request))

