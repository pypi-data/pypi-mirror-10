autodock-hipache
================

Hipache Plugin for autodock.

.. note:: See: `autodock <https://github.com/prologic/autodock>`_

Basic Usage
-----------

Start the daemon::
    
    $ docker run -d --name autodock prologic/autodock

Link and start the autodock Hipache Plugin::
    
    $ docker run -d --link autodock prologic/autodock-hipache

Now whenever you start a new container autodock will listen for Docker events
and discover containers that have been started. The ``autodock-hipache`` plugin
will specifically listen for starting containers that have a ``VIRTUALHOST``
environment variable and reconfigure the running ``hipache`` container.

Start a "Hello World" Web Application::
    
    $ docker run -d -e VIRTUALHOST=hello.local prologic/hello

Now assuming you had ``hello.local`` configured in your ``/etc/hosts``
pointing to your ``hipache`` container you can now visit http://hello.local/

::
    
    echo "127.0.0.1 hello.local" >> /etc/hosts
    curl -q -o - http://hello.local/
    Hello World!

.. note:: This method of hosting and managing webapps and websites is in production deployments and talked about in more detail in the post `A Docker-based mini-PaaS <http://shortcircuit.net.au/~prologic/blog/article/2015/03/24/a-docker-based-mini-paas/>`_.

``docker-compose.yml``:

.. code:: yaml

    autodock:
        image: prologic/autodock
        ports:
            - "1338:1338/udp"
            - "1338:1338/tcp"
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock

    autodockhipache:
        image: prologic/autodock-hipache
        links:
            - autodock
            - hipache:redis

    hello:
        image: prologic/hello
        environment:
            - VIRTUALHOST=hello.local

    hipache:
        image: hipache
        ports:
            - 80:80
            - 443:443
