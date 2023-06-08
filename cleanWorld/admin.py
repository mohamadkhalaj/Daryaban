from django.contrib import admin

from .models import cleans, contactus, garbageTypes, placeImages, reports, visitor

admin.site.site_header = "پنل ادمین دریابان"


def makeAsClean(modeladmin, request, queryset):
    rows_updated = queryset.update(cleanedStatus=True)
    if rows_updated == 1:
        message_bit = "one row marked as clean."
    else:
        message_bit = f"{rows_updated} rows marked as clean."

    modeladmin.message_user(request, message_bit)


makeAsClean.short_description = "انتخاب بعنوان تمیز شده"


def makeAsDirty(modeladmin, request, queryset):
    rows_updated = queryset.update(cleanedStatus=False)
    if rows_updated == 1:
        message_bit = "one row marked as dirty."
    else:
        message_bit = f"{rows_updated} rows marked as dirty."

    modeladmin.message_user(request, message_bit)


makeAsDirty.short_description = "انتخاب بعنوان آلوده شده"


class reportsAdmin(admin.ModelAdmin):
    list_display = ("reporter", "humanizeTime", "address", "cleanedStatus", "categoryToStr")
    list_filter = ("reporter", "cleanedStatus")
    actions = [makeAsClean, makeAsDirty]

    def categoryToStr(self, obj):
        return ", ".join([category.title for category in obj.garbageType.all()])

    categoryToStr.short_description = "دسته بندی ها"


admin.site.register(reports, reportsAdmin)


class cleansAdmin(admin.ModelAdmin):
    list_display = ("humanizeTime", "cleaner", "report")
    list_filter = ("cleaner", "report")


admin.site.register(cleans, cleansAdmin)


class contactusAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "text", "humanizeTime")
    list_filter = ("name", "email", "text")


admin.site.register(contactus, contactusAdmin)

admin.site.register(garbageTypes)


class placeImagesAdmin(admin.ModelAdmin):
    readonly_fields = ["image_tag"]
    list_display = ("image_tag", "user")


admin.site.register(placeImages, placeImagesAdmin)


class visitorAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "userAgent", "humanizeTime", "path", "isAdminPanel", "responseTime")
    list_filter = ("ip_address", "time", "isAdminPanel")
    search_fields = ("userAgent",)


admin.site.register(visitor, visitorAdmin)
