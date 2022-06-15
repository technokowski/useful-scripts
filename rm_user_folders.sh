#!/bin/bash

for dir in /Users/*/; do
    # for any folders you want to keep, add them below. Remember: full path or be damned!
	if [[ $dir == "/Users/super/" ]] || [[ $dir == "/Users/admin/" ]] || [[ $dir == "/Users/Shared/" ]] || [[ $dir == "/Users/vip/" ]]; then
        echo "Skipping user: $dir"
    else
        echo "Removing folder: $dir"
        # Removes the user directory; Uncomment the below line when you are ABSOLUTELY sure it removes the intended folders.
        # rm -rf $dir
    fi
done