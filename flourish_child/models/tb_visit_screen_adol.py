from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .model_mixins import CrfModelMixin
from ..choices import YES_NO_UNK_DWTA, COUGH_DURATION, YES_NO_DN_PNTA


class TbVisitScreeningAdolecent(CrfModelMixin):
    have_cough = models.CharField(
        verbose_name='Do you currently have a cough?',
        choices=YES_NO_UNK_DWTA,
        max_length=30)

    cough_duration = models.CharField(
        verbose_name='Do you currently have a cough that has been present for 2 weeks?',
        choices=YES_NO_UNK_DWTA,
        max_length=30,
        blank=True,
        null=True
    )

    fever = models.CharField(
        verbose_name='Do you currently have a fever?',
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30)

    fever_duration = models.CharField(
        verbose_name='Do currently have a fever that has been present for 2 weeks?',
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30)

    night_sweats = models.CharField(
        verbose_name='Do you currently have night sweats that has been present for 2 weeks?',
        choices=YES_NO_UNK_DWTA,
        help_text=(' A patient is considered to have night sweats if they have had more '
                   'than two nights of waking up with their night clothing drenched due '
                   'to sweating with a need to change the night clothing'),
        null=True,
        max_length=30)

    weight_loss = models.CharField(
        verbose_name='Have you been losing weight without trying to lose weight?',
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30)

    cough_blood = models.CharField(
        verbose_name='Have you coughed up blood in the last 2 weeks?',
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30)

    cough_blood_during_preg = models.CharField(
        verbose_name=('Did you have at least one illness involving coughing up blood '
                      'during pregnancy up to the day of delivery of your baby? '),
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30
    )

    enlarged_lymph_nodes = models.CharField(
        verbose_name='Do you currently have enlarged lymph nodes?',
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30)

    enlarged_lymph_nodes_postpartum_clinic = models.CharField(
        verbose_name=('Did you go to the clinic for this/these illnesses involving a '
                      'enlarged lymph nodes?'),
        null=True,
        blank=True,
        choices=YES_NO_UNK_DWTA,
        max_length=30
    )

    unexplained_fatigue = models.CharField(
        verbose_name='Do you currently have unexplained fatigue? ',
        choices=YES_NO_UNK_DWTA,
        null=True,
        max_length=30)

    class Meta:
        app_label = 'flourish_caregiver'
        verbose_name = 'TB Screen for adolescents'
        verbose_name_plural = 'TB Screen for adolescents'
