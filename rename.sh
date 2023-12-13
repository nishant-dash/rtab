snap=$(grep -E "^name:" snap/snapcraft.yaml | awk '{print $2}')
echo "renaming ${snap}_*.snap to ${snap}.snap"
echo -n "pwd: "
pwd
ls -al
echo "Removing previous snap if it exists"
if [[ -e "${snap}.snap" ]];
then
    rm "${snap}.snap"
fi
echo "Renaming snap here."
mv ${snap}_*.snap ${snap}.snap
