Title: Porting function based generic views to class based views
Date: 2011-09-16 12:12
Lang: en
Author: Kamal Mustafa
Tags: django; python; 2011;
Slug: porting-function-based-generic-views-to-class-based-views
Summary: How to port function based generic views to class based views

It not really obvious in the
documentation how we should proceed. I try to make as little changes as possible to
code. The following is a sample function that we need to port to class
based views.

    from django.views.generic import list_detail
    def supported_sending_networks(request, page=1):
    from django.core.paginator import Paginator, InvalidPage, EmptyPage
    _TEMPLATE_PATH = "faq/list_sending_networks.html"
    network_list = EZSPossibleSendNetwork.objects.all()
    paginator = Paginator(network_list, 15)
    return list_detail.object_list(
    request,
    queryset=network_list,
    paginate_by=15,
    page=page,
    template_name=_TEMPLATE_PATH,
    template_object_name='networks',
    )

The new equivalent class based views for this is
`django.views.generic.list.ListView`. My first attempt after looking at
the documentation:-

    def def supported_sending_networks(request, page=1):
    class SupportedSendingNetworkView(ListView):
    queryset = EZSPossibleSendNetwork.objects.all()
    paginate_by = 15
    context_object_name = 'networks_list'
    template_name = "faq/list_sending_networks.html"
    return SupportedSendingNetworkView.as_view()

but I got error related to something 'function object not iterable ...'.
Look like the as\_view() function call actually return a function object
rather than a response. Looking around I'm supposed to alias the class
with the function name.

    class SupportedSendingNetworkView(ListView):
    queryset = EZSPossibleSendNetwork.objects.all()
    paginate_by = 15
    context_object_name = 'networks_list'
    template_name = "faq/list_sending_networks.html"
    supported_sending_networks = SupportedSendingNetworkView.as_view()

Make sense since now `supported_sending_networks` would simply be a
plain function. While the views now work, there's still no pager. Turn
out that now Django only expect the `page` parameter for the pager to
work in either two ways only:-

-   Specified as parameter in the urlconf.
-   As query string parameter.

This mean I have to modify my urls.py definition. Once that defined, I
need to pass the page value as a context object by overriding the
get\_context\_data() method.

    class SupportedSendingNetworkView(ListView):
    queryset = EZSPossibleSendNetwork.objects.all()
    paginate_by = 15
    context_object_name = 'networks_list'
    template_name = "faq/list_sending_networks.html"
    def get_context_data(self, **kwargs):
    context = super(SupportedSendingNetworkView, self).get_context_data(**kwargs)
    try:
    context['page'] = int(self.args[0])
    except (IndexError, ValueError):
    context['page'] = 1
    return context

All parameters to the views now available as `self.args` or
`self.kwargs` respectively. Some other notes, function based generic
views would be [deprecated in
Django-1.5](https://docs.djangoproject.com/en/dev/internals/deprecation/)
so if you moving to Django-1.3 this a good time to start porting your
generic views usage to class based views. It also not obvious to me that
we have to call the superclass method when overriding `get_context_data`
method otherwise you would not have the complete context data. It only
after I found this blog [post](http://blog.oscarcp.com/?p=182).
