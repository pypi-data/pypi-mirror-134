# Generated by Django 3.1.5 on 2021-01-17 19:01

import random
import string

from django.db import migrations

from juntagrico.entity.member import Member


def fix_user_field(apps, schema_editor):
    # In case there are legacy members with user field None, trigger
    # standard pre-save option to create corresponding users
    for m in Member.objects.all():
        if getattr(m, 'user', None) is None:
            m.save()


def fix_user_field_reverse(apps, schema_editor):
    pass


def assign_sort_order(apps, entity, order_key):
    entity_class = apps.get_model('juntagrico', entity)
    for idx, item in enumerate(entity_class.objects.all().order_by(order_key)):
        item.sort_order = idx + 1
        item.save()


def depot_code_to_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'Depot', 'code')


def sort_order_to_depot_code(apps, schema_editor):
    Depots = apps.get_model('juntagrico', 'Depot')
    for depot in Depots.objects.all():
        # sort_order is not guaranteed to be unique, so append random string to ensure uniqueness
        depot.code = '{:05d}'.format(depot.sort_order) + '_' + ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=7))
        depot.save()


def subscriptionproduct_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'SubscriptionProduct', 'pk')


def activityarea_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'ActivityArea', 'pk')


def extrasubscriptioncategory_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'ExtraSubscriptionCategory', 'pk')


def extrasubscriptiontype_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'ExtraSubscriptionType', 'pk')


def subscriptiontype_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'SubscriptionType', 'pk')


def listmessage_sort_order(apps, schema_editor):
    assign_sort_order(apps, 'ListMessage', 'sort_order')


def sort_order_pass(apps, schema_editor):
    pass


def migrate_extras(apps, schema_editor):
    SubscriptionProduct = apps.get_model('juntagrico', 'SubscriptionProduct')
    SubscriptionSize = apps.get_model('juntagrico', 'SubscriptionSize')
    SubscriptionType = apps.get_model('juntagrico', 'SubscriptionType')
    SubscriptionPart = apps.get_model('juntagrico', 'SubscriptionPart')
    ExtraSubscriptionCategory = apps.get_model('juntagrico', 'ExtraSubscriptionCategory')
    ExtraSubscriptionType = apps.get_model('juntagrico', 'ExtraSubscriptionType')
    ExtraSubscription = apps.get_model('juntagrico', 'ExtraSubscription')
    ExtraSubBillingPeriod = apps.get_model('juntagrico', 'ExtraSubBillingPeriod')
    subprods = {}
    for ecat in ExtraSubscriptionCategory.objects.all():
        name = ecat.name
        number = 0
        while SubscriptionProduct.objects.filter(name=name).count() > 0:
            name = ecat.name + str(number)
            number = number + 1
        subprod_data = {
            'name': name,
            'description': ecat.description,
            'is_extra': True
        }
        subprods[ecat] = SubscriptionProduct.objects.create(**subprod_data)
    subtypes = {}
    for etype in ExtraSubscriptionType.objects.all():
        subsize_data = {
            'name': etype.name,
            'long_name': etype.size,
            'units': etype.id,
            'depot_list': etype.depot_list,
            'visible': etype.visible,
            'description': etype.description,
            'product': subprods[etype.category]
        }
        subtype_data = {
            'name': 'standard',
            'long_name': '',
            'size': SubscriptionSize.objects.create(**subsize_data),
            'required_assignments': 0,
            'price': 0,
            'visible': etype.visible,
            'description': ''
        }
        subtypes[etype] = SubscriptionType.objects.create(**subtype_data)
    for esub in ExtraSubscription.objects.all():
        subpart_data = {
            'subscription': esub.main_subscription,
            'type': subtypes[esub.type],
            'creation_date': esub.creation_date,
            'activation_date': esub.activation_date,
            'cancellation_date': esub.cancellation_date,
            'deactivation_date': esub.deactivation_date
        }
        SubscriptionPart.objects.create(**subpart_data)
    for esbp in ExtraSubBillingPeriod.objects.all():
        esbp.type2 = subtypes[esbp.type]
        esbp.save()


class Migration(migrations.Migration):
    dependencies = [
        ('juntagrico', '0031_pre_1_4'),
    ]

    operations = [
        migrations.RunPython(migrate_extras),
        migrations.RunPython(fix_user_field, fix_user_field_reverse),
        migrations.RunPython(depot_code_to_sort_order, sort_order_to_depot_code),
        migrations.RunPython(activityarea_sort_order, sort_order_pass),
        migrations.RunPython(subscriptionproduct_sort_order, sort_order_pass),
        migrations.RunPython(extrasubscriptioncategory_sort_order, sort_order_pass),
        migrations.RunPython(extrasubscriptiontype_sort_order, sort_order_pass),
        migrations.RunPython(subscriptiontype_sort_order, sort_order_pass),
        migrations.RunPython(listmessage_sort_order, sort_order_pass),
    ]
