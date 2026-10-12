        const upload = document.getElementById('upload-photo');
        const avatar = document.getElementById('profile-avatar');
        const headerAvatar = document.getElementById('header-avatar');
        const nameInput = document.getElementById('display-name');
        const headerName = document.getElementById('header-name');
        const wizardButtons = document.querySelectorAll('.wizard-btn');
        const stepPanels = document.querySelectorAll('.step-panel');
        const formActions = document.querySelector('.form-actions');

        upload.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(ev){
                avatar.style.backgroundImage = `url(${ev.target.result})`;
                avatar.textContent = '';
                headerAvatar.style.backgroundImage = `url(${ev.target.result})`;
                headerAvatar.textContent = '';
            }
            reader.readAsDataURL(file);
        });

        nameInput.addEventListener('input', () => {
            headerName.textContent = nameInput.value || 'Usuario';
        });

        wizardButtons.forEach(button => {
            button.addEventListener('click', () => {
                const target = button.dataset.target;
                wizardButtons.forEach(btn => btn.classList.toggle('active', btn === button));
                stepPanels.forEach(panel => {
                    panel.classList.toggle('active', panel.dataset.step === target);
                });
                formActions.style.display = target === '1' ? 'flex' : 'none';
            });
        });