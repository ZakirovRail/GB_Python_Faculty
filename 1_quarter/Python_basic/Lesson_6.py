# def print_human_name(human):
#     print(human['name'])
#
# h1 = {'name': 'Abc'}
# h2 = {'name': 'ASD'}
#
# print_human_name(h1) # Abc
# print_human_name(h2) # ASD

#================================================================================================

# class Phone:
#     def call(self):
#         print('calling')
#
#
# my_phone = Phone()
# my_phone.call()  # calling

#================================================================================================

# class Phone:
#
#     def __init__(self, phone_model):
#         self.model = phone_model
#
#     def call(self):
#         print('calling')
#
#     def loading(self):
#
# my_phone_1 = Phone('nokia 1100')
# print(my_phone_1.model) # nokia 1100
# my_phone_2 = Phone('nokia 3310')
# print(my_phone_2.model) # nokia 3310
#================================================================================================

# class Phone:
#
#     def __init__(self, phone_model):
#         self.model = phone_model
#         self.loading()
#
#     def call(self):
#         print('calling')
#
#     def loading(self):
#         print(self.model, 'loading')
#
# my_phone_1 = Phone('nokia 1100')
# # print(my_phone_1.model) # nokia 1100
# my_phone_2 = Phone('nokia 3310')
# # print(my_phone_2.model) # nokia 3310

#================================================================================================
# class Phone:
#
#     def __init__(self, phone_model):
#         self.model = phone_model
#         self._loading()
#         self._serial_number = 321500
#
#     def call(self):
#         print('calling')
#
#     def _loading(self):
#         print(self.model, 'loading')
#
#     def get_serial_number(self):
#         return self._serial_number
#
# my_phone_1 = Phone('nokia 1100') # nokia 1100 loading
# print(my_phone_1._serial_number) # 321500


#================================================================================================
# class Phone:
#     def __init__(self, phone_model):
#         self.model = phone_model
#         self._loading()
#         self.__serial_number = 321500
#     def call(self):
#         print('calling')
#     def _loading(self):
#         print(self.model, 'loading')
#     def get_serial_number(self):
#         return self.__serial_number
# my_phone_1 = Phone('nokia 1100') # nokia 1100 loading
# print(my_phone_1._Phone__serial_number) # 321500
#================================================================================================

# class SmartPhone(Phone):
#     def sms(self):
#         print('sms sending')
#
#     def email(self):
#         print('email sending')


# my_smartphone = SmartPhone('6600')
# my_smartphone.get_serial_number()
# my_smartphone.sms()

# class IPhone(SmartPhone):
#
#     def __init__(self, phone_model):
#         super().__init__(phone_model)
#         self.logo()
#
#     def player(self):
#         print('playing music')
#
#     def browser(self):
#         print('browser is opening')
#
#     def sms(self):
#         print('Imessage sending')
#
#     def logo(self):
#         print('showing log')
#
# my = IPhone('6')
# my.sms()
#
#
# class NextGenerationPhone(IPhone):
#
#     def touch_id(self):
#         print('touch_id is working')
#================================================================================================

# class Auto():
#     def auto_start(self, param_1, param_2=None):
#         if param_2 is not None:
#             print(param_1 + param_2)
#         else:
#             print(param_1)
#
# auto = Auto()
# auto.auto_start(50) # 50
#
# auto = Auto()
# auto.auto_start(50, 100) # 150

#================================================================================================
class Transport:
    def show_info(self):
        print('Parent')

class Auto(Transport):
    def show_info(self):
        print('Inherent class')


t = Transport()
t.show_info()

a = Auto()
a.show_info()

















