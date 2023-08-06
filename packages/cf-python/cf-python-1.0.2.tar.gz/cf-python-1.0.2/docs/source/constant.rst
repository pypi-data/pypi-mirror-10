.. currentmodule:: cf

Constants of the :mod:`cf` module
=================================

.. data:: cf.masked

    The :attr:`cf.masked` constant allows data array values to be
    masked by direct assignment. This is consistent with the
    :ref:`behaviour of numpy masked arrays
    <numpy:maskedarray.generic.constructing>`.

    For example, one way of masking every element of a field's data
    array is:

    >>> f.subspace[...] = cf.masked

    To mask every element of a field's data array whose value is less
    than zero:
    
    >>> f.setdata(cf.masked, None, f<0)

    .. seealso:: `cf.Field.hardmask`, `cf.Field.setdata`,
                 `cf.Field.subspace`
