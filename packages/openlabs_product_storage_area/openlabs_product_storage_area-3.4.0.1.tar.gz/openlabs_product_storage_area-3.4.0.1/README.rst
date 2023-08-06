trytond-product-storage-area
============================

This module provides a light weight way of knowing (not tracking) where
your inventory is in a warehouse.

When should I use this module ?
-------------------------------

* You want to know where products are (usually) located in your warehouse.
* You do not want to spend the time and energy to keep track of and move
  products at the bin level.

What are the alternatives ?
---------------------------

Tryton ``stock`` module comes built in with powerful locations feature
where you can have infinite depth on stock levels. You could create each
bin in your warehouse and track inventory for each of those bins.

The ``stock_product_location`` module allows you to specify preferred
locations for products in your warehouse helping you move products in and
out of the right bins (or aisles).

So why build this module ?
--------------------------

From our experience, tracking and managing inventory at the bin level
often requires dedicated man power and man hours to stay accurate. Small
businesses may not want to invest time into this, but may want to keep
track of where products are usually kept in the warehouse. This
information can help the new picker find the product and the restocker to
put the product in the right place, instead of spreading it around the
warehouse.

So, this module gives a light weight option where you can create ``storage
areas`` and tag them with products. The picking list report provided in
the module respects the sequence of the ``storage area`` and mentions it
in the report so it is easy for the picker.

I want to know more!
--------------------

Holler at us at the contact information below. You can also find us on the
``#tryton`` IRC channel.

Authors and Contributors
------------------------

This module was built at `Openlabs <http://www.openlabs.co.in>`_. 

Professional Support
--------------------

This module is professionally supported by `Openlabs <http://www.openlabs.co.in>`_.
If you are looking for on-site teaching or consulting support, contact our
`sales <mailto:sales@openlabs.co.in>`_ and `support
<mailto:support@openlabs.co.in>`_ teams.

