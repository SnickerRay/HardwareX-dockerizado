document.addEventListener('DOMContentLoaded', function () {

    console.log("admin.js cargado");


    // =====================================================
    // OBTENER LOS EQUIPOS ENVIADOS POR DJANGO
    // =====================================================

    const equiposElemento = document.getElementById('equipos-data');

    let equipos = [];

    if (equiposElemento) {

        equipos = JSON.parse(equiposElemento.textContent);

        console.log("Equipos cargados desde Django:", equipos);

    } else {

        console.log("No se encontró equipos-data");

    }


    // =====================================================
    // ELEMENTOS DEL MODAL ACTUALIZAR
    // =====================================================

    const selectorEquipo =
        document.getElementById('equipo_actualizar');

    const inputId =
        document.getElementById('actualizar_id_equipo');

    const inputCodigo =
        document.getElementById('actualizar_codigo');

    const inputTipo =
        document.getElementById('actualizar_tipo');

    const inputFecha =
        document.getElementById('actualizar_fecha');

    const inputUbicacion =
        document.getElementById('actualizar_ubicacion');

    const inputEstado =
        document.getElementById('actualizar_estado');


    // =====================================================
    // CUANDO SE SELECCIONA UN EQUIPO
    // =====================================================

    if (selectorEquipo) {

        selectorEquipo.addEventListener('change', function () {

            const idSeleccionado = this.value;

            console.log(
                "Equipo seleccionado:",
                idSeleccionado
            );


            // Si no seleccionó ningún equipo

            if (!idSeleccionado) {

                inputId.value = '';
                inputCodigo.value = '';
                inputTipo.value = '';
                inputFecha.value = '';
                inputUbicacion.value = '';
                inputEstado.value = 'operativo';

                return;
            }


            // Buscar el equipo

            const equipo = equipos.find(function (equipo) {

                return String(equipo.id) === String(idSeleccionado);

            });

            // SI ENCONTRAMOS EL EQUIPO
            if (equipo) {

                console.log(
                    "Equipo encontrado:",
                    equipo
                );


                // ID

                inputId.value = equipo.id;


                // Código

                inputCodigo.value = equipo.codigo;


                // Tipo

                inputTipo.value = equipo.tipo;


                // Fecha

                inputFecha.value = equipo.fecha || '';


                // Ubicación

                inputUbicacion.value =
                    equipo.ubicacion || '';


                // Estado

                inputEstado.value =
                    equipo.estado || 'operativo';

            }

        });

    }


    // =====================================================
    // LIMPIAR MODAL DE ACTUALIZAR
    // =====================================================

    const modalActualizar =
        document.getElementById('modalActualizarEquipo');


    if (modalActualizar) {

        modalActualizar.addEventListener(
            'hidden.bs.modal',
            function () {

                if (selectorEquipo) {
                    selectorEquipo.value = '';
                }

                if (inputId) {
                    inputId.value = '';
                }

                if (inputCodigo) {
                    inputCodigo.value = '';
                }

                if (inputTipo) {
                    inputTipo.value = '';
                }

                if (inputFecha) {
                    inputFecha.value = '';
                }

                if (inputUbicacion) {
                    inputUbicacion.value = '';
                }

                if (inputEstado) {
                    inputEstado.value = 'operativo';
                }

            }
        );

    }


    // =====================================================
    // MODAL AGREGAR
    // =====================================================

    const modalAgregar =
        document.getElementById('modalAgregarEquipo');


    if (modalAgregar) {

        modalAgregar.addEventListener(
            'hidden.bs.modal',
            function () {

                const formulario =
                    modalAgregar.querySelector('form');


                if (formulario) {

                    formulario.reset();

                }

            }
        );

    }

    // ELIMINAR EQUIPO

    const selectorEliminar =
        document.getElementById('equipo_eliminar');

    const inputIdEliminar =
        document.getElementById('eliminar_id_equipo');

    const infoEliminar =
        document.getElementById('info-equipo-eliminar');


    if (selectorEliminar) {

        selectorEliminar.addEventListener('change', function () {

            const idSeleccionado = this.value;

            console.log(
                "Equipo seleccionado para eliminar:",
                idSeleccionado
            );


            // Si no seleccionó nada

            if (!idSeleccionado) {

                inputIdEliminar.value = '';

                if (infoEliminar) {
                    infoEliminar.classList.add('d-none');
                }

                return;
            }


            // Guardamos el ID

            inputIdEliminar.value = idSeleccionado;


            // Mostrar advertencia

            if (infoEliminar) {
                infoEliminar.classList.remove('d-none');
            }


            // Buscar equipo

            const equipo = equipos.find(function (equipo) {

                return String(equipo.id) ===
                    String(idSeleccionado);

            });


            if (equipo) {

                console.log(
                    "Equipo que se va a eliminar:",
                    equipo
                );

            }

        });

    }


    // LIMPIAR MODAL ELIMINAR


    const modalEliminar =
        document.getElementById('modalEliminarEquipo');


    if (modalEliminar) {

        modalEliminar.addEventListener(
            'hidden.bs.modal',
            function () {

                if (selectorEliminar) {
                    selectorEliminar.value = '';
                }

                if (inputIdEliminar) {
                    inputIdEliminar.value = '';
                }

                if (infoEliminar) {
                    infoEliminar.classList.add('d-none');
                }

            }
        );

    }

});