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
