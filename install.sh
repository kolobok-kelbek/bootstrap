#!/usr/bin/env bash
# set default repositories in sources.list
{
    echo 'deb http://security.debian.org/ stretch/updates main non-free'
    echo 'deb-src http://security.debian.org/ stretch/updates main non-free'
    echo ''
    echo 'deb http://mirror.yandex.ru/debian stretch main non-free'
    echo 'deb-src http://mirror.yandex.ru/debian stretch main non-free'
    echo ''
    echo 'deb http://mirror.yandex.ru/debian stretch-updates main non-free'
    echo 'deb-src http://mirror.yandex.ru/debian stretch-updates main non-free'
    echo ''
    echo 'deb http://mirror.yandex.ru/debian/ stretch-proposed-updates main non-free contrib non-free'
    echo 'deb-src http://mirror.yandex.ru/debian/ stretch-proposed-updates main non-free contrib'
} > /etc/apt/sources.list

# update
apt-get update && apt-get -y upgrade

# install defauld need packages
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    gnupg \
    gnupg2 \
    curl \
    software-properties-common \
    wget \
    make \
    build-essential \
    dirmngr \
    cpp \
    gpp \
    g++ \
    snap \
    snapd \
    dialog \
    devscripts \
    equivs \
    gdebi-core \
    libssl-dev \
    python3 \
    python3-setuptools \
    python3-software-properties \
    firmware-iwlwifi

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

mkdir tmp
chmod 777 tmp

# run installer
python3 ./main.py
