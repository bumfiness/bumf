class Choices:
    """
    Helper class to make choices available as class variables, expose a list
    with valid choices and at the same time generate the choices tuples for
    the model class.

    Usage:
        class MyChoices(Choices):
            ONE = 'one'
            TWO = 'dwa'
            valid_choices = [ONE, TWO]

        class MyModel(models.Model):
            variant = models.CharField(
                max_length=MyChoices.get_max_length(),
                choices=MyChoices.get_choices(),
            )
    """
    @classmethod
    def get_choices(cls):
        return (
            (val, val) for val in cls.valid_choices
        )

    @classmethod
    def get_max_length(cls):
        return max([len(val) for val in cls.valid_choices])
