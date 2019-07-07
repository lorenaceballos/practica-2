
from django.db import models




class Question(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Fecha de publicacion')
    
	def __str__(self):
		return self.question_text

	


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=100)
	correcto= models.BooleanField(default=False)
    
	def __str__(self):
		return self.choice_text
   
