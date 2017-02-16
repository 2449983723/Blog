filelist=`ls /home/liunian/flyme_code/flyme_m85/flyme/frameworks/flyme-res/res-meizu-common/res/drawable`
home="/home/liunian/flyme_code/flyme_m85/flyme/frameworks/flyme-res/res-meizu-common/res/drawable"
outFile="/home/liunian/documents/tools/res/res.txt"
cd $home
for file in $filelist
do 
	OLD_IFS="$IFS" 
 	IFS='.'
	arr=($file)
	IFS="$OLD_IFS"
	echo ${arr[0]} >> $outFile
done

