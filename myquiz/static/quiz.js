// Afficher un message dans la console pour vérifier si le fichier est chargé
console.log('hello world');

// Obtenir l'URL de la page actuelle
const url = window.location.href;
console.log(url);

// Sélectionner la boîte où afficher les questions du quiz
const quizBox = document.getElementById("quiz-box");

// Effectuer une requête AJAX pour obtenir les données du quiz au format JSON
$.ajax({
    type: 'GET',
    // Utiliser l'URL pour obtenir les données du quiz
    url: `${url}data/`,
    success: function(response) {
        console.log(response);
        // Parcourir les données reçues
        const data = response.data;
        data.forEach(el => {
            // Parcourir chaque question et ses réponses
            for (const [question, answers] of Object.entries(el)) {
                // Ajouter une ligne pour chaque question
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `;
                // Ajouter un bouton radio pour chaque réponse
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `;
                });
            }
        });
    },
    error: function(error) {
        console.log(error);
    }
});


const quizForm = document.getElementById("quiz-form")
const csrf = document.getElementsByName("csrfmiddlewaretoken")


const sendData = () =>{
const elements = [...document.getElementsByClassName("ans")]
const data = {}
data["csrfmiddlewaretoken"] = csrf[0].value
elements.forEach(el=>{
    if (el.checked) {
  
        data[el.name] = el.value
         }else{
           if (!data[el.name]){
               data[el.name] = null
    }
    
    }
     

})
}

$ajax({
      type: "POST",
      url:  `{url}save/`,
      data: data,
      success: function(response){console.log(response)},
      error:function(error){console.log(error)}

})


quizForm.addEventListener("submit",e=>{
       e.preventDefault()
       sendData()

})