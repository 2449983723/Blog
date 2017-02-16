#从res-meizu-common拷贝出对应的资源到桌面
#参数１：资源名称
RES_HOME="/home/liunian/flyme_code/flyme_m86/flyme/frameworks/flyme-res/res-meizu-common/res/"
OUT_PATH="/home/liunian/桌面/"
drawableXhdpi="drawable-xhdpi"
drawableXxhdpi="drawable-xxhdpi"
drawableXxxhdpi="drawable-xxxhdpi"
split="/"

resName=$1
mkdir $OUT_PATH$resName
cd $OUT_PATH$resName
mkdir $drawableXhdpi
mkdir $drawableXxhdpi
mkdir $drawableXxxhdpi
cp $RES_HOME$drawableXhdpi$split$resName $drawableXhdpi
cp $RES_HOME$drawableXxhdpi$split$resName $drawableXxhdpi
cp $RES_HOME$drawableXxxhdpi$split$resName $drawableXxxhdpi
