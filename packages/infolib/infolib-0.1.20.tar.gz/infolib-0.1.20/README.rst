infolib
=======

*simple and complete PandasDataframe's stat overview*


| Python >=3.7 |

Installation
------------

Only through pip at this time https://test.pypi.org/project/infolib/

'pip install -i https://test.pypi.org/simple/ infolib'_

'from infolib.infolib import inf_'

How to use
----------

Using infolib is very simple:


`inf(pd.DataFarame)

inf() takes 1 positional argument and expects pandas DataFrame object`

Exemple
-------

series that will be part of the dataframe
's = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
i = [1,2,3]
f = [0.123,423.231,0.002]
c = ['A', 'B', 'C']
cn = [1, 2, 3]
b = [False, True, False]
n = [np.nan, np.nan, np.nan]''

import as pandas.Dtaframe
'test = pd.DataFrame({"A": s, "B": td, "C": i, "D":f, "E":c, "F":cn, "G":b, "H":n})''

transformation of two features as categories
'test['E'] = test_03['E'].astype('category')
test['F'] = test_03['F'].astype('category')''

run infolib
'inf(test)'

Development Status
------------------

Read well and don't say you didn't know.

✔️ Planning

✔️ Pre-Alpha

✔️ Alpha

❌ Beta

❌ Production/Stable

❌ Mature

❌ Inactive

The alpha version was tested in Colab (py 3.7) and on Jupyter (py 3.10
on Windows)

Demo
----

Demo on Colab: https://colab.research.google.com/drive/1KTI7CwP_E7IJod_WiD0PT31MaRBdhiki?usp=sharing

License
-------

MIT: https://github.com/AntonelloManenti/infolib/blob/main/LICENSE

Contacts
--------

linkedin: https://www.linkedin.com/in/antonello-manenti/
