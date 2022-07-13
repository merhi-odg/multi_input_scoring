# modelop.schema.0: input_schema_0.avsc
# modelop.schema.2: input_schema_2.avsc
# modelop.schema.1: output_schema.avsc


def action(input_1: dict, input_2: dict) -> dict:
    """concatenate two dicts into one and return that

    Args:
        input_1 (dict): {"a":<int>, "b":<float>}
        input_2 (dict): {"c":<str>, "d":<bool>}

    Returns:
        dict: {"a":<int>, "b":<float>, "c":<str>, "d":<bool>}
    """
    return input_1.update(input_2)
