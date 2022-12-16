#!/bin/bash
# Download a file on /tmp/TEMPDIR/FILENAME

URLDOWNLOAD="%MosyleCDNFile:670ae6de-00f3-45ad-ba6a-9733ead861c0%";
TEMPDIR="mosul";
PKGNAME="AdobeCCPSARM.zip"
SHRLOCATION="/Users/Shared"

FILENAME="$(basename $PKGNAME)";
DOWNLOADFILE="/Users/Shared/$TEMPDIR/$FILENAME";

if [ ! -d "/Users/Shared/$TEMPDIR" ]; then  
   mkdir -p "/Users/Shared/$TEMPDIR";  
fi;

curl -L --silent -o "$DOWNLOADFILE" "$URLDOWNLOAD";

ic="1"

if [ -e $DOWNLOADFILE ]; then 
  unzip -o -qq "$DOWNLOADFILE" -d "$SHRLOCATION";
  echo "$DOWNLOADFILE - Success";
else
  echo "Download failed";
fi

export ic=$?

if [ "$ic" -eq "0" ]; then 
	echo "Extraced successfully";
    installer -pkg /Users/Shared/Adobe\ CC\ Photoshop/Build/Adobe\ CC\ Photoshop_Install.pkg -target /;
else 
	echo "Installer failed! Check /var/log/system.log, /var/log/install.log"; 
fi
