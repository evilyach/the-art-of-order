# Props to @cdrx on GitHub for inspiration

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
RUN set -x

# Global settings
ARG WINE_VERSION=winehq-staging
ARG PYTHON_VERSION=3.8.2
ARG PYINSTALLER_VERSION=4.0

# Downloading basic packages
RUN dpkg --add-architecture i386
RUN apt update -qy
RUN apt install --no-install-recommends -qfy \
    apt-transport-https \
    software-properties-common \
    wget \
    gpg-agent \
    rename

# Downloading wine
RUN wget -nc https://dl.winehq.org/wine-builds/winehq.key
RUN apt-key add winehq.key
RUN add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'
RUN apt-get update -qy
RUN apt-get install --no-install-recommends -qfy \
    $WINE_VERSION \
    winbind \
    cabextract
RUN apt-get clean

# Downloading winetricks
RUN wget -nv https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
RUN chmod +x winetricks
RUN mv winetricks /usr/local/bin

# Wine settings
ENV WINEARCH win64
ENV WINEDEBUG fixme-all
ENV WINEPREFIX /wine

# PyPi repository and index location
ENV PYPI_URL=https://pypi.python.org/
ENV PYPI_INDEX_URL=https://pypi.python.org/simple

RUN winetricks win7
RUN for msifile in `echo core dev exe lib path pip tcltk tools`; do \
        wget -nv "https://www.python.org/ftp/python/$PYTHON_VERSION/amd64/${msifile}.msi"; \
        wine msiexec /i "${msifile}.msi" /qb TARGETDIR=C:/Python38; \
        rm ${msifile}.msi; \
    done
RUN cd /wine/drive_c/Python38
RUN echo 'wine '\''C:\Python38\python.exe'\'' "$@"' > /usr/bin/python
RUN echo 'wine '\''C:\Python38\Scripts\easy_install.exe'\'' "$@"' > /usr/bin/easy_install
RUN echo 'wine '\''C:\Python38\Scripts\pip.exe'\'' "$@"' > /usr/bin/pip
RUN echo 'wine '\''C:\Python38\Scripts\pyinstaller.exe'\'' "$@"' > /usr/bin/pyinstaller
RUN echo 'wine '\''C:\Python38\Scripts\pyupdater.exe'\'' "$@"' > /usr/bin/pyupdater
RUN echo 'assoc .py=PythonScript' | wine cmd
RUN echo 'ftype PythonScript=c:\Python38\python.exe "%1" %*' | wine cmd
RUN while pgrep wineserver >/dev/null; do echo "Waiting for wineserver"; sleep 1; done
RUN chmod +x /usr/bin/python /usr/bin/easy_install /usr/bin/pip /usr/bin/pyinstaller /usr/bin/pyupdater
RUN (pip install -U pip || true)
RUN rm -rf /tmp/.wine-*

# Windows settings
ENV W_DRIVE_C=/wine/drive_c
ENV W_WINDIR_UNIX="$W_DRIVE_C/windows"
ENV W_SYSTEM64_DLLS="$W_WINDIR_UNIX/system32"
ENV W_TMP="$W_DRIVE_C/windows/temp/_$0"

# Install Microsoft Visual C++ Redistributable for Visual Studio 2017 dll files
RUN rm -f "$W_TMP"/*
RUN wget -P "$W_TMP" https://download.visualstudio.microsoft.com/download/pr/11100230/15ccb3f02745c7b206ad10373cbca89b/VC_redist.x64.exe
RUN cabextract -q --directory="$W_TMP" "$W_TMP"/VC_redist.x64.exe
RUN cabextract -q --directory="$W_TMP" "$W_TMP/a10"
RUN cabextract -q --directory="$W_TMP" "$W_TMP/a11"
RUN cd "$W_TMP"
RUN rename 's/_/\-/g' *.dll
RUN cp "$W_TMP"/*.dll "$W_SYSTEM64_DLLS"/

# Install pyinstaller
RUN /usr/bin/pip install pyinstaller==$PYINSTALLER_VERSION

# Put /src/ folder inside wine
RUN mkdir /src/ && ln -s /src /wine/drive_c/src
VOLUME /src/
WORKDIR /wine/drive_c/src/
RUN mkdir -p /wine/drive_c/tmp

COPY ./dist/tao-0.1.0-py3-none-any.whl \
    ./src \
    /wine/drive_c/src/
COPY ./scripts/release-windows.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]