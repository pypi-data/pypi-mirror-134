from django.db.models.query import QuerySet

class uscalt_task(object):
    def __init__(self, method):
        self._method = method
    def __call__(self, *args, **kwargs):
        return self._method(self, *args, **kwargs)

    @classmethod
    def methods(cls):
        def g():
            subject = autodiscover()
            for mod in subject:
                for name in dir(mod.Uscalt):
                    method = getattr(mod.Uscalt, name)
                    if isinstance(method, uscalt_task):
                        yield name, method, mod
        return {name: [method, mod] for name,method,mod in g()}

    @classmethod
    def remove_fields(cls, fields, data):
        for i in data:
            for j in fields:
                del i[j]

        return data

    @classmethod
    def queryset_to_list(cls, queryset):
        if isinstance(queryset, QuerySet):
            return list(queryset.values())
        else:
            raise TypeError('Received incorrect type. Input should be QuerySet')

def autodiscover():
    """
    Autodiscover tasks.py files in much the same way as admin app
    """
    import imp
    from importlib import import_module
    from django.conf import settings
    tmp = []

    for app in settings.INSTALLED_APPS:
        app = app.split('.app')[0]
        try:
            app_path = import_module(app).__path__
        except (AttributeError, ImportError):
            continue
        try:
            imp.find_module('uscalt', app_path)
        except ImportError:
            continue

        tmp.append(import_module("%s.uscalt" % app))
    
    return tmp