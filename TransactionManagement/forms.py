
from django import forms
from TransactionManagement.models import BankAccount
# izi

field_errors = {
    'required': 'وارد کردن این فیلد ضروری است.',
    'invalid': 'داده وارد شده نادرست است.'
}

class WhithdrawForm(forms.Form):
    bank_account_id = forms.IntegerField(max_value=99999, min_value=10000, error_messages=field_errors)
    amount = forms.IntegerField(min_value=0, error_messages=field_errors)

    def save(self):
        bank_account_id = self.cleaned_data.get('bank_account_id')
        amount = self.cleaned_data.get('amount')

        while True:
            try:
                bank_account = BankAccount.objects.get(account_id=bank_account_id)
                bank_account.amount -= amount
                bank_account._do_update()
                self.cleaned_data['bank_account'] = bank_account
                break
            except:
                pass

# end_izi