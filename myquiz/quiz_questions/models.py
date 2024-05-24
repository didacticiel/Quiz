from django.db import models
from quiz.models import Quiz

# Create your models here.

class Question(models.Model):
      text = models.CharField(max_length=255,help_text="Questions de quiz")
      quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,help_text="case des quiz (les choix)")
      created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return str(self.text)
          
          
      def get_answers(self):
          return self.answer_set.all()
          
          
class Answer(models.Model):
      text = models.CharField(max_length=255)
      correct = models.BooleanField(default=False)
      question = models.ForeignKey(Question,on_delete=models.CASCADE)
      created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return f"question: {self.question.text},answer: {self.text}, correct: {self.correct}"