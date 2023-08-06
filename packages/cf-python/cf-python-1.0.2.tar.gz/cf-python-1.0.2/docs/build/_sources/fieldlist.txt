.. currentmodule:: cf
.. default-role:: obj

.. _fs_field_list:

Introduction to the `cf.FieldList` object
=========================================

A `cf.FieldList` object is an ordered sequence of `cf.Field` objects.

It supports nearly all of the :ref:`python list-like operations
<python:typesseq-mutable>`, the exceptions being the arithmetic and
comparison operators for which it has :ref:`its own definitions
<fs-fl-a-and-c>`. For example:

>>> fl
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>,
 <CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
>>> fl[0]
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>
>>> fl[::-1]
[<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>,
 <CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>]

>>> len(fl)
2
>>> f = fl.pop()
>>> f
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>
>>> len(fl)
1
>>> fl.append(f)
>>> len(fl)
2
>>> f in fl
True
>>> from operator import attrgetter
>>> fl
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>,
 <CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
>>> fl.sort(key=attrgetter('standard_name'))
[<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>,
 <CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>]


Methods, attributes and CF properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A field list object also has all of the callable methods, reserved
attributes and reserved CF properties that a field object has. When
used with a field list, a callable method (such as
`~cf.FieldList.item`) or a reserved attribute or CF property (such as
`~cf.FieldList.Units` or `~cf.FieldList.standard_name`) is applied
independently to each field and a sequence of the results is returned.

The type of sequence that may be returned will either be a
`cf.FieldList` object or else a `cf.List` object. For example,
`cf.FieldList.subspace` will return a new field list of subspaced
fields:

>>> fl
[<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>,
 <CF Field: air_pressure(time(12), latitude(73), longitude(96)) hPa>]
>>> fl.subspace[0, ...]
[<CF Field: air_temperature(time(1), latitude(73), longitude(96)) K>,
 <CF Field: air_pressure(time(1), latitude(73), longitude(96)) hPa>]

whereas `cf.FieldList.ndim`, `cf.FieldList.standard_name` and
`cf.FieldList.dim` return a `cf.List` of integer, string and dimension
coordinate objects respectively:

>>> fl.ndim
[3, 3]
>>> fl.standard_name
['air_temperature', 'air_pressure']
>>> fl.dim('time')
[<CF DimensionCoordinate: time(12) days since 1860-1-1>,
 <CF DimensionCoordinate: time(12) days since 1860-1-1>]

A `cf.List` object is like a field list, except that it may contain
arbitrary element types (not just field objects) and so has few of the
field-specific methods which a field list has. In particular, it has a
method, called `~cf.List.method`, which allows any callable method
(with arguments) to be applied independently to each element of the
list, returning the result in a new `cf.List` object:

>>> fl.standard_name[::-1]
['air_pressure', 'air_temperature']
>>> fl.standard_name.method('upper')
['AIR_TEMPERATURE', 'AIR_PRESSURE']
>>> fl.item('time').method('getprop', 'standard_name')
['time', 'time']
>>> fl.item('time').method('delrop')
[None, None]
>>> fl.item('time').method('setprop', 'standard_name', 'foo')
[None, None]
>>> fl.item('foo').method('getprop', 'standard_name')
['foo', 'foo']

The `cf.FieldList` object also has an equivalent method called
`~cf.FieldList.method` which behaves in an analogous way, thus
reducing the need to know which type of sequence has been returned
from a field list method:

>>> fl.getprop('standard_name') == fl.method('getprop', 'standard_name')
True

Assignment to reserved attributes and CF properties assigns the value
to each field in turn. Similarly, deletion is carried out on each field:

>>> fl.standard_name
['air_pressure', 'air_temperature']
>>> fl.standard_name = 'foo'
['foo', 'foo']
>>> del fl.standard_name
>>> fl.getprop('standard_name', 'MISSING')
['MISSING', 'MISSING']

Note that the new value is not copied prior to each field assignment,
which may be an issue for values which are mutable objects.

Changes tailored to each field in the list are easily carried out in a
loop:

>>> for f in fl:
...     f.long_name = 'An even longer ' + f.long_name

.. _fs-fl-a-and-c:

Arithmetic and comparison
^^^^^^^^^^^^^^^^^^^^^^^^^

Any arithmetic and comparison operation is applied independently to
each field element, so all of the :ref:`operators defined for a field
<Arithmetic-and-comparison>` are allowed.

In particular, the usual :ref:`python list-like arithmetic and
comparison operator behaviours <python:numeric-types>` do **not**
apply. For example, the ``+`` operator will concatenate two built-in
lists, but adding ``2`` to a field list will add ``2`` to the data
array of each of its fields.

For example these commands:

>>> gl = fl + 2
>>> gl = 2 + fl
>>> gl = fl == 0
>>> fl += 2

are equivalent to:

>>> gl = cf.FieldList(f + 2 for f in fl)
>>> gl = cf.FieldList(2 + f for f in fl)
>>> gl = cf.FieldList(f == 0 for f in fl)
>>> for f in fl:
...     f += 2

Field versus field list
^^^^^^^^^^^^^^^^^^^^^^^

In some contexts, whether an object is a field or a field list is not
known. So to avoid ungainly type testing, most aspects of the
`cf.FieldList` interface are shared by a `cf.Field` object.

A field may be used in the same iterative contexts as a field list:

>>> f
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>
>>> f is f[0] is f[slice(-1, None, -1)] is f[::-1]
True
>>> for g in f:
...     print repr(g)
...
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>

When it is not known whether or not you have a field or a field list,
iterating over the output of a callable method could be complicated
because the output of the field's method will be a scalar whilst the
output of the field list's method will be a sequence of scalars. The
problem is illustrated in this example:

>>> f = fl[0]
>>> for x in f.standard_name:
...     print x+'.',
...
a.i.r._.p.r.e.s.s.u.r.e.
>>> for x in fl.standard_name:
...     print x+'.',
...
air_pressure.air_temperature.

To overcome this difficulty, both the field and field list have a
method call `!iter` which has no effect on a field list, but which
changes the output of a field's callable method (with arguments) into
a single element sequence:

>>> f = fl[0]
>>> for x in f.iter('getprop', 'standard_name'):
...     print x+'.',
...
air_pressure.
>>> for x in fl.iter('getprop', 'standard_name'):
...     print x+'.',
...
air_pressure.air_temperature.

However, it may be preferable to create a new field list to achieve
the same result:

>>> for x in cf.FieldList(f).standard_name:
...     print x+'.',
...
air_pressure.
>>> for x in cf.FieldList(fl).standard_name:
...     print x+'.',
...
air_pressure.air_temperature.
