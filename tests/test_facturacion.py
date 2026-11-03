import pytest

from hospital.facturacion import DatosPaciente, calcular_total


def test_sin_beneficios_cobra_el_total_de_los_estudios():
    # Arrange
    importes = [1000, 500]
    paciente = DatosPaciente(False, False, 1)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == 1500


def test_cobertura_parcial_cobra_la_mitad_de_cada_estudio():
    # Arrange
    importes = [1000, 500]
    paciente = DatosPaciente(True, False, 1)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == 750


def test_obra_social_aplica_diez_por_ciento_de_descuento():
    # Arrange
    importes = [1000]
    paciente = DatosPaciente(False, True, 1)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == pytest.approx(900)


def test_todos_los_beneficios_se_aplican_en_orden():
    # Arrange
    importes = [1000, 500]
    paciente = DatosPaciente(True, True, 5)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == pytest.approx(575)


def test_con_tres_turnos_no_hay_bonificacion():
    # Arrange
    importes = [1000]
    paciente = DatosPaciente(False, False, 3)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == 1000


def test_lista_vacia_devuelve_cero():
    # Arrange
    importes = []
    paciente = DatosPaciente(False, False, 1)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == 0


def test_importes_nulos_lanzan_error():
    # Arrange
    paciente = DatosPaciente(False, False, 1)

    # Act / Assert
    with pytest.raises(ValueError, match="obligatorios"):
        calcular_total(None, paciente)


def test_importe_negativo_lanza_error():
    # Arrange
    importes = [500, -100]
    paciente = DatosPaciente(False, False, 1)

    # Act / Assert
    with pytest.raises(ValueError, match="negativos"):
        calcular_total(importes, paciente)


def test_bonificacion_no_deja_el_total_en_negativo():
    # Arrange
    importes = [50]
    paciente = DatosPaciente(False, False, 5)

    # Act
    total = calcular_total(importes, paciente)

    # Assert
    assert total == 50
