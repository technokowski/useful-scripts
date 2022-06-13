#!/bin/bash

# Loop through users with homes in /Users; exclude any accounts you don't want removed (i.e. local admin and current user if policy runs while someone is logged in)
# Below command lists all registered users

# to execute run: sudo bash (path to this file), ex;
# sudo bash /Users/SJUSD/Desktop/remove_all_users.sh
# make sure to execute from an admin profile, i.e;, ADMIN, PERSON.
# DO NOT EXECUTE from an admin profile other than those two unless you
# have added that user line 13, i.e;, | grep -v example ADMIN |
# dscl . -ls /Users

for username in `dscl . -ls /Users | grep -v PERSON|  grep -v ADMIN | grep -v Shared | grep -v username | grep -v Guest`
do
    echo 'Beginning User Removal'
    if [[ $username == `ls -l /dev/console | awk '{print $3}'` ]]; then
        echo "Skipping user: $username (current user)"

    elif [[ $username == _* ]] && echo "Starts with _"; then
	echo "Skip"

    else
        echo "Removing user: $username"

        dscl . -delete /Users/$username

    fi
done

for username in `dscl . -ls /Users | grep -v PERSON|  grep -v ADMIN | grep -v Shared | grep -v username | grep -v Guest`
do
    echo 'Beginning Home Folder Removal'
    if [[ $username == `ls -l /dev/console | awk '{print $3}'` ]]; then
        echo "Skipping user: $username (current user)"
    else
        echo "Removing folder: $username"
	echo "goodbye"

        # Removes the user directory
        rm -rf /Users/$username
    fi
done
