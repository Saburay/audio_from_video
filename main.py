from colorama import Fore
from colorama import init
from all_functions import  *
init()


def main():
    user_change = input(Fore.RESET + '\n[+] Выберите действие:\n   [1] Объединить видео\n   [2] Вырезать фрагмент\n   '
                        '[3] Удалить аудиодорожку из видео\n   [4] Извлечь аудио\n   [5] Изменить громкость видео\n'
                        '   [6] Добавить аудио к видео\n   [7] Извлечь кадры из видео\n   '
                        '[8] Создать клип из картинок\n   [9] Выход\n   >>> ')
    if user_change == "1":
        merge_video_clip(input('\n[+] Введите путь к папке с файлами: '),
                         input('[+] Введите название для объединенного видео: '))
    elif user_change == "2":
        clip_video(input('\n[+] Введите путь к файлу видео: '), input('[+] Введите время начала фрагмента\n'
                                                                      '   - пример: 02:25\n   >>> '),
                   input('[+] Введите время окончания фрагмента\n'
                         '   - пример: 03:50\n   >>> '))
    elif user_change == "3":
        remove_audio_from_video(input('\n[+] Введите путь к файлу видео: '))
    elif user_change == "4":
        extract_mp3(input('\n[+] Введите путь к видео или, к папке с видео: '))
    elif user_change == "5":
        zoom_in_out(input('\n[+] Введите путь к файлу видео: '),
                    input('[+] Введите коэффициент для изменения громкости\n   '
                          '- Нормальная громкость: 1 (пример коэффициента: 0.5, 1.2)\n   >>> '))
    elif user_change == "6":
        merge_video_audio(input('\n[+] Введите путь к файлу видео: '), input('[+] Введите путь к файлу аудио: '))
    elif user_change == "7":
        extract_image_from_video(input('\n[+] Введите путь к файлу видео: '))
    elif user_change == "8":
        clip_from_image(input('\n[+] Введите путь к папке с картинками: '), input('[+] Введите название клипа: '),
                        input('[+] Введите продолжительность показа кадра (прим.: 0.1 или 1): '))
    elif user_change == "9":
        exit(0)
    else:
        print(Fore.RED + '\n[-] Неопознанный выбор. Повторите снова')
        main()

