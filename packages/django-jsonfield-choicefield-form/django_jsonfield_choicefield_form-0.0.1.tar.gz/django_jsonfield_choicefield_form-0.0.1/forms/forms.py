import json
from django import forms


class KeyChoicesFieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_key_map = getattr(self.Meta, "json_key_map", None)
        if self.json_key_map is None:
            raise ValueError('KeyChoicesFieldForm has no json_key_map class specified.')
        instance = kwargs.get('instance', None)
        if instance:
            for json_field, json_keys in self.json_key_map.items():
                for key in json_keys:
                    if key not in self.fields:
                        raise ValueError(f"{key} must be specified with ChoiceField.")
                    self.fields[key].initial = getattr(instance, json_field).pop(key, None)

    def clean(self):
        cleaned_data = super().clean()
        for json_field, json_keys in self.json_key_map.items():
            json_data = json.loads(cleaned_data[json_field])
            for key in json_keys:
                json_data.update({key: cleaned_data.get(key)})
            cleaned_data[json_field] = json_data
        return cleaned_data
