'''
Инкапсуляция - это упаковка данных и функций, работающих с этими данными, в один компонент и ограничение доступа к некоторым компонентам объекта.

Инкапсуляция означает, что внутреннее представление объекта обычно скрыто от просмотра за пределами определения объекта.

Инкапсуляция: - Скрытие информации. 
Абстракция: - Скрытие реализации.



Есть 3 уровня доступа к данным:

* публичный (public, нет особого синтаксиса, publicData);
* защищенный (protected, одно нижнее подчеркивание в начале названия, _protectedData);
* приватный (private, два нижних подчеркивания в начала названия, __privateData).
'''


class Phone:
    username = "Kate"                # public variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone.call()
print( "The username is ", my_phone.username )
# my_phone.turn_on()
# my_phone.__turn_on()
# print( “Turned on: “, my_phone.__how_many_times_turned_on)
# print( “Turned on: “, my_phone.how_many_times_turned_on)
# это выдаст ошибку