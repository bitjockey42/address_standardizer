.. highlight:: shell

============
Docker
============

.. code-block:: console
    $ docker build -t address_standardizer .
    $ docker run -p 127.0.0.1:8080:8080/tcp -it --rm --name address_standardizer address_standardizer
