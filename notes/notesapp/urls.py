from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from notes import views as notes_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes_views.notes_list, name='notes_list'),
    path('notes/<int:pk>/', notes_views.note_details, name='note_details'),
    path('notes/create/', notes_views.notes_create, name='notes_create'),
    path('notes/update/<int:pk>/', notes_views.notes_update, name='notes_update'),
    path('notes/delete/<int:pk>/', notes_views.notes_delete, name='notes_delete'),
    path('notes/search', notes_views.notes_search, name='notes_search'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
