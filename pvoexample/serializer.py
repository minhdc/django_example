from rest_framework import serializers

from .models import Word,WordRelation

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Word
        fields      = ['id','word','definition','pic']

class WordRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model       = WordRelation
        fields      = ['word1_id','word2_id','relation']