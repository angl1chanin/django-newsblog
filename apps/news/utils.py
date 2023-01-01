from django.template.defaultfilters import slugify as django_slugify
from random import randint

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya', 'ь': ''}


def slugify_title(s: str) -> str:
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower())) + '-' + str(randint(10000, 99999))


def slugify_str(string: str) -> str:
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


def rename_photo_to_slug(filename: str, article_slug: str) -> str:
    file_extension = filename.split('.')[1]
    return article_slug + file_extension
