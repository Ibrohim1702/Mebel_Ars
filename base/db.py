



class ExtraModelHelper:
    def get_or_none(self, **kwargs):
        try:
            return self.objects.get(**kwargs)
        except:
            return None