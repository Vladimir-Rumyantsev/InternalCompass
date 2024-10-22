import os
import datetime
import time
from data import *

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
    @bot.message_handler(commands=['start'])
    def command_start(message):
        global ex_errors
        ex_errors = 0
        user = User(message.chat.id, dont_remember_mode=True)
        bot.send_message(message.chat.id, welcome_text, reply_markup=where_to_start_markup, parse_mode='Markdown')
        user.mode = 0
        user.write()

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        global ex_errors
        ex_errors = 0
        user = User(call.message.chat.id)

        if (((user.mode == 0) and (call.data == where_to_start_button.callback_data)) or
                (call.data == section_selection_button.callback_data)):
            bot.send_message(
                call.message.chat.id,
                main_menu,
                reply_markup=sections_for_training_markup,
                parse_mode='Markdown'
            )
            user.mode = 1

        elif user.mode == 1:
            match call.data:
                case sport_button.callback_data:
                    bot.send_message(call.message.chat.id, sport_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 2
                case nutrition_button.callback_data:
                    bot.send_message(call.message.chat.id, nutrition_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 3
                case sleep_button.callback_data:
                    bot.send_message(call.message.chat.id, sleep_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 4
                case meditation_button.callback_data:
                    bot.send_message(call.message.chat.id, meditation_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 5
                case relationships_button.callback_data:
                    bot.send_message(call.message.chat.id, relationships_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 6
                case work_button.callback_data:
                    bot.send_message(call.message.chat.id, work_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 7
                case hobby_button.callback_data:
                    bot.send_message(call.message.chat.id, hobby_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 8
                case relaxation_button.callback_data:
                    bot.send_message(call.message.chat.id, relaxation_text,
                                     reply_markup=benefit_markup, parse_mode='Markdown')
                    user.mode = 9
                case other_protocols_button.callback_data:
                    bot.send_message(call.message.chat.id, protocols_text,
                                     reply_markup=section_selection_markup, parse_mode='Markdown')
                    user.mode = 10

        elif 2 <= user.mode <= 9:
            response_text: str = ''
            match user.mode:
                case 2:
                    response_text = sport_benefits
                case 3:
                    response_text = nutrition_benefits
                case 4:
                    response_text = sleep_benefits
                case 5:
                    response_text = meditation_benefits
                case 6:
                    response_text = relationships_benefits
                case 7:
                    response_text = work_benefits
                case 8:
                    response_text = hobby_benefits
                case 9:
                    response_text = relaxation_benefits
            bot.send_message(call.message.chat.id, response_text,
                             reply_markup=how_to_do_it_markup, parse_mode='Markdown')
            user.mode += 8

        elif 10 <= user.mode <= 17:
            response_text: str = ''
            match user.mode:
                case 10:
                    response_text = sport_how_to_do_it
                case 11:
                    response_text = nutrition_how_to_do_it
                case 12:
                    response_text = sleep_how_to_do_it
                case 13:
                    response_text = meditation_how_to_do_it
                case 14:
                    response_text = relationships_how_to_do_it
                case 15:
                    response_text = work_how_to_do_it
                case 16:
                    response_text = hobby_how_to_do_it
                case 17:
                    response_text = relaxation_how_to_do_it
            bot.send_message(call.message.chat.id, response_text,
                             reply_markup=section_selection_markup, parse_mode='Markdown')

        user.write()

    bot.polling()


if __name__ == '__main__':
    main()
