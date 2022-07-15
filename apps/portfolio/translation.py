from modeltranslation.translator import register, TranslationOptions
from .models import AboutMe

@register(AboutMe)
class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)