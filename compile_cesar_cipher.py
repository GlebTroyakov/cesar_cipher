import sys
import cesar_cipher
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QRadioButton,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QSpinBox
)

import PyQt5
QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling, True)


def show_error(message):
    QMessageBox.critical(main_widget, "Ошибка", message)


def show_info(message):
    QMessageBox.information(main_widget, "Информация", message)


def on_open_click():
    """Реакция на нажатие кнопки "Загрузить из файла"."""
    try:
        file_name = QFileDialog.getOpenFileName(
            None,
            "Открыть файл",
            "",
            "Текстовые файлы (*.txt *.json *.csv)")

        if file_name[0] == "":
            return

        txt_main.setText(cesar_cipher.open_file(file_name[0]))  # вывод на экран виджета текст
        # show_info("Файл {} открыт.".format(file_name[0]))  # window about open file

        # Открыть файл с помощью utils.open_file() и
        # установить текст 'txt_main' в его содержимое

    except Exception as err:
        show_error(str(err))


def on_save_click():
    """Реакция на нажатие кнопки "Сохранить в файл..."."""
    try:
        file_name = QFileDialog.getSaveFileName(
            None,
            "Сохранить как...",
            "",
            "Текстовые файлы (*.txt *.json *.csv)")

        if file_name[0] == "":
            return

        cesar_cipher.save_file(file_name[0], txt_main.toPlainText())
        # Сохранить содержимое 'txt_main' в файл с помощью utils.save_file()

        # show_info("Файл {} сохранен.".format(file_name[0]))  # окно с завершением сохранения
    except Exception as err:
        show_error(str(err))


def on_do_crypt_click():
    """Реакция на нажатие кнопки "Выполнить"."""
    try:
        text = txt_main.toPlainText()  # возвращяет текст из окна виджета
        shift = int(sp_shift.text())  # text() сделал текстовое значение из окна а потом целое число

        if rd_encrypt.isChecked():  # проверяет виджет с отметкой
            res = cesar_cipher.ceasar(text, shift)
        else:
            res = cesar_cipher.ceasar(text, -shift)
        # Если радиокнопка 'rd_encrypt' выбрана (isChecked() == True),
        # выполняется шифрование, иначе дешифрование
        txt_main.setText(res)
    except Exception as err:
        show_error(str(err))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Главное окно приложения
    main_widget = QWidget()
    main_widget.resize(640, 350)
    main_widget.setWindowTitle("Шифр Цезаря")
    main_widget.setWindowIcon(QIcon('main_icon.png'))

    # 1. Левая часть окна
    vbox_left = QVBoxLayout()

    gb_file_actions = QGroupBox("Текст:")
    vbox_gb_file_actions = QVBoxLayout()

    # 1.1. Открытие/сохранение файлов
    btn_open = QPushButton("Загрузить из файла...")
    btn_save_as = QPushButton("Сохранить в файл...")

    vbox_gb_file_actions.addWidget(btn_open)
    vbox_gb_file_actions.addWidget(btn_save_as)

    gb_file_actions.setLayout(vbox_gb_file_actions)

    # Действия кнопок
    btn_open.clicked.connect(lambda: on_open_click())
    btn_save_as.clicked.connect(lambda: on_save_click())

    # 1.2. Шифрование / дешифрование
    gb_crypt_options = QGroupBox("Режим:")

    rd_encrypt = QRadioButton("Шифрование")
    rd_decrypt = QRadioButton("Дешифрование")
    lbl_shift = QLabel("Сдвиг:")
    sp_shift = QSpinBox()  #
    sp_shift.setMinimum(1)  # минимальный сдвиг
    sp_shift.setSingleStep(1)  # шаг для сдвига

    btn_do_crypt = QPushButton("Выполнить")
    rd_encrypt.setChecked(True)

    btn_do_crypt.clicked.connect(lambda: on_do_crypt_click())

    vbox_gb_crypt_options = QVBoxLayout()
    vbox_gb_crypt_options.addWidget(rd_encrypt)
    vbox_gb_crypt_options.addWidget(rd_decrypt)
    vbox_gb_crypt_options.addWidget(lbl_shift)
    vbox_gb_crypt_options.addWidget(sp_shift)
    vbox_gb_crypt_options.addWidget(btn_do_crypt)
    vbox_gb_crypt_options.addStretch()  # was off
    gb_crypt_options.setLayout(vbox_gb_crypt_options)

    vbox_left.addWidget(gb_file_actions)
    vbox_left.addWidget(gb_crypt_options)
    vbox_left.addStretch()

    # 2. Правая часть окна

    # Текст
    vbox_right = QVBoxLayout()

    # txt_tmp = ''
    # print(txt_tmp)

    txt_main = QTextEdit()
    txt_main.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    # a = txt_main.toPlainText()
    vbox_right.addWidget(txt_main)

    # 3. Общее расположение элементов
    main_layout = QHBoxLayout()
    main_layout.setSpacing(15)
    main_layout.addLayout(vbox_left)
    main_layout.addLayout(vbox_right)

    # Запуск приложения
    main_widget.setLayout(main_layout)
    main_widget.show()
    sys.exit(app.exec_())