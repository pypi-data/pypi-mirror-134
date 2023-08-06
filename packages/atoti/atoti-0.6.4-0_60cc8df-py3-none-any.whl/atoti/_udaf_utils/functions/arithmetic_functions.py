"""Java function implementations for arithmetic operations."""
from ..java_function import ExistingJavaFunction

ATOTI_OPERATOR_PACKAGE = "io.atoti.udaf.operators"

ADD_FUNCTION = ExistingJavaFunction(
    method_call_string="ArithmeticOperator.add",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

SUB_FUNCTION = ExistingJavaFunction(
    method_call_string="ArithmeticOperator.minus",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

TRUEDIV_FUNCTION = ExistingJavaFunction(
    method_call_string="ArithmeticOperator.divide",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

MUL_FUNCTION = ExistingJavaFunction(
    method_call_string="ArithmeticOperator.multiply",
    import_package=ATOTI_OPERATOR_PACKAGE,
)
