from celery import shared_task
from django.utils.translation import gettext_noop

from common.utils import get_logger
from orgs.utils import org_aware_func, tmp_to_root_org
from django.utils.translation import ugettext_lazy as _

logger = get_logger(__file__)
__all__ = [
    'push_accounts_to_assets',
]


@org_aware_func("assets")
def push_accounts_to_assets_util(accounts, assets, username=None):
    from assets.models import PushAccountAutomation
    task_name = gettext_noop("Push accounts to assets")
    task_name = PushAccountAutomation.generate_unique_name(task_name)
    if username is None:
        account_usernames = list(accounts.values_list('username', flat=True))
    else:
        account_usernames = [username]

    data = {
        'name': task_name,
        'accounts': account_usernames,
        'comment': ', '.join([str(i) for i in assets])
    }
    instance = PushAccountAutomation.objects.create(**data)
    instance.assets.add(*assets)
    instance.execute()


@shared_task(queue="ansible", verbose_name=_('Push accounts to assets'))
def push_accounts_to_assets(account_ids, asset_ids, username=None):
    from assets.models import Asset, Account
    with tmp_to_root_org():
        assets = Asset.objects.filter(id__in=asset_ids)
        accounts = Account.objects.filter(id__in=account_ids)

    return push_accounts_to_assets_util(accounts, assets, username)
