.. code-block:: pycon
from type_constraint import BasicCheck, CheckMeta, Check

class A:
    __metaclass__ = CheckMeta()
    def f(self, i, j):
        """
        @param i str
        @param j str
        """
        return i + j

a = A()
a.f('1', '2')

@BasicCheck
def test_func(i, j):
    """
    this is a test function for type constraint
    @param i int   :this is the first operand
    @param j float :this is the second operand
    @return float
    """
    return i / j

