from django.db import models

# Create your models here.


class Word(models.Model):
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length = 50)
    definition = models.TextField(default="undefined")
    pic_url = models.URLField(default="")

class Example(models.Model):
    id = models.BigAutoField(primary_key=True)
    example_desc = models.TextField()
    keywords = models.TextField(default="nokeyword")
    source = models.CharField(max_length = 200)
    relation = models.IntegerField(default=-1)

class WordExampleRelation(models.Model):
    word_id = models.ForeignKey(Word,on_delete = models.CASCADE) # need to reconsider
    example_id = models.ForeignKey(Example,on_delete = models.CASCADE)
    relation = models.SmallIntegerField()

class WordRelation(models.Model):
    word1_id = models.ForeignKey(Word,on_delete = models.CASCADE,related_name='word1_id')
    word2_id = models.ForeignKey(Word,on_delete = models.CASCADE,related_name='word2_id')
    relation = models.SmallIntegerField()

