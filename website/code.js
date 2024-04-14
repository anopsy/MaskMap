
let url = "http://localhost:5000/predict";
let answer;

document.getElementById('myForm').addEventListener('submit', function(event) {
  event.preventDefault();
  answer = document.getElementById('fname').value;
  console.log("Tekst zapisany w input_user: " + answer );
  //let selectedOption = document.querySelector('input[name="option"]:checked').value;
 // console.log("Wybrana opcja: " + selectedOption);

  //czyści pole tekstowe
  document.getElementById('fname').value = "";

  let input_user = {"text": answer};

  console.log(input_user);

  fetch(url, {
      method: 'POST', 
      mode: 'cors',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(input_user) 
  })
  .then( function(response){
          response.json().then( function(data){
              console.log(data);
              updateResponse(data)
          });
        });
});

function updateResponse(data) {
  console.log("chla: " + data.prediction);
  const dataValue = data.prediction;
  let resultElement = document.getElementById('question-result');
  resultElement.textContent = dataValue;
};

let randomQuestions = [
  "Can you share an instance when you deliberately copied someone’s body language or facial expressions during an interaction?",
  "How do you monitor your body language or facial expressions to appear relaxed?",
  "Can you describe a situation where you didn’t feel the need to put on an act to get through it?",
  "What kind of script have you developed to follow in social situations?",
  "How do you adjust your body language or facial expressions to appear interested in the person you are interacting with?",
  "Can you describe a situation where you felt like you were ‘performing’ rather than being yourself?",
  "What are some behaviors you’ve learned from watching others that you use in your own social interactions?",
  "How often do you think about the impression you make on other people?",
  "In what ways do you rely on the support of others to socialize?",
  "How do you practice your facial expressions and body language to ensure they look natural?",
  "Can you explain why you don’t feel the need to make eye contact with others if you don’t want to?",
  "Can you share an experience where you had to force yourself to interact with people in a social situation?",
  "How have you tried to improve your understanding of social skills by watching others?",
  "How do you monitor your body language or facial expressions to appear interested in the person you’re interacting with?",
  "What strategies do you use to avoid interacting with others in social situations?",
  "What kind of research have you done on the rules of social interactions to improve your social skills?",
  "How do you maintain awareness of the impression you make on others?",
  "Can you describe a situation where you felt free to be yourself with others?",
  "How do you learn about body language and facial expressions from television, films, or fiction?",
  "How do you adjust your body language or facial expressions to appear relaxed?",
  "Can you describe a conversation where you felt it flowed naturally?",
  "What social skills have you learned from television shows and films, and how do you use them in your interactions?",
  "Can you explain why you don’t pay attention to what your face or body are doing during social interactions?",
  "Can you share a situation where you felt like you were pretending to be ‘normal’ in a social situation?"
];

// Funkcja do generowania losowego pytania
function generateRandomQuestion() {
  let randomIndex = Math.floor(Math.random() * randomQuestions.length);
  return randomQuestions[randomIndex];
}

// Funkcja do wyświetlania losowego pytania
function displayRandomQuestion() {
  let randomQuestions = generateRandomQuestion();
  document.getElementById('question').textContent =randomQuestions;
}









