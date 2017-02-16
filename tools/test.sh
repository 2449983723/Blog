applehome="/home/liunian/Android5.0/emojis/changsizeAppleEmojis"
androidhome="/home/liunian/Android5.0/emojitool/NotoColorEmojis/"
iosmore="/home/liunian/Android5.0/emojis/iosmore/"

filelist=`ls /home/liunian/Android5.0/emojis/changsizeAppleEmojis`
cd $applehome
for file in $filelist
do 
	echo $file
	# 这里的-f参数判断$myFile是否存在
	if [ ! -f "$androidhome$file" ]
	then
	 	cp $file $iosmore
		echo $iosmore$file
	fi
done
