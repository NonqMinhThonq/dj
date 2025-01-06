from django import forms
from .models import Career, Enterprise

class CareerForm(forms.ModelForm):
    field = forms.ChoiceField(choices=[], required=False)

    class Meta:
        model = Career
        fields = ['enterprise', 'name', 'field', 'image', 'description', 'requirement', 'number_of_recruitment', 'date', 'location', 'start', 'end']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Kiểm tra xem có dữ liệu enterprise không
        if 'enterprise' in self.data:
            enterprise_id = self.data.get('enterprise')
            print(f"Enterprise ID: {enterprise_id}")  # Debug ID của enterprise
            if enterprise_id:
                try:
                    enterprise = Enterprise.objects.get(id=enterprise_id)
                    print(f"Enterprise: {enterprise.name}, Fields: {enterprise.get_available_fields()}")  # In thông tin Enterprise
                    fields = enterprise.get_available_fields()  # Lấy các field của enterprise
                    self.fields['field'].choices = [(field, field) for field in fields]
                except Enterprise.DoesNotExist:
                    print("Enterprise not found")
        elif self.instance.pk:
            enterprise = self.instance.enterprise
            if enterprise:
                fields = enterprise.get_available_fields()
                self.fields['field'].choices = [(field, field) for field in fields]
