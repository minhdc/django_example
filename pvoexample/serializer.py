from rest_framework import serializers

from .models import Word,WordRelation,Example,WordExampleRelation

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Word
        fields      = ['id','word','definition','pic']

class WordRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model       = WordRelation
        fields      = ['word1_id','word2_id','relation']

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Example
        fields      = "__all__"

class WordExampleRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model       = WordExampleRelation
        fields      = "__all__"