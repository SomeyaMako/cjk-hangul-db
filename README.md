# cjk-hangul-db

A repository for CJK characters' hangul pronunciation.

### Usage
- Run the script ```h2h.py``` by typing the following command in the terminal:
```
python h2h.py
```
Input the character(s) to search for readings in Korean
```
$> python h2h.py
草長鶯飛二月天
漢字「草」的讀音爲：초
漢字「長」的讀音爲：장
漢字「鶯」的讀音爲：앵
漢字「飛」的讀音爲：비
漢字「二」的讀音爲：이
漢字「月」的讀音爲：월
漢字「天」的讀音爲：천
$> _
```
or input hangul(s) to search for characters with that pronunciation.
```
$> python h2h.py
묘서동처
讀音爲「묘」的漢字：卯吵墓妙廟描昴杳淼渺猫眇秒竗緲苗藐貓錨
讀音爲「서」的漢字：叙噬墅壻婿嶼序庶庻徐恕抒捿揟撕敍敘暑曙書栖棲樨湑澨犀瑞筮紓絮緒緖署耡胥舒芧薯西誓諝谞逝鉏鋤閪黍鼠
讀音爲「동」的漢字：仝侗倲偅働僮冬凍動同哃垌峒彤憧朣東桐棟橦洞涷潼炵疼瞳童胴艟苳茼董蕫蝀銅錬鮗鼕
讀音爲「처」的漢字：凄処妻悽淒狙萋處褄覷郪
$> _
```
Note that you can also mix those two scripts when using.
```
$> python h2h.py
漢한
漢字「漢」的讀音爲：한
讀音爲「한」的漢字：佷僩厂嫺嫻寒恨悍扞捍旱暵桿汗漢澣瀚罕翰邗邯閈閑閒限韓駻鷳鼾
$> _
```
```h2hext.py```provides a (nearly) full support for CJK/CJK Comp./CJK Ext.A. The basic one (```h2h.py```) cannot handle Simplified Chinese
```
$> python h2h.py
简体字读音检索
未找到漢字「简」的讀音
漢字「体」的讀音爲：분/체
漢字「字」的讀音爲：자
未找到漢字「读」的讀音
漢字「音」的讀音爲：음
未找到漢字「检」的讀音
漢字「索」的讀音爲：삭/색
$> _
```
while the extended one can deal with it pretty well.
```
$> python h2hext.py
简体字读音检索
漢字「简」的讀音爲：간
漢字「体」的讀音爲：분/체
漢字「字」的讀音爲：자
漢字「读」的讀音爲：독
漢字「音」的讀音爲：음
漢字「检」的讀音爲：검
漢字「索」的讀音爲：삭/색
$> _
```
