from django.urls import path
from .views import start_page_view, single_gadget_view,\
      single_gadget_int_view, GadgetView, RedirectToGadgetView


urlpatterns = [
    path('', RedirectToGadgetView.as_view()),
    path('start/', start_page_view),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', single_gadget_view),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),

]
