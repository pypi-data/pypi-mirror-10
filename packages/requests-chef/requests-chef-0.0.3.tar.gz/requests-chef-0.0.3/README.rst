requests-chef
=============

| |latest|
| `Chef auth <https://docs.chef.io/auth.html#authentication-headers>`__
  support for Python-Requests

.. code:: python

    import requests_chef

    auth = requests_chef.ChefAuth('chef-user', '~/chef-user.pem')
    response = requests.get('https://api.chef.io/users/chef-user',
                            headers={'X-Chef-Version': '12.0.2'},
                            auth=auth)
    response.json()
        {'display_name': 'chef-user',
         'email': 'chef-user@example.com',
         'first_name': 'Chef',
         'last_name': 'User',
         'middle_name': '',
         'public_key': '-----BEGIN PUBLIC KEY-----\nMIIBIj...IDAQAB\n-----END PUBLIC KEY-----\n',
         'username': 'chef-user'}

.. |latest| image:: https://img.shields.io/pypi/v/requests-chef.svg
   :target: https://pypi.python.org/pypi/requests-chef
