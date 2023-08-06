django-admin-daterange-filter/README.rst
=====
admin_daterange_filter
=====

DateRangeFilter in django admin 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "admin_daterange_filter" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'admin_daterange_filter',
    )
2. use DateRangeFilter in list_filter::
	class YourAdmin(admin.ModelAdmin):
		list_filter=(
			('yourdate',DateRangeFilter),
		)

3. note:
	jquery-core use django.jquery, so I only modify the js file for Chinese Language, you can modify yourself for other's language