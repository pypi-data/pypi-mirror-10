.. currentmodule:: cf
.. default-role:: obj

cf.Field
========

.. autoclass:: cf.Field
   :no-members:
   :no-inherited-members:

.. _field_cf_properties:

Field CF Properties
-------------------
 
.. autosummary::
   :toctree: ../generated/
   :template: attribute.rst

   ~cf.Field.add_offset
   ~cf.Field.calendar
   ~cf.Field.cell_methods
   ~cf.Field.comment
   ~cf.Field.Conventions
   ~cf.Field._FillValue
   ~cf.Field.flag_masks
   ~cf.Field.flag_meanings
   ~cf.Field.flag_values
   ~cf.Field.history
   ~cf.Field.institution
   ~cf.Field.leap_month
   ~cf.Field.leap_year
   ~cf.Field.long_name
   ~cf.Field.missing_value
   ~cf.Field.month_lengths
   ~cf.Field.references
   ~cf.Field.scale_factor
   ~cf.Field.source
   ~cf.Field.standard_error_multiplier
   ~cf.Field.standard_name
   ~cf.Field.title
   ~cf.Field.units
   ~cf.Field.valid_max
   ~cf.Field.valid_min
   ~cf.Field.valid_range

.. _field_attributes:

Field attributes
----------------
   
.. autosummary::
   :toctree: ../generated/
   :template: attribute.rst

   ~cf.Field.ancillary_variables
   ~cf.Field.array
   ~cf.Field.attributes
   ~cf.Field.data
   ~cf.Field.day
   ~cf.Field.domain
   ~cf.Field.dtarray
   ~cf.Field.dtvarray
   ~cf.Field.dtype
   ~cf.Field.Flags
   ~cf.Field.hardmask
   ~cf.Field.hour
   ~cf.Field.isscalar
   ~cf.Field.mask
   ~cf.Field.minute
   ~cf.Field.month
   ~cf.Field.ndim
   ~cf.Field.properties
   ~cf.Field.rank
   ~cf.Field.second
   ~cf.Field.shape
   ~cf.Field.size
   ~cf.Field.subspace
   ~cf.Field.unique
   ~cf.Field.Units
   ~cf.Field.varray
   ~cf.Field.year

.. _field_methods:

Field methods
-------------
   
.. autosummary::
   :nosignatures:
   :toctree: ../generated/
   :template: method.rst

   ~cf.Field.allclose
   ~cf.Field.anchor
   ~cf.Field.asdatetime
   ~cf.Field.asreftime
   ~cf.Field.aux
   ~cf.Field.auxs
   ~cf.Field.axes
   ~cf.Field.axes_sizes
   ~cf.Field.axis
   ~cf.Field.axis_name
   ~cf.Field.axis_size
   ~cf.Field.binary_mask
   ~cf.Field.ceil
   ~cf.Field.chunk
   ~cf.Field.clip
   ~cf.Field.close
   ~cf.Field.collapse
   ~cf.Field.coord
   ~cf.Field.coords
   ~cf.Field.copy
   ~cf.Field.cos
   ~cf.Field.cyclic
   ~cf.Field.data_axes
   ~cf.Field.datum
   ~cf.Field.delattr
   ~cf.Field.delprop
   ~cf.Field.dim
   ~cf.Field.dims
   ~cf.Field.dump
   ~cf.Field.equals
   ~cf.Field.equivalent
   ~cf.Field.equivalent_data
   ~cf.Field.equivalent_domain
   ~cf.Field.expand_dims
   ~cf.Field.fill_value
   ~cf.Field.flip
   ~cf.Field.floor
   ~cf.Field.getattr
   ~cf.Field.getprop
   ~cf.Field.hasattr
   ~cf.Field.hasprop
   ~cf.Field.identity
   ~cf.Field.indices
   ~cf.Field.insert_aux
   ~cf.Field.insert_axis
   ~cf.Field.insert_data
   ~cf.Field.insert_dim
   ~cf.Field.insert_measure
   ~cf.Field.insert_ref
   ~cf.Field.iscyclic
   ~cf.Field.item
   ~cf.Field.item_axes
   ~cf.Field.items
   ~cf.Field.items_axes
   ~cf.Field.iter
   ~cf.Field.mask_invalid
   ~cf.Field.max
   ~cf.Field.mean
   ~cf.Field.match
   ~cf.Field.measure
   ~cf.Field.measures
   ~cf.Field.method
   ~cf.Field.mid_range
   ~cf.Field.min
   ~cf.Field.name
   ~cf.Field.override_units
   ~cf.Field.period
   ~cf.Field.range
   ~cf.Field.ref
   ~cf.Field.refs
   ~cf.Field.remove_axes
   ~cf.Field.remove_axis
   ~cf.Field.remove_data
   ~cf.Field.remove_item
   ~cf.Field.remove_items
   ~cf.Field.rint
   ~cf.Field.roll
   ~cf.Field.sample_size
   ~cf.Field.sd
   ~cf.Field.select
   ~cf.Field.setattr
   ~cf.Field.setcyclic
   ~cf.Field.setprop
   ~cf.Field.sin
   ~cf.Field.sort
   ~cf.Field.squeeze
   ~cf.Field.subspace
   ~cf.Field.sum
   ~cf.Field.transpose
   ~cf.Field.trunc
   ~cf.Field.unsqueeze
   ~cf.Field.var
   ~cf.Field.weights
   ~cf.Field.where

Field class methods
-------------------

.. autosummary::
   :nosignatures:
   :toctree: ../generated/
   :template: method.rst

   ~cf.Field.concatenate

Field arithmetic and comparison operations
------------------------------------------

See the section on :ref:`arithmetic and comparison operations
<Arithmetic-and-comparison>`.

Field special methods
---------------------

**Standard library functions**

.. autosummary::
   :nosignatures:
   :toctree: generated/
   :template: method.rst

   ~cf.Field.__deepcopy__

**Container customization**

.. autosummary::
   :nosignatures:
   :toctree: generated/
   :template: method.rst

   ~cf.Field.__len__
   ~cf.Field.__getitem__ 
   ~cf.Field.__contains__

**String representations**

.. autosummary::
   :nosignatures:
   :toctree: generated/
   :template: method.rst

   ~cf.Field.__repr__
   ~cf.Field.__str__
