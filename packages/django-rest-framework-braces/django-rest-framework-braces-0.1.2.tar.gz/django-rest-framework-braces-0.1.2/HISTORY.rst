.. :changelog:

History
-------

0.1.2 (2015-07-02)
~~~~~~~~~~~~~~~~~~

* Added custom ``to_representation()`` to ``EmptyStringFieldMixin`` which allows to pass empty string or ``None`` values.
  This is especially useful for fields like ``IntegerField`` which would blow up when passing empty string value for non-required fields.

0.1.1 (2015-06-25)
~~~~~~~~~~~~~~~~~~

* Fixed a bug in ``FormSerializer`` which did not honor ``field_mapping`` in any of the subclasses

0.1.0 (2015-06-15)
~~~~~~~~~~~~~~~~~~

* First release on PyPI.
