class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exceptiom_ = MeuError('a', 'b', 'c')
    exceptiom_.add_note('fala chupinga')
    raise exceptiom_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    excepetion_ = OutroError('Vou lancar de novo')
    raise excepetion_ from error