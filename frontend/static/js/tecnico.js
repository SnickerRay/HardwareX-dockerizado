document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.wizard-btn');

    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            const target = button.dataset.target;
            document.querySelectorAll('.step-panel').forEach((panel) => {
                panel.classList.toggle('active', panel.dataset.step === target);
            });

            buttons.forEach((btn) => btn.classList.toggle('active', btn === button));
        });
    });
});
