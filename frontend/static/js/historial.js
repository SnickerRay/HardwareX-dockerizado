
        // Mostrar mensaje cuando no haya registros en la tabla
        const tableBody = document.getElementById('record-table-body');
        const emptyState = document.getElementById('empty-state');

        function updateEmptyState() {
            const hasRecords = tableBody.querySelectorAll('tr.record-row').length > 0;
            emptyState.classList.toggle('visible', !hasRecords);
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateEmptyState();
        });
