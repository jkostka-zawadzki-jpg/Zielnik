from django.db import migrations


def seed_teas(apps, schema_editor):
    TeaProduct = apps.get_model('Blog', 'TeaProduct')
    items = [
        {
            'name': 'Herbata z melisy',
            'image': 'melisa.png',
            'category': 'Relaks',
            'benefits': 'Uspokojenie, Sen',
            'caffeine_free': True,
            'price': 14.90,
            'description': 'Delikatny napar na wyciszenie po dniu.',
        },
        {
            'name': 'Rumianek klasyczny',
            'image': 'rumianek.png',
            'category': 'Trawienie',
            'benefits': 'Trawienie, Lagodzenie',
            'caffeine_free': True,
            'price': 12.50,
            'description': 'Lekka herbata lagodzaca i wspierajaca zoladek.',
        },
        {
            'name': 'Mieta pieprzowa',
            'image': 'mieta.png',
            'category': 'Trawienie',
            'benefits': 'Trawienie, Odswiezajaca',
            'caffeine_free': True,
            'price': 13.50,
            'description': 'Swiezy aromat i ulga po posilku.',
        },
        {
            'name': 'Lawenda i lipa',
            'image': 'lawendailipa.png',
            'category': 'Sen',
            'benefits': 'Sen, Relaks',
            'caffeine_free': True,
            'price': 16.00,
            'description': 'Mieszanka na spokojny wieczor.',
        },
        {
            'name': 'Imbir i cytryna',
            'image': 'sklep.png',
            'category': 'Odpornosc',
            'benefits': 'Odpornosc, Rozgrzewajaca',
            'caffeine_free': True,
            'price': 15.90,
            'description': 'Rozgrzewajacy napar na chlodne dni.',
        },
        {
            'name': 'Pokrzywa z mieta',
            'image': 'sklep.png',
            'category': 'Oczyszczenie',
            'benefits': 'Oczyszczenie, Swiezosc',
            'caffeine_free': True,
            'price': 17.50,
            'description': 'Lekka mieszanka do codziennego picia.',
        },
        {
            'name': 'Szalwia i tymianek',
            'image': 'sklep.png',
            'category': 'Odpornosc',
            'benefits': 'Odpornosc, Gardlo',
            'caffeine_free': True,
            'price': 18.90,
            'description': 'Aromatyczna herbata na sezon jesienny.',
        },
        {
            'name': 'Zielona z jasminezka',
            'image': 'sklep.png',
            'category': 'Energia',
            'benefits': 'Energia, Koncentracja',
            'caffeine_free': False,
            'price': 19.50,
            'description': 'Delikatna zielona herbata z nutami jasminu.',
        },
        {
            'name': 'Dziurawiec i dzika roza',
            'image': 'sklep.png',
            'category': 'Nastroj',
            'benefits': 'Nastroj, Odpornosc',
            'caffeine_free': True,
            'price': 21.00,
            'description': 'Mieszanka na lepszy dzien.',
        },
        {
            'name': 'Rooibos waniliowy',
            'image': 'sklep.png',
            'category': 'Relaks',
            'benefits': 'Relaks, Slodycz',
            'caffeine_free': True,
            'price': 18.00,
            'description': 'Naturalnie bezkofeinowy rooibos.',
        },
    ]

    for data in items:
        TeaProduct.objects.get_or_create(name=data['name'], defaults=data)


def unseed_teas(apps, schema_editor):
    TeaProduct = apps.get_model('Blog', 'TeaProduct')
    names = [
        'Herbata z melisy',
        'Rumianek klasyczny',
        'Mieta pieprzowa',
        'Lawenda i lipa',
        'Imbir i cytryna',
        'Pokrzywa z mieta',
        'Szalwia i tymianek',
        'Zielona z jasminezka',
        'Dziurawiec i dzika roza',
        'Rooibos waniliowy',
    ]
    TeaProduct.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_teaproduct'),
    ]

    operations = [
        migrations.RunPython(seed_teas, reverse_code=unseed_teas),
    ]
