from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class FirstName(models.Model):
    name = models.CharField(max_length=100, unique=True)
    FEMALE = 'f'
    MALE = 'm'
    SEX = (
        (FEMALE, 'female'),
        (MALE, 'male')
    )
    sex = models.CharField(max_length=1, choices=SEX)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LastName(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def form_is_determined_by_sex(self):
        """
        According to http://sjp.pwn.pl/poradnia/haslo/nazwiska-kobiet;3521.html,
        we want to replace letters 'i' and 'y' with 'a' for female names.
        """
        return self.name.endswith(('i', 'y'))
    form_is_determined_by_sex.short_description = 'Sex-determined form'
    form_is_determined_by_sex.boolean = True
    form_is_determined_by_sex.admin_order_field = 'name'

    def get_correct_form(self, sex):
        if sex == FirstName.FEMALE and self.form_is_determined_by_sex():
            return self.name[0:-1] + 'a'
        return self.name

    def __str__(self):
        return self.name
