from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import flourish_child_admin
from ..forms import Brief2SelfReportedForm
from ..models import Brief2SelfReported
from .model_admin_mixins import ChildCrfModelAdminMixin


@admin.register(Brief2SelfReported, site=flourish_child_admin)
class Brief2SelfReportedAdmin(ChildCrfModelAdminMixin, admin.ModelAdmin):

    form = Brief2SelfReportedForm

    fieldsets = (
        (None, {
            'fields': [
                'child_visit',
                'report_datetime',
                'short_attention_span',
                'task_completion_prob',
                'bothered_by_change',
                'no_planning',
                'impulsive',
                'poor_writing',
                'stuck_on_activty',
                'easily_upset',
                'overreact',
                'forgetful',
                'delayed_task_completion',
                'unthinking'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {'short_attention_span': admin.VERTICAL,
                    'task_completion_prob': admin.VERTICAL,
                    'bothered_by_change': admin.VERTICAL,
                    'no_planning': admin.VERTICAL,
                    'impulsive': admin.VERTICAL,
                    'poor_writing': admin.VERTICAL,
                    'stuck_on_activty': admin.VERTICAL,
                    'easily_upset': admin.VERTICAL,
                    'overreact': admin.VERTICAL,
                    'forgetful': admin.VERTICAL,
                    'delayed_task_completion': admin.VERTICAL,
                    'unthinking': admin.VERTICAL, }
