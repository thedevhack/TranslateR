from rest_framework import serializers


class LanguageSerializer(serializers.Serializer):
    source_lang = serializers.CharField()
    target_languages = serializers.ListField()
