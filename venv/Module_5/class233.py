class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exceptiom_ = MeuError('a', 'b', 'c')
    raise exceptiom_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    excepetion_ = OutroError('Vou lancar de novo')
    raise excepetion_ from error