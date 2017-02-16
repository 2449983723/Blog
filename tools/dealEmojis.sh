home="/home/liunian/Android5.0/emojis/iosmore/"
filelist=`ls /home/liunian/Android5.0/emojis/iosmore`
needAddEmojisThree="/home/liunian/Android5.0/emojis/needAddEmojisThree/"
split="."
cd $home
for file in $filelist
do 
	OLD_IFS="$IFS" 
 	IFS='.'
	arr=($file)
	IFS="$OLD_IFS" 
	num=${#arr[@]}
	if [ $num -eq 2 ]
    then
		name=${arr[0]}
		OLD_IFS="$IFS"
	 	IFS='_'
		splitArr=($name})
		IFS="$OLD_IFS" 
		if [ ${#splitArr[@]} -eq 2 ]
		then
			echo $file
			cp $file "/home/liunian/Android5.0/emojis/needAddEmojisTwo"
		else
			echo $file
			cp $file "/home/liunian/Android5.0/emojis/needAddEmojisOne"
		fi
	elif [ $num -eq 3 ]
	then
		echo $file
		if [ ${arr[1]} == "1" ]
		then
			cp $file $needAddEmojisThree
			cd $needAddEmojisThree
			newName=${arr[0]}$split${arr[2]}
			mv $file $newName
			cd $home
		else
			cp $file "/home/liunian/Android5.0/emojis/needDeleteEmojis"
		fi
	else
		cp $file "/home/liunian/Android5.0/emojis/needDeleteEmojis"
	fi
done


