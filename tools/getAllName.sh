filelist=`ls /home/liunian/Android5.0/emojitool/NotoColorEmojis`
home="/home/liunian/Android5.0/emojitool/NotoColorEmojis"
startItem="    <item>"
endItem="</item>"
cd $home
for file in $filelist
do 
	OLD_IFS="$IFS" 
 	IFS='.'
	arr=($file)
	IFS="$OLD_IFS"
	if [ ${arr[1]} == "png" ]
	then
		echo $startItem$file$endItem >> /home/liunian/Android5.0/emojitool/allemojis.xml
	fi
done

