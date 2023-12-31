# Generated by Django 4.2.5 on 2023-09-09 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="game",
            name="home_team",
        ),
        migrations.AddField(
            model_name="player",
            name="assists",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="blocks",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="defensive_fouls",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="defensive_rebounds",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="free_throws_attempted",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="free_throws_made",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="is_starter",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="player",
            name="minutes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="offensive_fouls",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="offensive_rebounds",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="points",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="steals",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.team"
            ),
        ),
        migrations.AddField(
            model_name="player",
            name="three_pointers_attempted",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="three_pointers_made",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="turnovers",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="two_pointers_attempted",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="two_pointers_made",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="Shot",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_make", models.BooleanField()),
                ("location_x", models.DecimalField(decimal_places=2, max_digits=5)),
                ("location_y", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.player"
                    ),
                ),
            ],
        ),
    ]
