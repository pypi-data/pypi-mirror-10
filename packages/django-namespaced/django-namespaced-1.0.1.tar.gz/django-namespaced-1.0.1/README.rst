Namespace resolution context processor
======================================

Django supports namespaces that help applications find out their current
namespace and refer to themselves in a stable way even if there are more
than one instance of the same module in the url patterns.

However, Django does not automatically set the ``current_app`` context
which means that the app will actually resolve the namespaced urls to
the last announced instance of itself.

This context processor digs the detail up and voilá.

Usage
-----

The context processor needs to be added to the template configuration. The
rude way to do it is as follows::

    TEMPLATES[0]['OPTIONS']['context_processors'].append(
        'namespaced.context_processors.namespaced')

Using a context processor for this use is a bit questionable and generally
a middleware would be the correct place to edit requests. However middlewares
are executed at a stage where the URL resolution has not been matched and will
traverse all URLs even if they are not going to be used. This code is mostly
relevant in views anyway.

This enables you to have two separate instances of the same app in two
different urls. Normally Django would always refer to the last instance by the
app name which will mess up all internal linkage within any of the previous
instances. Let's assume we have this inside an app::

    {% url 'myapp:index' %}

To make this work for both instances, the ``urls.py`` should look something
like this::

    urlpatterns = [
        url(r'^first/', include('myapp.urls', namespace='first', app_name='myapp')),
        url(r'^last/', include('myapp.urls', namespace='last', app_name='myapp)),
    ]

The apps can refer to themselves with `myapp:`, each other with `first:` and
`last:`. It will most likely make sense to use the explicit names in the rest
of the project.

For now, the use without namespaces has not been tested.
