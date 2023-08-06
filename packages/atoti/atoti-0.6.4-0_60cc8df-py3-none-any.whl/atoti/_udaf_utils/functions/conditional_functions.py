"""Java function implementations for conditional opperations."""
from ..java_function import ExistingJavaFunction

ATOTI_OPERATOR_PACKAGE = "io.atoti.udaf.operators"


EQ_FUNCTION = ExistingJavaFunction(
    method_call_string="ConditionalOperator.eq",
    import_package=ATOTI_OPERATOR_PACKAGE,
)


NEQ_FUNCTION = ExistingJavaFunction(
    method_call_string="ConditionalOperator.neq",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

GT_FUNCTION = ExistingJavaFunction(
    method_call_string="ConditionalOperator.gt",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

GTE_FUNCTION = ExistingJavaFunction(
    method_call_string="ConditionalOperator.gte",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

LT_FUNCTION = ExistingJavaFunction(
    method_call_string="ConditionalOperator.lt",
    import_package=ATOTI_OPERATOR_PACKAGE,
)

LTE_FUNCTION = ExistingJavaFunction(
    method_call_string="ConditionalOperator.lte",
    import_package=ATOTI_OPERATOR_PACKAGE,
)
