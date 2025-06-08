# Instrucciones del Sistema de Gestión Clínica

## Cómo ejecutar el sistema

### Requisitos previos
- Python 3.7 o superior
- Ninguna dependencia externa adicional (solo bibliotecas estándar de Python)

### Ejecución del sistema principal

Para iniciar el sistema de gestión clínica, ejecute desde la raíz del proyecto:

```bash
python main.py
```

O alternativamente:

```bash
python src/cli/cli.py
```

### Navegación en el sistema

El sistema presenta un menú interactivo con las siguientes opciones:

```
SISTEMA DE GESTIÓN CLÍNICA
==================================================
1) Agregar paciente
2) Agregar médico
3) Agendar turno
4) Agregar especialidad a médico
5) Emitir receta
6) Ver historia clínica
7) Ver todos los turnos
8) Ver todos los pacientes
9) Ver todos los médicos
0) Salir
==================================================
```

### Flujo de trabajo recomendado

1. **Registrar médicos** primero con sus especialidades
2. **Registrar pacientes**
3. **Agendar turnos** entre pacientes y médicos
4. **Emitir recetas** cuando sea necesario
5. **Consultar historias clínicas** para ver el registro completo

## Cómo ejecutar las pruebas

### Ejecutar todas las pruebas

Para ejecutar todas las pruebas unitarias del sistema:

```bash
python run_tests.py
```

### Ejecutar pruebas específicas

Para ejecutar pruebas de una clase específica:

```bash
python -m unittest tests.test_paciente
python -m unittest tests.test_medico
python -m unittest tests.test_clinica
```

Para ejecutar una prueba específica:

```bash
python -m unittest tests.test_paciente.TestPaciente.test_creacion_paciente_exitosa
```

### Ejecutar pruebas con mayor verbosidad

```bash
python -m unittest discover -v tests/
```

## Explicación del diseño general

### Arquitectura del sistema

El sistema está diseñado siguiendo los principios de **Programación Orientada a Objetos** y **separación de responsabilidades**:

```
Sistema de Gestión Clínica/
├── src/
│   ├── modelo/          # Lógica de negocio y clases del dominio
│   │   ├── paciente.py       # Clase Paciente
│   │   ├── medico.py         # Clase Medico
│   │   ├── especialidad.py   # Clase Especialidad
│   │   ├── turno.py          # Clase Turno
│   │   ├── receta.py         # Clase Receta
│   │   ├── historia_clinica.py # Clase HistoriaClinica
│   │   ├── clinica.py        # Clase principal Clinica
│   │   └── exepciones.py     # Excepciones personalizadas
│   └── cli/             # Interfaz de usuario
│       └── cli.py            # Interfaz de línea de comandos
├── tests/               # Pruebas unitarias
├── main.py             # Punto de entrada principal
└── run_tests.py        # Script para ejecutar pruebas
```

### Principios de diseño aplicados

#### 1. **Separación de responsabilidades**
- **Modelo**: Contiene toda la lógica de negocio y validaciones
- **CLI**: Solo maneja la interacción con el usuario y presenta datos
- **Pruebas**: Verifican el comportamiento correcto del modelo

#### 2. **Validaciones en el modelo**
- Todas las validaciones de datos están implementadas en las clases del modelo
- La CLI solo captura excepciones y muestra mensajes amigables
- Principio: "La lógica de negocio vive en el modelo, no en la interfaz"

#### 3. **Excepciones personalizadas**
- Cada tipo de error tiene su excepción específica
- Permite manejo granular de errores
- Facilita la depuración y el mantenimiento

#### 4. **Encapsulamiento**
- Atributos privados (`__atributo`) en todas las clases
- Acceso controlado a través de métodos públicos
- Protege la integridad de los datos

### Clases principales y sus responsabilidades

#### **Clinica** (Clase principal)
- Coordina todas las operaciones del sistema
- Mantiene registros de pacientes, médicos y turnos
- Implementa la lógica de validación de turnos y disponibilidad

#### **Paciente**
- Representa a un paciente con validaciones de DNI y datos personales
- Valida formato de fecha de nacimiento

#### **Medico**
- Representa a un médico con su matrícula y especialidades
- Gestiona múltiples especialidades con días de atención

#### **Especialidad**
- Define una especialidad médica con días de atención
- Valida días de la semana y evita duplicados

#### **Turno**
- Representa una cita médica entre paciente y médico
- Valida fechas futuras y coherencia de datos

#### **Receta**
- Representa una prescripción médica
- Valida medicamentos y registra fecha de emisión

#### **HistoriaClinica**
- Mantiene el registro completo de turnos y recetas de un paciente
- Proporciona vistas consolidadas del historial médico

### Características destacadas

- **Validaciones estrictas**: Todos los datos se validan en el momento de creación
- **Excepciones específicas**: Manejo de errores granular y descriptivo
- **Interfaz amigable**: CLI con menús claros y mensajes informativos
- **Pruebas completas**: Cobertura de casos exitosos y de error
- **Código mantenible**: Separación clara de responsabilidades
- **Documentación completa**: Código autodocumentado con docstrings

### Casos de uso cubiertos

- Gestión completa de pacientes y médicos
- Agendamiento de turnos con validación de disponibilidad
- Emisión de recetas médicas
- Mantenimiento de historias clínicas
- Validación de especialidades y horarios de atención
- Prevención de turnos duplicados
- Manejo robusto de errores

---

## Notas adicionales

- El sistema utiliza solo bibliotecas estándar de Python
- Todas las fechas deben ingresarse en formato `dd/mm/aaaa`
- Las horas se ingresan en formato `HH:MM` (24 horas)
- Los días de la semana deben especificarse en español (lunes, martes, etc.)
- El DNI debe tener entre 7 y 8 dígitos
- La matrícula médica debe tener entre 4 y 10 dígitos 