import copy
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

SRC = Path(r"C:\Users\ajtab\Downloads\Шаблон отчета.docx")
DST = Path(r"C:\Users\ajtab\Desktop\practica\lab1\output_Отчет_React_SPA.docx")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def para_text(para):
    return "".join(t.text or "" for t in para.findall(".//w:t", NS)).strip()


def set_para_text(para, text):
    ts = para.findall(".//w:t", NS)
    if not ts:
        r = ET.SubElement(para, W + "r")
        t = ET.SubElement(r, W + "t")
        t.text = text
        return
    ts[0].text = text
    for t in ts[1:]:
        t.text = ""


replacements = {
    "Лабораторная работа №1 «Название»": "Лабораторная работа №1 «Введение в React и SPA»",
    "Лабораторная работа №2 «Название»": "Лабораторная работа №2 «Компонент корзины и управление состоянием»",
    "2024": "2026",
}

goal_1 = (
    "Изучить основы React, JSX и принципов построения SPA, а также собрать каркас "
    "приложения на Vite и научиться передавать данные между компонентами через props."
)
goal_2 = (
    "Закрепить использование состояния в React, реализовать счетчик товаров в корзине "
    "и научиться обрабатывать событие нажатия кнопки."
)
step_1 = "Создание структуры проекта"
step_2 = "Реализация компонента Korzina"
desc_1 = (
    "Проект реализован на React с использованием Vite. В главном компоненте App "
    "выведен заголовок «Овощи» и подключен компонент Korzina, которому передаются "
    "название товара, цена и изображение. Такой подход отделяет разметку страницы "
    "от логики отдельного товарного блока."
)
desc_2 = (
    "В компоненте Korzina используется hook useState для хранения количества добавлений. "
    "При нажатии на кнопку значение count увеличивается на единицу, а на странице сразу "
    "отображается актуальное число. Передача параметров через props делает компонент "
    "универсальным и позволяет повторно использовать его для любых товаров."
)
caption_1 = "Рисунок 1 - Главная страница приложения"
caption_2 = "Рисунок 1 - Работа счетчика добавления товара"
concl_1 = (
    "В ходе работы была создана основа одностраничного приложения и отработан принцип "
    "разбиения интерфейса на независимые компоненты."
)
concl_2 = (
    "Реализована интерактивная карточка товара, которая демонстрирует работу props, "
    "useState и событий в React."
)


with zipfile.ZipFile(SRC, "r") as zin:
    doc = ET.fromstring(zin.read("word/document.xml"))
    paras = doc.findall(".//w:p", NS)
    for p in paras:
        txt = para_text(p)
        if txt in replacements:
            set_para_text(p, replacements[txt])

    # Targeted paragraph edits by order, matching the template structure.
    pmap = {
        37: "«____» _________ 2026 года",
        47: "Лабораторная работа №1 «Введение в React и SPA»3",
        48: "Лабораторная работа №2 «Компонент корзины и управление состоянием»4",
        52: goal_1,
        53: step_1,
        54: desc_1,
        56: caption_1,
        57: concl_1,
        60: goal_2,
        61: step_2,
        62: desc_2,
        64: caption_2,
        65: concl_2,
    }
    for idx, text in pmap.items():
        set_para_text(paras[idx - 1], text)

with zipfile.ZipFile(DST, "w", compression=zipfile.ZIP_DEFLATED) as zout:
    with zipfile.ZipFile(SRC, "r") as zin:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = ET.tostring(doc, encoding="utf-8", xml_declaration=True)
            zout.writestr(item, data)
