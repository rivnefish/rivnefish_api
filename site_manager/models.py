from django.db import models


class Countries(models.Model):

    country_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'countries'


class Regions(models.Model):

    region_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    country_id = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'regions'


class Districts(models.Model):

    district_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    region = models.ForeignKey(Regions)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'districts'


class Fishes(models.Model):

    fish_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ukr_name = models.CharField(max_length=255, blank=True)
    icon_url = models.CharField(max_length=2083)
    icon_width = models.IntegerField()
    icon_height = models.IntegerField()
    latin_name = models.CharField(max_length=255, blank=True)
    eng_name = models.CharField(max_length=255, blank=True)
    folk_name = models.CharField(max_length=255, blank=True)
    predator = models.CharField(max_length=3, blank=True)
    redbook = models.CharField(max_length=3, blank=True)
    picture = models.CharField(max_length=2083, blank=True)
    description = models.TextField(blank=True)
    article_url = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'fishes'


class Markers(models.Model):

    PERMIT_CHOICES = (('free', 'free'),
                      ('paid', 'paid'),
                      ('prohibited', 'prohibited'),
                      ('unknown', 'unknown'))
    TIME_TO_FISH_CHOICES = (('24h', '24h'),
                            ('daylight', 'daylight'),
                            ('unknown', 'unknown'))

    marker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    area = models.IntegerField(null=True, blank=True)
    content = models.TextField(blank=True)
    conveniences = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    max_depth = models.DecimalField(null=True, max_digits=8, decimal_places=2,
                                    blank=True)
    average_depth = models.DecimalField(null=True, max_digits=8,
                                        decimal_places=2, blank=True)
    distance_to_rivne = models.IntegerField(null=True,
                                            db_column='distance_to_Rivne',
                                            blank=True)
                                            # Field name made lowercase.
    permit = models.CharField(max_length=30, choices=PERMIT_CHOICES,
                              default='unknown')

    price_24h = models.DecimalField(null=True, max_digits=7, decimal_places=2,
                                    blank=True)
    dayhour_price = models.DecimalField(null=True, max_digits=7,
                                        decimal_places=2, blank=True)
    boat_usage = models.CharField(max_length=3, blank=True)
    time_to_fish = models.CharField(max_length=24, blank=True,
                                    choices=TIME_TO_FISH_CHOICES,
                                    default='unknown')
    paid_fish = models.TextField(blank=True)
    note = models.TextField(blank=True)
    note2 = models.CharField(max_length=200)
    photo_url1 = models.CharField(max_length=2083, blank=True)
    photo_url2 = models.CharField(max_length=2083, blank=True)
    photo_url3 = models.CharField(max_length=2083, blank=True)
    photo_url4 = models.CharField(max_length=2083, blank=True)
    approval = models.CharField(max_length=24)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()
    author_id = models.IntegerField(null=True, blank=True)
    post_id = models.IntegerField(null=True, blank=True)
    gallery_id = models.IntegerField(null=True, blank=True)
    district = models.ForeignKey(Districts, null=True, db_column='district',
                                 blank=True)
    region = models.ForeignKey(Regions, null=True, db_column='region',
                               blank=True)
    country = models.ForeignKey(Countries, null=True, db_column='country',
                                blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'markers'


class MarkersFishes(models.Model):

    id = models.AutoField(primary_key=True)
    marker = models.ForeignKey(Markers, related_name='fishes_set')
    fish = models.ForeignKey(Fishes, related_name='markers_set')
    weight_avg = models.IntegerField(null=True, blank=True)
    weight_max = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.marker.name

    class Meta:
        db_table = u'markers_fishes'


class MarkersLog(models.Model):

    log_id = models.AutoField(primary_key=True)
    log_text = models.TextField()
    user_info = models.TextField(blank=True)
    log_date = models.DateTimeField()

    #==========================================================================
    # def __unicode__(self):
    #     return ''
    #==========================================================================

    class Meta:
        db_table = u'markers_log'


class Passports(models.Model):

    passport_id = models.AutoField(primary_key=True)
    marker = models.ForeignKey(Markers)
    url_suffix = models.CharField(max_length=600)
    modify_date = models.DateTimeField()
    icon_url = models.CharField(max_length=6249, blank=True)

    #===========================================================================
    # def __unicode__(self):
    #     return self.marker.name
    #===========================================================================

    class Meta:
        db_table = u'passports'
