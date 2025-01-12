from eth_account import Account

def generate_account(nums: int, output_file: str = None):
    """
    Генерация Ethereum-кошельков с мнемоническими фразами.

    :param nums: Количество кошельков для генерации.
    :param output_file: Путь для сохранения данных в текстовый файл (необязательно).
    :return: Список сгенерированных кошельков.
    """
    accounts = []
    try:
        # Открываем файл с указанием кодировки UTF-8
        with open(output_file, "w", encoding="utf-8") if output_file else None as file:
            for i in range(nums):
                # Включаем возможность работы с мнемониками
                Account.enable_unaudited_hdwallet_features()
                # Генерируем аккаунт и мнемонику
                account, mnemonic = Account.create_with_mnemonic()
                # Формируем структуру данных
                account_data = {
                    "address": account.address,
                    "mnemonic": mnemonic,
                    "private_key": "0x" + account.key.hex()
                }
                accounts.append(account_data)

                # Форматируем строку для записи
                account_text = (
                    f"Аккаунт {i + 1}:\n"
                    f"Адрес: {account.address}\n"
                    f"Фраза: {mnemonic}\n"
                    f"Приватный ключ: {account_data['private_key']}\n"
                    f"{'-' * 40}\n"
                )

                # Выводим в консоль
                print(account_text)

                # Записываем в файл, если указан путь
                if file:
                    file.write(account_text)

        if output_file:
            print(f"Данные аккаунтов сохранены в файл: {output_file}")

        return accounts

    except Exception as e:
        print(f"Ошибка при генерации аккаунтов: {e}")
        return []

# Пример вызова функции
if __name__ == "__main__":
    output_path = "accounts.txt"  # Путь для сохранения в текстовый файл
    generate_account(10, output_file=output_path)
