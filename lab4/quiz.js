const quizQuestions = [
    { question: "What is the colour of sky?", answer: "blue" },
    { question: "Which planet is known as the Red Planet?", answer: "mars" },
    { question: "What is 5 + 7?", answer: "12" },
    { question: "what is 25 times 25?", answer: "625" },
    { question: "language for reactivity in websites?", answer: "javascript" }
];

function runQuiz() {
    let score = 0;

    for (let i = 0; i < quizQuestions.length; i++) {
        let userAnswer = prompt(quizQuestions[i].question);

        if (userAnswer === null) {
            alert("Quiz ended early.");
            break;
        }

        userAnswer = userAnswer.toLowerCase().trim();

        if (userAnswer === quizQuestions[i].answer) {
            score++;
            alert("Correct");
        } else {
            alert("Incorrect. Correct answer:" + quizQuestions[i].answer);
        }
    }

    alert(`Your final score is ${score} out of ${quizQuestions.length}`);
}

runQuiz();