from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from model_utils.models import TimeStampedModel


class Cover(TimeStampedModel):
    cover = models.ImageField(_('cover'), upload_to='covers/%Y/%m/%d/')
    cover_370_230 = ImageSpecField(source='cover',
                                   processors=[ResizeToFill(370, 230)],
                                   format='JPEG',
                                   options={'quality': 100})
    cover_770_300 = ImageSpecField(source='cover',
                                   processors=[ResizeToFill(770, 300)],
                                   format='JPEG',
                                   options={'quality': 100})
    cover_caption = models.CharField(_('caption'), max_length=255, blank=True)

    def __str__(self):
        return 'Cover-{0}: {1}'.format(self.pk, self.cover_caption or self.cover.name)

    class Meta:
        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'
