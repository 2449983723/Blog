newApk="/home/liunian/FixBug/AndFixTest/apk/newApk/app-release.apk" #新的apk
oldApk="/home/liunian/FixBug/AndFixTest/apk/oldApk/app-release.apk" #旧的apk
patchPath="/home/liunian/FixBug/AndFixTest/patch/"           #保存输出补丁的目录
keystore="/home/liunian/.android/android_studio.jks"      #打包所用的kyestore
keystorePassword="123456"                                 #keystore的密码
keystoreAlias="android_studio"                            #keystore用户别名
keystoreAliasPassword="123456"                            #keystore用户别名密码

cd /home/liunian/FixBug/AndFixTest/AndFix-master/tools/apkpatch-1.0.3
./apkpatch.sh -f $newApk -t $oldApk -o $patchPath -k $keystore -p $keystorePassword -a $keystoreAlias -e $keystoreAliasPassword
