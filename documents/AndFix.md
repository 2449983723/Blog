# AndFix源码分析

### AndFix介绍
		AndFix是Android app的一个在线热补丁框架，是阿里巴巴的开源项目。使用此框架，我们能够在不重复发版的情况下，在线修改App中的Bug。就目前来说，AndFix支持Android2.3到6.0版本。完美支持Dalvik与ART的Runtime。

源码地址：[https://github.com/alibaba/AndFix](https://github.com/alibaba/AndFix) 
### AndFix的使用

１、在项目中引入andfix
	
在build.gradle中加入
	
	dependencies {
    	compile 'com.alipay.euler:andfix:0.3.1@aar'
	}
２、在自定义的Application中加载补丁

在AndroidManifest.xml文件中配置application为我们自定义的application
	
	    <application
        	android:name=".MainApplication"
        	android:allowBackup="true"
        	android:icon="@mipmap/ic_launcher"
        	android:label="@string/app_name"
        	android:theme="@style/AppTheme">
在自定义的Application中加载补丁

        package com.yang.tony.andfixdemo;
    
        import android.app.Application;
        import android.os.Environment;
        import android.util.Log;
        import com.alipay.euler.andfix.patch.PatchManager;
        import java.io.File;
        import java.io.IOException;
    
        /**
         * sample application
         *
         * @author liunian@meizu.com
         */
        public class MainApplication extends Application {
            private static final String TAG = "liunian";
    
            private static final String APATCH_PATH = "/out.apatch"; //要加载的补丁文件路径
    
            private static final String DIR = "apatch"; //AndFix存放补丁的缓存文件夹
            /**
             * patch manager
             */
            private PatchManager mPatchManager;
    
            @Override
            public void onCreate() {
                super.onCreate();
                // 初始化patch管理类
                mPatchManager = new PatchManager(this);
                // 初始化patch版本
                mPatchManager.init("1.0");
                // 加载已经添加到PatchManager中的patch
                mPatchManager.loadPatch();
    
                // add patch at runtime
                try {
                    // 下载补丁文件
                    downPatch();
                    // 补丁文件路径
                    String patchFileString = Environment.getExternalStorageDirectory()
                            .getAbsolutePath() + APATCH_PATH;
                    //添加patch，只需指定patch的路径即可，补丁会立即生效
                    mPatchManager.addPatch(patchFileString);
    
                    //缓存且加载补丁成功后，删除下载的补丁
                    File f = new File(this.getFilesDir(), DIR + APATCH_PATH);
                    if (f.exists()) {
                        boolean result = new File(patchFileString).delete();
                        if (!result)
                            Log.e(TAG, patchFileString + " delete fail");
                    }
                } catch (IOException e) {
                    Log.e(TAG, "", e);
                }
            }
    
            //当apk版本升级，需要把之前patch文件的删除
            public void removeAllPatch() {
                //删除所有已加载的patch文件
                mPatchManager.removeAllPatch();
            }
    
            // 客户端请求服务器接口(api)，服务器根据用户传递的数据分析是否有需要修复的bug。如果有bug需要修复，
            // 就下载服务器指定的.apatch文件的链接，下载完后及时加载并修复，使用addpatch(path)方法，补丁会立即生效。
            private void downPatch() {
                // 这里就不模拟下载的过程了，直接将补丁文件拷贝到对应的目录即可
            }
        }
    
    

３、补丁文件的生成

使用工具：apkpatch-1.0.3

工具路径：AndFix-master/tools/apkpatch-1.0.3（AndFix-master为AndFix的源码）

原理：根据两个apk包，生成一个差异文件，就是所谓的补丁文件

apkpatch的用法：

        命令 : ./apkpatch.sh -f new.apk -t old.apk -o output1 -k debug.keystore -p android -a androiddebugkey -e android
        
        -f <new.apk> ：新版本
        -t <old.apk> : 旧版本
        -o <output> ： 输出目录
        -k <keystore>： 打包所用的keystore
        -p <password>： keystore的密码
        -a <alias>： keystore 用户别名
        -e <alias password>： keystore 用户别名密码

根据以上用法，我写了一个脚本，每次只需要执行脚本就可以方便的输出.patch文件

        newApk="/home/liunian/FixBug/AndFixTest/apk/newApk/app-release.apk" #新的apk
        oldApk="/home/liunian/FixBug/AndFixTest/apk/oldApk/app-release.apk" #旧的apk
        patchPath="/home/liunian/FixBug/AndFixTest/patch/"           #保存输出补丁的目录
        keystore="/home/liunian/.android/android_studio.jks"      #打包所用的kyestore
        keystorePassword="123456"                                 #keystore的密码
        keystoreAlias="android_studio"                            #keystore用户别名
        keystoreAliasPassword="123456"                            #keystore用户别名密码
        
        cd /home/liunian/FixBug/AndFixTest/AndFix-master/tools/apkpatch-1.0.3
        ./apkpatch.sh -f $newApk -t $oldApk -o $patchPath -k $keystore -p $keystorePassword -a $keystoreAlias -e $keystoreAliasPassword

这样，每次需要生成补丁文件时，只需要将新旧apk拷贝到对应目录中，在执行该脚本即可在输出目录看到补丁文件：

![](/home/liunian/图片/2016-04-21 11:10:41的屏幕截图.png)

### AndFix原理

