from django.contrib import admin
from jobapp.models import (
    Question,
    Topic,
    Circular,
    Organization,
    catagory,
    postName,
    savedCircular,
    circularImage,
    examQuestion,
    questionImage,
)

# Register your models here.
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Circular)
admin.site.register(Organization)
admin.site.register(catagory)
admin.site.register(postName)
admin.site.register(savedCircular)
admin.site.register(circularImage)
admin.site.register(examQuestion)
admin.site.register(questionImage)
