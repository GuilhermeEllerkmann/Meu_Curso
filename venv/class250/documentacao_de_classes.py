"""Este e um modulo de exemplo

Este modulo contem funcoes e exemplos de documentacao de funcoes.
A funcao soma voce ja conhece bastante

"""

variavel_1 = 1

class Foo():

    """Este e um modulo de exemplo

    Este modulo contem funcoes e exemplos de documentacao de funcoes.
    A funcao soma voce ja conhece bastante

    """
    
    def soma(self, x: int | float, y: int | float) -> int | float:
        """Soma x e y

        Este modulo contem funcoes e exemplos de documentacao de funcoes.
        A funcao soma voce ja conhece bastante

        :param x: Numero 1
        :type x: int or float
        :param y: Numero 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """

        return x + y

    def multiplica(
            self, 
            x: int | float,
            y: int | float,
            z: int | float | None = None
    ) -> int | float:
        """Multiplica x, y e/ou z
        
        Multiplica x e y, Se z for enviado, multiplica x, y, z
        """

        if z is None:
            return x * z
        return x * y * z
    
    def bar(self) -> int:
        """o que ele faz
        
        
        :raises NotImplementedError: se o metodo nao for definido
        :raises ValueError: se o metodo nao for definido
        """
        raise NotImplementedError('Teste')

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4
    