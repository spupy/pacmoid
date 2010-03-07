#!/bin/bash

# Remove old plasmoid
plasmapkg -r pacmoid
rm -rf /home/uibxn/.kdemod4/share/apps/plasma/plasmoids/pacmoid
rm /home/uibxn/.kdemod4/share/kde4/services/*pacmoid*
echo "Uninstalled old plasmoid."

# Deploy the new code
zip -r pacmoid.zip contents metadata.desktop
plasmapkg -i pacmoid.zip
echo "Installed new plasmoid."

echo "Done."
echo "Open and close \"Add Widgets\" to load the plasmoid in the catalog."
