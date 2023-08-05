About tgext.langdomain
----------------------

tgext.langdomain is a TurboGears2 extension that supports detecting the user
language from the domain it is connecting from.

Installing
----------

tgext.langdomain can be installed from pypi::

    pip install tgext.langdomain

should just work for most of the users.

Enabling
--------

To enable tgext.langdomain put inside your application
``config/app_cfg.py`` the following::

    import tgext.langdomain
    tgext.langdomain.plugme(base_config)

or you can use ``tgext.pluggable`` when available::

    from tgext.pluggable import plug
    plug(base_config, 'tgext.langdomain')

Options
-------

langdomain will force the language of the current request based on:
**Top Level Domain**, **SubDomain** and **param** unless there is
already a language stored into the session.

**By default none of those behaviours is enabled**

When plugging langdomain the following options to turn on behaviours are available:

    *param* -> Name of the GET param used to force language, ``True`` means ``lang``.

    *tld* -> Dict of *tld*s that map to a language

        EXAMPLE::

             plug(app_cfg, 'tgext.langdomain',
                  tld={
                    'com': 'en',
                    'it': 'it'
             })

    *subdomain* -> Dict of subdomains that map to a language

        EXAMPLE::

             plug(app_cfg, 'tgext.langdomain',
                  subdomain={
                    'en': 'en',
                    'it': 'it'
             })

When requests are performed like **it.server.net** it will lookup **it** inside
the ``subdomain`` dictionary and **net** inside the ``tld`` dictionary.
