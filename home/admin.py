from django.contrib import admin


from .models import IconsForDesktop , BottomSideIcons , HandGest, CommandHistory

admin.site.register(IconsForDesktop)
admin.site.register(BottomSideIcons)
admin.site.register(HandGest)
admin.site.register(CommandHistory)
