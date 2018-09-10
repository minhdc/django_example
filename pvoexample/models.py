from django.urls import reverse
from django.db import models

# Create your models here.


class Word(models.Model):
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length = 50)
    definition = models.TextField(default="")  
    pic = models.ImageField(default="",upload_to="img")
    
    def get_absolute_url(self):
        return reverse('word:detail',kwargs={"id":self.id})

class Example(models.Model):
    id = models.BigAutoField(primary_key=True)
    example_desc = models.TextField()
    keywords = models.TextField(default="nokeyword")
    source = models.CharField(max_length = 200)    
        

class WordExampleRelation(models.Model):
    word_id = models.ForeignKey(Word,on_delete = models.CASCADE) # need to reconsider
    example_id = models.ForeignKey(Example,on_delete = models.CASCADE)
    relation_id = models.SmallIntegerField(null=False)       

class WordRelation(models.Model):
    #word1_id = models.ForeignKey(Word,on_delete = models.CASCADE,related_name='word1_id')
    #word2_id = models.ForeignKey(Word,on_delete = models.CASCADE,related_name='word2_id')    
    parent_id = models.ForeignKey(Word,on_delete = models.CASCADE,related_name='parent_id')
    child_id = models.ForeignKey(Word,on_delete = models.CASCADE,related_name='child_id')    
    relation = models.SmallIntegerField()


