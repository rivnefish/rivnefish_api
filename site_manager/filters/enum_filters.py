import django_filters


class FilterForEnumField(django_filters.Filter):
    """
    """

    def __init__(self, *args, **kwargs):
        self.available = kwargs.pop('available', None)
        self.used_int = kwargs.pop('used_int', None)
        super(FilterForEnumField, self).__init__(*args, **kwargs)

    def filter(self, qs, value):
        if not self.available:
            return qs

        if self.used_int and value:
            try:
                value = int(value)
            except Exception as err:
                # print err
                value = 0

        if value and value in self.available:
            print {'%s__%s' % (self.name, self.lookup_type): value}
            return qs.filter(**{'%s__%s' % (self.name,
                                            self.lookup_type): value})
        return qs
