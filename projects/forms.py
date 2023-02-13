from django import forms
from projects.models import Contact

# Create your forms here.

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ["first_name","last_name","email_address", "reason_for_contact", "message"]

	message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': "width:100%;",
									 'placeholder': 'Insert your message here.'})
	)

	reason_for_contact = forms.Select()



	def clean(self):
 
		# data from the form is fetched using super function
		super(ContactForm, self).clean()
			
		# extract the username and text field from the data
		first_name = self.cleaned_data.get('first_name')
		message = self.cleaned_data.get('message')
		email_address = self.cleaned_data.get('email_address')

		# conditions to be met for the username length
		if (first_name is None):
			self._errors['first_name'] = self.error_class([
				'Please let me know your name.'])
		if (email_address is None):
			self._errors['email_address'] = self.error_class([
				'Please let me how to reach you via e-mail.'])
		if (message is None) or (len(message) < 10):
			self._errors['message'] = self.error_class([
				'Let me know what you\'d like to share.'])

		# return any errors if found
		return self.cleaned_data