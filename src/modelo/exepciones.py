class PacienteNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un paciente."""
    pass


class MedicoNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un médico."""
    pass


class MedicoNoDisponibleException(Exception):
    """Excepción lanzada cuando un médico no está disponible para una especialidad en un día."""
    pass


class TurnoOcupadoException(Exception):
    """Excepción lanzada cuando se intenta agendar un turno en un horario ya ocupado."""
    pass


class RecetaInvalidaException(Exception):
    """Excepción lanzada cuando se intenta emitir una receta inválida."""
    pass


class PacienteDuplicadoException(Exception):
    """Excepción lanzada cuando se intenta registrar un paciente con DNI duplicado."""
    pass


class MedicoDuplicadoException(Exception):
    """Excepción lanzada cuando se intenta registrar un médico con matrícula duplicada."""
    pass


class EspecialidadDuplicadaException(Exception):
    """Excepción lanzada cuando se intenta agregar una especialidad duplicada a un médico."""
    pass


class DatosInvalidosException(Exception):
    """Excepción lanzada cuando se proporcionan datos inválidos."""
    pass
