from django.forms import ModelForm,Textarea
from django.utils.translation import gettext_lazy as _
from .models import Group
def GroupForm(ModelForm):
    class Meta:
        model=Group
        fields=('group_name','deposit','fine','reward_method','teammates','rules')
        widgets={
            'rules':Textarea(attrs={'cols':80,'rows':20}),
        }
        labels={
            'group_name':_('Group Name'),
            'deposit':_('Required Deposit'),
            'fine':_('Fine'),
            'reward_method':_('Choose how to distribute reward'),
            'teammates':_('Input ID of your teammates'),
            'rules':_('Rules of this study group'),
        }