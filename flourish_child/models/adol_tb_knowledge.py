from django.db import models
from edc_constants.choices import YES_NO
from edc_base.model_fields import OtherCharField

from ..choices import YES_NO_PNTA, YES_NO_DN_PNTA, COMMUNITY_TREATMENT, COMMUNITY_IMPACT
from .list_models import TbKnowledgeMedium
from .child_crf_model_mixin import ChildCrfModelMixin


class TbKnowledgeAdol(ChildCrfModelMixin):

    tb_informed = models.CharField(
        verbose_name='Do you feel well-informed about tuberculosis (TB)',
        choices=YES_NO_PNTA,
        max_length=15,)

    tb_knowledge_medium = models.ManyToManyField(
        TbKnowledgeMedium,
        verbose_name='Where did you first learn about TB? Did you learn about TB through')

    tb_knowledge_medium_other = OtherCharField(
        verbose_name='If other, specify',)

    fever_knowledge = models.CharField(
        verbose_name='Fever?',
        choices=YES_NO_DN_PNTA,
        max_length=30,)

    cough_knowledge = models.CharField(
        verbose_name='Cough?',
        choices=YES_NO_DN_PNTA,
        max_length=30,)

    night_sweats_knowledge = models.CharField(
        verbose_name='Night Sweats?',
        choices=YES_NO_DN_PNTA,
        max_length=30,)

    weight_loss_knowledge = models.CharField(
        verbose_name='Weight Loss?',
        choices=YES_NO_DN_PNTA,
        max_length=30,)

    rash_knowledge = models.CharField(
        verbose_name='Rash?',
        choices=YES_NO_DN_PNTA,
        max_length=30,)

    headache_knowledge = models.CharField(
        verbose_name='Headache?',
        choices=YES_NO_DN_PNTA,
        max_length=30,)

    vomiting_knowledge = models.CharField(
        verbose_name='Vomiting?',
        choices=YES_NO_DN_PNTA,
        max_length=30, )

    body_ache_knowledge = models.CharField(
        verbose_name='Body aches?',
        choices=YES_NO_DN_PNTA,
        max_length=30, )

    other_knowledge = models.TextField(
        verbose_name='Other: (free text)',
        max_length=150,
        blank=True,
        null=True)

    tb_utensils_transmit = models.CharField(
        verbose_name='Can a person get TB by sharing dishes, plates, cups, and spoons?',
        choices=YES_NO_DN_PNTA,
        max_length=25,)

    tb_air_transmit = models.CharField(
        verbose_name='Can a person get TB through the air when a person with TB coughs',
        choices=YES_NO_DN_PNTA,
        max_length=25,)

    tb_treatable = models.CharField(
        verbose_name='Can TB be treated? ',
        choices=YES_NO_DN_PNTA,
        max_length=25,)

    tb_curable = models.CharField(
        verbose_name='Can TB be cured? ',
        choices=YES_NO_DN_PNTA,
        max_length=25,)

    tb_community = models.CharField(
        verbose_name='How would you rate TB as a problem in your community?',
        choices=COMMUNITY_IMPACT,
        max_length=60, )

    tb_community_treatment = models.CharField(
        verbose_name='In your community, how is a person who has TB usually'
                     ' regarded/treated by other people in the community?',
        choices=COMMUNITY_TREATMENT,
        max_length=60, )

    tb_community_treatment_other = OtherCharField(
        verbose_name='If other, specify',
    )

    class Meta:
        app_label = 'flourish_child'
        verbose_name = 'Knowledge and attitudes for TB'
        verbose_name_plural = 'Knowledge and attitudes for TB'
