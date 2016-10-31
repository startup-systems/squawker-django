from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from squawker.models import Squawk
# from squawker.forms import SquawkForm


def index(request):
    squawks = Squawk.objects.order_by('-id')
    return render(request, 'squawker/index.html', {'squawks': squawks})


def add_squawk(request):
    if request.method == 'POST':
        # TODO: Server side validation
        # if len(request.POST.get('squawk_text')) > 140:
        #     abort(400)
        # Use django ORM api to store squawk
        s = Squawk(text=request.POST.get('squawk_text'))
        s.save()
    return HttpResponseRedirect('/')


# pagination object from flask documentation
class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages


# get squawks for page
def get_squawks_for_page(squawks_list, page, PER_PAGE):
    # iterate over squawks
    if (page == 1):
        i = 0
        j = 20
    else:
        i = ((page - 1) * PER_PAGE)
        j = page * PER_PAGE
    # get squawks for indicated page
    squawks = squawks_list[i:j]
    return squawks


# url generator
def url_for_pages(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_pages'] = url_for_pages
