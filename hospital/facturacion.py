"""Módulo de facturación médica del Hospital Central."""

from dataclasses import dataclass

PORCENTAJE_COBERTURA_PARCIAL = 0.5
FACTOR_DESCUENTO_OBRA_SOCIAL = 0.9
TURNOS_PARA_BONIFICACION = 3
BONIFICACION = 100


@dataclass
class DatosPaciente:
    tiene_cobertura_parcial: bool
    tiene_obra_social: bool
    cantidad_turnos: int


def calcular_total(importes, paciente):
    """Calcula el total a facturar por los estudios de un paciente.

    Aplica la cobertura parcial a cada estudio, el descuento de obra social
    al subtotal y una bonificación a pacientes con más de 3 turnos, siempre
    que el total supere el monto de la bonificación.
    """
    if importes is None or paciente is None:
        raise ValueError("Los importes y los datos del paciente son obligatorios")

    total = 0.0
    for importe in importes:
        if importe < 0:
            raise ValueError("Los importes no pueden ser negativos")
        if paciente.tiene_cobertura_parcial:
            total += importe * PORCENTAJE_COBERTURA_PARCIAL
        else:
            total += importe

    if paciente.tiene_obra_social:
        total *= FACTOR_DESCUENTO_OBRA_SOCIAL

    if paciente.cantidad_turnos > TURNOS_PARA_BONIFICACION and total > BONIFICACION:
        total -= BONIFICACION

    return total
