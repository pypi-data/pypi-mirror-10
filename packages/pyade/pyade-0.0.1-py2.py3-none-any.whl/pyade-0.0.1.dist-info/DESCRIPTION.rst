|Build Status| |Documentation Status|

pyade
=====

A minimal Python class to use ADE Web API for ADE Planning from
`Adesoft <http://www.adesoft.com/>`__.

This is an unofficial development. I am in no way related to this
company. Use it at your own risk.

WORK IN PROGRESS

Usage
-----

Command Line Interface script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You might first define 3 environment variables.

::

    export ADE_WEB_API_URL="https://server/jsp/webapi"
    export ADE_WEB_API_LOGIN="user_login"
    export ADE_WEB_API_PASSWORD="user_password" 

Than you can run sample using:

::

    $ python sample/main.py

You can also pass url, login, password as optional parameters of command
line interface using:

::

    $ python sample/main.py --url https://server/jsp/webapi --user user_login --password user_password

Interactive usage
~~~~~~~~~~~~~~~~~

Run IPython using:

::

    $ ipython

You can use interactively this class

::

    In [1]: from pyade import ADEWebAPI, Config

    In [2]: import logging

    In [3]: logging.basicConfig(level=logging.DEBUG)

    In [4]: config = Config.create()

You can safely display config in a console, your password will not
appear.

::

    In [5]: config
    Out[5]:
    <Config {'url': 'https://server/jsp/webapi', 'login': 'user_login', 'password': '*********'}>

But you can access to any key like a dict. For example:

::

    In [6]: config['url']
    Out[6]: 'https://server/jsp/webapi'

Config can be unpacked using ``**`` operator and use as parameter for
``ADEWebAPI`` constructor.

::

    In [7]: myade = ADEWebAPI(**config)

You can display methods of ADEWebAPI using "." and tab key

::

    In [8]: myade.
    myade.connect                 myade.getActivities           myade.getProjects             myade.opt_params
    myade.create_list_of_objects  myade.getCaracteristics       myade.getResources            myade.password
    myade.disconnect              myade.getCosts                myade.hide_dict_values        myade.sessionId
    myade.exception_factory       myade.getDate                 myade.logger                  myade.setProject
    myade.factory                 myade.getEvents               myade.login                   myade.url

Docstring can be print using "?"

::

    In [8]: ?myade.connect
    Signature: myade.connect()
    Docstring: Connect to server
    File:      ~/pyade/pyade/__init__.py
    Type:      instancemethod

Let's connect to server (using url, login and password)

::

    In [9]: myade.connect()
    DEBUG:ADEWebAPI:send {'function': 'connect', 'login': 'user_login', 'password': '*********', 'sessionId': '14cef8679e2'}
    INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): server
    DEBUG:requests.packages.urllib3.connectionpool:"GET /jsp/webapi?function=connect&login=user_login&password=user_password&sessionId=14cef8679e2 HTTP/1.1" 200 None
    DEBUG:ADEWebAPI:<Response [200]>
    DEBUG:ADEWebAPI:<?xml version="1.0" encoding="UTF-8"?>
    <session id="14cef878c17"/>

    Out[9]: True

A list of dict describing projects can be given using:

::

    In [10]: myade.getProjects()
    DEBUG:ADEWebAPI:send {'function': 'getProjects', 'sessionId': '14cef8679e2'}
    INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): server
    DEBUG:requests.packages.urllib3.connectionpool:"GET /jsp/webapi?function=getProjects&sessionId=14cef8679e2 HTTP/1.1" 200 None
    DEBUG:ADEWebAPI:<Response [200]>
    DEBUG:ADEWebAPI:<?xml version="1.0" encoding="UTF-8"?>
    <projects>
        <project id="6"/>
        <project id="5"/>
    </projects>

    Out[10]: [{'id': '6'}, {'id': '5'}]

You can also use optional parameters such as ``detail``,
``myade.getProjects(detail=4)``

::

    In [11]: myade.getProjects(detail=4)
    DEBUG:ADEWebAPI:send {'function': 'getProjects', 'sessionId': '14cef8679e2', 'detail': 4}
    INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): server
    DEBUG:requests.packages.urllib3.connectionpool:"GET /jsp/webapi?function=getProjects&sessionId=14cef8679e2&detail=4 HTTP/1.1" 200 None
    DEBUG:ADEWebAPI:<Response [200]>
    DEBUG:ADEWebAPI:<?xml version="1.0" encoding="UTF-8"?>
    <projects>
        <project id="6" name="2015-2016" uid="1428406688761" version="600" loaded="true"/>
        <project id="5" name="2014-2015" uid="1364884711514" version="520" loaded="true"/>
    </projects>

    Out[11]:
    [{'id': '6',
      'loaded': 'true',
      'name': '2015-2016',
      'uid': '1428406688761',
      'version': '600'},
     {'id': '5',
      'loaded': 'true',
      'name': '2014-2015',
      'uid': '1364884711514',
      'version': '520'}]

You can set ``myade`` instance of class ``ADEWebAPI`` in order methods
output list of objects instead of list of dictionaries

::

    In [12]: myade.create_list_of_objects(True)

    In [13]: myade.getProjects()
    DEBUG:ADEWebAPI:send {'function': 'getProjects', 'sessionId': '14cef8679e2'}
    INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): server
    DEBUG:requests.packages.urllib3.connectionpool:"GET /jsp/webapi?function=getProjects&sessionId=14cef8679e2 HTTP/1.1" 200 None
    DEBUG:ADEWebAPI:<Response [200]>
    DEBUG:ADEWebAPI:<?xml version="1.0" encoding="UTF-8"?>
    <projects>
        <project id="6"/>
        <project id="5"/>
    </projects>

    Out[13]:
    [Project({'id': '6'}),
     Project({'id': '5'})]

Set current project

::

    In [14]: myade.setProject(5)
    Out[14]: True

...

Don't forget to disconnect from server before quitting.

::

    In [15]: myade.disconnect()
    DEBUG:ADEWebAPI:send {'function': 'disconnect', 'sessionId': '14cef8679e2'}
    INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): server
    DEBUG:requests.packages.urllib3.connectionpool:"GET /jsp/webapi?function=disconnect&sessionId=14cef8679e2 HTTP/1.1" 200 None
    DEBUG:ADEWebAPI:<Response [200]>
    DEBUG:ADEWebAPI:<?xml version="1.0" encoding="UTF-8"?>
    <disconnected sessionId="14cef8679e2"/>

    Out[15]: True

.. |Build Status| image:: https://travis-ci.org/scls19fr/pyade.svg
   :target: https://travis-ci.org/scls19fr/pyade
.. |Documentation Status| image:: https://readthedocs.org/projects/pyade/badge/?version=latest
   :target: http://pyade.readthedocs.org/en/latest/


