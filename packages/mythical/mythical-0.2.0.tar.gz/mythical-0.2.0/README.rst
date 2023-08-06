============
mythical-client
============

.. image:: https://magnum.travis-ci.com/verygoodgroup/mythical-client.svg?token=ykTaJtscxcuMJxYq2Nt5&branch=travis
   :target: https://magnum.travis-ci.com/verygoodgroup/mythical-client

test
====

.. code:: bash

   $ git clone git@github.com:verygoodgroup/mythical-client.git
   $ cd mythical-client
   $ git submodule update --init --recursive
   $ mkvirtualenv mythical-client
   (mythical-client)$ pip install -e .[tests]
   (mythical-client)$ export \
   MYTHICAL_SUITE_ROOT=https://mythical-test-4w3ebo.vgs.io \
   MYTHICAL_SUITE_USERNAME=company \
   MYTHICAL_SUITE_PASSWORD=password
   (mythical-client)$ py.test suite.py --cov=mythical

suite
=====

If you have many suite targets (e.g. test, local, proxied, etc.) dump them in
``~/.mythical`` like e.g.:

.. code:: bash

   $ cat <<EOF >> ~/.mythical
   
   [suite:dev]
   http_root=https://vault-all-dev-b6oy83-mythical-http.noxious.io
   sftp_host=vault-all-dev-b6oy83-mythical-sftp.noxious.io
   sftp_port=8022
   username=travis-057e4f1be6c742cc876af9d8cdc74981
   password=xxxxxxxxxxxxxxxxxxx
   
   EOF

and target them like:

.. code:: bash

   (mythical-client)$ MYTHICAL_SUITE=dev py.test suite.py
   ...

proxy
=====

To route through a `token proxy <https://github.com/verygood/vault>`_ install the client:

.. code:: bash

   (mythical-client)$ pip install vault

setup a target:

.. code:: bash

   (mythical-client)$ cat <<EOF >> ~/.mythical
   
   [suite:dev-proxy]
   http_root=https://mythical-LoadBala-1RZB12W0TY5A0-1578257076.us-west-2.elb.amazonaws.com
   sftp_host=mythical-LoadBala-1RZB12W0TY5A0-1578257076.us-west-2.elb.amazonaws.com
   sftp_port=8022
   username=vault
   password=vaultvault
   tokenize=
       import vault
   
       token_key = """\
       -----BEGIN PUBLIC KEY-----
       MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFJEBRUTO6URKuJYboKeSeYYIa
       a4AE4zN/bZg/q+F/6y9mODqUC8Ldye6M4a+rSSC8ilVJ7UuLGnVGUztg9VVpBdt5
       a1WTpvf4VnyqSkKhQkQ95La7y98FDm8HEI5DZvSlROG39fdyUfTl9PDlEfK9nf40
       jQmoXIeRgEF9l2LFiwIDAQAB
       -----END PUBLIC KEY-----\
       """
   
       token_version = '0'
   
       tokenize = vault.ephemeral.InlineTokenizer.from_config(
           vault.ephemeral.InlineTokenizer.Config(
               key=token_key, version=token_version
       ))
   
   EOF

and test:

.. code:: bash

   (mythical-client)$ MYTHICAL_SUITE=dev-proxy py.test suite.py
