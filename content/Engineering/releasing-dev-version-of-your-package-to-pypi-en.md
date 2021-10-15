Title: Releasing dev version of your package to PyPI
Date: 2012-03-20 08:50
Author: Kamal Mustafa
Tags:  python; tool; developer; 2012;
Slug: releasing-dev-version-of-your-package-to-pypi
Lang: en
Summary: release dev version of your package to PyPI

[PyPI](http://pypi.python.org/pypi) (Python Package Index) has become a
central place for python developers these days to look for third party
libraries. Common tools such as easy\_install, pip or buildout by
default will look into [PyPI](http://pypi.python.org/pypi) when asked to
install certain packages. For example:-

    easy_install Django
    easy_install Django==1.3.1
    pip install Django
    pip install Django==1.2.4

all those commands above will either install the latest stable release
of Django or an exact version as specified as argument to the command.
For our own mamopublic
package, I'd plan to also release it on
[PyPI](http://pypi.python.org/pypi) so it more inline with other third
party libraries that we need to install as part of our project
dependencies. The process actually pretty straightforward, once you have
sign up and get your username and password, all you have to do is from
your package root:-

    python setup.py register # this will register the package name on pypi
    python setup.py sdist upload

It will ask you to save the username and password in `~/.pypirc` so you
don't have to  
type username and password everytime you want to upload to
[PyPI](http://pypi.python.org/pypi). Now I can install
mamopublic simpy by just
typing `easy_install mamopublic`. That will grab the tarball from
[PyPI](http://pypi.python.org/pypi) website. There's always a case that
I want to install the latest code from our github commit. I have seen
lot of packages on [PyPI](http://pypi.python.org/pypi) that allow us to
install their latest dev release using command such as:-

    easy_install django-nose==dev

Looking around in setuptools/distribute documentation, I didn't found
any settings for `setup.py` that allow us to specify the url to download
the package instead from [PyPI](http://pypi.python.org/pypi)'s tarball.
Finally, checking package edit page on PyPI I noticed that there's an
input field for download url. So what I did was to change the version in
setup.py to 'dev' instead of '1.8' and then upload it to PyPI. Since
'dev' version not exists yet, PyPI happily accept that. PyPI apparently
refused to accept upload of package of similar version. You have to bump
the version number or delete the package from PyPI first. Then I went to
the package edit page and specified the download url pointing to github
generated tarball from latest commit.

Now it's possible to install our latest commit simply by using
`easy_install -U mamopublic==dev`.
