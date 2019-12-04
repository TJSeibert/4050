from django import forms
from django.core.validators import RegexValidator


class TicketForm(forms.Form):
    child_tickets = forms.IntegerField(min_value=0, label="Child", initial=0)
    adult_tickets = forms.IntegerField(min_value=0, label="Adult", initial=0)
    senior_tickets = forms.IntegerField(min_value=0, label="Senior", initial=0)

    def __init__(self, c_t, a_t, s_t, rows, cols=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if cols is None:
            self.rows = len(rows[0])
            self.cols = len(rows)
        else:
            self.rows = rows
            self.cols = cols
        for x in range(self.cols):
            for y in range(self.rows):
                initial = False
                disabled = False
                if cols is None:
                    val = rows[x][y]
                    initial = val == 1
                    disabled = val == -1
                field_name = f"seat_{x}_{y}"
                self.fields[field_name] = forms.BooleanField(required=False, initial=initial, disabled=disabled)

    def clean(self):
        chosen_seats = []
        for x in range(self.cols):
            for y in range(self.rows):
                if self.cleaned_data[f"seat_{x}_{y}"]:
                    chosen_seats.append((x, y))
        self.cleaned_data["chosen_seats"] = chosen_seats

    def get_rows(self):
        for y in range(self.rows):
            res = []
            for x in range(self.cols):
                res.append(self[f"seat_{x}_{y}"])
            yield res

    def get_seat_fields(self):
        for x in range(self.cols):
            for y in range(self.rows):
                yield self[f"seat_{x}_{y}"]

    def get_ticket_fields(self):
        yield self["child_tickets"]
        yield self["adult_tickets"]
        yield self["senior_tickets"]