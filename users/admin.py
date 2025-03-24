from django.contrib import admin
from .models import UserProfile
from .models import Availability
from .models import ReferralProfile

#from .models import view_availability
#from .models import edit_availability


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Availability)
admin.site.register(ReferralProfile)
#admin.site.register(view_availability)
#admin.site.register(edit_availability)
#admin.site.register(edit_profile)
#admin.site.register(delete_account)
#admin.site.register(home)


