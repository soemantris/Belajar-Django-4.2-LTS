from django.core.exceptions import ValidationError

user_tidak_boleh_posting = ['admin', 'operator', 'teknisi']


def validate_penulis(value):
    if value in user_tidak_boleh_posting:
        raise ValidationError(f'{value} tidak boleh posting artikel 🥲')

    # if 'admin' in value:
    #     raise ValidationError('admin tidak boleh posting artikel')


def validate_tag(value):
    if len(value) < 5:
        raise ValidationError('tag ini kurang dari 5 karakter!')
