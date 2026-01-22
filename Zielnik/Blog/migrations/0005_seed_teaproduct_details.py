from django.db import migrations


def seed_details(apps, schema_editor):
    TeaProduct = apps.get_model('Blog', 'TeaProduct')
    details = {
        'Herbata z melisy': {
            'image': 'melisa.png',
            'origin': 'Polska, regiony podmiejskie i ogrody zielarskie',
            'grows_where': 'Melisa rośnie na słonecznych stanowiskach, na lekkich i przepuszczalnych glebach. Spotkasz ją w ogrodach i na małych plantacjach.',
            'properties': 'Wycisza, wspiera sen, łagodzi napięcie i delikatnie wspiera trawienie.',
            'history': 'W klasztornych ogrodach średniowiecznej Europy melisa uchodziła za ziele poprawiające nastrój.',
        },
        'Rumianek klasyczny': {
            'image': 'rumianek.png',
            'origin': 'Polska i Europa Srodkowa',
            'grows_where': 'Najczesciej na lakach, miedzach i polach uprawnych, w miejscach naslonecznionych.',
            'properties': 'Lagodzi, wspiera trawienie i pomaga ukoić podraznienia.',
            'history': 'Rumianek byl ceniony juz w starozytnym Egipcie i Grecji jako ziolo naparowe i do okladów.',
        },
        'Mieta pieprzowa': {
            'image': 'mieta.png',
            'origin': 'Europa, uprawy zielarskie',
            'grows_where': 'Lubi wilgotne gleby i polcien, czesto rośnie w ogrodach przydomowych.',
            'properties': 'Odswiezajaca, wspiera trawienie i pomaga przy uczuciu ciezkosci.',
            'history': 'W starozytnej Grecji mieta byla symbolem goscinnosci i uzywana do aromatyzowania napojow.',
        },
        'Lawenda i lipa': {
            'image': 'lawendailipa.png',
            'origin': 'Lawenda z poludnia Europy, lipa z regionu CEE',
            'grows_where': 'Lawenda rośnie na suchych, slonecznych stanowiskach, a lipy tworza alejki i lasy w strefie umiarkowanej.',
            'properties': 'Wycisza, ulatwia zasypianie i uspokaja wieczorny rytual.',
            'history': 'Lawenda byla uzywana w rzymskich lazniach, a lipa od wiekow towarzyszy slowianskim naparom.',
        },
        'Imbir i cytryna': {
            'image': 'imbircytryna.png',
            'origin': 'Imbir z Azji, cytryna z basenu Morza Srodziemnego',
            'grows_where': 'Imbir wymaga klimatu tropikalnego, cytryny rosna w cieplym i slonecznym klimacie.',
            'properties': 'Rozgrzewa, wspiera odpornosc i dodaje energii.',
            'history': 'Imbir byl ceniony na Jedwabnym Szlaku jako korzen rozgrzewajacy i dodatek do naparow.',
        },
        'Pokrzywa z mieta': {
            'image': 'pokrzywa z mieta.png',
            'origin': 'Europa, lokalne zbiory',
            'grows_where': 'Pokrzywa rosnie na zyznych glebach, mieta preferuje miejsca wilgotne i polcieniste.',
            'properties': 'Wspiera oczyszczenie, mineralizuje i odswieza.',
            'history': 'Pokrzywa byla wiosennym ziolowym klasykiem w kuchni ludowej i naparach codziennych.',
        },
        'Szalwia i tymianek': {
            'image': 'szalwiatymianek.png',
            'origin': 'Basen Morza Srodziemnego',
            'grows_where': 'Rosna na suchych, slonecznych stanowiskach i kamienistych glebach.',
            'properties': 'Wspiera gardlo i odpornosc, ma intensywny aromat.',
            'history': 'Szalwia byla uznawana za ziolo dlugowiecznosci, a tymianek za ziolo odwagi.',
        },
        'Zielona z jasminezka': {
            'image': 'zielonajasmin.png',
            'origin': 'Chiny',
            'grows_where': 'Herbata zielona rośnie na plantacjach w klimacie subtropikalnym.',
            'properties': 'Delikatnie pobudza, wspiera koncentracje i daje lekka swiezosc.',
            'history': 'Jasminowa herbata powstala w Chinach w okresie dynastii Song jako napar o wyjatkowym aromacie.',
        },
        'Dziurawiec i dzika roza': {
            'image': 'dziurawiec.png',
            'origin': 'Europa',
            'grows_where': 'Dziurawiec rosnie na lakach i nieuzytkach, dzika roza w zywoplotach i na skrajach lasow.',
            'properties': 'Wspiera nastroj i odpornosc, dodaje lekko kwaskowatej nuty.',
            'history': 'Dziurawiec tradycyjnie zbierano w okolicach Nocy Swietojanskiej.',
        },
        'Rooibos waniliowy': {
            'image': 'roibos.png',
            'origin': 'RPA, region Cederberg',
            'grows_where': 'Rooibos rosnie w suchym klimacie i na piaszczystych glebach.',
            'properties': 'Naturalnie bezkofeinowy, lagodny i slodkawy.',
            'history': 'Rooibos to tradycyjny napar rdzennych mieszkancow RPA.',
        },
    }

    for name, data in details.items():
        TeaProduct.objects.filter(name=name).update(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_teaproduct_fields_and_images'),
    ]

    operations = [
        migrations.RunPython(seed_details, reverse_code=migrations.RunPython.noop),
    ]
