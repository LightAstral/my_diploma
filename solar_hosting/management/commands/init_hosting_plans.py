from django.core.management.base import BaseCommand
from solar_hosting.models import HostingPlan


class Command(BaseCommand):
    help = 'Initialize Hosting Plans'

    def handle(self, *args, **options):
        # Ваш код для создания и сохранения экземпляров HostingPlan
        basic_plan = HostingPlan(name='Basic Plan', plan_id='basic', price=9.99, description='Basic hosting plan',
                                 domains=1, disk_space=10, bandwidth=100, free_domains=0)
        basic_plan.save()

        premium_plan = HostingPlan(name='Premium Plan', plan_id='premium', price=19.99,
                                   description='Premium hosting plan', domains=5, disk_space=50, bandwidth=500,
                                   free_domains=1)
        premium_plan.save()

        ultimate_plan = HostingPlan(name='Ultimate Plan', plan_id='ultimate', price=29.99,
                                    description='Ultimate hosting plan', domains=10, disk_space=100, bandwidth=1000,
                                    free_domains=5)
        ultimate_plan.save()

        self.stdout.write(self.style.SUCCESS('Hosting Plans initialized successfully'))
