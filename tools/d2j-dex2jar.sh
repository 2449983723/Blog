#用于将dex文件转换为jar包
#参数１：dex路径
#参数２：生成的jar路径
DEX2_HOME="/home/liunian/Android5.0/反编译/dex2jar-2.0"
dexFilePath=$1
jarFilePath=$2
cd $DEX2_HOME
cp $dexFilePath $DEX2_HOME
dexFileName=$(basename $dexFilePath)
split="/"
temDexFilePath=$DEX2_HOME$split$dexFileName
./d2j-dex2jar.sh $temDexFilePath
rm -f $temDexFilePath
dexFileNameWithoutSuf=$(basename $dexFilePath .dex)
addJarName="-dex2jar.jar"
jarFileName=$dexFileNameWithoutSuf$addJarName
echo $jarFileName
mv -f $DEX2_HOME$split$jarFileName $jarFilePath

