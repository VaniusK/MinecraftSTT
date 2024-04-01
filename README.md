В проекте используется SpeechRecognition, их лицензия можете найти в их README на гитхабе

STT(речь в тескт) для Майнкрафта.
Записывает микрофон, отправляет аудио в гугл, выводит полученное в чат

Конфиг:
Language - язык. ru/en/etc
Prefix - То, что будет каждый раз выводиться в чат вместе с вашими сообщениями
StartKey - Клавиша, которая начинает запись
StopKey - Клавиша, которая заканчивает запись
NecessaryKey - Клавиша, которая заканчивает запись, если она НЕ нажата. Рекомендуется использовать значение из StartKey или None
Можно указать "None" - тогда соответствующая клавиша работать не будет

ExtraRecordingTime - Время(в секундах), когда аудио продолжает записываться, если уже была нажата клавиша остановки. Полезно, если конец сообщения обрезается



The project uses SpeechRecognition, their license can be found in their README on Github

STT (speech to text) for Minecraft.
Records a microphone, sends audio to Google, and outputs the received message to chat

Config:
Language - language. ru/en/etc
Prefix - What will be displayed in the chat every time along with your messages
StartKey - The key that starts recording
StopKey - Key that ends recording
NecessaryKey - The key that ends recording if it is NOT pressed. It is recommended to use the value from StartKey or None
You can specify "None" - then the corresponding key will not work

ExtraRecordingTime - Time (in seconds) that audio continues to be recorded if the stop key has already been pressed. Useful if the end of the message is cut off