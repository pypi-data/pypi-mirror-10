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
   >>> api.get_data('c1161', 2)
   {'feature_id': 2, 'mid': 0, 'layer_id': 'c1161', 'user_id': 307, 'status': 0, 'moduserid': 0, 'created': '2013/07/19 17:01:02', 'attrs': {'attr6': '35.8706965', 'attr8': '04-7154-0333 ', 'attr3': '流山市西初石6-185-2（流山おおたかの森S・C内3階）', 'attr7': '139.9261438', 'attr1': '出張所', 'attr0': '市役所・出張所', 'attr2': 'おおたかの森出張所'}, 'geometry': 'POINT(139.9261438 35.8706965)', 'files': {}, 'distance': 0}
   >>>
   >>> from pyny.models import Model
   >>> from pyny.fields import DecimalField, StringField
   >>>
   >>> class SampleModel(Model):
   ...     layer_id = StringField()
   ...     longitude = DecimalField('attrs.attr7')
   ...
   >>> data = SampleModel.get_data('c1161', 2)
   >>> data.layer_id
   'c1161'
   >>> data.longitude
   Decimal('139.9261438')
   >>>

Documentation
-------------

https://github.com/7pairs/pyny/blob/master/docs/usage.md


