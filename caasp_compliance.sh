#!/bin/bash

# sbac user must exist.
SPACES="https://www.path-to-file.plist"
HOTKEY="https://www.path-to-file.plist"

curl -LJ -o "/Users/Shared/com.apple.spaces.plist" "$SPACES"
curl -LJ -o "/Users/Shared/com.apple.symbolichotkeys.plist" "$HOTKEY"

cp /Users/Shared/com.apple.spaces.plist /Users/sbac/Library/Preferences/com.apple.spaces.plist
cp /Users/Shared/com.apple.symbolichotkeys.plist /Users/sbac/Library/Preferences/com.apple.symbolichotkeys.plist

defaults write com.apple.assistant.support "Assistant Enabled" -bool false

exit
