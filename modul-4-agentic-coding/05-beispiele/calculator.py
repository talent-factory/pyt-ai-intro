"""
Calculator-Klasse für TDD-Beispiel
Verwendung: Lektion 2 - Test-Driven Development mit KI
"""


class Calculator:
    """
    Einfacher Taschenrechner mit Grundrechenarten.
    
    Beispiel:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.divide(10, 2)
        5.0
    """

    def add(self, a: float, b: float) -> float:
        """
        Addiert zwei Zahlen.
        
        Args:
            a: Erste Zahl
            b: Zweite Zahl
            
        Returns:
            Summe von a und b
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtrahiert b von a.
        
        Args:
            a: Minuend
            b: Subtrahend
            
        Returns:
            Differenz a - b
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multipliziert zwei Zahlen.
        
        Args:
            a: Erste Zahl
            b: Zweite Zahl
            
        Returns:
            Produkt von a und b
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Dividiert a durch b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient a / b
            
        Raises:
            ValueError: Wenn b gleich 0 ist
        """
        if b == 0:
            raise ValueError("Division durch Null nicht erlaubt")
        return a / b


if __name__ == "__main__":
    # Kurze Demo
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"5 * 6 = {calc.multiply(5, 6)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

