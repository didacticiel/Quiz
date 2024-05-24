// Sélectionner tous les boutons modaux
const modalBtns = [...document.getElementsByClassName("modal-button")];
// Sélectionner le corps du modal
const modalBody = document.getElementById('modal-body-confirm');
// Sélectionner le bouton de démarrage
const startBtn = document.getElementById("start-button");
// Obtenir l'URL de la page actuelle
const url = window.location.href;

// Pour chaque bouton modal, ajouter un écouteur d'événements au clic
modalBtns.forEach(modalBtn => {
    modalBtn.addEventListener("click", () => {
        // Récupérer les données du quiz à partir des attributs de données
        const pk = modalBtn.getAttribute('data-pk');
        const name = modalBtn.getAttribute('data-quiz');
        const numQuestions = modalBtn.getAttribute('data-questions');
        const difficulty = modalBtn.getAttribute('data-difficulty');
        const scoreTopass = modalBtn.getAttribute('data-pass');
        const time = modalBtn.getAttribute('data-time');

        // Remplir le corps du modal avec les détails du quiz
        modalBody.innerHTML = `
            <div class="h5 mb-3"> Voulez-vous commencer "<b>${name}</b>"? </div>
            <div class="text-muted">
                <ul>
                    <li>Difficulté : <b> ${difficulty}</b></li>
                    <li>Nbr de questions : <b> ${numQuestions}</b></li>
                    <li>Score à atteindre : <b> ${scoreTopass}%</b></li>
                    <li>Temps : <b> ${time}</b></li>
                </ul>
            </div>
        `;

        // Ajouter un écouteur d'événements au bouton de démarrage
        startBtn.addEventListener("click", () => {
            // Rediriger l'utilisateur vers la page du quiz avec l'identifiant du quiz
            window.location.href = url + pk;
        });
    });
});
