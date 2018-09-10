from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from .models import Word,WordRelation,Example,WordExampleRelation

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Word
        fields      = ['id','word','definition','pic']

class WordRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model       = WordRelation
        fields      = ['parent_id','child_id','relation']
        validators = [
            UniqueTogetherValidator(
                queryset = WordRelation.objects.all(),
                fields=('parent_id','child_id')
            )
        ]

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Example
        fields      = "__all__"

class WordExampleRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model       = WordExampleRelation
        fields      = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset = WordExampleRelation.objects.all(),
                fields=('word_id','example_id')
            )
        ]