#!/bin/bash
# Download a file on /tmp/TEMPDIR/FILENAME

URLDOWNLOAD1="/url-for-umbrella.pkg";
URLDOWNLOAD2="/url-for-umbrella-license.plist";
PKGNAME="umbrellaremote.pkg";
PLISTNAME="umbrellaorg.zip";
SHRLOCATION="/Users/Shared";

FILENAME1="$(basename $PKGNAME)";
FILENAME2="$(basename $PLISTNAME)";

DOWNLOADFILE1="/Users/Shared/$FILENAME1";
DOWNLOADFILE2="/Users/Shared/$FILENAME2";

curl -L --silent -o "$DOWNLOADFILE1" "$URLDOWNLOAD1";

ic="1"
if [ -e $DOWNLOADFILE1 ]; then 
  #unzip -o -qq "$DOWNLOADFILE" -d "$SHRLOCATION";
  echo "$DOWNLOADFILE1 - Success";
else
  echo "Download failed";
fi
export ic=$?

curl -L --silent -o "$DOWNLOADFILE2" "$URLDOWNLOAD2";

ic="1"
if [ -e $DOWNLOADFILE2 ]; then 
  unzip -o -qq "$DOWNLOADFILE2" -d "$SHRLOCATION";
  echo "$DOWNLOADFILE2 - Success";
else
  echo "Download failed";
fi
export ic=$?



if [ "$ic" -eq "0" ]; then 
	echo "Extraced successfully";
    installer -pkg /Users/Shared/umbrellaremote.pkg -target /Applications;
else 
	echo "Installer failed! Check /var/log/system.log, /var/log/install.log"; 
fi

rm "/Users/Shared/Orginfo.plist";
rm "/Users/Shared/umbrellaorg.zip";
rm "/Users/Shared/umbrellaremote.pkg";