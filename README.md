## **Flask Application Design**

**App Name:** An app that helps you learn machine learning

### **HTML Files**

- **Home Page (`index.html`):** 
    - Title: Welcome to Machine Learning
    - Introduction to the purpose of the app
    - Navigation links to other pages
- **Lesson Page (`lesson.html`):** 
    - Title: Machine Learning Lesson
    - Display lesson content dynamically based on lesson ID
    - Navigation menu to browse lessons
- **Quiz Page (`quiz.html`):** 
    - Title: Machine Learning Quiz
    - Display quiz questions dynamically based on quiz ID
    - Form to submit quiz answers for evaluation

### **Routes**

- **Home Route (`/`):** 
    - HTTP Method: GET
    - Renders `index.html`
- **Lesson Route (`/lesson/<lesson_id>`):** 
    - HTTP Method: GET
    - Renders `lesson.html` with the specified lesson ID
- **Quiz Route (`/quiz/<quiz_id>`):** 
    - HTTP Method: GET
    - Renders `quiz.html` with the specified quiz ID
- **Quiz Submission Route (`/quiz-submit`):** 
    - HTTP Method: POST
    - Receives submitted quiz answers, evaluates them, and displays the result