from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import languages_dict, google_translate, language_2_code, detect_language
from .serializers import LanguageSerializer
from main.decorator import user_rate_limit # noqa


class LanguageListView(APIView):

    def get(self, request, format=None):
        source_language = request.query_params.get('source_language')

        if not source_language:
            return Response({'error': 'Source Language Parameter is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        if source_language not in languages_dict:
            return Response({'error': 'Invalid Source Language'}, status=status.HTTP_400_BAD_REQUEST)

        target_languages = languages_dict[source_language]

        serializer = LanguageSerializer(data={
            'source_lang': source_language,
            'target_languages': target_languages
        })

        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranslateView(APIView):

    @user_rate_limit
    def post(self, request):

        text = request.data.get('text')
        src_lang = request.data.get('src_lang')
        dest_lang = request.data.get('dest_lang')

        print(text, src_lang, dest_lang)

        if not text or not src_lang or not dest_lang:
            return Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)

        if src_lang not in languages_dict:
            return Response({'error': 'Invalid Source Language'}, status=status.HTTP_400_BAD_REQUEST)

        if dest_lang not in languages_dict[src_lang]:
            return Response({'error': 'Invalid Source-Destination Language'}, status=status.HTTP_400_BAD_REQUEST)

        translated_text = google_translate(text, language_2_code[src_lang], language_2_code[dest_lang])

        return Response({'translated_text': translated_text}, status=status.HTTP_200_OK)


class DetectLanguage(APIView):

    def post(self, request):
        print("Here is the Data")
        text = request.data.get('text')

        if text is None:
            return Response({'error': 'Text missing'},
                            status=status.HTTP_400_BAD_REQUEST)

        detected_language = detect_language(text)

        if detected_language == '':
            return Response({'error': 'Unknown Language'},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'detectedLanguage': detected_language},
                        status=status.HTTP_200_OK)
