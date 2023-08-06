0.3pre2
-------

* Fixed compatibility with Django 1.7 and 1.8

0.3pre1
-------

* Fixed package setup: Added `README.md` to `MANIFEST.in`


0.3pre0
-------

* Initial `django-piston3` (_pre_-)release.
* Based on [`django-piston-0.2.3`](
    https://pypi.python.org/pypi/django-piston/0.2.3)
* Contains additional commits from:
  * <https://bitbucket.org/j00bar/django-piston/commits>
  * <https://bitbucket.org/spookylukey/django-piston/commits>

* __ISSUE__: Creation of `request.PUT` and `request.FILES`
  on __PUT__ requests, handled by `piston3.utils.coerce_put_post`,
  doesn't work properly
