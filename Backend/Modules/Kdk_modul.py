from os import *
from docx import Document
from docx.shared import Inches,Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from datetime import datetime as dt

now = dt.now().strftime("%Y.%m.%d")
esc_num=114

class KDK:
    def __init__(self, date, tribunal):
        self.date = date
        self.tribunal = tribunal
        self.cases = []
        self.my_folder = 0

    def creat_folder(self):
        if self.my_folder == 0:
            self.my_folder = getcwd() + f'\\MFF_Base\\КДК\\Заседание {self.date}'
            mkdir(self.my_folder)
        else:
            print('Папка уже создана')

    def agenda(self):
        if self.cases == []:
            print('Дел для рассмотрения нет')
        pass

    def my_agenda(self):
        if self.cases == []:
            print('Дел для рассмотрения нет')
        pass

    def dec_on_site(self):
        if self.cases == []:
            print('Дел для рассмотрения нет')
        pass


class Case:
    def __init__(self,date, number, side_one, side_two, potential_art):
        self.date=date
        self.number = number
        self.side_one = side_one
        self.side_two = side_two
        self.potential_art = potential_art
        self.case_files = ''
        self.my_folder = 0
        self.my_notifications=[]

    def creat_folder(self):
        if self.my_folder == 0:
            self.my_folder = getcwd() + f'\\MFF_Base\\КДК\\Заседание {self.date}\\{self.side_one.name} - {self.side_two.name}'
            mkdir(self.my_folder)
        else:
            print('Папка уже создана')

    def creat_notification(self):
        chdir(self.my_folder)
        notif=Notification(self.date,self.side_one,self.side_two,self.potential_art)
        self.my_notifications.append(notif)
        return notif


    def creat_desicion(self):
        pass

    def send(self):
        pass


class Notification:

    def __init__(self,date,side_one,side_two,potential_art):
        self.date=date
        self.side_one = side_one
        self.side_two = side_two
        self.potential_art = potential_art
        document = Document()

        sections = document.sections
        for section in sections:
            section.top_margin=314400

        font_styles = document.styles
        font_head = font_styles.add_style('HeadStyle', WD_STYLE_TYPE.CHARACTER)
        font_object = font_head.font
        font_object.size = Pt(11.5)
        font_object.name = 'Times New Roman'

        font_default=font_styles.add_style('DefaultStyle', WD_STYLE_TYPE.CHARACTER)
        font_object_2 = font_default.font
        font_object_2.size = Pt(13)
        font_object_2.name = 'Times New Roman'


        logo=document.add_picture('img/mff_logo.png', width=Inches(1.25))
        last_paragraph = document.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        head = document.add_paragraph()
        head.add_run('Региональная общественная организация\n'
                  '«Московская федерация футбола»\n'
                  'Контрольно-дисциплинарный комитет',style='HeadStyle').bold=True
        head.alignment=1

        numb=document.add_paragraph()
        numb.add_run(f'Исх. №{esc_num} от {now}',style='DefaultStyle')

        club_1=document.add_paragraph()
        club_1.add_run(f'{self.side_one.name}',style='DefaultStyle').bold=True
        club_1.alignment = 2
        club_2 = document.add_paragraph()
        club_2.add_run(f'{self.side_two.name}', style='DefaultStyle').bold = True
        club_2.alignment = 2

        main_text=document.add_paragraph()
        main_text.add_run(f'Контрольно-дисциплинарным комитетом Региональной общественной организации '
                          f'«Московская федерация футбола» (далее – «КДК РОО МФФ») '
                          f'рассматриваются вопросы о несоблюдении требований Регламента '
                          f'«Чемпионата г. Москвы по футболу среди мужчин в рамках зонального '
                          f'этапа Всероссийских спортивных соревнований по футболу «III дивизион» '
                          f'сезона 2021 года» со стороны ГБУ «СШ № 75 «Савеловская» Москомспорта, а именно:'
                          f'Нарушение ст.4.22 Регламента Чемпионата, в соответствии с которым в '
                          f'протокол матча Клуба, участвующего в Дивизионе «А», могут '
                          f'включаться не более 5 (пяти) футболистов по карточке Клуба, '
                          f'участника Чемпионата в дивизионе «Б», но не старше 21 года, '
                          f'если учредителем этих клубов является одно юридическое лицо.',
                          style='DefaultStyle')
        call_text=document.add_paragraph()
        call_text.add_run(f'Уведомляем Вас, что заседание КДК состоится 10 июня 2021 года в 13:00 по адресу: '
                          f'город Москва, ул. Радио д.12, стр.2, в помещение конференц-зала. '
                          f'КДК счел необходимым явку следующих лиц:'
                          f'Заместитель директора по СП - Ражев В.В.',style='DefaultStyle')
        notify_text=document.add_paragraph()
        notify_text.add_run(f'Заинтересованные лица, в срок до 18:00 09.06.2021г., '
                            f'вправе предоставить КДК РОО МФФ свои пояснения с обоснованием своей позиции '
                            f'по рассматриваемым дисциплинарным нарушениям со ссылкой на доказательства '
                            f'(документы направлять по адресу email: Zyxel1995@mail.ru).',style='DefaultStyle')

        # document.add_heading('Heading, level 1', level=1)
        # document.add_paragraph('Intense quote', style='Intense Quote')
        #
        # document.add_paragraph(
        #     f'Команда {self.side_one.name}', style='List Bullet'
        # )
        # document.add_paragraph(
        #     f'Вызвает команду {self.side_two.name} на бой', style='List Number'
        # )
        #
        # records = (
        #     (3, '101', 'Spam'),
        #     (7, '422', 'Eggs'),
        #     (4, '631', 'Spam, spam, eggs, and spam')
        # )
        #
        # table = document.add_table(rows=1, cols=3)
        # hdr_cells = table.rows[0].cells
        # hdr_cells[0].text = 'Qty'
        # hdr_cells[1].text = 'Id'
        # hdr_cells[2].text = 'Desc'
        # for qty, id, desc in records:
        #     row_cells = table.add_row().cells
        #     row_cells[0].text = str(qty)
        #     row_cells[1].text = id
        #     row_cells[2].text = desc
        #
        # document.add_page_break()

        document.save(f'Иcx№  {self.side_one.shrt_name}-{self.side_two.shrt_name}.docx')


class Decesion:
    pass
