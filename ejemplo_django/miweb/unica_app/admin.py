from django.contrib import admin
from unica_app.models import NumeroHistorico, Persona
import datetime

@admin.register(NumeroHistorico)
class NumeroHistoricoAdmin(admin.ModelAdmin):
    def cuanto_paso(self,obj):
        return (datetime.datetime.now().replace(tzinfo=None) - obj.created_at.replace(tzinfo=None))

    list_display = ('number', 'created_at', 'cuanto_paso')

    # def view_birth_date(self, obj):
    #     return obj.birth_date

    # view_birth_date.empty_value_display = '???'

admin.site.register(Persona)

# @admin.register(ReviewFragment)
# class ReviewFragmentAdmin(admin.ModelAdmin):
#     def therapeuticsession_fragment__id(self,obj): return obj.therapeuticsession_fragment.id
#     def therapeuticsession_fragment__speaker(self,obj): return obj.therapeuticsession_fragment.speaker
#     def therapeuticsession_fragment__text(self,obj): return obj.therapeuticsession_fragment.text
#     list_display = ('timestamp','user','notes', 'therapeuticsession_fragment__id', 'therapeuticsession_fragment__speaker', 'therapeuticsession_fragment__text')

