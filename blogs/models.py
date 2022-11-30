from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title =models.CharField(max_length = 1000)
    content = models.TextField(blank = True)
    
    def __str__(self):
        return self.title
    

class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, max_length=100)

    def __str__(self):
        return self.movie_title


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "Choice: {}, Question:{}".format(self.choice_text, self.question.question_text)
