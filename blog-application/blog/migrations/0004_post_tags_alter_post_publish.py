# Generated by Django 5.1.1 on 2024-09-14 13:44

import datetime
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_publish_comment"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 9, 14, 13, 44, 37, 895156, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
