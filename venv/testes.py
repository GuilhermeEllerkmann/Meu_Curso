import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("O ambiente virtual está ativo.")
else:
    print("O ambiente virtual não está ativo.")
