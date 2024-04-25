from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Update the site domain and name'

    def handle(self, *args, **kwargs):
        site = Site.objects.get_current()
        site.domain = "https://secureweb-beta.vercel.app" # Use your React app URL here
        site.name = 'Simple App'  # Choose a name for your site
        site.save()
        self.stdout.write(self.style.SUCCESS('Site domain and name updated successfully'))
