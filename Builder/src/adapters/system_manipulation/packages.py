from src.application.configurator.enums import DriverTypeEnum

PACMAN_DEPENDENCIES = [
    'tumbler', 'ffmpegthumbnailer', 'lsd', 'alacritty', 'brightnessctl',
    'automake', 'blueman', 'bluez', 'bluez-utils', 'dunst', 'fakeroot', 'feh',
    'gcc', 'gedit', 'git', 'gnu-netcat', 'btop', 'lxappearance',
    'mat2', 'mpd', 'mpv', 'thunar', 'ncmpcpp', 'fastfetch', 'network-manager-applet', 'nitrogen',
    'pamixer', 'papirus-icon-theme', 'pavucontrol', 'polybar', 'autoconf', 'mpc', 'pipewire',
    'pipewire-alsa', 'python-pyalsa', 'ranger', 'redshift', 'reflector', 'rofi', 'rofi-calc',
    'rofi-emoji', 'sudo', 'slop', 'tree', 'unrar', 'zip', 'unzip', 'uthash', 'xarchiver',
    'xorg-xbacklight', 'zathura', 'zathura-djvu', 'zathura-pdf-mupdf',
    'cmake', 'clang', 'gzip', 'make', 'openssh', 'shellcheck',
    'vlc', 'usbutils', 'picom', 'networkmanager-openvpn', 'alsa-plugins', 'alsa-tools', 'alsa-utils', 'ffmpeg',
    'p7zip', 'gparted', 'sshfs', 'openvpn', 'xclip', 'gpick', 'wget', 'ueberzug', 'netctl', 'light',
    'breeze', 'intel-ucode', 'ttf-jetbrains-mono', 'ttf-jetbrains-mono-nerd', 'ttf-fira-code',
    'ttf-iosevka-nerd', 'zsh', 'curl', 'screenkey', 'timeshift', 'ghex', 'gufw', 'python-pywal',
    'bleachbit', 'veracrypt', 'gtkhash', 'gnome-firmware', 'touche', 'dconf-editor',
    'obs-studio', 'telegram-desktop', 'code',
    'deluge-gtk', 'flameshot', 'sqlitebrowser', 'python-pip', 'cloc',
]

AUR_DEPENDENCIES = [
    'cava', 'i3lock-color', 'ptpython', 'google-chrome', 'rofi-greenclip'
]

DRIVER_PACKAGES = {
    DriverTypeEnum.AMD_GPU_FREE: [
        'mesa', 'vulkan-radeon', 'libva-mesa-driver', 'lib32-libva-mesa-driver', 'lib32-mesa', 'lib32-vulkan-radeon',
        'vulkan-tools', 'vulkan-headers', 'vulkan-icd-loader', 'lib32-vulkan-icd-loader'
    ]
}
