
document.addEventListener('DOMContentLoaded', function () {

    console.log("admin.js cargado");

    // =====================================================
    // ELEMENTOS DEL MODAL ACTUALIZAR
    // =====================================================

    const selectorEquipo = document.getElementById('equipo_actualizar');
    const inputId = document.getElementById('actualizar_id_equipo');
    const inputCodigo = document.getElementById('actualizar_codigo');
    const inputTipo = document.getElementById('actualizar_tipo');
    const inputFecha = document.getElementById('actualizar_fecha');
    const inputUbicacion = document.getElementById('actualizar_ubicacion');
    const inputEstado = document.getElementById('actualizar_estado');

    // =====================================================
    // SELECCIONAR EQUIPO PARA ACTUALIZAR
    // =====================================================

    if (selectorEquipo) {

        selectorEquipo.addEventListener('change', function () {

            const opcion = this.selectedOptions[0];

            if (!this.value || !opcion) {
                inputId.value = '';
                inputCodigo.value = '';
                inputTipo.value = '';
                inputFecha.value = '';
                inputUbicacion.value = '';
                inputEstado.value = 'operativo';
                return;
            }

            const datos = opcion.dataset;

            inputId.value = this.value;
            inputCodigo.value = datos.codigo || '';
            inputTipo.value = datos.tipo || '';
            inputFecha.value = datos.fecha || '';
            inputUbicacion.value = datos.ubicacion || '';
            inputEstado.value = datos.estado || 'operativo';

            console.log("Equipo cargado para actualizar:", this.value);
        });

    }

    // =====================================================
    // LIMPIAR MODAL ACTUALIZAR
    // =====================================================

    const modalActualizar = document.getElementById('modalActualizarEquipo');

    if (modalActualizar) {

        modalActualizar.addEventListener('hidden.bs.modal', function () {

            if (selectorEquipo) selectorEquipo.value = '';
            if (inputId) inputId.value = '';
            if (inputCodigo) inputCodigo.value = '';
            if (inputTipo) inputTipo.value = '';
            if (inputFecha) inputFecha.value = '';
            if (inputUbicacion) inputUbicacion.value = '';
            if (inputEstado) inputEstado.value = 'operativo';

        });

    }

    // =====================================================
    // LIMPIAR MODAL AGREGAR
    // =====================================================

    const modalAgregar = document.getElementById('modalAgregarEquipo');

    if (modalAgregar) {

        modalAgregar.addEventListener('hidden.bs.modal', function () {

            const formulario = modalAgregar.querySelector('form');

            if (formulario) {
                formulario.reset();
            }

        });

    }

    // =====================================================
    // ELEMENTOS DEL MODAL DAR DE BAJA
    // =====================================================

    const selectorEliminar = document.getElementById('equipo_eliminar');
    const inputIdEliminar = document.getElementById('eliminar_id_equipo');
    const infoEliminar = document.getElementById('info-equipo-eliminar');

    // =====================================================
    // SELECCIONAR EQUIPO PARA DAR DE BAJA
    // =====================================================

    if (selectorEliminar) {

        selectorEliminar.addEventListener('change', function () {

            const idSeleccionado = this.value;

            if (!idSeleccionado) {

                if (inputIdEliminar) inputIdEliminar.value = '';

                if (infoEliminar) {
                    infoEliminar.classList.add('d-none');
                }

                return;
            }

            if (inputIdEliminar) {
                inputIdEliminar.value = idSeleccionado;
            }

            if (infoEliminar) {
                infoEliminar.classList.remove('d-none');
            }

            console.log("Equipo seleccionado para dar de baja:", idSeleccionado);

        });

    }

    // =====================================================
    // LIMPIAR MODAL DAR DE BAJA
    // =====================================================

    const modalEliminar = document.getElementById('modalEliminarEquipo');

    if (modalEliminar) {

        modalEliminar.addEventListener('hidden.bs.modal', function () {

            if (selectorEliminar) selectorEliminar.value = '';
            if (inputIdEliminar) inputIdEliminar.value = '';

            if (infoEliminar) {
                infoEliminar.classList.add('d-none');
            }

        });

    }

});
