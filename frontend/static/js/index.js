document.addEventListener('DOMContentLoaded', function () {

    // =========================================================
    // ELEMENTOS
    // =========================================================

    const steps = Array.from(
        document.querySelectorAll('.wizard-step')
    );

    const panels = Array.from(
        document.querySelectorAll('.step-panel')
    );

    const progressBar = document.getElementById(
        'wizard-progress'
    );

    const nextButton = document.getElementById(
        'next-button'
    );

    const prevButton = document.getElementById(
        'prev-button'
    );

    const submitButton = document.getElementById(
        'submit-button'
    );

    const formError = document.getElementById(
        'form-error'
    );

    const form = document.getElementById(
        'repair-form'
    );


    // =========================================================
    // CAMPOS
    // =========================================================

    const equipoSelect = document.getElementById(
        'id_equipo'
    );

    const ubicacionInput = document.getElementById(
        'device-location'
    );

    const tipoInput = document.getElementById(
        'device-type'
    );

    const codigoInput = document.getElementById(
        'device-code'
    );

    const issueType = document.getElementById(
        'issue-type'
    );

    const urgency = document.getElementById(
        'urgency'
    );

    const description = document.getElementById(
        'description'
    );


    // =========================================================
    // PASOS
    // =========================================================

    let currentStep = 1;


    const fieldsByStep = {

        1: [
            equipoSelect
        ],

        2: [
            issueType,
            urgency,
            description
        ]

    };


    // =========================================================
    // MOSTRAR PASO
    // =========================================================

    function showStep(step) {

        currentStep = step;

        panels.forEach(function (panel) {

            panel.classList.toggle(
                'active',
                Number(panel.dataset.step) === step
            );

        });


        steps.forEach(function (stepElement) {

            stepElement.classList.toggle(
                'active',
                Number(stepElement.dataset.step) === step
            );

        });


        // Botón anterior

        prevButton.hidden = step === 1;


        // Botón siguiente

        nextButton.hidden = step === 3;


        // Botón confirmar

        submitButton.hidden = step !== 3;


        // Progreso

        progressBar.style.width =
            `${((step - 1) / 2) * 100}%`;


        formError.textContent = '';


        if (step === 3) {

            fillSummary();

        }


        updateProgressFill();

    }


    // =========================================================
    // VALIDAR PASO
    // =========================================================

    function validateStep(step) {

        const requiredFields =
            fieldsByStep[step] || [];


        for (const field of requiredFields) {

            if (!field) {
                continue;
            }


            if (!field.value.trim()) {

                formError.textContent =
                    'Por favor completa todos los campos obligatorios antes de continuar.';

                field.focus();

                return false;

            }

        }


        formError.textContent = '';

        return true;

    }


    // =========================================================
    // ACTUALIZAR PROGRESO
    // =========================================================

    function updateProgressFill() {

        const currentFields =
            fieldsByStep[currentStep] || [];


        if (!currentFields.length) {
            return;
        }


        const filled =
            currentFields.filter(function (field) {

                return field &&
                    field.value.trim();

            }).length;


        const percent =
            Math.round(
                (filled / currentFields.length) * 100
            );


        progressBar.style.width =
            `${((currentStep - 1) / 2) * 100 +
            (percent / 200 * 100)}%`;

    }


    // =========================================================
    // SELECCIONAR EQUIPO
    // =========================================================

    if (equipoSelect) {

        equipoSelect.addEventListener(
            'change',
            function () {

                const option =
                    this.options[this.selectedIndex];


                if (!option || !option.value) {

                    ubicacionInput.value = '';
                    tipoInput.value = '';
                    codigoInput.value = '';

                    return;

                }


                // Obtener datos del equipo

                const tipo =
                    option.dataset.tipo || '';

                const codigo =
                    option.dataset.codigo || '';

                const ubicacion =
                    option.dataset.ubicacion ||
                    'Sin ubicación';


                // Mostrar datos

                tipoInput.value = tipo;

                codigoInput.value = codigo;

                ubicacionInput.value = ubicacion;


                console.log(
                    'Equipo seleccionado:',
                    {
                        id: option.value,
                        codigo: codigo,
                        tipo: tipo,
                        ubicacion: ubicacion
                    }
                );


                updateProgressFill();

            }
        );

    }


    // =========================================================
    // RESUMEN
    // =========================================================

    function fillSummary() {

        const selectedOption =
            equipoSelect.options[
                equipoSelect.selectedIndex
            ];


        document.getElementById(
            'summary-device'
        ).textContent =
            selectedOption
                ? selectedOption.textContent.trim()
                : 'No especificado';


        document.getElementById(
            'summary-location'
        ).textContent =
            ubicacionInput.value.trim()
            || 'No especificado';


        document.getElementById(
            'summary-type'
        ).textContent =
            tipoInput.value.trim()
            || 'No especificado';


        document.getElementById(
            'summary-issue'
        ).textContent =
            issueType.options[
                issueType.selectedIndex
            ]?.textContent
            || 'No especificado';


        document.getElementById(
            'summary-urgency'
        ).textContent =
            urgency.options[
                urgency.selectedIndex
            ]?.textContent
            || 'No especificado';


        document.getElementById(
            'summary-description'
        ).textContent =
            description.value.trim()
            || 'No especificado';


        document.getElementById(
            'summary-serial'
        ).textContent =
            codigoInput.value.trim()
            || 'No especificado';

    }


    // =========================================================
    // BOTÓN SIGUIENTE
    // =========================================================

    nextButton.addEventListener(
        'click',
        function () {

            console.log(
                'Siguiente. Paso actual:',
                currentStep
            );


            if (validateStep(currentStep)) {

                showStep(currentStep + 1);

            }

        }
    );


    // =========================================================
    // BOTÓN ANTERIOR
    // =========================================================

    prevButton.addEventListener(
        'click',
        function () {

            console.log(
                'Anterior. Paso actual:',
                currentStep
            );


            if (currentStep > 1) {

                showStep(currentStep - 1);

            }

        }
    );


    // =========================================================
    // ENVIAR FORMULARIO
    // =========================================================

    form.addEventListener(
        'submit',
        function (event) {

            if (!validateStep(2)) {

                event.preventDefault();

                return;

            }


            console.log(
                'Enviando solicitud al servidor...'
            );

            // NO hacemos preventDefault.
            // Django recibirá el POST.

        }
    );


    // =========================================================
    // ACTUALIZAR PROGRESO AL ESCRIBIR
    // =========================================================

    Object.values(fieldsByStep)
        .flat()
        .forEach(function (field) {

            if (!field) {
                return;
            }


            field.addEventListener(
                'input',
                updateProgressFill
            );


            field.addEventListener(
                'change',
                updateProgressFill
            );

        });


    // =========================================================
    // INICIAR
    // =========================================================

    showStep(1);

});