def vernam_cipher(message, key):
    message_binary = ''.join(format(ord(char), '08b') for char in message)
    key_binary = ''.join(format(ord(char), '08b') for char in key)

    # Вычисляем длину сообщения и ключа
    message_len = len(message_binary)
    key_len = len(key_binary)

    # Генерируем одноразовый ключ длина которого равна длине сообщения
    one_time_pad = ''
    for i in range(message_len):
        one_time_pad += str(int(key_binary[i % key_len]) ^ int(message_binary[i]))

    # Преобразуем зашифрованный текст в символы
    ciphertext = ''
    for i in range(0, len(one_time_pad), 8):
        ciphertext += chr(int(one_time_pad[i:i+8], 2))

    return ciphertext


# Зашифровываем сообщение
message = "I DOLBAEB"
key = "fsflsjflsdjflsfjksdlfkslfksdlfkslfskdl"
ciphertext = vernam_cipher(message, key)
print("Зашифрованное сообщение:", ciphertext)

# Расшифровываем сообщение
decrypted_text = vernam_cipher(ciphertext, key)
print("Расшифрованное сообщение:", decrypted_text)

#Ну вы поняли что надо на русском сделать нужно