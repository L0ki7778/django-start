from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
from .dummy_data import gadgets as gadgets
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
import json

# Create your views here.


def start_page_view(request):
    return render(request, 'tech_gadgets/test.html')

class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget.id",0)]["name"])
        new_kwargs = {"gadget_slug":slug}
        return super().get_redirect_url(*args, **new_kwargs)


class GadgetView(View):
    def get(self, request, gadget_slug=""):
        gadget_match = None
        for matching_gadget in gadgets:
           print(f"gadget_slug is {gadget_slug}")
           print(slugify(matching_gadget["name"]))
           if slugify(matching_gadget["name"]) == gadget_slug:
               gadget_match = matching_gadget
        if not gadget_match:
            raise Http404()
        return JsonResponse(gadget_match)

    def post(self, request):

        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response":"das war was"})
        except:
            return JsonResponse({"response": "NOPE!"})

def single_gadget_int_view(request, gadget_id):
    if gadget_id < len(gadgets):
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse('gadget_slug_url', args=[new_slug])

        return redirect(new_url)
    return HttpResponseBadRequest("Kein gadget mit dieser ID")



def single_gadget_view(request, gadget_slug=""):
    if request.method == "GET":
        gadget_match = None

        for matching_gadget in gadgets:
            if slugify(matching_gadget["name"]) == gadget_slug:
                gadget_match = matching_gadget
        if not gadget_match:
            raise Http404()
        return JsonResponse(gadget_match)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response":"das war was"})
        except:
            return JsonResponse({"response": "NOPE!"})
