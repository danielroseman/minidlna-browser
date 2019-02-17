miniDLNA Database Browser - Flask app
===========

A basic Flask app to browse the contents of a miniDLNA database

Installation
------------

First you need to install some dependencies:

```

    # Debian Wheezy 
    $ sudo apt-get install python2.7 python2.7-minimal python2.7-dev python-pkg-resources python-setuptools build-essentials python-pip

    # Optionally if pip install fails, change some lines in the python code of pip, to define HTTPS as primary way of connection
    # See the patch below

    $ sudo pip install flask
    $ sudo pip install jinja2-ospath

```


** http2https.patch **

```
diff -Naur /usr/share/pyshared/pip/commands/install.py /usr/share/pyshared/pip/commands/install.py
--- /usr/share/pyshared/pip/commands/install.py    2012-02-16 20:55:20.000000000 +0100
+++ /usr/share/pyshared/pip/commands/install.py    2019-02-17 15:54:36.000000000 +0100
@@ -49,7 +49,7 @@
             '-i', '--index-url', '--pypi-url',
             dest='index_url',
             metavar='URL',
-            default='http://pypi.python.org/simple/',
+            default='https://pypi.python.org/simple/',
             help='Base URL of Python Package Index (default %default)')
         self.parser.add_option(
             '--extra-index-url',
diff -Naur /usr/share/pyshared/pip/commands/search.py /usr/share/pyshared/pip/commands/search.py
--- /usr/share/pyshared/pip/commands/search.py     2012-01-20 14:15:47.000000000 +0100
+++ /usr/share/pyshared/pip/commands/search.py     2019-02-17 15:55:23.000000000 +0100
@@ -22,7 +22,7 @@
             '--index',
             dest='index',
             metavar='URL',
-            default='http://pypi.python.org/pypi',
+            default='https://pypi.python.org/pypi',
             help='Base URL of Python Package Index (default %default)')

     def run(self, options, args):
diff -Naur /usr/share/pyshared/pip/index.py /usr/share/pyshared/pip/index.py
--- /usr/share/pyshared/pip/index.py       2012-02-16 20:55:20.000000000 +0100
+++ /usr/share/pyshared/pip/index.py       2019-02-17 15:56:07.000000000 +0100
@@ -347,7 +347,7 @@
         for mirror_url in mirrors:
             # Make sure we have a valid URL
             if not ("http://" or "https://" or "file://") in mirror_url:
-                mirror_url = "http://%s" % mirror_url
+                mirror_url = "https://%s" % mirror_url
             if not mirror_url.endswith("/simple"):
                 mirror_url = "%s/simple/" % mirror_url
             mirror_urls.add(mirror_url)

```


To run **minidlna-database-browser** change the values in **minidlna-database-browser.cfg** to your personal settings, and start the app:

```
    $ export BROWSER_APP_SETTINGS='./minidlna-database-browser.cfg'; python ./browser.py
```

