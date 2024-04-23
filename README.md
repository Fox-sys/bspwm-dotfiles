# Мой билдер для bspwm основанный на билдере от Zproger

#### Ссылка на основной репозиторий: https://github.com/Zproger/bspwm-dotfiles

## Установка

- Установить Arch
- Отредактировать файл `/etc/locale.gen` и раскоментировать `ru_RU.UTF-8`
- `sudo locale-gen`
- `sudo pacman -S xorg xorg-xinit bspwm sxhkd xterm git python3 poetry git`
- Отредактировать файл `/etc/X11/xinit/xinitrc` (`exec xterm -geometry 80x66+0+0 -name login` -> `exec bspwm`)
- `git clone https://github.com/Fox-sys/bspwm-dotfiles.git`
- `cd bspwm-dotfiles`
- `poetry init`
- `poetry run python Builder/src/run/install.py`
- `startx`

### !!! Если этот способ не сработал, можно использовать старый билдер `python BuilderOld/install.py` !!!