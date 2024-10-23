import os
import datetime
import data
import time


ex_errors = 0


def main():
    sleep = [0, 3, 10, 30, 60, 150, 300]

    while True:
        try:
            write_logs(f'{(datetime.datetime.today()).strftime("%d.%m.%Y %H:%M:%S")} -> Start')
            telegram_bot()
        except Exception as ex:
            global ex_errors
            if ex_errors < len(sleep):
                ex_errors += 1
            write_logs(f'{(datetime.datetime.today()).strftime("%d.%m.%Y %H:%M:%S")} -> Exception\n{ex}')
            time.sleep(sleep[ex_errors - 1])


def write_logs(text):
    with open("logs.txt", "a", encoding="utf-8") as logs_file:
        logs_file.write(f'{text}\n\n')


class User:
    def __init__(self, identifier, dont_remember_mode: bool = False):
        self.identifier = identifier
        user_id_str = "{:010d}".format(identifier)
        self.path = os.path.join('users', *list(user_id_str))

        if not os.path.exists(self.path):
            os.makedirs(self.path)
            self.mode = 0

        elif dont_remember_mode:
            self.mode = 0

        else:
            try:
                with open(f'{self.path}/data.txt', "r", encoding='utf-8') as f:
                    self.mode = int(f.readlines()[1])
            except FileNotFoundError:
                self.mode = 0
                write_logs(f'{(datetime.datetime.today()).strftime("%d.%m.%Y %H:%M:%S")} -> Exception\n'
                           f'Exception code: 76\nID: {identifier}\nException: The file was not found')
            except Exception as ex:
                self.mode = 0
                with open(f'{self.path}/data.txt', "r", encoding='utf-8') as f:
                    write_logs(f'{(datetime.datetime.today()).strftime("%d.%m.%Y %H:%M:%S")} -> Exception\n'
                               f'Exception code: 81\nID: {identifier}\nFile text: {f.read()}\nException: {ex}')

    def write(self):
        with open(f'{self.path}/data.txt', "w", encoding='utf-8') as f:
            f.write(f'{str(self.identifier)}\n{str(self.mode)}')


def telegram_bot():
    @data.bot.message_handler(commands=['start'])
    def command_start(message):
        global ex_errors
        ex_errors = 0
        user = User(message.chat.id, dont_remember_mode=True)
        with open(data.photo_path, 'rb') as photo:
            data.bot.send_photo(
                message.chat.id,
                photo,
                caption=data.welcome_text,
                reply_markup=data.where_to_start_markup,
                parse_mode='Markdown'
            )
        user.mode = 0
        user.write()

    @data.bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        global ex_errors
        ex_errors = 0
        user = User(call.message.chat.id)

        if (((user.mode == 0) and (call.data == data.where_to_start_button.callback_data)) or
                (call.data == data.main_button.callback_data)):
            data.bot.send_message(
                call.message.chat.id,
                data.main_menu,
                reply_markup=data.sections_for_training_markup,
                parse_mode='Markdown'
            )
            user.mode = 1

        elif user.mode == 1:
            match call.data:
                case data.sport_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.sport_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 2
                case data.nutrition_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.nutrition_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 3
                case data.sleep_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.sleep_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 4
                case data.meditation_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.meditation_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 5
                case data.relationships_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.relationships_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 6
                case data.work_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.work_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 7
                case data.hobby_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.hobby_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 8
                case data.relaxation_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.relaxation_text,
                        reply_markup=data.benefit_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 9
                case data.other_protocols_button.callback_data:
                    data.bot.send_message(
                        call.message.chat.id,
                        data.protocols_text,
                        reply_markup=data.main_markup,
                        parse_mode='Markdown'
                    )
                    user.mode = 10

        elif (2 <= user.mode <= 9) and (call.data == data.benefit_button.callback_data):
            response_text: str = ''
            match user.mode:
                case 2:
                    response_text = data.sport_benefits
                case 3:
                    response_text = data.nutrition_benefits
                case 4:
                    response_text = data.sleep_benefits
                case 5:
                    response_text = data.meditation_benefits
                case 6:
                    response_text = data.relationships_benefits
                case 7:
                    response_text = data.work_benefits
                case 8:
                    response_text = data.hobby_benefits
                case 9:
                    response_text = data.relaxation_benefits
            data.bot.send_message(
                call.message.chat.id,
                response_text,
                reply_markup=data.how_to_do_it_markup,
                parse_mode='Markdown'
            )
            user.mode += 8

        elif (10 <= user.mode <= 17) and (call.data == data.how_to_do_it_button.callback_data):
            response_text: str = ''
            match user.mode:
                case 10:
                    response_text = data.sport_how_to_do_it
                case 11:
                    response_text = data.nutrition_how_to_do_it
                case 12:
                    response_text = data.sleep_how_to_do_it
                case 13:
                    response_text = data.meditation_how_to_do_it
                case 14:
                    response_text = data.relationships_how_to_do_it
                case 15:
                    response_text = data.work_how_to_do_it
                case 16:
                    response_text = data.hobby_how_to_do_it
                case 17:
                    response_text = data.relaxation_how_to_do_it
            data.bot.send_message(
                call.message.chat.id,
                response_text,
                reply_markup=data.main_markup,
                parse_mode='Markdown'
            )

        user.write()

    data.bot.polling()


if __name__ == '__main__':
    main()
