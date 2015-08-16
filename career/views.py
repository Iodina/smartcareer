from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.core.urlresolvers import reverse
# Create your views here.

# auth
# from django.conf import settings
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout as auth_logout
# from django.contrib.messages.api import get_messages

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LinkForm
from algorithm1 import *



def home(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            link_name = str(cd['link'])
            crawler = Crawler()

            error = ''
            try:
                if "linkedin" in link_name:
                    if 'profile/view' in link_name:
                        # link_name = crawler.get_local_link(link_name)
                        crawler.login()
                # profs = get_profession(crawler.get_skills(link_name))
                # list1 = sort_skills(profs)[:3]
                list1 = sort_skills(get_profession(crawler.get_skills(link_name)))[:3]


                prof_obj = [Profession.objects.filter(name__icontains=item) for item in list1]
                list_sphere = [it[0].sphere.all() for it in prof_obj]
                spheres = []
                for l in list_sphere:
                    spheres += [li for li in l]

                list(set(spheres))    #list of spheres
                spheres_name = [str(s.name) for s in list(set(spheres))]
                spheres_descr = [s.discription for s in list(set(spheres))] #a problem here

                links = [str(Course.objects.filter(sphere = sph)[0].name) for sph in list(set(spheres))]
                link = "https://www.coursera.org/courses?categories="
                for b in links:
                    link += b +','
                link = link[:-1]
                dict = {}
                for a in range(len(spheres_name)):
                    dict[spheres_name[a]] = spheres_descr[a]


            except:
                if "linkedin" not in link_name:
                    error = "Please enter link from LinkedIn"
                else:
                    error = "Please fill your profile with more information"
            if not error:
                t = get_template('career/result.html')
                result = t.render(Context({'user':request.user, 'dict': dict, 'link':link}))
                return HttpResponse(result)
            else:
                form = LinkForm()
                return render(request, 'career/home.html', {'form': form, 'error': error})

    else:
        form = LinkForm()
    return render(request, 'career/home.html', {'form': form})


#
# for item in list:
#
## prof = Profession.objects.filter(name__icontains = 'Data Analyst')   list = object needed
## list_sphere = prof[0].sphere.all()   -- list of spheres
## str(list_sphere[0].name)  -- name of a particular sphere


#### str(Course.objects.filter(sphere = Sphere.objects.all()[0])[0].name)     -- name_link
##

def about(request):
    t = loader.get_template('career/about.html')
    result = t.render(Context({'user':request.user}))
    return HttpResponse(result)

def faq(request):
    t = loader.get_template('career/faq.html')
    result = t.render(Context())
    return HttpResponse(result)

def contact(request):
    return render_to_response('career/contact.html', context_instance=RequestContext(request))

def search_form(request):
    return render(request, 'career/search_form.html')




