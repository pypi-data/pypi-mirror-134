"""
    This is an extension of `2ppy` to support serialization of Terms/Theories from/to python str.
    
    Serialization convert Terms/Theories into Prolog plain text as Python str.
    Vice versa you can convert Prolog plain text via parse_* methods available from `2ppy`.

    e.g.
        # Create a Struct via 2ppy
        struct: Struct = tuprolog.core.parser.parse_struct('p(a, X)')
        # Recreate the str via serialize_terms
        srtuct_str = serialize_terms(struct)
        > p(a, X)
"""

from .serializer import serialize_term, serialize_theory
