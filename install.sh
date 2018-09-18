# install defauld need packages
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    gnupg \
    curl \
    software-properties-common \
    wget \
    make \
    build-essential \
    cpp \
    gpp \
    g++ \
    snap \
    snapd \
    dialog \
    libssl-dev \
    python3 \
    python3-setuptools \
    python3-software-properties \
    firmware-iwlwifi \
    wicd

# install need packages
apt-get install -y \
    git \
    nano \
    htop \
    terminator \
    nautilus \
    default-jre

# generation ssh key
mkdir -p ~/.ssh
ssh-keygen

# install descriptions for installer programm
pip3 install -r requirements.pip

# run installer
python3 ./main.py
