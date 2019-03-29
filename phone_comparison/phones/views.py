from django.shortcuts import render
from .models import Phone, Apple, Xiaomi, Motorola


def show_catalog(request):

    phones = Phone.objects.all()

    context = list()
    fields_verbose = list()
    fields_name = list()
    for phone in phones:
        for field in phone._meta.get_fields()[len(phones) + 2:]:
            if field.verbose_name not in fields_verbose:
                fields_verbose.append(field.verbose_name)
        for field in phone._meta.get_fields()[len(phones) + 2:]:
            if field.name not in fields_name:
                fields_name.append(field.name)

    for phone in [Apple, Xiaomi, Motorola]:
        for field in phone._meta.get_fields()[1:]:
            if field.verbose_name not in fields_verbose:
                fields_verbose.append(field.verbose_name)
        for field in phone._meta.get_fields()[1:]:
            if field.name not in fields_name:
                fields_name.append(field.name)

    for fields in fields_verbose:
        context.append([fields])

    for phone in Phone.objects.all():
        c = 0
        for field in fields_name:
            if hasattr(phone, field):
                context[c].append(getattr(phone, field))
                # c += 1
            else:
                for model in [Apple, Motorola, Xiaomi]:
                    if model.objects.filter(model_id=phone.id):
                        if hasattr(model.objects.get(model_id=phone.id), field):
                            context[c].append(getattr(model.objects.get(model_id=phone.id), field))
                        else:
                            context[c].append('-')
            c += 1
    print(Phone.objects.all())


    return render(
        request,
        'catalog.html',
        {'phones': context}
    )
