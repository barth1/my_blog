from django.apps import AppConfig


class LoginAppConfig(AppConfig):
    name = 'login_app'

    
    def ready(self):

        #Pre save signal for ReservedItem model
        reserved_model = self.get_model('ReservedItem')
        pre_save.connect(
            reserveditem_create_order_reference,
            sender=reserved_model,
            dispatch_uid="my_unique_identifier"
        )
