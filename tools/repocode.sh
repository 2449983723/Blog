cd /home/liunian/flyme_code/flyme_m85
cd frameworks/base
git checkout sdk_M85-l1_base
git stash
git branch -D M85-l1_base
git checkout -b M85-l1_base remotes/meizu/M85-l1_base
cd ../../
cd meizu/SDK/MeizuCommon
git checkout flyme5-dev
git stash
git branch -D flyme5_base
git checkout -b flyme5_base remotes/meizu/flyme5_base
cd ../MeizuWidget
git checkout flyme5-dev
git stash
git branch -D flyme5_base
git checkout -b flyme5_base remotes/meizu/flyme5_base
cd ../ColorTheme
git checkout flyme5-dev
git stash
git branch -D flyme5_base
git checkout -b flyme5_base remotes/meizu/flyme5_base
cd ../../../
cd flyme/frameworks/flyme-res/
git checkout flyme5-dev
git stash
git branch -D flyme5_base
git checkout -b flyme5_base remotes/meizu/flyme5_base
cd ../../../

repo sync
# rm -rf out
source build/envsetup.sh
lunch full_meizu6795_lwt_l1-userdebug
make update-api && make
make cts

cd frameworks/base
git checkout .
git checkout sdk_M85-l1_base
git stash pop
cd ../../
cd meizu/SDK/MeizuCommon
git checkout .
git checkout flyme5-dev
git stash pop
cd ../MeizuWidget
git checkout .
git checkout flyme5-dev
git stash pop
cd ../ColorTheme
git checkout .
git checkout flyme5-dev
git stash pop
cd ../../../
cd flyme/frameworks/flyme-res/
git checkout flyme5-dev
git stash pop
cd ../../../

