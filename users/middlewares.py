from django.shortcuts import redirect


def auth(view_function):
    def wrapped_view(request,*args,  **kwargs):
        if request.user.is_authenticated==False:
            return redirect('users:login')
        return view_function(request, *args, **kwargs)
    return wrapped_view



def gust(view_function):
    def wrapped_view(request,*args,  **kwargs):
        if request.user.is_authenticated:
            return redirect('product_list')
        return view_function(request, *args, **kwargs)
    return wrapped_view