from django.db import models

from edc_base.utils import get_utcnow
from edc_base.model_validators import date_not_future
from edc_constants.choices import POS_NEG, YES_NO, YES_NO_NA
from edc_protocol.validators import date_not_before_study_start
from ..choices import HIV_STATUS

from .child_crf_model_mixin import ChildCrfModelMixin


class ChildPregTesting(ChildCrfModelMixin):

    test_done = models.CharField(
        verbose_name='Was a pregnancy test performed?',
        max_length=17,
        choices=YES_NO_NA)

    test_date = models.DateField(
        verbose_name='Date of pregnancy test',
        default=get_utcnow,
        validators=[date_not_future, date_not_before_study_start])

    preg_test_result = models.CharField(
        verbose_name='What is the result of the pregnancy test?',
        max_length=10,
        choices=POS_NEG,
        blank=True,
        null=True,)
    
    current_hiv_status = models.CharField(
        verbose_name="What is the current HIV status of this child/adolescent?",
        choices=HIV_STATUS,
        max_length=15,
        null=True,
        blank=True,
    )
    
    last_menstrual_period = models.DateField(
        verbose_name="Date of Last Menstrual Period (DD/MMM/YYYY)",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    is_lmp_date_estimated = models.CharField(
        verbose_name="Is the Last Menstrual Period date estimated?",
        choices=YES_NO,
        max_length=3,
        blank=True,
        null=True,
    )

    comments = models.TextField(blank=True, null=True)

    class Meta(ChildCrfModelMixin.Meta):
        app_label = 'flourish_child'
        verbose_name = 'Pregnancy Testing for Female Adolescents'
        verbose_name_plural = 'Pregnancy Testing for Female Adolescents'
       