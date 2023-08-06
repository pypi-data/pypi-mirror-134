infolib
=======

*simple and complete PandasDataframe's stat overview*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|PyPI - Status| |Build Status| |PyPI - Downloads|

Installation
------------

Only through pip at this time https://test.pypi.org/project/infolib/

.. code:: sh

   pip install -i https://test.pypi.org/simple/ infolib

.. code:: sh

   from infolib.infolib import inf

How to use
----------

Using infolib is very simple:

.. code:: sh

   inf(pd.DataFarame)

inf() takes 1 positional argument and expects pandas DataFrame object

Exemple
-------

.. code:: sh

   # series that will be part of the dataframe
   s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
   td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
   i = [1,2,3]
   f = [0.123,423.231,0.002]
   c = ['A', 'B', 'C']
   cn = [1, 2, 3]
   b = [False, True, False]
   n = [np.nan, np.nan, np.nan]

   # import as pandas.Dtaframe
   test = pd.DataFrame({"A": s, "B": td, "C": i, "D":f, "E":c, "F":cn, "G":b, "H":n})

   # transformation of two features as categories
   test['E'] = test_03['E'].astype('category')
   test['F'] = test_03['F'].astype('category')

.. code:: sh

   # run infolib
   inf(test)

.. image:: https://raw.githubusercontent.com/AntonelloManenti/infolib/main/tests/output_infolib.PNG
   :alt: Infolib output

Development Status
------------------

Read well and don't say you didn't know.

== =================
\  Status
== =================
✔️ Planning
✔️ Pre-Alpha
✔️ Alpha
❌ Beta
❌ Production/Stable
❌ Mature
❌ Inactive
== =================

The alpha version was tested in Colab (py 3.7) and on Jupyter (py 3.10
on Windows)

Demo
^^^^

`Demo on Colab`_

License
-------

`MIT`_

Contacts
--------

`linkedin`_

.. _Demo on Colab: https://colab.research.google.com/drive/1KTI7CwP_E7IJod_WiD0PT31MaRBdhiki?usp=sharing
.. _MIT: https://github.com/AntonelloManenti/infolib/blob/main/LICENSE
.. _linkedin: https://github.com/AntonelloManenti/infolib/blob/main/LICENSE

.. |PyPI - Status| image:: https://img.shields.io/pypi/status/infolib
.. |Build Status| image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue
.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dm/infolib?color=green
