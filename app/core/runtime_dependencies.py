
"""
DynamiCore V6.12.1
Enterprise Runtime Dependency Manager
"""


def optional_import(
    module
):

    try:

        return __import__(
            module
        )

    except ImportError:

        return None



streamlit = optional_import(
    "streamlit"
)


passlib = optional_import(
    "passlib"
)


stripe = optional_import(
    "stripe"
)


openai = optional_import(
    "openai"
)
