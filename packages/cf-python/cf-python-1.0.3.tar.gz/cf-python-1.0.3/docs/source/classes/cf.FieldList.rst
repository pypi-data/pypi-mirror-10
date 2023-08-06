.. currentmodule:: cf
.. default-role:: obj

cf.FieldList
============

.. autoclass:: cf.FieldList
   :no-members:
   :no-inherited-members:

FieldList CF Properties
-----------------------
 
.. autosummary::
   :toctree: ../generated/
   :template: attribute.rst

   ~cf.FieldList.add_offset
   ~cf.FieldList.calendar
   ~cf.FieldList.cell_methods
   ~cf.FieldList.comment
   ~cf.FieldList.Conventions
   ~cf.FieldList._FillValue
   ~cf.FieldList.flag_masks
   ~cf.FieldList.flag_meanings
   ~cf.FieldList.flag_values
   ~cf.FieldList.history
   ~cf.FieldList.institution
   ~cf.FieldList.leap_month
   ~cf.FieldList.leap_year
   ~cf.FieldList.long_name
   ~cf.FieldList.missing_value
   ~cf.FieldList.month_lengths
   ~cf.FieldList.references
   ~cf.FieldList.scale_factor
   ~cf.FieldList.source
   ~cf.FieldList.standard_error_multiplier
   ~cf.FieldList.standard_name
   ~cf.FieldList.title
   ~cf.FieldList.units
   ~cf.FieldList.valid_max
   ~cf.FieldList.valid_min
   ~cf.FieldList.valid_range


FieldList attributes
--------------------

.. autosummary::
   :toctree: ../generated/
   :template: attribute.rst

   ~cf.FieldList.ancillary_variables
   ~cf.FieldList.array
   ~cf.FieldList.attributes
   ~cf.FieldList.data
   ~cf.FieldList.day
   ~cf.FieldList.domain
   ~cf.FieldList.dtarray
   ~cf.FieldList.dtvarray
   ~cf.FieldList.dtype
   ~cf.FieldList.hardmask
   ~cf.FieldList.hour
   ~cf.FieldList.isscalar
   ~cf.FieldList.Flags
   ~cf.FieldList.mask
   ~cf.FieldList.minute
   ~cf.FieldList.month
   ~cf.FieldList.ndim
   ~cf.FieldList.properties
   ~cf.FieldList.second
   ~cf.FieldList.subspace
   ~cf.FieldList.shape
   ~cf.FieldList.size
   ~cf.FieldList.sum
   ~cf.FieldList.unique
   ~cf.FieldList.Units
   ~cf.FieldList.varray
   ~cf.FieldList.year

FieldList methods
-----------------

.. autosummary::
   :nosignatures:
   :toctree: ../generated/
   :template: method.rst

   ~cf.FieldList.all
   ~cf.FieldList.anchor
   ~cf.FieldList.any
   ~cf.FieldList.aux
   ~cf.FieldList.auxs
   ~cf.FieldList.axes
   ~cf.FieldList.binary_mask
   ~cf.FieldList.chunk
   ~cf.FieldList.clip
   ~cf.FieldList.close
   ~cf.FieldList.collapse
   ~cf.FieldList.coord
   ~cf.FieldList.coords
   ~cf.FieldList.copy
   ~cf.FieldList.cos
   ~cf.FieldList.cyclic
   ~cf.FieldList.data_axes
   ~cf.FieldList.datum
   ~cf.FieldList.delattr
   ~cf.FieldList.delprop
   ~cf.FieldList.dim
   ~cf.FieldList.dims
   ~cf.FieldList.dump
   ~cf.FieldList.equals
   ~cf.FieldList.expand_dims
   ~cf.FieldList.fill_value
   ~cf.FieldList.flip
   ~cf.FieldList.getattr
   ~cf.FieldList.getprop
   ~cf.FieldList.hasattr
   ~cf.FieldList.hasprop
   ~cf.FieldList.identity
   ~cf.FieldList.indices
   ~cf.FieldList.insert_data
   ~cf.FieldList.iscyclic
   ~cf.FieldList.item
   ~cf.FieldList.item_axes
   ~cf.FieldList.items
   ~cf.FieldList.iter
   ~cf.FieldList.mask_invalid
   ~cf.FieldList.match
   ~cf.FieldList.max
   ~cf.FieldList.measure
   ~cf.FieldList.measures
   ~cf.FieldList.method
   ~cf.FieldList.mid_range
   ~cf.FieldList.min
   ~cf.FieldList.name
   ~cf.FieldList.override_units
   ~cf.FieldList.range
   ~cf.FieldList.ref
   ~cf.FieldList.refs
   ~cf.FieldList.remove_axes
   ~cf.FieldList.remove_axis
   ~cf.FieldList.remove_data
   ~cf.FieldList.remove_item
   ~cf.FieldList.remove_items
   ~cf.FieldList.roll
   ~cf.FieldList.sample_size
   ~cf.FieldList.sd
   ~cf.FieldList.select
   ~cf.FieldList.set_equals
   ~cf.FieldList.setattr
   ~cf.FieldList.setprop
   ~cf.FieldList.sin
   ~cf.FieldList.var
   ~cf.FieldList.squeeze
   ~cf.FieldList.subspace
   ~cf.FieldList.transpose
   ~cf.FieldList.unsqueeze
   ~cf.FieldList.where

FieldList list-like methods
---------------------------

These methods provide functionality similar to that of a built-in
:py:obj:`list`.

Undocumented methods behave exactly as their counterparts in a
built-in :py:obj:`list`.

.. autosummary::
   :nosignatures:
   :toctree: ../generated/
   :template: method.rst

   ~cf.FieldList.append
   ~cf.FieldList.count
   ~cf.FieldList.extend
   ~cf.FieldList.index
   ~cf.FieldList.insert
   ~cf.FieldList.pop
   ~cf.FieldList.reverse
   ~cf.FieldList.sort

FieldList arithmetic and comparison operations
----------------------------------------------

Any arithmetic, bitwise or comparison operation is applied
independently to each field element, so all of :ref:`operators defined
for a field <Arithmetic-and-comparison>` are allowed.

In particular, the usual list-like operator behaviours do not
apply. For example, the ``+`` operator will concatenate two built-in
lists, but adding ``2`` to a field list will add ``2`` to the data
array of each of its fields.
