
document.addEventListener('DOMContentLoaded', () => {

    // ==========================================
    // ELEMENTOS DEL PERFIL
    // ==========================================

    const upload = document.getElementById('upload-photo');
    const avatar = document.getElementById('profile-avatar');
    const headerAvatar = document.getElementById('header-avatar');

    const nameInput = document.getElementById('nombre_usuario');
    const headerName = document.getElementById('header-name');

    const wizardButtons = document.querySelectorAll('.wizard-btn');
    const stepPanels = document.querySelectorAll('.step-panel');
    const formActions = document.querySelector('.form-actions');

    const profileForm = document.getElementById('profile-form');


    // ==========================================
    // ACTUALIZAR NOMBRE DE USUARIO
    // ==========================================

    if (nameInput && headerName) {

        nameInput.addEventListener('input', () => {
            headerName.textContent = nameInput.value || 'Usuario';
        });

    }


    // ==========================================
    // VISTA PREVIA DE FOTO DE PERFIL
    // ==========================================

    if (upload && avatar && headerAvatar) {

        upload.addEventListener('change', (event) => {

            const file = event.target.files[0];

            if (!file) {
                return;
            }

            if (!file.type.startsWith('image/')) {
                alert('Selecciona un archivo de imagen válido.');
                upload.value = '';
                return;
            }

            const reader = new FileReader();

            reader.onload = (event) => {

                avatar.style.backgroundImage =
                    `url(${event.target.result})`;

                avatar.textContent = '';

                headerAvatar.style.backgroundImage =
                    `url(${event.target.result})`;

                headerAvatar.textContent = '';
            };

            reader.readAsDataURL(file);
        });

    }


    // ==========================================
    // NAVEGACIÓN ENTRE SECCIONES
    // ==========================================

    wizardButtons.forEach(button => {

        button.addEventListener('click', () => {

            const target = button.dataset.target;

            wizardButtons.forEach(btn => {
                btn.classList.toggle('active', btn === button);
            });

            stepPanels.forEach(panel => {
                panel.classList.toggle(
                    'active',
                    panel.dataset.step === target
                );
            });

            if (formActions) {
                formActions.style.display =
                    target === '1' ? 'flex' : 'none';
            }

        });

    });


    // ==========================================
    // VALIDACIÓN BÁSICA DEL FORMULARIO
    // ==========================================

    if (profileForm) {

        profileForm.addEventListener('submit', () => {

            const saveButton = document.getElementById('save-button');

            if (saveButton) {
                saveButton.disabled = true;
                saveButton.textContent = 'Guardando...';
            }

        });

    }

});
