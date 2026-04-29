from deep_translator import GoogleTranslator

my_translator = GoogleTranslator(source="ko", target="en")
result = my_translator.translate("국어 점수를 입력하세요.")
print(result)