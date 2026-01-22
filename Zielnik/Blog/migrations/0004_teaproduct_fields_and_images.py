from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_seed_teaproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaproduct',
            name='origin',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='teaproduct',
            name='grows_where',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='teaproduct',
            name='properties',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='teaproduct',
            name='history',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='TeaProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Blog.teaproduct')),
            ],
        ),
    ]
