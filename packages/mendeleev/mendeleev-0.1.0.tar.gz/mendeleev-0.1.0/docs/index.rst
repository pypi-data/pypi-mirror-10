====================================
Welcome to mendeleev's documentation
====================================

This package provides an API for accessing various properties of elements from
the periodic table of elements.

Data
====

The followig data is currently avaialble:

+-----------------------+-------+-------------------------------------+-------------+
| Name                  | Type  | Comment                             | Data Source |
+=======================+=======+=====================================+=============+
| annotation            | str   | Annotations regarding ithe data     |             |
+-----------------------+-------+-------------------------------------+-------------+
| atomic_number         | int   | Atomic number                       |             |
+-----------------------+-------+-------------------------------------+-------------+
| atomic_radius         | float | Atomic radius in pm                 |             |
+-----------------------+-------+-------------------------------------+-------------+
| atomic_volume         | float | Atomic volume in cm3/mol            |             |
+-----------------------+-------+-------------------------------------+-------------+
| block                 | int   | Block in periodic table             |             |
+-----------------------+-------+-------------------------------------+-------------+
| boiling_point         | float | Boiling temperature in K            |             |
+-----------------------+-------+-------------------------------------+-------------+
| covalent_radius       | float | Covalent radius in pm               |             |
+-----------------------+-------+-------------------------------------+-------------+
| density               | float | Density at 295K in g/cm3            |             |
+-----------------------+-------+-------------------------------------+-------------+
| description           | str   | Short description of the element    |             |
+-----------------------+-------+-------------------------------------+-------------+
| dipole_polarizability | float | Dipole polarizability in a.u.       | [1]_        |
+-----------------------+-------+-------------------------------------+-------------+
| electron_affinity     | float | Electron affinity in eV             |             |
+-----------------------+-------+-------------------------------------+-------------+
| electronegativity     | float | Electronegativity (Pauling scale)   |             |
+-----------------------+-------+-------------------------------------+-------------+
| econf                 | str   | Ground state electron configuration |             |
+-----------------------+-------+-------------------------------------+-------------+
| evaporation_heat      | float | Evaporation heat in kJ/mol          |             |
+-----------------------+-------+-------------------------------------+-------------+
| fusion_heat           | float | Fusion heat in kJ/mol               |             |
+-----------------------+-------+-------------------------------------+-------------+
| group                 | int   | Group in periodic table             |             |
+-----------------------+-------+-------------------------------------+-------------+
| ionenergy             | tuple | Ionization energies in eV           | [2]_        |
+-----------------------+-------+-------------------------------------+-------------+
| ionic_radii           | list  | Ionic radii                         | [3]_        |
+-----------------------+-------+-------------------------------------+-------------+
| isotopes              | list  | Isotopes                            |             |
+-----------------------+-------+-------------------------------------+-------------+
| lattice_constant      | float | Lattice constant in Angstrom        |             |
+-----------------------+-------+-------------------------------------+-------------+
| lattice_structure     | str   | Lattice structure code              |             |
+-----------------------+-------+-------------------------------------+-------------+
| mass                  | float | Relative atomic mass.               |             |
+-----------------------+-------+-------------------------------------+-------------+
| melting_point         | float | Melting temperature in K            |             |
+-----------------------+-------+-------------------------------------+-------------+
| name                  | str   | Name in english                     |             |
+-----------------------+-------+-------------------------------------+-------------+
| oxistates             | list  | Oxidation states                    |             |
+-----------------------+-------+-------------------------------------+-------------+
| period                | int   | Period in periodic table            |             |
+-----------------------+-------+-------------------------------------+-------------+
| series                | int   | Index to chemical series            |             |
+-----------------------+-------+-------------------------------------+-------------+
| specific_heat         | float | Specific heat in J/g mol @ 20 C     |             |
+-----------------------+-------+-------------------------------------+-------------+
| symbol                | str   | Chemical symbol                     |             |
+-----------------------+-------+-------------------------------------+-------------+
| thermal_conductivity  | float | Thermal conductivity in @/m K @25 C |             |
+-----------------------+-------+-------------------------------------+-------------+
| vdw_radius            | float | Van der Waals radius in pm          |             |
+-----------------------+-------+-------------------------------------+-------------+

.. [1] P. Schwerdtfeger "Table of experimental and calculated static dipole
   polarizabilities for the electronic ground states of the neutral elements
   (in atomic units)", February 11, 2014 `source <http://ctcp.massey.ac.nz/Tablepol2014.pdf>`_
.. [2] `NIST Atomic Database <http://physics.nist.gov/cgi-bin/ASD/ie.pl>`_
   accessed on April 13, 2015
.. [3] Shannon, R. D. (1976). Revised effective ionic radii and systematic
   studies of interatomic distances in halides and chalcogenides.
   Acta Crystallographica Section A.
   `doi:10.1107/S0567739476001551 <http://www.dx.doi.org/10.1107/S0567739476001551>`_



Installation
============

The package can be installed using `pip <https://pypi.python.org/pypi/pip>`_

.. code-block:: bash

   pip install mendeleev

You can also install the most recent version from the repository:

.. code-block:: bash

   pip install https://bitbucket.org/lukaszmentel/mendeleev/get/tip.tar.gz

Usage
=====

The simple interface to the data is through the ``element`` method that returns
the ``Element`` objects::

   >>> from mendeleev import element

The ``element`` method accepts unique identifiers: atomic number, atomic
symbol or element's name in english. To retrieve the entries on Silicon by
symbol type

.. code-block:: python

   >>> si = element('Si')
   >>> si
   Element(
	    annotation=u'',
   	    atomic_number=14,
 	 	atomic_radius=132.0,
 	 	atomic_volume=12.1,
 	 	block=u'p',
 	 	boiling_point=2628.0,
 	 	covalent_radius=111.0,
 	 	density=2.33,
 	 	description=u"Metalloid element belonging to group 14 of the periodic table. It is the second most abundant element in the Earth's crust, making up 25.7% of it by weight. Chemically less reactive than carbon. First identified by Lavoisier in 1787 and first isolated in 1823 by Berzelius.",
 	 	dipole_polarizability=37.31,
 	 	electron_affinity=1.389521,
 	 	electronegativity=1.9,
 	 	electronic_configuration=u'[Ne] 3s2 3p2',
 	 	evaporation_heat=383.0,
 	 	fusion_heat=50.6,
 	 	group_id=14,
 	 	lattice_constant=5.43,
 	 	lattice_structure=u'DIA',
 	 	mass=28.0855,
 	 	melting_point=u'1683',
 	 	name=u'Silicon',
 	 	period=3,
 	 	specific_heat=0.703,
 	 	symbol=u'Si',
 	 	thermal_conductivity=149.0,
 	 	vdw_radius=210.0,
   )

Similarly to access the data by atomic number or element names type

.. code-block:: python

   >>> al = element(13)
   >>> al.name
   'Aluminium'
   >>> o = element('Oxygen')
   >>> o.atomic_number
   8

Lists of elements
-----------------

The ``element`` method also accepts list or tuple  of identifiers and then
returns a list of ``Element`` objects

.. code-block:: python

   >>> c, h, o = element(['C', 'Hydrogen', 8])
   >>> c.name, h.name, o.name
   ('Carbon', 'Hydrogen', 'Oxygen')

Composite Attributes
--------------------

Currently four of the attributes are more complex object than ``str``, ``int``
or ``float``, those are:

* ``oxistates``, returns a list of oxidation states
* ``ionenergies``, returns a dictionary of ionization energies
* ``isotopes``, returns a list of ``Isotope`` objects
* ``ionic_radii`` returns a list of ``IonicRadius`` objects

Oxidation states
++++++++++++++++

For examples ``oxistates`` returns a list of oxidation states for
a given element

.. code-block:: python

   >>> fe = element('Fe')
   >>> fe.oxistates
   [6, 3, 2, 0, -2]

Ionization energies
+++++++++++++++++++

The ``ionenergies`` returns a dictionary with ionization energies as values and
degrees of ionization as keys.

.. code-block:: python

   >>> fe = element('Fe')
   >>> fe.ionenergies
   {1: 7.9024678,
    2: 16.1992,
    3: 30.651,
    4: 54.91,
    5: 75.0,
    6: 98.985,
    7: 125.0,
    8: 151.06,
    9: 233.6,
    10: 262.1,
    11: 290.9,
    12: 330.81,
    13: 361.0,
    14: 392.2,
    15: 456.2,
    16: 489.312,
    17: 1262.7,
    18: 1357.8,
    19: 1460.0,
    20: 1575.6,
    21: 1687.0,
    22: 1798.43,
    23: 1950.4,
    24: 2045.759,
    25: 8828.1875,
    26: 9277.681}

Isotopes
++++++++

The ``isotopes`` attribute returns a list of ``Isotope`` objects with the
following attributes per isotope

* ``atomic_number``
* ``mass``
* ``abundance``
* ``mass_number``

.. code-block:: python

   >>> fe = element('Fe')
   >>> for iso in fe.isotopes:
   ...     print(iso)
    26   55.93494  91.75%    56
    26   56.93540   2.12%    57
    26   57.93328   0.28%    58
    26   53.93961   5.85%    54

The columns represent the attributes ``atomic_number``, ``mass``,
``abundance`` and ``mass_number`` respectively.

Ionic radii
+++++++++++

Another composite attribute is ``ionic_radii`` which returns a list of
``IonicRadius`` object with the following attributes

* ``atomic_number``, atomic number of the ion
* ``charge``, charge of the ion
* ``econf``, electronic configuration of the ion
* ``coordination``, coordination type of the ion
* ``spin``, spin state of the ion (*HS* or *LS*)
* ``crystal_radius``
* ``ionic_radius``
* ``origin``, source of the data
* ``most_reliable``, recommended value

.. code-block:: python

   >>> fe = element('Fe')
   >>> for ir in fe.ionic_radii:
   ...     print(ir)
   charge=   2, coordination=IV   , crystal_radius= 0.770, ionic_radius= 0.630
   charge=   2, coordination=IVSQ , crystal_radius= 0.780, ionic_radius= 0.640
   charge=   2, coordination=VI   , crystal_radius= 0.750, ionic_radius= 0.610
   charge=   2, coordination=VI   , crystal_radius= 0.920, ionic_radius= 0.780
   charge=   2, coordination=VIII , crystal_radius= 1.060, ionic_radius= 0.920
   charge=   3, coordination=IV   , crystal_radius= 0.630, ionic_radius= 0.490
   charge=   3, coordination=V    , crystal_radius= 0.720, ionic_radius= 0.580
   charge=   3, coordination=VI   , crystal_radius= 0.690, ionic_radius= 0.550
   charge=   3, coordination=VI   , crystal_radius= 0.785, ionic_radius= 0.645
   charge=   3, coordination=VIII , crystal_radius= 0.920, ionic_radius= 0.780
   charge=   4, coordination=VI   , crystal_radius= 0.725, ionic_radius= 0.585
   charge=   6, coordination=IV   , crystal_radius= 0.390, ionic_radius= 0.250

API
===

.. toctree::
   :maxdepth: 2

   Module Reference <_reference/modules>

License
=======

.. literalinclude:: ../LICENSE.txt

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
