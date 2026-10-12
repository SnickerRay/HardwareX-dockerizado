const registerButton =
    document.getElementById("register");

const loginButton =
    document.getElementById("login");

const container =
    document.getElementById("container");


if (registerButton && container) {

    registerButton.addEventListener(
        "click",
        () => {

            container.classList.add(
                "right-panel-active"
            );

        }
    );

}


if (loginButton && container) {

    loginButton.addEventListener(
        "click",
        () => {

            container.classList.remove(
                "right-panel-active"
            );

        }
    );

}


// ==========================================
// LOGIN
// ==========================================

const loginForm =
    document.getElementById("loginForm");


if (loginForm) {

    loginForm.addEventListener(
        "submit",
        async (event) => {

            event.preventDefault();

            const formData =
                new FormData(loginForm);


            try {

                const response =
                    await fetch(
                        loginForm.action,
                        {
                            method: "POST",

                            body: formData,

                            credentials:
                                "same-origin",

                            headers: {
                                "X-Requested-With":
                                    "XMLHttpRequest"
                            }
                        }
                    );


                /*
                 * El login todavía puede utilizar
                 * fetch porque aquí queremos recibir
                 * información para mantener la sesión.
                 */

                if (
                    response.redirected
                ) {

                    window.location.href =
                        response.url;

                    return;

                }


                const contentType =
                    response.headers.get(
                        "content-type"
                    );


                if (
                    contentType &&
                    contentType.includes(
                        "application/json"
                    )
                ) {

                    const data =
                        await response.json();

                    if (!response.ok) {

                        alert(
                            data.detail ||
                            "Correo o contraseña incorrectos."
                        );

                        return;
                    }

                } else {

                    /*
                     * Django respondió con HTML.
                     * Lo utilizamos directamente.
                     */

                    document.open();

                    document.write(
                        await response.text()
                    );

                    document.close();

                }


            } catch (error) {

                console.error(
                    "Error al iniciar sesión:",
                    error
                );

                alert(
                    "No se pudo conectar con el servidor."
                );

            }

        }
    );

}


// ==========================================
// REGISTRO
// ==========================================
//
// IMPORTANTE:
//
// NO HAY FETCH
// NO HAY API
// NO HAY JSON
//
// El formulario se manda directamente a Django.
//

const registerForm =
    document.getElementById("registerForm");


if (registerForm) {

    /*
     * NO ponemos submit.
     *
     * NO hacemos event.preventDefault().
     *
     * Django recibirá directamente el POST.
     */

}