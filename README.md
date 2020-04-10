# Joystick-con-raspberry-pi-y-python
Joystick con raspberry pi y python
 Ahora, vamos a aprender un nuevo sistema electrónic
módulo Joystick que trabaja en el mismo principio que el potenciómetro rotativo.

Joystick es un tipo de sensor utilizado con los dedos, que es ampliamente utilizado en gamepad y control remoto.Puede cambiar en dirección Y o dirección X al mismo tiempo. Y también se puede presionar en la dirección Z.
Dos potenciómetros giratorios dentro del joystick están configurados para detectar la dirección de cambio del dedo, y un empuje
en dirección vertical se establece para detectar la acción de pulsar.
Cuando se leen los datos del joystick, hay algunos diferentes entre el eje: los datos de los ejes X e Y son analógicos, que
necesidad de usar ADC. Los datos del eje Z son digitales, por lo que puede utilizar directamente el GPIO para leer, o también puede utilizar ADC para leer.

