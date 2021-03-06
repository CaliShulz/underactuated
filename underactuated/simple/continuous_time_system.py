from pydrake.systems.framework import VectorSystem


# Define the system.
class SimpleContinuousTimeSystem(VectorSystem):

    def __init__(self):
        VectorSystem.__init__(
            self,
            0,  # Zero inputs.
            1)  # One output.
        self.DeclareContinuousState(1)  # One state variable.

    # xdot(t) = -x(t) + x^3(t)
    def DoCalcVectorTimeDerivatives(self, context, u, x, xdot):
        xdot[:] = -x + x**3

    # y(t) = x(t)
    def DoCalcVectorOutput(self, context, u, x, y):
        y[:] = x
