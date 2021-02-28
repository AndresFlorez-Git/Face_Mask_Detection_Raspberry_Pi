sudo apt-get install python3-pip
sudo apt-get install python3-picamera

sudo apt-get update
sudo apt-get upgrade

pip3 install numpy
pip3 install matplotlib
pip3 install opencv-python
pip3 install scipy

sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev
python3 -m pip install keras_applications --no-deps
python3 -m pip install keras_preprocessing --no-deps
python3 -m pip install h5py
sudo apt-get install -y openmpi-bin libopenmpi-dev
sudo apt-get install -y libatlas-base-dev
python3 -m pip install -U six wheel mock


wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.3.0/tensorflow-2.3.0-cp37-none-linux_armv7l.whl
python3 -m pip uninstall tensorflow
python3 -m pip install tensorflow-2.3.0-cp37-none-linux_armv7l.whl
