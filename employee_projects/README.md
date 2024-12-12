# Módulo de Proyectos de Empleados

Este módulo permite a los usuarios gestionar proyectos vinculados a empleados dentro del sistema Odoo. Incluye funciones como visualizar, crear y listar proyectos con diseños dinámicos.

## Características

- **Botón Inteligente**: Muestra el número total de proyectos asociados a un empleado.
- **Diseño Dinámico**: Tarjetas de proyectos estilizadas para una mejor visualización en el portal.
- **Gestión de Proyectos**: Permite la creación, filtrado y visualización de detalles de proyectos a través del portal.
- **Diseño Adaptativo**: Diseños adaptables para diferentes dispositivos.

## Instalación

Sigue estos pasos para instalar el módulo:

1. **Descargar el Módulo**:
   - Asegúrate de tener la carpeta del módulo (`employee_projects`) disponible en tu sistema.

2. **Ubicar el Módulo**:
   - Copia la carpeta `employee_projects` en el directorio de addons personalizados de Odoo. Ejemplo:
     ```
     /odoo/custom_addons/employee_projects
     ```

3. **Actualizar Lista de Aplicaciones**:
   - Inicia sesión en tu instancia de Odoo como administrador.
   - Ve a `Aplicaciones` y haz clic en `Actualizar Lista de Aplicaciones`.

4. **Instalar el Módulo**:
   - Busca `Employee Projects` en la lista de aplicaciones.
   - Haz clic en `Instalar` para habilitar el módulo.

## Configuración

1. **Derechos de Acceso**:
   - Asegúrate de que los usuarios relevantes tengan acceso a los módulos `HR` y `Portal`.
   - Asigna los roles necesarios para la gestión de proyectos.

2. **Imágenes y Estilos Personalizados**:
   - Reemplaza las imágenes de ejemplo (por ejemplo, `project_icon.png`) con imágenes específicas de tu organización en el directorio `static/src/img`.

## Pruebas del Módulo

### Entorno de Pruebas

1. **Pre-requisitos**:
   - Instancia de Odoo (v16 o superior).
   - Acceso como administrador.

2. **Pasos para las Pruebas**:

   #### A. Usuario del Portal
   - Inicia sesión como usuario del portal.
   - Navega a la sección de proyectos y verifica:
     - Visualización correcta de las tarjetas de proyectos.
     - Funcionamiento del filtrado basado en fechas.
     - Redirección correcta a los detalles de los proyectos.

   #### B. Empleado
   - Inicia sesión como empleado.
   - Abre el menú `Empleados`.
   - Haz clic en el botón inteligente de proyectos.
   - Verifica:
     - Conteo correcto de proyectos.
     - Visualización precisa de datos en vistas tipo árbol y formulario.

   #### C. Administrador
   - Inicia sesión como administrador.
   - Prueba la instalación y configuración del módulo.
   - Agrega/elimina datos de prueba para garantizar estabilidad y capacidad de respuesta.

## Capturas de Pantalla

### Botón Inteligente:
Muestra el total de proyectos vinculados a los empleados directamente en el formulario del empleado.

### Vista del Portal:
Tarjetas estilizadas para los proyectos con botones para ver detalles y opciones de filtrado.
