uname -r
echo "Wont work unless on the correct version has to be an arch based version. If under here there is an error it isn't compatible with your system otherwise its fine."
pacman --version
sudo pacman -S python
sudo pacman -S python-pip
python --version
pip install pygame
./Calamity.sh