from admin import Admin

admin_user = Admin('Keris', 'Monk', 20, 'IN')
admin_user.describe_user()
admin_user.privileges.show_privileges()