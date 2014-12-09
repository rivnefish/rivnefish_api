import django_filters


# Get example of custom filters here http://bit.ly/1ythc3Z
class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',') if v]
            qs.filter(**{'%s__%s' % (self.name,
                                     self.lookup_type): integers})
        return qs


class IntegerListFilterUniq(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            for _id in set([int(v) for v in value.split(',') if v]):
                qs = qs.filter(fishes_set__fish=_id)
        return qs
