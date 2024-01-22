from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QHBoxLayout, QLineEdit, QCheckBox, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt
import string
import random

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        welcome_layout = QVBoxLayout()

        
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(128, 0, 0))  
        self.setPalette(palette)

        
        welcome_label = QLabel('<font size="6" color="white">Random Password Generator</font>')
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_layout.addWidget(welcome_label)

        
        logo_image = QLabel(self)
        pixmap = QPixmap('/Users/404qea/Downloads/mkemalatatukr.jpeg').scaledToWidth(300) 
        logo_image.setPixmap(pixmap)
        logo_image.setAlignment(Qt.AlignCenter)
        welcome_layout.addWidget(logo_image)

       
        telegram_label = QLabel('<font size="4" color="white">Telegram: Qea404</font>')
        telegram_label.setAlignment(Qt.AlignCenter)
        welcome_layout.addWidget(telegram_label)

        
        start_button = QPushButton('Programı Başlat', self)
        start_button.clicked.connect(self.open_main_window)
        welcome_layout.addWidget(start_button)

        self.setLayout(welcome_layout)
        self.setWindowTitle('Türk Hack Team & Black Hat Team-e Selam Olsun # Developed by 404Qea')
        self.setGeometry(300, 300, 600, 400)  
        self.setWindowIcon(QIcon('/Users/404qea/Downloads/404qealg.png'))  

        self.main_window = None

    def open_main_window(self):
        self.main_window = PasswordGenerator()
        self.main_window.show()
        self.hide()

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        options_groupbox = QGroupBox('Oluşturmak İstediğiniz Şifre Seçeneklerini Seçiniz')
        options_groupbox.setStyleSheet("QGroupBox:title { subcontrol-origin: margin; padding-left: 250px; padding-right: 500px; padding-top: 2px; padding-bottom: 5px; color: white; border: 2px solid white; border-radius: 5px; font-weight: bold; background-color: #800000; }")

        options_layout = QVBoxLayout()

        length_groupbox = QGroupBox('')
        length_groupbox.setStyleSheet("QGroupBox:title { subcontrol-origin: margin; padding-left: 5px; padding-right: 5px; padding-top: 10px; padding-bottom: 5px; color: white; border: 15px solid white; border-radius: 15px; font-weight: bold; background-color: #800000; }")

        length_layout = QHBoxLayout(length_groupbox)
        self.label_length = QLabel('Şifre Uzunluğunu Giriniz:')
        length_groupbox.setStyleSheet("QGroupBox:title { subcontrol-origin: margin; padding-left: 5px; padding-right: 5px; padding-top: 10px; padding-bottom: 5px; color: white; border: 15px solid white; border-radius: 15px; font-weight: bold; background-color: #800000; }")
        self.length_input = QLineEdit(self)
        length_layout.addWidget(self.label_length)
        length_layout.addWidget(self.length_input)

        options_layout.addWidget(length_groupbox)

        
        buttons_layout = QHBoxLayout()

        
        self.uppercase_button = QPushButton('Büyük Harf Kullan', self)
        self.lowercase_button = QPushButton('Küçük Harf Kullan', self)
        self.digits_button = QPushButton('Rakam Kullan', self)
        self.special_char_button = QPushButton('Özel Karakter Kullan', self)
        

       
        self.style_buttons([self.uppercase_button, self.lowercase_button, self.digits_button, self.special_char_button])

        
        self.uppercase_button.clicked.connect(lambda: self.toggle_checkbox(self.uppercase_checkbox))
        self.lowercase_button.clicked.connect(lambda: self.toggle_checkbox(self.lowercase_checkbox))
        self.digits_button.clicked.connect(lambda: self.toggle_checkbox(self.digits_checkbox))
        self.special_char_button.clicked.connect(lambda: self.toggle_checkbox(self.special_char_checkbox))

        buttons_layout.addWidget(self.uppercase_button)
        buttons_layout.addWidget(self.lowercase_button)
        buttons_layout.addWidget(self.digits_button)
        buttons_layout.addWidget(self.special_char_button)

       
        options_layout.addLayout(buttons_layout)

        options_groupbox.setLayout(options_layout)
        main_layout.addWidget(options_groupbox)

        self.generate_button = QPushButton('Şifre Oluştur', self)
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_button.setFixedSize(200, 40)
        self.generate_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")

        generate_button_layout = QHBoxLayout()
        generate_button_layout.addStretch(1)  
        generate_button_layout.addWidget(self.generate_button)
        generate_button_layout.addStretch(1)  

        main_layout.addLayout(generate_button_layout)

        
        password_layout = QVBoxLayout()
        password_layout.addStretch(1)  
        password_and_logos_layout = QHBoxLayout()

        

        
        logo1 = QLabel(self)
        pixmap_logo1 = QPixmap('/Users/404qea/Downloads/bayrak.png').scaledToWidth(125)  
        logo1.setPixmap(pixmap_logo1)
        logo1.setAlignment(Qt.AlignLeft | Qt.AlignTop)  

        
        logo2 = QLabel(self)
        pixmap_logo2 = QPixmap('/Users/404qea/Downloads/tsklt.jpeg').scaledToWidth(100) 
        logo2.setPixmap(pixmap_logo2)
        logo2.setAlignment(Qt.AlignLeft | Qt.AlignTop)  

        
        logo_container = QHBoxLayout()
        logo_container.addWidget(logo1)
        logo_container.addWidget(logo2)

        
        password_and_logos_layout.addLayout(logo_container)

        password_and_logos_layout.addLayout(logo_container)

      
        self.password_label = QLabel('')
        self.password_display = QTextEdit(self)
        self.password_display.setReadOnly(True)
        self.password_display.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        self.password_display.setFixedSize(400, 160)
        password_and_logos_layout.addWidget(self.password_label)
        password_and_logos_layout.addWidget(self.password_display)

        
        main_layout.addLayout(password_and_logos_layout)

      
        logo_layout = QHBoxLayout()

        logo1 = QLabel(self)
        pixmap_logo1 = QPixmap('/Users/404qea/Downloads/thtlogo.png').scaledToWidth(100)  
        logo1.setPixmap(pixmap_logo1)
        logo1.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        logo_layout.addWidget(logo1)

       
        logo_layout.addSpacing(1)

        logo2 = QLabel(self)
        pixmap_logo2 = QPixmap('/Users/404qea/Downloads/bhtlogo.jpeg').scaledToWidth(100)  
        logo2.setPixmap(pixmap_logo2)
        logo2.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        logo_layout.addWidget(logo2)

        password_and_logos_layout.addLayout(logo_layout)

        password_layout.addLayout(password_and_logos_layout)
        password_layout.addStretch(1) 
        main_layout.addLayout(password_layout)

    
        copy_button = QPushButton('Kopyala', self)
        copy_button.clicked.connect(self.copy_to_clipboard)
        copy_button.setFixedSize(200, 40)
        copy_button.setStyleSheet("background-color: #008CBA; color: white; font-size: 16px;")

        recreate_button = QPushButton('Yeniden Oluştur', self)
        recreate_button.clicked.connect(self.recreate_password)
        recreate_button.setFixedSize(200, 40)
        recreate_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 16px;")

        button_container = QVBoxLayout()
        button_container.addWidget(copy_button, alignment=Qt.AlignHCenter) 
        button_container.addWidget(recreate_button, alignment=Qt.AlignHCenter)  
        button_container.addStretch(1) 

        button_container_widget = QWidget(self)  
        button_container_widget.setLayout(button_container)  

        main_layout.addWidget(button_container_widget, alignment=Qt.AlignHCenter)  

        self.setLayout(main_layout)
        self.setWindowTitle('Şifre Oluşturucu')

       
        self.uppercase_checkbox = QCheckBox('Büyük Harf Kullan', self)
        self.lowercase_checkbox = QCheckBox('Küçük Harf Kullan', self)
        self.digits_checkbox = QCheckBox('Rakam Kullan', self)
        self.special_char_checkbox = QCheckBox('Özel Karakter Kullan', self)

        
        self.style_checkboxes([self.uppercase_checkbox, self.lowercase_checkbox, self.digits_checkbox, self.special_char_checkbox])

    def toggle_checkbox(self, checkbox):
        checkbox.setChecked(not checkbox.isChecked())

    def style_buttons(self, buttons):
        for button in buttons:
            button.setCheckable(True)
            button.setFixedSize(200, 40)
            button.setStyleSheet("background-color: #3498db; color: white; font-size: 16px; margin-bottom: 10px;")

    def style_checkboxes(self, checkboxes):
        for checkbox in checkboxes:
            checkbox.setStyleSheet("font-size: 14px; color: #3498db; margin-top: 5px;")

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                raise ValueError("Uzunluk pozitif bir tam sayı olmalıdır.")

            use_uppercase = self.uppercase_checkbox.isChecked()
            use_lowercase = self.lowercase_checkbox.isChecked()
            use_digits = self.digits_checkbox.isChecked()
            use_special_char = self.special_char_checkbox.isChecked()

            characters = ''
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_lowercase:
                characters += string.ascii_lowercase
            if use_digits:
                characters += string.digits
            if use_special_char:
                
                special_chars = '!@#$%^&*()_-+=<>?/,.'
                characters += special_chars

            if not characters:
                raise ValueError("En az bir karakter tipi seçilmelidir.")

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.setPlainText(password)
        except ValueError as e:
            QMessageBox.critical(self, 'Hata', str(e))

    def copy_to_clipboard(self):
        password = self.password_display.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(password)
        QMessageBox.information(self, 'Başarı', 'Şifre panoya kopyalandı!')

    def recreate_password(self):
        # Şifreyi temizle
        self.password_display.clear()
        # Yeni bir şifre oluştur
        self.generate_password()

if __name__ == '__main__':
    app = QApplication([])
    welcome_screen = WelcomeScreen()
    welcome_screen.show()
    app.exec_()