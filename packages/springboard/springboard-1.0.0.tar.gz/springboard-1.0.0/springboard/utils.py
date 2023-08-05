import re
from functools import wraps
from urlparse import urlparse


def parse_repo_name(repo_url):
    pr = urlparse(repo_url)
    _, _, repo_name_dot_git = pr.path.rpartition('/')
    if repo_name_dot_git.endswith('.git'):
        repo_name, _, _ = repo_name_dot_git.partition('.')
        return repo_name
    return repo_name_dot_git


def ga_context(context_func):
    """
    A decorator for Cornice views that allows one to set extra parameters
    for Google Analytics tracking::

        @ga_context(lambda context: {'dt': context['category'].title, })
        @view_config(route_name='page')
        def view(request):
            return {
                'category': self.workspace.S(Category).filter(title='foo')[0],
            }

    :param func context_func:
        A function which takes one argument, a context dictionary made
        available to the template.
    :returns:
        A dict containing the extra variables for Google Analytics
        tracking.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            context = func(self, *args, **kwargs)
            self.request.google_analytics.update(context_func(context))
            return context
        return wrapper
    return decorator


def config_list(data):
    """
    A function that takes a string of values separated by newline characters
    and returns a list of those values

    :param func context_func:
        A function which takes one argument, a string of values separated by
        newline characters

    :returns:
        A list containing the values separated by newline characters,
        stripped of whitespace between the value and newline character

    """
    return filter(None, (x.strip() for x in data.splitlines()))


def config_dict(data):
    """
    A function that takes a string of pair values, indicated by '=', separated
    by newline characters and returns a dict of those value pairs

    :param func context_func:
        A function which takes one argument, a string of value pairs with
        '= between them' separated by newline characters

    :returns:
        A dict containing the value pairs separated by newline characters

    """
    lines = config_list(data)
    return dict(re.split('\s*=\s*', value) for value in lines)
