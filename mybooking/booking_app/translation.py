from .models import (Country, City, Services, Hotel, Room)
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class ProductTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(City)
class ProductTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Services)
class ProductTranslationOptions(TranslationOptions):
    fields = ('service_name',)


@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'street', 'description')


@register(Room)
class ProductTranslationOptions(TranslationOptions):
    fields = ('room_type', 'room_status', 'description')