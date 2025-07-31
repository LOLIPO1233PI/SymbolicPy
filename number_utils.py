from fractions import Fraction
from numbers import Number
from decimal import Decimal

def ConvertNumberToFraction(value: Number, precisionFraction: int = 1000) -> Fraction:
    if not isinstance(value, Number) or not isinstance(precisionFraction, int):
        raise ValueError("Please pass a valid arguments inside ConvertNumberToFraction")
    return (Fraction(value) if isinstance(value, Decimal) else Fraction(value)).limit_denominator(precisionFraction)

def IntegerPart(value: float) -> int:
    if not isinstance(value, float):
        raise ValueError("Please pass a float inside the IntegerPart function")
    return int(value)

def DecimalPart(value: float) -> float:
    if not isinstance(value, float):
        raise ValueError("Please pass a float inside the DecimalPart function")
    return value - IntegerPart(value) if value > 0 else - value - IntegerPart(value)

SuperScriptNumbers: list[str] = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def TurnNumbertoSuperScript(value: Number) -> str:
    if not isinstance(value, float):
        raise ValueError("Please pass a number inside the DecimalPart function")
    Translationtable = str.maketrans('0123456789.', f"{''.join(SuperScriptNumbers)}˙")
    return str(value).translate(Translationtable)