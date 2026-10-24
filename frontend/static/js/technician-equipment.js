document.addEventListener("click", (event) => {
    const openButton = event.target.closest("[data-open-dialog]");
    if (openButton) {
        document.getElementById(openButton.dataset.openDialog)?.showModal();
        return;
    }

    const closeButton = event.target.closest("[data-close-dialog]");
    if (closeButton) {
        closeButton.closest("dialog")?.close();
    }
});

document.querySelectorAll(".technician-equipment-dialog").forEach((dialog) => {
    dialog.addEventListener("click", (event) => {
        if (event.target === dialog) {
            dialog.close();
        }
    });
});
