from django.contrib import admin
from .models import OtherPacket, Video, ChapterPacket
# Register your models here.
admin.site.register(OtherPacket)
admin.site.register(ChapterPacket)
admin.site.register(Video)
