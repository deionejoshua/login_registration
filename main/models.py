from django.db import models

class user_info_manager(models.Manager):
    def validation(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name_error'] = "First Name must be longer than 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name_error'] = "Last Name must be longer than 2 characters"

        if len(post_data['email_address']) == 0:
            errors['email_address'] = "Enter a valid email"

        if len(post_data['user_password']) < 1:
            errors['password_len_error'] = "PW must be longer"
        
        if post_data['user_password'] != post_data['confirm_password']:
            errors['password_match_error'] = "Passwords must match"

        return errors





class user_info(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = user_info_manager()
