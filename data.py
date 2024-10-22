import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')

welcome_text = ('*Привет! Давай начнём.*\n\nНаш мир быстро меняется, но наши биологические способности не поспевают за'
                ' технологиями. Это вызывает тревожность, стресс и депрессию\n\nВ этой войне человека и современного '
                'мира мы будем вашей поддержкой: сделаем вас сильнее и вы сможете постоять за себя в этой борьбе🤼‍♂')

where_to_start_button = types.InlineKeyboardButton(text='Здорово! С чего мне начать?', callback_data='button_01')
where_to_start_markup = types.InlineKeyboardMarkup()
where_to_start_markup.add(where_to_start_button)

main_menu = ('Мы будем работать над несколькими аспектами ментального здоровья. Если вы улучшите одну часть своей'
             ' жизни, это повлияет и на другие. Главное сделать первый шаг!\n\n*Выберите секцию для обучения*')

sport_button = types.InlineKeyboardButton(text='Спорт', callback_data='button_02')
nutrition_button = types.InlineKeyboardButton(text='Питание', callback_data='button_03')
sleep_button = types.InlineKeyboardButton(text='Сон', callback_data='button_04')
meditation_button = types.InlineKeyboardButton(text='Медитация', callback_data='button_05')
relationships_button = types.InlineKeyboardButton(text='Отношения', callback_data='button_06')
work_button = types.InlineKeyboardButton(text='Работа', callback_data='button_07')
hobby_button = types.InlineKeyboardButton(text='Хобби', callback_data='button_08')
relaxation_button = types.InlineKeyboardButton(text='Релаксация', callback_data='button_09')
other_protocols_button = types.InlineKeyboardButton(text='Другие протоколы', callback_data='button_10')
sections_for_training_markup = types.InlineKeyboardMarkup()
sections_for_training_markup.add(sport_button, nutrition_button, sleep_button)
sections_for_training_markup.add(meditation_button, relationships_button, work_button)
sections_for_training_markup.add(hobby_button, relaxation_button, other_protocols_button)

section_selection_button = types.InlineKeyboardButton(text='Вернуться к выбору секции', callback_data='button_11')
section_selection_markup = types.InlineKeyboardMarkup()
section_selection_markup.add(section_selection_button)

benefit_button = types.InlineKeyboardButton(text='Польза', callback_data='button_12')
benefit_markup = types.InlineKeyboardMarkup()
benefit_markup.add(benefit_button)
benefit_markup.add(section_selection_button)

how_to_do_it_button = types.InlineKeyboardButton(text='Как делать?', callback_data='button_13')
how_to_do_it_markup = types.InlineKeyboardMarkup()
how_to_do_it_markup.add(how_to_do_it_button)
how_to_do_it_markup.add(section_selection_button)

sport_text = (
    '*Спорт\n\nСпорт и физические нагрузки* — это любая физическая активность.\n\nЭто может включать в себя '
    'тренировки в спортзале, занятия командными видами спорта, бег, йогу, плавание и даже простые прогулки.'
)
sport_benefits = (
    '*Польза\n\n• Улучшение настроения:* Физическая активность способствует выработке эндорфинов, '
    'которые известны как "гормоны счастья".\n\n'
    '*• Снижение стресса:* Регулярные тренировки помогают снизить уровень '
    'кортизола (гормона стресса) и способствуют расслаблению.\n\n'
    '*• Повышение самооценки:* Достижения в спорте и улучшение физической формы могут повысить уверенность в себе.\n\n'
    '*• Улучшение сна:* Физическая активность способствует более глубокому и качественному сну.'
)
sport_how_to_do_it = (
    '*Как делать?\n\n• Выбор активности:* Найдите вид спорта или физической активности, который вам нравится. '
    'Это может быть бег, плавание, теннис, йога, танцы или командные виды спорта.\n\n'
    '*• Регулярность:* Старайтесь заниматься не менее 150 минут в неделю умеренной физической активности '
    'или 75 минут интенсивной активности.\n\n'
    '*• Постепенное увеличение нагрузки:* Начинайте с небольших нагрузок и постепенно увеличивайте '
    'интенсивность и продолжительность тренировок.\n\n'
    '*• Слушайте свое тело:* Обращайте внимание на свои ощущения. Если вы чувствуете усталость или боль, '
    'дайте себе время на восстановление.\n\n'
    '*• Создайте рутину:* Определите время для занятий спортом в своем расписании, чтобы сделать это привычкой.'
)

nutrition_text = (
    '*Питание*\n\nМы - то, что мы едим. Чтобы ваша био-машина работала исправно, ей необходимо правильное топливо'
)
nutrition_benefits = (
    '*Польза\n\n• Общее здоровье:* Здоровое питание способствует укреплению иммунной системы '
    'и предотвращению различных заболеваний.'
)
nutrition_how_to_do_it = (
    '*Как делать?\n\n• Включите в рацион больше овощей и фруктов:* Старайтесь есть разнообразные цвета, '
    'чтобы получать все необходимые витамины и минералы.\n\n'
    '*• Добавьте источники омега-3:* Рыба (лосось, сардины), орехи (грецкие) и семена (чиа, льняные) '
    'помогут улучшить работу мозга.\n\n'
    '*• Сократите потребление сахара:* сахар вызывает резкие колебания настроения, ухудшает работу мозга. '
    'Можно заменить фруктами, орехами, сухофруктами.\n\n'
    '*• Регулярно пейте воду:* Даже небольшое обезвоживание негативно сказывается на работе мозга.\n\n'
    '*• Следите за режимом питания:* Регулярные приемы пищи помогут избежать скачков сахара в крови '
    'и поддерживать стабильное настроение.'
)

sleep_text = (
    '*Сон*\n\nСон —  играет ключевую роль в восстановлении организма, '
    'поддержании психоэмоционального равновесия и улучшении когнитивных функций.'
)
sleep_benefits = (
    '*Польза\n\n• Восстановление нервной системы:* Качественный сон способствует регенерации нейронов '
    'и улучшению работы мозга, что помогает справляться со стрессом и тревожностью.\n\n'
    '*• Улучшение настроения:* Достаточное количество сна помогает регулировать уровень гормонов, '
    'таких как серотонин и дофамин, что влияет на общее эмоциональное состояние.\n\n'
    '*• Повышение когнитивных функций:* Сон способствует улучшению памяти, концентрации и способности к обучению.\n\n'
    '*• Снижение уровня стресса:* Хороший сон помогает организму справляться с ежедневными стрессами '
    'и снижает уровень кортизола.\n\n'
    '*• Поддержание физического здоровья:* Качественный сон укрепляет иммунную систему '
    'и снижает риск развития различных заболеваний, что также положительно сказывается на психическом состоянии.'
)
sleep_how_to_do_it = (
    '*Как делать?\n\n• Создайте регулярный режим сна:* Ложитесь и вставайте в одно и то же время каждый день, '
    'даже в выходные. Это помогает установить внутренние биоритмы.\n\n'
    '*• Обеспечьте комфортные условия для сна:* Убедитесь, что ваша спальня темная, тихая и прохладная. '
    'Используйте удобный матрас и подушки.\n\n'
    '*• Избегайте экранов перед сном:* Ограничьте использование телефонов, компьютеров и '
    'телевизоров за 1-2 часа до сна, чтобы не подвергать себя воздействию синего света.\n\n'
    '*• Практикуйте расслабляющие ритуалы:* Чтение книги, медитация или '
    'легкая растяжка помогут подготовить тело и разум к отдыху.\n\n'
    '*• Соблюдайте здоровый образ жизни:* Регулярные физические нагрузки и '
    'сбалансированное питание способствуют улучшению качества сна.\n\n'
    '*• Избегайте кофеина и алкоголя перед сном:* Эти вещества могут нарушать цикл сна и ухудшать его качество.'
)

meditation_text = (
    '*Медитация\n\nМедитация* — это практика, которая включает в себя сосредоточение внимания '
    'и осознанность, направленные на достижение состояния спокойствия и внутреннего покоя.'
)
meditation_benefits = (
    '*Польза\n\n• Снижение стресса:* Регулярная медитация помогает уменьшить уровень кортизола, '
    'гормона стресса, что способствует общему расслаблению.\n\n'
    '*• Улучшение эмоционального состояния:* Практика медитации способствует повышению уровня счастья '
    'и удовлетворенности жизнью, а также снижению тревожности и депрессии.\n\n'
    '*• Увеличение концентрации и внимания:* Медитация развивает способность сосредотачиваться '
    'и улучшает когнитивные функции, что помогает в повседневной жизни.\n\n'
    '*• Повышение осознанности:* Практика осознанности помогает лучше понимать свои мысли и эмоции, '
    'что способствует более здоровому реагированию на стрессовые ситуации.\n\n'
    '*• Улучшение сна:* Медитация может помочь расслабиться и подготовиться к спокойному сну, '
    'снижая уровень беспокойства.'
)
meditation_how_to_do_it = (
    '*Как это делать?\n\n• Выберите подходящее место и время:* Найдите тихое место, где вас никто не будет отвлекать. '
    'Выберите время, когда вам удобно заниматься медитацией — утром, днем или вечером.\n\n'
    '*• Сядьте удобно:* Устройтесь в комфортной позе — сидя на стуле или на полу, '
    'с прямой спиной и расслабленными плечами.\n\n'
    '*• Сосредоточьтесь на дыхании:* Закройте глаза и начните обращать внимание на свое дыхание. '
    'Вдыхайте глубоко через нос, задерживайте дыхание на несколько секунд и выдыхайте через рот.\n\n'
    '*• Отпустите мысли:* Если ваши мысли начинают блуждать, не судите себя. '
    'Просто мягко верните внимание к дыханию или к выбранному объекту медитации (например, мантре или образу).\n\n'
    '*• Практикуйте регулярно:* Начните с 5-10 минут в день и постепенно увеличивайте время до 20-30 минут. '
    'Регулярность важнее продолжительности.\n\n'
    '*• Используйте приложения или видео:* Если вам сложно начать, попробуйте использовать приложения '
    'для медитации или следовать за видеоуроками. Это самый простой способ начать.'
)

relationships_text = (
    '*Отношения\n\nОтношения* — дружба, романтические связи, семейные узы и профессиональные контакты. '
    'Крепкие и поддерживающие отношения играют важную роль в жизни человека и его психоэмоциональном состоянии.'
)
relationships_benefits = (
    '*Польза\n\n• Эмоциональная поддержка:* Наличие близких людей позволяет делиться переживаниями и чувствами, '
    'что снижает уровень стресса и тревожности.\n\n'
    '*• Улучшение самооценки:* Поддержка со стороны других может повысить '
    'уверенность в себе и чувство собственной ценности.\n\n'
    '*• Снижение одиночества:* Крепкие отношения помогают избежать чувства изоляции, '
    'что положительно сказывается на общем психическом состоянии.\n\n'
    '*• Развитие навыков общения:* Взаимодействие с другими людьми способствует развитию социальных навыков, '
    'что важно для успешной адаптации в обществе.\n\n'
    '*• Увеличение счастья:* Положительные взаимодействия с другими людьми могут '
    'повысить уровень счастья и удовлетворенности жизнью.'
)
relationships_how_to_do_it = (
    '*Как это делать?\n\n• Инвестируйте время в отношения:* Регулярно общайтесь с близкими, '
    'проводите время вместе, делитесь своими мыслями и чувствами.\n\n'
    '*• Будьте открытыми и честными:* Открытость в общении способствует углублению взаимопонимания и доверия.\n\n'
    '*• Поддерживайте друг друга:* Будьте готовы оказать помощь и поддержку своим близким в трудные времена.\n\n'
    '*• Развивайте новые знакомства:* Участвуйте в социальных мероприятиях, '
    'группах по интересам или волонтерских проектах для расширения круга общения.\n\n'
    '*• Работайте над конфликтами:* Учитесь конструктивно решать споры и недопонимания, '
    'чтобы укреплять отношения вместо их разрушения.\n\n'
    '*• Выражайте благодарность:* Регулярно говорите своим близким о том, '
    'как вы цените их поддержку и присутствие в вашей жизни.'
)

work_text = (
    '*Работа\n\nРабота* — может включать профессиональную деятельность, волонтерство или любые другие формы занятости.'
)
work_benefits = (
    '*Польза\n\n• Структура и рутина:* Работа помогает установить распорядок дня, '
    'что способствует стабильности и предсказуемости в жизни.\n\n'
    '*• Социальные связи:* Место работы часто становится источником общения и '
    'взаимодействия с коллегами, что помогает избежать одиночества.\n\n'
    '*• Чувство достижения:* Завершение задач и достижение целей на работе повышает самооценку и уверенность в себе.'
    '\n\n*• Финансовая независимость:* Наличие дохода позволяет обеспечить себя и своих близких, '
    'что снижает уровень стресса и беспокойства.\n\n'
    '*• Развитие навыков:* Работа способствует обучению и развитию новых навыков, '
    'что может повысить удовлетворенность жизнью и карьерный рост.'
)
work_how_to_do_it = (
    '*Как это делать?\n\n• Выбирайте работу по призванию:* Стремитесь найти занятие, '
    'которое вам интересно и соответствует вашим увлечениям.\n\n'
    '*• Устанавливайте границы:* Научитесь отделять рабочее время от личного, чтобы избежать выгорания.\n\n'
    '*• Создавайте поддерживающую атмосферу:* Стремитесь к позитивным отношениям с коллегами, '
    'делитесь опытом и поддерживайте друг друга.\n\n'
    '*• Регулярно отдыхайте:* Не забывайте делать перерывы в течение рабочего дня '
    'для восстановления сил и предотвращения стресса.\n\n'
    '*• Участвуйте в обучении:* Ищите возможности для профессионального развития и повышения квалификации, '
    'что может повысить вашу удовлетворенность работой.\n\n'
    '*• Заботьтесь о балансе между работой и личной жизнью:* Уделяйте время хобби, '
    'отдыху и общению с близкими, чтобы поддерживать психоэмоциональное здоровье.'
)

hobby_text = (
    '*Хобби\n\nХобби* — это деятельность, которую человек выполняет в свободное время для удовольствия и отдыха. '
    'Это может быть что угодно: от творчества и спорта до садоводства и коллекционирования.'
)
hobby_benefits = (
    '*Польза\n\n• Снижение стресса:* Занятия любимым делом помогают отвлечься от повседневных забот и расслабиться.\n\n'
    '*• Улучшение настроения:* Хобби приносит радость и удовлетворение, '
    'что способствует повышению общего эмоционального фона.\n\n'
    '*• Развитие креативности:* Творческие хобби, такие как рисование или музыка, '
    'стимулируют мозг и способствуют развитию креативного мышления.\n\n'
    '*• Социальные связи:* Участие в групповых хобби (например, спортивные команды или клубы по интересам) '
    'помогает завести новых друзей и укрепить социальные связи.\n\n'
    '*• Чувство достижения:* Завершение проектов или достижение целей в хобби повышает самооценку и уверенность в себе.'
    '\n\n*• Улучшение концентрации:* Занятия хобби требуют внимания и сосредоточенности, '
    'что может помочь развить навыки концентрации.'
)
hobby_how_to_do_it = (
    '*Как это делать?\n\n• Выбор хобби:* Найдите занятие, которое вам интересно и приятно, '
    'пробуйте разные варианты, пока не найдете то, что вам действительно нравится.\n\n'
    '*• Регулярность:* Уделяйте время своему хобби на регулярной основе, чтобы оно стало частью вашей жизни.\n\n'
    '*• Создание комфортной обстановки:* Обеспечьте себе удобное место и необходимые материалы для занятия хобби.'
    '*• Участие в сообществах:* Присоединяйтесь к клубам или группам по интересам, '
    'где можно общаться с единомышленниками.\n\n'
    '*• Не ставьте слишком высоких ожиданий:* Наслаждайтесь процессом, а не только результатом. '
    'Позвольте себе ошибаться и учиться на этом.\n\n'
    '*• Экспериментируйте:* Не бойтесь пробовать новое и выходить за рамки привычного — '
    'это может привести к новым увлечениям и открытиям.'
)

relaxation_text = (
    '*Релаксация\n\nТехники релаксации* — это методы, направленные на снижение напряжения и стресса, '
    'улучшение общего самочувствия и восстановление внутреннего баланса. '
    'К ним относятся дыхательные упражнения, медитация, йога, прогрессивная мышечная релаксация и визуализация.'
)
relaxation_benefits = (
    '*Польза\n\n• Снижение уровня стресса:* Релаксация помогает уменьшить физическое '
    'и эмоциональное напряжение, что способствует общему спокойствию.\n\n'
    '*• Улучшение настроения:* Регулярные практики релаксации могут снизить '
    'уровень тревожности и депрессии, улучшая общее эмоциональное состояние.\n\n'
    '*• Повышение концентрации:* Способы релаксации помогают улучшить внимание и сосредоточенность, '
    'что может быть полезно в повседневной жизни и работе.\n\n'
    '*• Физическое здоровье:* Релаксация снижает уровень кортизола (гормона стресса), '
    'что положительно влияет на иммунную систему и общее здоровье.\n\n'
    '*• Улучшение сна:* Техники релаксации помогают успокоить ум и подготовить тело к restful sleep.'
)
relaxation_how_to_do_it = (
    '*Как это делать?\n\n• Дыхательные упражнения:* Практикуйте глубокое дыхание: вдохните медленно через нос, '
    'задержите дыхание на несколько секунд и выдохните через рот. Повторяйте 5-10 раз.\n\n'
    '*• Медитация:* Найдите тихое место, закройте глаза и сосредоточьтесь на своем дыхании '
    'или повторяйте мантру. Начните с 5-10 минут в день и постепенно увеличивайте время.\n\n'
    '*• Йога:* Запишитесь на занятия по йоге или следуйте онлайн-урокам. '
    'Йога сочетает физические упражнения с дыхательными техниками и медитацией.\n\n'
    '*• Прогрессивная мышечная релаксация:* Поочередно напрягайте и расслабляйте группы мышц, '
    'начиная с ног и заканчивая головой. Это помогает осознать напряжение в теле и научиться его отпускать.\n\n'
    '*• Визуализация:* Закройте глаза и представьте себе спокойное место (например, пляж или лес). '
    'Сосредоточьтесь на деталях: звуках, запахах, ощущениях. Это помогает создать чувство умиротворения.\n\n'
    '*• Регулярность:* Уделяйте время техникам релаксации ежедневно или несколько раз в неделю, '
    'чтобы они стали частью вашей рутины.'
)

protocols_text = (
    '*Протоколы*\n\nМаленькие детали дня, которые могут повлиять на ваше настроение и состояние\n\n'
    '*Холодный душ*\nКак делать: Принимайте холодный душ 1-2 минуты каждое утро. Пробуйте заканчивать душ холодной '
    'водой в течение последних 30 секунд и постепенно увеличивайте время под холодной водой.\n'
    'Почему: Стимулирует кровообращение, улучшает настроение и даёт заряд бодрости.\n\n'
    '*Хвалить себя*\nКак делать: Каждый день находите время, чтобы отметить свои достижения, даже маленькие.\n'
    'Почему: Укрепляет самооценку и создает позитивный внутренний диалог.\n\n'
    '*Благодарность*\nКак делать: Записывайте 3 вещи, за которые вы благодарны, каждый вечер. '
    'Например, я благодарен своим друзьям за сегодняшний вечер. Или я благодарен родителям за их поддержку.\n'
    'Почему: Помогает сосредоточиться на положительном и снижает уровень тревоги.\n\n'
    '*Ввести дневник*\nКак делать: Пишите о своих мыслях и чувствах 5-10 минут в день.\n'
    'Почему: Способствует самоанализу и помогает разобраться в эмоциях.\n\n'
    '*Приложение трекеры*\nКак делать: Используйте приложение для отслеживания привычек '
    '(например, физическая активность, сон) хотя бы по 1 минуте в день.\n'
    'Почему: Помогает создать структуру и осознанность в повседневной жизни.\n\n'
    '*Уберите телефон за час до сна*\nКак делать: Отключайте телефон и другие устройства за час до сна. '
    'Замените использование телефона на чтение книги или медитацию.\n'
    'Почему: Улучшает качество сна и снижает уровень стресса.\n\n'
    '*Прибрать комнату*\nКак делать: Уделяйте 10-15 минут в день на уборку.\n'
    'Почему: Чистое пространство способствует ясности ума и уменьшает тревогу.\n\n'
    '*Избавиться от нерешенных проблем*\nКак делать: Составьте список нерешенных вопросов и '
    'выделите время для их решения.\nПочему: Устранение неопределенности снижает уровень стресса '
    'и повышает уверенность, даёт пространство для мыслей.'
)