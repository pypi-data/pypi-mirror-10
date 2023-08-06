.. currentmodule:: cf
.. default-role:: obj

.. _class:

Classes of the :mod:`cf` module
===============================

Field classes
-------------

.. autosummary::
   :nosignatures:
   :toctree: classes/

   cf.Field		              
   cf.FieldList		              

Field component classes
-----------------------

.. autosummary::
   :nosignatures:
   :toctree: classes/

   cf.AncillaryVariables
   cf.AuxiliaryCoordinate
   cf.CellMeasure
   cf.CellMethods
   cf.CoordinateBounds
   cf.CoordinateReference
   cf.Data
   cf.DimensionCoordinate
   cf.Domain
   cf.Flags
   cf.Units

Miscellaneous classes
---------------------

.. autosummary::
   :nosignatures:
   :toctree: classes/

   cf.Datetime
   cf.Query
   cf.TimeDuration

Base classes
------------

.. autosummary::
   :nosignatures:
   :toctree: classes/
         
   cf.Coordinate
   cf.Dict       
   cf.List
   cf.Variable       

.. comment
   Data component classes
   ----------------------
   
   .. autosummary::
      :nosignatures:
      :toctree: classes/
   
      cf.Partition
      cf.PartitionMatrix


.. _inheritance_diagrams:

Inheritance diagrams
--------------------

The classes defined by the `cf` package inherit as follows:

----

.. image:: images/inheritance1.png

.. commented out
   .. inheritance-diagram:: cf.Domain
                            cf.Data
                            cf.Flags	
                            cf.Units
                            cf.Datetime
                            cf.TimeDuration
                            cf.Query
      :parts: 1

----

.. image:: images/inheritance2.png

.. commented out
   .. inheritance-diagram:: cf.CoordinateBounds
      			 cf.AuxiliaryCoordinate
                            cf.DimensionCoordinate
                            cf.Field
                            cf.CellMeasure
      :parts: 1

----

.. image:: images/inheritance3.png

.. commented out
   .. inheritance-diagram:: cf.FieldList
            		 cf.AncillaryVariables
                            cf.CellMethods
            		 cf.CoordinateReference
      :parts: 1

----

This inheritance diagrams show, for example:

* `cf.Field` and `cf.DimensionCoordinate` objects have all of the
  features of a `cf.Variable` object, e.g. they may have a data array
  and CF properties.

* `cf.FieldList` objects are mutable, :ref:`iterable
  <python:typeiter>` objects.

* `cf.CoordinateReference` objects are mutable, :ref:`mapping
  <python:typesmapping>` objects.
