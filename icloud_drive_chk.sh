#!/bin/bash

iCloudDrivePath="/Library/Mobile Documents/com~apple~CloudDocs"

# It was discovered that Catalina at one point moved the iCloud drive folder
# On macs upgraded to 10.15 the folder is still 'Mobile Documents'.
# If discovered that some 10.15 macs have it moved to CloudStorage
# Then uncomment out the lines below.

# OSver="$(/usr/bin/sw_vers -productVersion | /usr/bin/cut -d . -f 2)"
# if [ "$OSver" -ge "15" ]; then
#   iCloudDrivePath="/Library/CloudStorage/iCloud Drive";
# else iCloudDrivePath="/Library/Mobile Documents/com~apple~CloudDocs" echo 'not cat';
# fi

# Get the logged in user and their home folder
grabConsoleUserAndHome()
{
currentUser=$(stat -f %Su "/dev/console")
homeFolder=$(dscl . read "/Users/$currentUser" NFSHomeDirectory | cut -d: -f 2 | sed 's/^ *//'| tr -d '\n')
  case "$homeFolder" in
     *\ * )
           homeFolder=$(printf %q "$homeFolder")
          ;;
       *)
           ;;
esac
}

grabConsoleUserAndHome

if [[ "$currentUser" == "root" ]]
    then
        exit
fi

# Checks if the drive path and file exists
if [[ -e "$homeFolder""$iCloudDrivePath" ]]
    then
        # Checks status of iCloud Drive Desktop and Documents setting
        iCloudDesktop=$(defaults read /Users/$currentUser/Library/Preferences/com.apple.finder.plist FXICloudDriveDesktop)
        if [[ "$iCloudDesktop" = 1 ]];
            then
                echo 'iCloud Desktop Enabled';
                echo "<result>true</result>"

        else
            echo 'Drive enabled, Desktop Disabled';
            echo "<result>false</result>"

        fi;

    else
        echo "User does not have iCloud Drive setup"
        echo "<result>false</result>"
fi

exit 0
