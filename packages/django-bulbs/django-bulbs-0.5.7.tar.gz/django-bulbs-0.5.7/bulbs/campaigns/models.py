from django.db import models

from djbetty import ImageField

from djes.models import Indexable

from bulbs.content.models import ElasticsearchImageField


class Campaign(Indexable):

    sponsor_name = models.CharField(max_length=255)
    sponsor_logo = ImageField(null=True, blank=True)
    sponsor_url = models.URLField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    campaign_label = models.CharField(max_length=255)
    impression_goal = models.IntegerField(null=True, blank=True)

    class Mapping:
        sponsor_logo = ElasticsearchImageField()


class CampaignPixel(models.Model):

    LOGO = 0
    HOMEPAGE = 1
    PIXEL_TYPES = (
        (LOGO, 'Logo'),
        (HOMEPAGE, 'Homepage'),
    )

    campaign = models.ForeignKey(Campaign, related_name='pixels')
    url = models.URLField()
    pixel_type = models.IntegerField(choices=PIXEL_TYPES, default=LOGO)
