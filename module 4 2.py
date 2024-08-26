def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        inner_function()
inner_function()
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
#Вызов функци inner_function() вне функции test_function приводит к появлению ошбики
# Так как мы пытаемся вызвать функцию в глобальном пространстве имён
# А она находиться в обьемлющем пространстве имён