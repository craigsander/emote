from django.contrib import admin
from . import models

model = (
models.Incident,
models.Checkin,
models.Quote,

)




admin.site.register(model)
