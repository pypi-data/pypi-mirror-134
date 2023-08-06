from lpaas_client.serializer import serialize_term


def compare_terms_with_var(term1, term2) -> bool:
    """Return True if term1 == term2"""
    return serialize_term(term1) == serialize_term(term2)
