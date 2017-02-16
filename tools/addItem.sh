home="/home/liunian/桌面"
startItem="    <item>"
endItem="</item>"
cd $home

while read line
do
	echo $startItem$line$endItem >> unicode.xml
done < "unicode.txt"

