# from flourish_child_validations.form_validators import Brief2ParentFormValidator

from .child_form_mixin import ChildModelFormMixin
from ..models import ChildCBCLSection1, ChildCBCLSection2, ChildCBCLSection3, ChildCBCLSection4


class ChildCBCLSection1Form(ChildModelFormMixin):

#     form_validator_cls = Brief2ParentFormValidator

    class Meta:
        model = ChildCBCLSection1
        fields = '__all__'


class ChildCBCLSection2Form(ChildModelFormMixin):

    class Meta:
        model = ChildCBCLSection2
        fields = '__all__'


class ChildCBCLSection3Form(ChildModelFormMixin):

    class Meta:
        model = ChildCBCLSection3
        fields = '__all__'


class ChildCBCLSection4Form(ChildModelFormMixin):

    class Meta:
        model = ChildCBCLSection4
        fields = '__all__'
