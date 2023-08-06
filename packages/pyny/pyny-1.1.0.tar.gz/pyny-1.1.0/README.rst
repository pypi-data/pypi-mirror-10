====
pyny
====

.. image:: https://travis-ci.org/7pairs/pyny.svg?branch=master
   :target: https://travis-ci.org/7pairs/pyny

.. image:: https://coveralls.io/repos/7pairs/pyny/badge.svg?branch=master
   :target: https://coveralls.io/r/7pairs/pyny?branch=master

Sample
------

::

   >>> from pyny import api
   >>> data = api.get_by_id('c1161', 2)
   >>>
   >>> import pprint
   >>> p = pprint.PrettyPrinter()
   >>> p.pprint(data)
   {'attrs': {'attr0': '市役所・出張所',
              'attr1': '出張所',
              'attr2': 'おおたかの森出張所',
              'attr3': '流山市西初石6-185-2（流山おおたかの森S・C内3階）',
              'attr6': '35.8706965',
              'attr7': '139.9261438',
              'attr8': '04-7154-0333 '},
    'created': '2013/07/19 17:01:02',
    'distance': 0,
    'feature_id': 2,
    'files': {},
    'geometry': 'POINT(139.9261438 35.8706965)',
    'layer_id': 'c1161',
    'mid': 0,
    'moduserid': 0,
    'status': 0,
    'user_id': 307}
   >>>
   >>> from pyny.models import Model
   >>> from pyny.fields import DecimalField, StringField
   >>>
   >>> class SampleModel(Model):
   ...     layer_id = StringField()
   ...     longitude = DecimalField('attrs.attr7')
   ...
   >>> data = SampleModel.get_by_id('c1161', 2)
   >>> data.layer_id
   'c1161'
   >>> data.longitude
   Decimal('139.9261438')
   >>>

Documentation
-------------

https://github.com/7pairs/pyny/blob/master/docs/usage.md
