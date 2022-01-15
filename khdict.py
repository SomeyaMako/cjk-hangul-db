#!/usr/bin/env python3
# -*- coding: utf-8 -*
db={
	'가':'㗎㚙㞹㢦㤉㤎㧝㪃㪼㱒㹢䂟䈔䑝䔅䕒䪪䯊䴥䶗个仮伽佳価假傢價加叚可呵咖哥哿嘉嘏坷婽嫁宊家尜岢幏彁徦愘戓戨拁斚斝暇架枷柯椵榎榢槚樖檟歌毠泇渮溊滒炣牁牫牱犌猳玍珂珈痂瘸癿稼笳笴糘耞胢腵舸苛茄葭蚵街袈訶謌诃豭貑賈贾跏跒軻轲迦酠鉫鉲鎵鎶镓駕驾髂魺鲄鴐鴚麚',
	'각':'㑢㔖㕁㙾㤩㩁㰌㱋㱿㲉㴶㾡䁷䇶䐘䖼䟩䧄䶅佫傕刻却卻各咯埆墧壳崅恪悫愙愨慤捔搁搉擱斍斠桷櫊殻殼毃玨珏礐胳脚腳茖袼覐覚覺觉角踋較閣阁隺鵅鵤',
	'간':'㫔㵎㶕㶥㸔㸧㿻䉍䓸䔵䧲䫀䯎䳚䵟乾亁侃倝偘刊囏墹墾奸姦姧婜孯干幹忓恳悭慳懇拣揀擀攼斡旰暕杆柬栞桿榦檊涆涧澗玕珢痫癇癎癷皯盰看瞯硍磵礀秆稈竿筸简簡簳粯繝羟羥肝艮艰艱芉茛葌蕑蕳虷衎衦裉裥襇襉覸諫谏豤貇赶趕踬迀鐗鐧锏閒間间靬顅馯鬜鬝鳱鶫齦龈',
	'갈':'㐓㓞㓤㠰㬞㮖㵣㵧䂒䅥䈓丐乫匄咭喝嘠噶圿嵑嶱扴掲揭擖暍曷楬毼渇渴獦碣礍秸竭羯葛蝎蠍褐輵轕鍻鞂鞨頡騔骱鶡鹖',
	'감':'㒈㔋㔶㘛㙳㜟㤌㦑㪠㮀㰸㺂㽍䀍䃭䇞䊻䌠䗣䘓䛓䤗䧩䲺佄冚减凲凵勘厱咁坎坩埳堪堿塪墈尲尶崁嵁嵅嵌弇惂感憨憾戡撖撼敢柑椷橄欠欿歁歛汵泔淦減澉玪玵瑊甘甝疳监監瞰矙砍碱磡礛竷篏粓紺绀苷莰蚶詌譼贑輡轁轗邯酣鉴鍳鍼鑑鑒鑬魐鱤鳡鵮鹐鹸鹻鹼龕龛',
	'갑':'㓣㕅㕉㗐㠷㧁㪉㭱䐦䖬䗘䘥䪺䫦匣匼厒合岬帢押搕敆玾甲瞌笚筪胛舺醘鉀钾閘闸韐',
	'갓':'㖙',
	'강':'㓻㔔㛨㝩㟠㟵㢜㧏㩖㭃㭎㱂㳾㹔㼚㼹㽘㾤䃃䃨䆲䌉䕬䗧䗵䚗䡉䥒䬕䴚傋僵冈冮刚剛勥匟唴啌嗴囥堈堽壃夅奋姜嫝岗岡峕崗嵹嵻干康弜弶強强彊忼慶慷扛掆控摃摾杠棡椌槺橿殭江溬漒漮焵牨犅犟犺猐獇玒玜琷瓨畕畺疅疆矼砊碙礓穅筻粇糠糡糨絳綱繈繦繮绛缰罡羌羗羫翞耩腔膙舡茳葁蔃薑虹蜣袶襁講謽讲豇躿鋼鎠鏮鏹钢镪降韁顜鱇',
	'개':'㑘㕢㝏㠹㨟㪡㮣㯼㱾㿍䁗䃈䇒䏗䐩䐴䒓䡷䤤䪱䯰䰺䱄䲸丐个丯乢介价佳個凯凱剀剴勓匃匄吤喈嗰嘅垲塏奒媘尬岕幆庎开忋忦恝恺愷愾慨戤揩摡改斺暟概槩槪湝溉漑炌炏烗煯犗玠琾瓂疥皆盖砎磕礚祄祴稭箇絠腉芥葢蒈蓋蚧蝔衸解豈郂鈣鍇鎎鎧鐦钙铠锎锴開闓闿阣颽魀魪鶛豈',
	'객':'㗆䘔喀塥客揢碦衉',
	'갯':'㖋㖎',
	'갱':'㧶㰢㹴䃘䎴䡖䡠䡰䢚劥坈坑妔更硁硜硻秔稉粳羮羹賡赓銵鍞鏗铿阬更',
	'갹':'㖸㷾䣰勪噱臄谻醵',
	'거':'㝒㞐㠪㣄㨿㩀㪯㫢㭕㯫㰦䅕䆽䒧䛯䝣䝻䟊䢹䱟䵕䶙举伡佉佢俥倨凥勮匷厺去呿啹壉姖婮居岠崌巨弆怇懅拒拠挙据據擧攑昛柜椐榉櫸欅歫洰涺淭渠澽炬琚璖璩磲祛秬筥簴籧粔紶翗耟胠腒舉艍苣莒菃蕖蘧虡蚷蜛螶蟝衐袪裾襷詎詓讵豦距踞躆車遽醵鉅鋸鐻钜键锯阹駏鮔鱋鶋麮鼁車﨔',
	'걱':'巪',
	'건':'㓺㔓㗔㨜㨴㩃㩮㩷㸫䇂䇟䊕䖍䘜䙭䞿䭈䮿乹乾亁件健囝墘寈寋巾建弿徤愆揵搴攐攓旔楗榩毽湕漧瀽犍睷腱荐藆虔褰諐謇踺蹇鍵鑳鞬騝騫骞鰎鰬鶱',
	'걸':'㐦㘶㹇䎢䒗乞乬偈傑嵥搩朅杰桀榤櫭渇渴滐竭芞藒',
	'검':'㧄䇜䈩䩎仱俭倹儉剑剣剱劍劎劒劔忴捡撿柑检検檢歛泔淦澉睑瞼矙脸臉芡轗酣鈐钤鹻黔',
	'겁':'㤼㥘㭲㹤㾀䀷䂲䂶刦刧刼劫怯抾昅极砝蜐衱袷跲迲鉣魥鵖',
	'것':'唟',
	'게':'偈卟垍愒憇憩掲揭碣',
	'격':'㐿㦘㦴㪾䁶䂆䈪䐙䙐䛿䞦䠐䴗击呄嗝垎墼愅挌搹搿撃擊敋格楁檄欫毄湨滆激燩犑狊獥礊綌緙繳绤缂缴膈臵薂蛒覡觋觡諽譤轚郹鄓閴闃阒隔鞷骼鬲鴃鵙鶪鸄鼳',
	'견':'㑠㝁㢾㭴㯞㯠㹂䄯䅌䅐䋌䋗䌑䌸䑷䗗䚈䚊䡓䣺䪈䭤䳌䵖䵛䵡䵤䶬健儙坚堅岍幵悓挸掔掮撁枤枧梘樫汧汱涀熞牵牽犬犭狷猏獧瓹甄甽畎睊笕筧絸絹縳縴繭繾绢缱罥羂肩茾菺蚈蜸蠒蠲裐襺見见詃譴谴豜豣趼遣鄄鈃銒鋻鏲鑓钘雃鰹鲣鳽鵑鵳鹃麉',
	'결':'㓗㓶㛃㭈㮮㹟㼤䀗䊽䍳䏐䝌䤿䥛䦬䦼僪决刔妜抉拮挗決洯潔炔焆玦砄結结缺缼芵蒛蚗蛪袺觖觼訣诀赽趹迼逫釨鈌鐑闋阕駃魝鴂',
	'겸':'㻩䈤䈴䊴䭠䯡傔兼嗛岒嵰慊拑槏歉箝縑缣羬膁蒹謙谦趝鉗鎌钳鰜鳒鶼鹣黚鼸',
	'겹':'䀫䁍䛟䩡侠俠唊圶掐殎裌郏郟鵊',
	'경':'㒌㓏㜔㢣㤯㩩㪅㬌㯋㯳㷀㷡㷫㹩㹵㹹㼇㾘䃄䋁䌄䌹䔔䔛䜘䪫䮐䯧䲔䵞京亰俓倞倾傹傾儆儝冂冋冏刭剄剠劲勁勍卿哽囧坕坙坰埂埛境婛峺巠幜庆庚庼廎弪弳径徑惸慶憬憼扃挭挳掶摼擎擏敬景暻曔更桱梗棾椩樈橩檠檾櫦殌氢氫泾浭涇滰漀澃炅烃烱烴焭焿煚煛煢熲燛燝牼狅猄獍琼璚璟璥瓊畊痉痙睘瞏硬磬竞竟競竸絅経綆經綗经绠罄耕耿胫脛苘茎茕莄莖菮葝藑蘏蟼褧誙誩謦警赹踁軽輕轻迳逕郠鍄鏡鑋镜鞕頃頚頸顈顷颈颎駉駫驚骾鯁鯨鲠鲸鵛鶁鶊鹒麖麠黥',
	'계':'㑧㒅㕃㖑㛷㡭㪈㬖㮷㲅㳦㳵㶉㻑㾵䀘䁈䁉䋜䋯䏿䙆䚉䛺䠏䡔䦇䫔䭫䭬䳶乩係卟启呇唘啓啔啟喺嗘堦堺契季屆届峜嵠彐彑悈悸戒挈昋晵暩枅栔桂械棨楐檕檵洎溪瀱烓甈界畍痵瘈瘛癸碶磎禊稽笄筀筓系紒継綮縘繋繫繼继罊罽葜葪蓕蓟薊蘮蘻蟿計誡諬计诫谿銈鍥鎅鑙锲闙阶階雞髻鯚鳮鶏鷄鸂鸡齘',
	'고':'㑬㓬㕝㗝㘼㚉㚖㛈㟸㣨㤒㧽㪣㰏㱠㴌㸆㼋㼥㽽㾸㿁䀇䀦䆁䇢䉉䉐䍛䎋䐻䑩䓘䓢䔌䔯䚌䜂䣗䧸䫧䭅䯌䯨䯪䯻估侤僱凅刳勂叝古叩吿告呱咎咕哌嚳固圐堌塙夃姑婟嫴孤尻崓崮嵪库庫怘拷挎搞攷故敲暠杲枯柧栲桍棝楛槀槁槔槹橭橰檺櫜沽泒洘滜烤焸煰燺牯狜痼瘔皋皐皷盬睾瞽祮祰祻禞秙稁稒稾稿笟筶箍箛篐篙糕絝绔罛罟羔羖羙翱翶翺考股胍胯脵膏臌臯苦苽菇菒菰薣薧藁藳蛄蛊蛌蠱袴裤褲觚詁誥诂诰賈跍軱軲轱辜郀郜酤鈲鈷銬鋯錮钴铐锆锢雇靠韟顧顾餻骷高髙髚髛鮕鮳鯌鯝鲓鲴鴣鷎鷱鸪鼓鼔鼛賈',
	'곡':'㖆㪶㮂㻃䀰䈸䎥䐨䒼䚛䢗䧊䧼䳔䵈䶜俈匤吿告哭唂唃喾嘝嚳斛曲梏榖槲毂浀濲瀔瀫焀焅牿玨珏瑴硞硲穀筁粬糓縠蔛蛐螜觳谷轂逧髷鵠鹄﨏',
	'곤':'㒭㙥㡓㨰㫻㬷㱎䃂䎾䖵䙛䜇䠅䵪丨困坤堃堒壸壼尡崐崑悃惃捁捆昆晜梱棍棞涃混滚滾潉焑熴猑琨瑻璭睏睔睴硱磙祵稇綑緄绲臗菎蓘蔉蜫衮袞裈裍裩褌謴輥辊醌錕锟閫閸阃騉髠髡髨鮌鯀鯤鲧鲲鵾鶤鹍齫',
	'골':'㐔㐣㒴㾶䮩䯇傦圣尳愲抇搰杚榾汨汩滑矻縎蓇顝餶馉骨鶻鹘滑',
	'곱':'䯩',
	'곳':'㖛㖜廤蒊',
	'공':'㒶㓋㓚㓛㕬㣉㤟㤨㧬㧭㫒㭟㮪㯯㲁㳟㸜㺬㼦䂬䂵䅃䅝䇨䊄䔈䜤䡗䢼䣏䰸䱋䲲䳍供倥公共功卭埪塨孔崆工巩幊廾恐恭悾愩慐拱拲控攻栱桏槓涳灨熕珙疘硿碽空笻筇箜篢糼糿紅羾舼蒆蚣蛩蛬貢贛贡赣跫躻輁邛釭銎鞏鞚髸鵼龏龔龚',
	'곶':'串廤串',
	'과':'㐄㗻㚌㛻㡁㧓㪙㳀㳡㶽㸯㼫㽿㾧㿆䆼䈑䈖䌀䙨䠸䣬䫚䯄䯞䴹侉冎剐剮咵坬垮埚堁堝夥夸姱媧寡嵙恗惈戈挝撾敤晇果棵檛歄淉濄煱犐猓瓜瘑科稞窠簻粿綶胯腂膼舿荂菓萪薖蜾蝌裹誇課諣课跨踝踻輠过過鈛銙錁鍋鐹锅锞顆颗餜馃騍骒骻髁',
	'곽':'㗥㸌䣤䦆䧐墎崞廓椁槨欔漷瀖癨籗藿躩郭钁霍鞟鞹',
	'관':'㮡㯘䏓䕀䗆䗰䘾䙮䝺䤽䥗䦎䩪䪀䲌䲘丱串倌冠卝官宽寛寬悹悺惯慣掼摜棺樌欟欵款歀毌泴涫潅灌烪爟琯瓘痯瘝盥矔礶祼窤窽窾筦管綰綸绾罆罐舘莞菅蒄覌観觀观貫賗贯躀輨遦錧鏆鑧鑵関闗關雚顴颧館馆髋髖鱹鳤鸛鹳館',
	'괄':'䒷䟯䣶䦚䯏䯺佸刮劀恝懖括栝桰檜活筈聒葀适銽頢颳髺鬠鴰鸹',
	'광':'㤮㫕㫛㹰㼅㾠㿠䇊䊯䒰䖱䯑侊俇僙儣光劻匡匩哐圹垙壙姯広廣恇懬懭抂拡撗擴旷昿曠桄框洭洸灮炗炚炛烡爌犷狂獷珖眶矌矿砿硄磺礦穬筐筺絋絖纊纩胱臦臩茪誆誑诓诳軖軭輄迋逛邝邼鄺鉱銧鋛鑛鵟黆黋',
	'괘':'㖞卦叏叧呙咼啩喎挂掛枴柺絓罣罫褂詿诖',
	'괴':'㔞㕟㘨㙕㚍㧔㻁㾩䂯䂷䃶䈐䈛䓒䓙䙌䯣䯤乖会傀儈凷劊喟嘳块塊墤壊壞媿巜廥怪恠愧拐旝晆會槐櫆欳烠瑰璝瓌癐箉糩膭蒉蒯蕢蘾襘謉魁',
	'괵':'㶁䂸䬎剨啯嘓帼幗慖掴摑漍聝腘膕虢蝈蟈馘',
	'굉':'㚚䆖䡌䡏䧀䩑䵃卝厷咣宏汯浤渹硡竤紘綋纮翃翝耾肱觥觵訇軣轟轰錓鍠鍧锽閎闳鞃',
	'교':'㚁㚣㚽㝯㠐㢗㤍㤭㬵㰾㳢㶀㺒㽱㽲䀉䀊䂪䂭䃝䍊䎗䘨䚩䡈䢒䢪䥞䮦䱁䲾䴔丂乔交佼侨僑儌咬啋啮喬嘂嘄嘐嘦嘺噛噭嚙墽姣娇嬌嬓孂屩屫峤峧嵺嶠巧恔憍招挍挢搅撟撹撽攪敎教敫敲敽敿晈暞曒校桥榷槗橋滘漖灚烄燆犞狡獟珓璬皎皦矫矯硗硚磽礄礉穚窌窖簥糾絞繑纐绞翘翹膠臫茭荍荞蕎虠蛟蟂蟜覚覺譑譥賋趫趬跤跷踍蹺蹻躈較轇轎轿较邬郊郻鄡鄥鉸鐈铰鞒鞽頝餃饺驕骄骹髜鮫鱎鲛鴵鵁鷍鷮齩',
	'구':'㐀㐜㐤㓂㔚㕤㖵㗕㘗㘳㙀㚱㛏㜹㝌㝤㞗㟈㡚㡱㣘㤹㧨㨌㪺㬬㭝㰶㲃㲄㲘㳋㳰㶢㸨㺃㺫㺵㻤㽛䀠䂂䃓䄔䅓䆒䈮䉩䊆䊵䋧䐟䑦䓻䙔䛮䜪䝭䞤䟬䟵䡂䣇䤛䥲䦰䧢䧱䧶䪷䬨䬲䮃䰗䲥䲫䳎䳹䳼䵶䶚丘丠丩久乆九亀仇伛佉佝俅俱倃倶傴具冓冦剾劬劶勼勾匓匛匶区區厩厹口句叴呕呴咎嘔坵坸垢埧够夠夻奺妪姤媾嫗宼寇寠屦屨岖岣岴嶇巯巰廄廏廐彀彄忂怐惧愳慦懼戵扏扣抅抠拒拘捄搆搝摳撀敂救敺斪旧昫朐朹杦构枸柩柾桕梂椇榘構欋欍欧欨歐殏殴毆毬氍求汣沟沤泃浗溝滱漚灈灸煹熰爠牞犋犰狗玖玽球璆瓯甌畂疚痀癯皳盚眍眗瞉瞘瞿矩穀究窛窭窶竘竬笱筘篝簆簼粂糗紌絇絿緱缑翑耇耈耉聥肍胊脙膒臞臼舅舊舏艽芶苟茩萛葋蒟蓲蔲蔻蘒蚯蚼蛷蝺蠷蠼衢袧裘褠覯觏觓觩訄訅訽詬謳讴诟豿賕購购赇跔躣躯軀軥逑遘邭邱釓釚釦鈎鉤銶鑺钆钩镹阄雊鞫鞲韝韭韮韯颶飓駆駈駒驅驱驹鬮鮈鯄鯦鰸鳩鴎鴝鷇鷗鸜鸠鸥鸲麔鼩鼽齨龜龟',
	'국':'㘲㥌㩴㹼㽤䆐䋰䎤䏱䕮䗇䜯䡞䪕䱡侷匊囗囯囶囻国圀國婅局巈挶掬梮椈檋毩毱泦淗焗粷菊蘜諊趜跼踘躹輂鋦锔閰陱鞠鞫駶驧鵴麯麴麹',
	'군':'㖥㪊㴫㿏䝍䭽侰僒军君宭帬捃攈攟桾涒珺皲皸皹窘羣群莙蜠裙裠軍輑郡鍕頵鮶鲪鵘麇',
	'굴':'㐇㐝㩿㪂㭾㵠㻕䂗䓛䖦䘿䞷䠇倔厥堀屈崛崫弡掘朏淈煀窟胐虳袦詘誳诎趉镼鶌',
	'굿':'㖌',
	'궁':'㑋㴦䓖䛪䠻䤝匑匔宆宫宮弓杛焪熍穷穹窮竆芎藭躬躳',
	'권':'㒽㟡㢧㩲㪻㬺䄅䄐䅚䊎䌯䑏䖭䟒䠰倦券劝劵勌勧勬勸卷啳圈圏埢奆婘孉巏巻帣惓慻拳捲搼权桊棬椦権權淃牶犈眷睠箞絭綣绻菤蔨虇蜷蠸裷觠踡錈锩韏飬餋鬈鬳齤',
	'궐':'㙭㵐䙠亅厥噘孒孓嶡嶥憠掘橛橜欮氒灍獗瘚蕨蟨蟩蹶蹷鐝镢闕阙鱖鳜鷢',
	'궤':'㔲㔳㙺㞦㧪㱮䃽䅪䍯䕚䠩䡄䣀䣒䤥佹儿几凧劂匦匭匮匱厬圚垝姽嬇帰恑愦憒撅攱机樻櫃歸殨氿溃潰祪篑簂簋簣籄繢缋蔮蛫觤詭诡跪蹶軌轨鐀鑎闠阓陒鞼餽饋馈鱖鱥麂',
	'귀':'㱕㸵䁛䌆䙡䝿䞈䢜䰎亀刿劌勾句嘳宄尯帰归撌晷椢槶櫷歸皈瞆瞶聭腃蘬貴贵騩鬼龜句龜',
	'규':'㙓㧃㨒䂓䅅䆻䖯䙵䞨䟸䠑䤆䯓䲅䳏䳫䶯九乣刲叫呌喹圭奎妫媯嫢嬀岿巋恘恷戣揆摎摫暌朻椝楏楑槻槼樛沩湀溈潙煃犪玌珪睽瞡硅窍窐窥窺竅糺糾紤纠聧胿芁芤茥葵藈虬虯蝰袿規规訆赳跬蹞逵邽郌鄈鍨鍷閨闚闺頃頄頍頯馗鬶鬹黊鼼',
	'균':'㚬㟒䇹䐃亀勻匀呁囷均峮抣汮畇碅稛筠箘箟菌蚐袀覠鈞銁銞钧麇麏麕龜龜',
	'귤':'䤎䰬橘蹫',
	'극':'㘌㞃㥛㦸㳳㻷䓧䧍䩯䪂丮亟克剋剧劇勀勊可娔尅屐戟撠棘極橶殛氪茍蕀裓襋郄郤鋴隙隟革',
	'근':'㘦㝻㞬㢙㧆㨷㮗㹏䈥䈽䌍䒺䤺伒僅劤勤卺厪哏堇墐嫤巹廑慬懃懄斤斳根槿歏殣漌瑾瘽矜筋芹荕菦菫蓳螼覲觐觔謹谨赾跟近釿靳饉馑馸',
	'글':'㐎㔕䞘䰴契契',
	'금':'㕋㦗㩒㪁㯲㱈㱽㲐㾣䃢䋮䌝䑤䔷䘳䥅䥆䦦䫴䶖今僸凎凚厼唫噙噤坅妗嵚嶔庈惍扲捦搇擒昑檎澿珡琴琹琻砛禁禽笒紟耹肣芩菳蚙蠄衾衿襟赺軡金釒鈙錦鍂鐢钅锦雂靲顉鳹鵭黅黔齽金',
	'급':'㤂㧀㬤㽺䏜䏠䲯伋及喼圾嬆岌彶忣急扱汲皀礏礘笈級給级给芨觙鷑﨤',
	'긍':'㥤㮓䱍䱎䱭䱴亘亙兢刯堩奟恒掯揯搄殑矜矝絚緪縆肎肯肻褃錹鹶',
	'기':'㒫㖉㙋㙨㚡㚻㞆㞓㞛㞯㞿㟓㟚㟢㠌㠱㡬㡮㥍㥓㨳㩻㩽㫅㫓㫷㯦㰟㱦㲹㼄㽶䀈䃆䄎䄫䅲䇫䉻䋟䎛䐀䑴䒻䓅䓫䓽䔇䕤䕫䗁䘛䙫䛗䛴䝸䞚䟇䟚䡋䢋䢎䢳䤒䥓䩓䩭䫏䭶䭼䰇䳢䶞丌乞亓亟企伎俟倚倛僛僟其兾冀刉刏剘剞叽呚呩呮唭嗜嘰噐器圻坖基埼塈墍夔夡奇妀妓娸婍寄居屺岂岐岓崎嵜己帺幾庋庪弃徛忌忮怾惎愭懻技掎掑攰攲敧旂旗旡既旣暣暨曁朞期杞枳桤梞棄棊棋榿槣樭機檱櫀欺歧气気氣汽沂淇渏溰濝炁焏猉玂玑玘琦琪璂璣畸畿盀盵矶碁碕磯示祁祇祈祺禥禨稘稩穊穖竒箕簊簯簱籏粸紀綥綦綨綺纪绮羁羇羈耆耭肌肵臮芑芪芰萁蔇蕲藄蘄蘎蘷虁虮蚑蚔蚚蜝蜞螧蟣衹裿褀覉覊覬觊觭記誋諅諆譏讥记豈起跂跽踑踦躨躸軝邔鄿錡錤鐖锜陭隑鞿頎颀飢饑饥騎騏驥骐骑骥鬐鬾鬿魌魕魢鯕鰭鱀鱾鲯鳍鵋鵸鶀麒黖齮﨑',
	'긴':'紧緊菣',
	'길':'㐞㐟㣟䓀䟌佶吉咭姞拮桔洁狤蛣趌郆銡鞊鮚鲒',
	'김':'金',
	'끋':'印',
	'끗':'㖝',
	'끽':'喫噄',
	'나':'㑚㔮㖠㡅㧱㰙䛔乸傩儺哪嗱奈娜懦懧拏拿挐挪梛橠砈稬穤糥糯蒘誽那郍鎿镎難喇奈懶癩羅蘿螺裸邏',
	'낙':'掿格諾诺樂洛烙珞落酪駱',
	'난':'㫱㬉㬮䎡偄奻戁暖渜煖煗赧难難餪亂卵欄爛蘭鸞',
	'날':'䖓䖧捏捺涅苶陧',
	'남':'㑲㓓㣮㭷㵜㽖䈒䊖侽南喃娚婻揇暔枏柟楠湳煵男畘罱腩莮萳蝻諵遖嵐濫藍襤',
	'납':'㨥䈫䪏內内妠笝納纳蒳衲軜鈉钠靹魶拉臘蠟',
	'낭':'㚂㶞䁸乪儾嚢囊囔娘擃攮曩欜灢饢齉廊朗浪狼郎',
	'내':'㐻㚷㜨㭆㮈㮏㲡㴎㾍䯮䱞䲎乃內内匂奈奶嬭孻廼摨撆柰氖氝渿熋疓耏耐能萘螚褦迺釢錼鼐來',
	'냉':'冷',
	'냑':'蹃逽',
	'녀':'㵖䋈䘫女帤挐袽釹钕',
	'녁':'䭆惄疒',
	'년':'㬗㮟䄭䄵哖姩年撚涊碾秊簐脌躎鵇鼰秊',
	'녈':'㖏㘿䂼囓圼夨涅篞',
	'념':'㑫䧔䬯埝念恬拈捻焾艌踗',
	'녑':'㚔㩶㵊䇣䌰䎎䳖喦帇幉惗捻敜鈢鉩錜',
	'녕':'㝕㣷㲌㲰㿦䆨䔭䗿䭢佞侫儜咛嚀嬣寍寕寗寜寧拧擰橣檸澝濘甯矃聍聹薴鑏鬡鸋',
	'녘':'榒',
	'녜':'䄲昵',
	'노':'㚢㞪㺁㺜䛝䜀䜧伖伮努呶夒奴孥峱巎巙帑弩怒怓猱獿瑙砮笯粩胬臑蛯詉鑥镥駑驽鴑勞擄櫓爐盧老蘆虜路露魯鷺',
	'녹':'傉搙角碌祿綠菉錄鹿',
	'논':'㯎淪論',
	'놀':'㐐㐗',
	'놈':'㖈',
	'농':'㶶䙶䢉䵜侬儂农哝噥嶩檂欁浓濃燶癑禯秾穠竜繷脓膿蕽襛農辳醲鬞齈龐壟弄籠聾',
	'놔':'雫',
	'놜':'豽貀',
	'뇌':'㑎㛴㼏匘垴堖娞恼悩惱憹挼捼碯脑脳腇腦餒馁鮾鯘牢磊賂雷',
	'뇨':'㒟㜵㞙㠡㳮䃩䃵䙚䦊䮍䴃啂嫋嫐嬝嬲尿淖溺硇硵磠脲袅裊褭譊鐃铙閙闹鬧',
	'누':'㜌㝅㝹䅶䨲啂槈檽獳羺耨譨譳鎒鐞壘屢樓淚漏累縷陋',
	'눈':'㜛㡪㶧媆嫩嫰',
	'눌':'㕯䟜吶呐抐肭訥讷',
	'뉴':'㖻㺲䂇䋴䏔妞忸扭杻沑炄狃粈紐纽莥鈕钮靵',
	'뉵':'䖡䘐䚼䶊恧朒衂衄',
	'늑':'䅞䎪勒肋',
	'늠':'凜',
	'능':'㴰䏻䘅能凌稜綾菱陵',
	'늦':'莻',
	'니':'㞾㦐䕥䘦䛏䝚伱你倷呢坭埮妮妳尼屔怩您抳旎柅檷泥濔狔祢禰秜胒腻膩臡苨蚭跜迡鈮鉨鑈铌隬馜',
	'닉':'㥾㲻匿嫟嬺愵搦搻氼溺糑',
	'닐':'䁥䘌䵑䵒昵暱痆',
	'님':'䋻䌾拰',
	'닙':'㘝囡',
	'다':'䫂䯬嗲多夛爹茤茶觰跢鯺',
	'단':'㟨㠆㡺㣋㣶㩛㫁㫜㱭䃪䉡䊜䐷䒟䕊䜝䜥䝎䞡䠪䢷䦔䩥䵎丹亶但偳刐剬剸勯匰单単唌單团団團坍坛塅壇媏彖慱抟担摶断斷旦枬柦椴槫檀檲段毈泹湍湪漙潬澾煅煓猯玬瑖璮疍瘅癉短砃碫端箪簖簞籪糰緞緣縁繵缎耑胆腶葮蛋蜑袇袒褍褖褝襌襢觛貒貚踹躖郸鄲鉭鍛鍴鏄钽锻駳驙鴠鶨鷒鷤鷻',
	'달':'㒓㣵㳠㺚㼀㿹䃮䵣呾哒噠垯墶妲怛挞撻橽澾炟燵狚獺疸笪繨羍荙薘蟽詚跶躂逹達鐽闥闼靼鞑韃',
	'담':'㕪㗖㘱㚮㜤㲜㲭㲷㳩㴂㻼㽎㽑䃫䆦䆱䉞䊤䐺䑙䔜䗊䜖䨢䨵䭛倓偡儋啖啗啿嘾噇噉嚪坍埿墰墵壜妉姏婒媅帎惔憛憺擔曇曋橝毯氮淡湛潭澸澹瓭甔痰癚禫窞紞緂罈罎耼聃聸腅膽舑舕荨菼萏蕁薝藫蟫衴覃談譚谈谭贉郯醈醰錟锬霮顃餤饏馾驔髧黕黮黵',
	'답':'㙮㜓㟷㧺㭼㯚㳫㾑㿯㿴䂿䈋䌋䍇䍝䎓䐛䓠䜚䠌䪚䳴䵬䶀䶁剳匒崉榙沓涾溚濌畓畣眔答荅褟褡誻譶踏蹋蹹躢遝鎉龖龘',
	'당':'㑽㓥㙶㜍㜭㭻㲥㼕㼺㽆㿩䃥䅯䉎䌅䕋䚒䣊䣘䣣䧜䭚倘傏傥儅儻党凼劏唐啺嘡噇噹坣垱堂塘壋嵣幢当憆戃戅戆戇挡搪摚撞擋攩曭档棠榶檔欓氹溏漟澢灙煻爣珰瑭璫瓽當瞊瞠矘磄礑禟筜篖簹糃糖糛耥膅膛艡蓎螗螳蟷裆襠譡讜谠赯蹚躺鄌醣鎕鎲鏜鐺钂铛镋镗闛闣隚鞺餳餹饄饧鶶黨鼞',
	'대':'㐲㒗㓫㘆㙜㙵㚎㛿㝳㞭㠚㣕㦠㬃㬣㭖㯂㳔㷘㸀㻖䃍䈆䑓䒫䙊䚞䚟䨴䯟䲦亣代儓坮垈大嬯对対對岱帒带帯帶廗待怼憝憞懛懟戴擡旲枱柋檯歹汏濧瀩瀻玳瑇甙碓祋簤籉臺艜薱薹袋襨襶譈譵貸贷蹛軑軚轛轪錞鐓鐜镦队隊鮘黛黱',
	'댁':'宅',
	'덕':'㤫㥁徳德恴悳惪',
	'도':'㞵㠀㢭㧅㨶㫞㬸㭸㴞㷹㸓㹗㻌㻬㻯䀞䀾䂽䄻䅷䆃䈱䊭䌦䑬䑲䖘䛬䞮䟻䣄䣝䤾䩣䩲䬞䬢䬭䮻䳜䵚倒凃刀刂到匋叨咷唋啕喥嘟噵図图圖圗堵塗壔夲嫍导導屠屶岛島峹嵞嶀嶋嶌嶹帾幍度庩廜弢徒忉悼慆挑捈捣捯掉掏搗搯擣旫暏朷桃梌梼棹椡槄槅槝檤檮櫂氘洮涂涛淘渡滔潳濤焘熖燾琽瑫瓙瘏盗盜睹祷祹禂禱稌稲稻筡綢綯縚纛绹翿舠艔荼菟菿萄蒤蓞虭蜪衜衟裪覩詜謟賭赌跳跿蹈軇迯逃途道都酴醄醏釖鋾鍍镀闍阇陦陶隝隯靯鞀鞉鞱韜韬飸饀饕馟駼騊魛鱽鳭鵌鷋鷵鼗都﨩',
	'독':'㒔㞘㱩㸿㾄䄣䈞䐁䓯䛢䢱䫳䮷凟匵嬻椟櫝殰毒涋涜渎瀆牍牘犊犢独獨瓄痜皾督碡禿秃竺笃篤纛蝳裻読讀讟读豄贕鋵錖鑟韇韣韥騳鵚黩黷',
	'돈':'㢯㥫㩐㪟㬿㹠㻻䃦䔻䪃䵊䵍伅囤墩墪崸庉弴忳惇扥扽撉撴敦旽暾朜橔沌潡炖焞燉犜獤盾砘礅豘豚趸蹾躉軘逇遁韕頓顿飩饨驐魨鲀黗',
	'돌':'㐑㟮㷝㻠䃐䠈乭凸咄嚉堗怢揬柮湥突腯葖迌鈯鍎飿饳鶟鼵',
	'돗':'㘏',
	'동':'㑈㓊㖦㗢㚵㠉㠽㢥㣠㤏㨂㫡㯵㲇㷲㸗㼧㼯㼿䂈䂢䆚䍶䞒䮵䰤䱰䳉䳋䴀䵔䶱东仝侗倲偅働僮冬冻凍动動勭同咚哃垌埬墥姛娻嬞岽峂峒峝崠崬庝彤憧懂戙挏昸晍曈朣東栋桐棟橦氃氡氭洞浵涷湩潼炵烔燑犝狪獞疼眮瞳砼硐秱穜童笗箽粡絧罿胨胴腖膧艟苳茼菄董蕫蘔蚒蝀衕詷諌赨迵酮鉖鉵銅錬铜霘餇駧鮗鮦鯟鲖鶇鸫鼕',
	'두':'㓱㛒㞳㟕㢄㨮㪷㰯㺶㿡䄈䇆䇺䕆䕱䚵䢏䬦䱏䲧䵉亠侸兜兠剅吺唗唞土头抖斁斗杜枓梪橷殬毭浢痘窦竇篼紏肚脰荰荳蔸蚪螙蠧蠹読讀豆逗郖酘鈄鋀钭閗阧陡頭餖饾鬥讀﨣',
	'둑':'㪲',
	'둔':'㩔㼊䜳䤜吨坉屯窀臀臋芚踲迍遁遯鈍钝霕頓',
	'둘':'㐈㐙乧',
	'둣':'㖍',
	'둥':'㪳',
	'득':'㝶䙷䙸嘚得棏淂鍀锝',
	'등':'㔁㲪㽅䒅䒭䓁䔲䕨䗳䙞䠬䠮䮴䲍䲢䳾僜儯凳噔墱嬁嶝幐戥朩橙櫈滕漛灯燈璒登磴竳等簦籐籘縢腾膯艠藤虅螣覴誊謄豋蹬邆邓鄧鐙镫隥霯駦騰驣鰧鼟',
	'똥':'㖯㖰',
	'뜰':'㐢',
	'라':'㑩㒩㞅㦬㩡㰁㱻㼈㽋㿚䇔䉓䊨䌱䌴䯁亽倮儸剆啰喇嗠嚹囉囖懒懶拏摞攞攭旯曪椤欏灕猡玀瘰癞癩砢箩籮纙罖罗羅脶腡臝萝蓏蘿螺蠃裸覙覶覼躶逻邏鎯鏍鑼锣镙陏饠騾驘骡鸁拏',
	'락':'㓢㦡䀩䈷䎊嗠峈樂泺洛濼烙犖珞硌笿絡络荦落諾酪鉻铬雒餎饹駱骆鮥鴼樂諾',
	'란':'㘓㡩㦨㱍㱫㳕䃹䑌䖂䦨䪍乱亂亪兰卵囒圝圞嬾孄孏幱懶拦攔斓斕曫栏栾欄欒欗滦澜瀾灓灡灤烂燗爛爤瓓癵籣糷羉膥蘭虊襕襴襽譋讕谰躝釠銮鑭鑾钄镧闌阑韊鵉鸞鸾丹',
	'랄':'㸊㻋㻝䀳䏀䓥䓶䱫䶛剌喇垃埒埓捋揦揧攋楋獭瓎瘌蝲辢辣頱鬎鯻',
	'람':'㑣㘕㛦㜮㞩㧛㨫㩜㰓㰖㲯䆾䌫䍀䨬䰐儖啉嚂囕壈婪岚嵐惏懢揽擥攬榄欖浨滥漤濫灆灠燣燷爁爦璼礷篮籃繿纜缆葻蓝藍蘫褴襤覧覽览顲',
	'랍':'㕇㡴䂰䃳䇱䗶啦拉搚柆爉磖翋臈臘菈蝋蠟邋鑞镴鞡',
	'랑':'㓪㙟㟍㢃㫰㮾㱢㾿䆡䍚䕞䡙䯖䱶勆啷埌塱嫏崀廊朖朗朤桹榔樃欴浪烺狼琅瑯硠稂筤艆莨蒗蓈蓢蜋螂誏躴郎郒郞鋃锒閬阆駺',
	'래':'㚓㴺㾢䂾䅘䋱䚅䧒來俫倈儽勑唻婡崃崍庲徕徠来梾棶涞淶猍琜睐睞箂莱萊逨郲錸铼騋鯠鵣鶆麳黧',
	'랭':'冷唥',
	'략':'㑼㗉㨼䂮䌎䛚剠圙掠撂洜略畧',
	'량':'㒳㔀㔝㝗㹁㾗䀶䁁䓣䝶䠃䣼䩫䭪両两亮俍俩倆兩凉剠哴唡啢喨墚悢惊掚掠斏晾梁椋樑涼湸煷簗粮粱糧綡緉羪脼良蜽裲諒谅踉輌輛輬辆辌量魉魎',
	'레':'螺',
	'려':'㑦㒧㓯㛎㠟㠠㭚㰀㱺㴝㾐㾔㿛䉫䊪䓞䔣䔧䕡䕻䗍䘈䣓䥨䥿䮉䰕䴡丽侣侶俪儢儷刕励勴勵厉厲吕呂唳囇婯巁庐廬廲悷慮戻戾挔捛攊攦旅曞曥栛梠棙榈櫖櫚欐沴沵滤濾焒爈珕瓈疠癘盭矋砺礪祣禲稆穞穭粝糲絽綟胪膂膐臚茘荔藘藜蛎蛠蜧蟸蠇蠡蠣邌郘鋁鏫鑗鑢铝閭闾馿騹驢驪驴骊鱱鱺鲡鵹麗黎黧',
	'력':'㔏㠣㧰㬏㯤㱹㷴㺡㻺㽁㿨䃯䍥䍽䔉䟏䟐䤙䥶䮥䰛䰜儮力历厤厯叻呖嚦坜壢屴擽攊暦曆朸枥栎檪櫟櫪歴歷沥瀝爏瓅瓑疬癧皪砳砾磿礫礰秝苈蒚藶蚸蝷觻讈赲跞躒轢轣轹郦酈鎘镉雳靂靋韷鱳鳨',
	'련':'㜃㜕㜻㝈㟀㥕㦁㪝㰈㶌㺦㼑䃛䏈䜌僆嗹噒堜奱娈媡嫾孌徚怜恋慩憐戀挒挛摙撵攆攣梿楝槤櫣涟湅漣炼煉琏瑓璉癴練縺纞练翴联聨聫聮聯脔膦臠莲萰蓮裢褳謰蹥輦辇连連鄻錬鍊鏈链零鰊鰱鲢零',
	'렬':'㤠㬯㭞㭩㸹㽟䅀䟹䮋䴕冽列劣劽咧哷姴戻戾挒挘捩栵洌浖烈烮煭爄睙脟茢蛚蛶裂趔迣迾鋝鋢锊颲鮤鴷',
	'렴':'㝺㡘㢘㪘㯬㱨㶑㼓䁠䆂䌞䙺䥥䭑亷劆匲匳奁奩嬚帘廉搛敛斂殮溓潋澰濂濓瀲熑燫磏稴簾籢籨羷臁莶蔹薕薟蘝蘞螊蠊覝鐮镰鬑',
	'렵':'㯿㲱㼃㼲䁽䉭䜲䝓䪉儠巤擸犣猟獵聗躐鬣鱲',
	'령':'㚑㡵㦭㩕㪮㬡㯪㱓㲆㸳㻏㾉䄥䉁䉖䉹䌢䍅䕘䖅䙥䠲䡼䡿䨩䯍䰱䴇䴒䴫令伶刢另呤呬囹坽姈孁寧岭岺嶺彾怜拎昤朎柃棂櫺欞泠澪灵炩燯爧狑玲瓴皊砱秢竛笭紷羚翎聆舲苓蕶蘦蛉衑袊詅跉軨逞酃醽鈴铃閝阾零霊霗霛霝靈領领駖魿鴒鸰鹷麢齡齢龄龗寧',
	'례':'㘑㡂㤡㽝䅄䵩例劙櫔欚澧濿犡瓥砅礼禮豊醴隷隸鱧鳢礼',
	'로':'㔧㔪㗦㟉㢚㢳㧯㨓㪭㭔㯝㯭㳣㿖䃕䇭䜎䜮䝁䡎䲏䲐䳓䵏僗劳労勞卢卤咾哰唠嘮噜嚕嚧垆塷壚嫪崂嶗怒恅憥憦捞掳撈撸擄擼攎朥栌栳樐橯橹櫓櫨氇氌泸浶涝滷潞澇澛瀂瀘炉爐牢狫獹玈珯璐瓐痨癆盧矑硓磱窂簩簬簵籚纑罏老耂耢耮舻艣艪艫蓾蕗蘆虂虏虜蟧蠦賂路軂輅轤轳辂銠鏀鏴鐒鐪鑪铑铹露顱颅髗髝魯魲鮱鱸鲁鲈鷺鸕鸬鹭鹵黸怒',
	'록':'㖨㜙㟤㦇㪖㫽㯟㲶㼾䃙䌒䍡䎑䎼䐂䘵䚄䟿䩮䱚䴪圥塶娽廘彔录摝梺椂樚氯淥渌漉熝琭甪盝睩碌祿禄箓簏簶籙粶綠緑绿膔菉蔍螰觮趢蹗轆辘逯醁錄録錴騄騼鵦鹿麓龣',
	'론':'㤻婨惀溣碖菕論论',
	'롱':'㑝㙙㛞㟖㢅㰍㳥㺯䆍䏊䡁䪊儱厐咙哢嚨垄垅壟壠巃巄弄拢挊挵攂攏昽曨朧栊梇槞櫳泷滝瀧珑瓏砻硦礱礲竉笼篭籠聋聾胧茏蘢蠪裃襱豅鏧鑨陇隴靇鸗龍龎龓',
	'뢰':'㑍㒦㔣㠥㲕㵢㵽㼍㿔䄤䉪䍣䐯䒹䛶䠭䢮䣂䨓䮑䲚傫儡壨擂攂檑櫑櫴洡濑瀨瀬牢珱瓃畾癗磊磥礌礧礨筙籁籟纇罍耒蕾藾蠝襰誄讄诔賂賚賴赂赉赖轠酹銇錑鐳鑘鑸镭雷靁頛頪頼顂颣鱩',
	'료':'㙩㝋㞠㟹㡻㵳㶫䄦䉼䎆䑠䒿䕩䜍䝤䢧䨅䩍䭜了佬僚叾嘹嫽寥寮尞尥尦屪嶚嶛廖廫憀憭撩敹料暸曢橑潦炓熮燎爎爒爳獠璙疗療瞭窲窷竂簝繚缭翏聊膋膫蓼藔蟉蟟豂賿蹘蹽轑辽遼鄝醪鐐镣镽顟飂飉髎鬧鷯鹩',
	'룡':'㡣徿瀧爖瓏眬矓竜蠬贚躘驡龍龒龙',
	'루':'㒍㔷㙼㜢㟺㡞㥪㪹㲎㴃㶟㹎㺏㻲䁖䄛䅹䉂䝏䣚䫫䮫䱾䴎偻僂厽喽嘍垒塁塿壘娄婁嫘屚屡屢嵝嶁廔慺搂摟楼樓櫐氀泪涙淚溇漊漏熡甊瘘瘺瘻癳瞜篓簍累縷缕耧耬膢艛蒌蔞蝼螻褛褸謱貗軁遱鏤镂陋鞻髅髏鷜鼺',
	'뤼':'厽',
	'류':'㐬㙧㧕㳅㶯㽌㽞㾋䄂䉧䖻䗜䚧䝀䣦䬟䰘䱖䶉刘劉嚠塯媹嬼嵧廇懰旈旒柳栁桺榴樏橊橮欙流浏溜漻澑瀏灅熘珋琉瑠瑬璢畄留畱疁瘤癅硫磂禷类絫綹縲纍纝绺缧罶羀艈蒥蓅蔂蕌藟藰蘱蘲蘽虆裗謬谬蹓遛鉚鋶鎏鎦鏐鐂铆锍镏镠雡霤類飀飅飗飹餾馏駠駵騮驑骝鬸鰡鶹鷚鸓鹨麍',
	'륙':'㓐㛬䡜僇六剹勎勠坴戮淕磟稑穋踛陆陸鯥鵱',
	'륜':'㓆㖮㷍䈁䑳仑伦侖倫嗧囵圇埨崘崙抡掄棆沦淪潤磮稐綸纶耣腀蜦踚輪轮錀閏陯鯩',
	'률':'㖀㗚㟳㪐㮚䔁䔞䡃䬆侓傈凓垏塛寽峍嵂律徍慄搮栗溧率瑮硉箻篥繂膟葎鷅麜率',
	'륭':'㚅㝫㦕䃧䥢嶐湰烿癃窿蕯隆霳',
	'륵':'仂勒嘞忇扐椚氻泐玏竻簕肋艻阞鰳鳓',
	'를':'㔹',
	'름':'㐭㨆䕲凛凜廩廪懍懔檁檩澟癛癝菻',
	'릉':'㖫㘄㥄㱥䈊䉄䔖䧙䬋䮚倰凌堎夌婈崚庱愣掕棱楞淩琌睖碐祾稜綾绫菱蓤蔆薐裬踜輘錂陵鯪鲮',
	'리':'㒿㛤㤦㥎㦒㰚㲠㷰㸚㹈㻳㼖㾖䄜䅻䇐䊍䋥䍠䍦䔆䖽䖿䙰䚕䣫䤚䦄䧉䬜䱘䴻䵓俐俚俬兣刕利剓剺劙厘吏哩唎喱嚟囄娌娳嫠孋孷履峛峢峲彨彲悝悡悧摛攡李梨梩梸棃樆氂浬浰涖漓犁犂犛狸猁理琍璃瓼甅痢盠睝瞝矖离穲竰筣篱籬粚粴糎縭繌纚缡罹羸脷艃荲莅莉菞蒞蓠蔾蘺蜊螭蟍蠫裏裡褵詈謧貍逦邐醨里釐鋫鋰錅锂離鬁魑鯉鯏鯬鱺鲤鸝鹂麗麶黐黧異',
	'린':'㔂㖁㷠䉮䗲䚏䚬䢯䫰䮼䱯亃僯厸吝壣嶙恡悋撛斴暽橉潾焛燐獜璘甐疄瞵磷粦粼繗翷蔺藺蹸躏躙躪轔轥辚遴邻鄰鏻閵隣驎鱗鳞麐麟',
	'림':'㝝㣩㵉䫐冧崊晽林棽淋瀮瀶琳痳碄箖臨醂霖',
	'립':'㕸䇉䢂䲞䶘岦湁砬立笠粒苙鉝雴鴗',
	'마':'㐃㐷㦄㾺䃺䔍䗫䘞䜆䣕䣖䧞䩋䭩䯢䲈䳸亇亍傌劘吀吗哶唛嗎嘛嘜嚒嚤嚰妈媽嫲嬤嬷尛懡戂摩擵杩榪溤犘犸獁玛瑪痲码碼磨礳祃禡耱蔴藦蘑蚂螞蟆蟇鎷饝馬马髍鬕魔鰢鷌麻麼麽麿',
	'막':'㠳㦝㱳㷬䒬䮬劰嗼塻寞幕幙暯漠瘼瞐瞙縸膜莫貌邈鄚鏌镆饃馍',
	'만':'㒼㗄㗈㙢㡢㬅㵘㸘㻴㿸䅋䅼䊡䐽䒥䕕䘎䜱䝡䝢䡬䤍䯶䰋万僈卍卐塆墁壪娩嫚屘峦巒幔弯彎慢慲挽摱晚晩曼梚槾樠湾満满滿漫潫澫澷濷灣熳獌睌瞒瞞矕縵缦脕萬蔄蔓蘰蛮螨蟃蟎蠻襔謾谩贎蹒蹣輓鄤鋔鏋鏝镘鞔顢颟饅馒鬗鬘鬛鰻鳗',
	'말':'㑻㨸㭐㶬䍪䏞䬴䯦䱅䴲唜妺帓帕怽抹昩末枺沫瀎皌眜睰砞礣秣粖茉袜袹襪閁靺韈韤魩',
	'맘':'㛧䥑鋄錽鎫',
	'망':'㒺㕵㟌㟐㟿㤀㬒䁳䅒䋄䋞䍏䒎䒽䓼䥈䰣䰶䱩䵨亡亾兦吂壾奀妄娏孟忘忙恾惘望朢杗杧棢汒漭焹牤琞痝盳硥硭笀網纲网罒罓罔芒茫茻莣莽莾菵蘉蛧蝄蟒蠎誷輞辋邙釯鋩铓魍',
	'매':'㙁㜥㦟㭑㵋㺳䀛䀜䁲䆀䊈䍙䔦䚑䜕䜸䤂䨪䰨䰪䵢买佅凂劢勱卖呅呆嘪嚜坆埋塺売妹媒寐抺挴昧枚某梅楳槑毎每沬浼湈煤玫珻痗眛禖罵脄脢腜苺荬莓蕒薶買賣跊迈邁酶鋂霉霾韎駡骂鬽魅鷶黣',
	'맥':'㵹㹮䘑䨫䮮䳮帞百眽眿絈脈脉蓦蛨衇覛貃貉貊貘陌霡霢驀麥麦',
	'맹':'䁅䇇䈍䉚䓝䖟䗈䥰儚勐孟掹擝橗氓猛瓾甍甿盟盲艋莔萌蕄虻蜢蝱鄳錳锰鯭鼆',
	'먀':'乜',
	'멋':'矃',
	'멍':'儚甍甿虻',
	'며':'㢱厼旀',
	'멱':'㯒䈿䌐䖑䣾䮭冖冪塓幂幎幦汨淿漞濗簚糸糹纟羃覓覔觅鼏',
	'면':'㒙㛯㝃㝰㨠㨺㮌㰃㴐䀎䃇䛉䛲䤄䫵䰓丆丏俛偭免冕勉勔喕婂媔嬵宀愐棉檰櫋汅沔湎眄眠瞑矈矊矏糆綿緜緬绵缅腼臱芇莬葂蝒面靣鮸麪麫麵麺',
	'멸':'㒝㓕㩢䁾䈼䌩䘊䡸䩏孭幭懱揻搣櫗滅灭篾蔑薎蠛衊鑖鱴鴓',
	'명':'㓁㗮㝠㟰㫥䄙䆩䊅䏃䒌䫤䳟佲冥凕名命姳嫇慏掵明暝朙椧榠洺溟焽熐猽皿眀眳瞑笽茗蓂螟覭詺鄍酩銘铭鳴鵈鸣',
	'몌':'袂',
	'모':'㑄㒵㒻㖼㘪㛌㝟㟂㡌㧇㧌㪞㴘㹸㺺㿞䋃䖥䗋䡚䫉䭷侔侮兞冃冐冒募哞姆姥娒媢嫫峔帽恈慔慕摸摹旄暮木枆某栂模橅母毛毟毪毮毷氁洠牟牡牦獏玥瑁瓱皃眊眸矛砪秏竓粍糢罞耄耗膜艒芼茅莫萺蓩蛑蝐蝥蟊蟱覒謀謨謩谋谟貌軞酕鉾髦魹鴾鶜麰',
	'목':'㜈㣎㾇䀲䊾䑵䜼䲷䳱冒凩匹坶木杢楘毣沐炑牧狇目睦穆苜莯蚞鉬钼雮霂鶩鹜',
	'몰':'勿圽朰歽歾歿殁沒没莈',
	'몸':'鯍',
	'몽':'㒱㙹㜴㝱㠓㩚㴳䀄䏵䑃䑅䒐䙦䙩䝉䟥䠢䤓䥂䰒䲛䴌䴿䵆冡夢夣幪懜懞懵曚朦梦檬氋溕濛獴甮瞢矇矒礞艨蒙蠓鄸雺霥霿靀饛鸏鹲',
	'묘':'㑤㚹䁧䅦䏚䖢冇卯吵喵墓妙媌嫹峁庙庿廟戼描昴杳泖淼渵渺猫玅畆畒眇瞄秒竗笷篎緢緲缈苗茆藐覅貓錨锚鱙鶓鹋',
	'묠':'乮',
	'무':'㒇㡔㣳㭌㮊㮘㱐㳇㵲㶃㷻㽗䀤䉑䋷䌗䍢䏬䒉䓮䟼䥐䥻䨁䱕䳇亡亩亾仫倵儛兦务劺務呒呣嘸堥墲奦妩娬婺嫵嵍巫幠庑廡怃愗憮懋戊抚拇撫敄无暓柕楙橆武毋潕無熃牳珷璑甒畝畞畮瞀瞴碔繆缪胟膴舞芜茂莁蕪袤袰誈誣譕诬貿贸踇躌鄮鉧錻鍪雾霚霧鞪騖骛髳鵐鵡鷡鹀鹉',
	'묵':'㩏㫯㷵䁼䁿䘃万嘿嚜墨嫼濹爅癦纆蟔默黙',
	'문':'㗃㡈㦖㭣㵍㻊䊟䎹䎽䘇䟂䠺䦩䫒䰚亹们伆們免刎勽匁吻呅呡問妏彣悗懑懣扪抆捫文暪汶渂炆珳璊璺紊紋絻纹聞肳脗芠菛虋蚉蚊螡蟁鈫鍆钔門閅閺閿闅门问闻阌雯馼駇魰鳼鴍鼤',
	'물':'㫚䥼勿岉昒沕物粅',
	'므':'謬',
	'미':'㜆㜫㜷㝥㞑㟜㠧㣆㣲㥝㫆㳽㴹㵟㸏䅏䆊䇻䉋䉠䉲䊊䊳䋛䌕䍘䓺䕳䕷䙿䛧䞔䥩䥸䦵䬿䭧䱊䴢亹侎冞味咩咪堳娓媄媚媺嬍孊尾嵄嵋嶶弥弭彌微徾捤擟攗攠敉斖未梶楣洣浘渳渼湄溦瀰灖煝爢猕猸獼瑂癓眉眫眯睂睸瞇矀祙穈篃米糜縻罙羋美脒艉芈苿荱菋葞葿蒾蔝薇蘪蘼蝞覹詸謎谜躾迷郿醚醾醿釄銤鎂鎇镁镅镾霺靡鮇鶥鹛麊麋麛黴',
	'민':'㞶㟩㟭㥃㥗㥸㨉㫣㬆䁕䂥䃉䋋䝧䟨䡑䡻䪸䲄僶冺刡勄勔垊姄岷崏忞忟怋悯悶愍慜憫抿捪敃敏敯旻旼暋民泯渑湣潣澠焖燘燜玟珉琘琝瑉痻盿砇碈笢簢緍緡缗罠苠鈱錉鍲閔閩闵闷闽鰵鳘鴖黽黾',
	'밀':'㫘㳴㴵㵥䁇䌏䛑䤉嘧宻密峚樒櫁淧滵蔤藌蜜蠠謐谧',
	'박':'㕷㗘㙸㩧㬍㴖㵡㹒㺪㼎㿺䂍䃗䄸䍸䎅䑈䗚䙏䥤䥬䨌䨔䨣䨰䪇䪙䪨䬪䭦䮀䰊䶈亳剝剥博啪噗嚗圤廹彴愽懪拍搏撲擈敀朴樸檏欂泊溥炇烞煿爆牔犦狛猼珀璞瓟瞨砶礡礴窇箔簙簿粕縛缚胉膊舶艊萡蒪薄襮趵迫釙鉑鎛鏷鑮钋铂镈镤雹颮飑餺馎駁駮驳骲髆髉',
	'반':'㐴㚘㜶㢖㪵㫠㭧㮽㶗㽃㽹㿀䃑䃲䆺䈲䉊䉽䊩䙪䛀䡊䣲䬳䰉䰔仮伴冸半反叛坢奤姅婏媻嬎嬔幋弁怑憣扮扳拌搫搬攀攽斑斒朌柈槃沜泮溿潘瀊炍牉班畔番瘢癍盘盤盼矾磐磻礬秚竝絆縏繁绊肦胖般蒰虨螌蟠褩襻詊跘辬返鉡鋬鎜鑻闆靽鞶頒頖颁飯飰饭魬鳻飯',
	'발':'㔇㔜㗶㛘㛲㞈㟑㧊㧞㪍㴾㶿㺴䍨䘠䚨䟛䟦䢌䣪䣮䥽䪬䭯䮂䯋䳁䳊侼勃叐发哱坺墢妭彂悖愂抜拔拨挬撥柭桲沷泼浌浡渤溌潑炦犮癶癹発發盋砵秡綍缽胈脖茇荸菝葧袚袯襏詙跋蹳軷郣酦醗醱鈸鉢鋍鏺钵钹餑饽馛馞驋髪髮魃鮁鱍鲅鵓鹁鼥',
	'밤':'湴',
	'방':'㑂㕩㕫㝑㤃㤶㥬㧍㨍㫄㭋㭶㮄㿶䂜䄱䅭䏺䏾䒍䖫䠙䢍䢶䦁䧛䨦䩷䰷䲱仿倣傍匚厖哤嗙坊垹埅堏塄塝妨嫎尨帮幇幚幫庞庬彭彷徬房挷搒放方旁旊昉昘枋梆榜氆汸浝淓滂炐牓牥牻狵玤瓬眆磅稖篣紡綁縍纺绑耪肨肪胮膀膖舫舽艕芳蒡蚄蚌蛖蜯螃覫訪謗访谤趽逄邡邦邫鈁錺鎊钫镑防雱霶鞤駹髈髣魴鰟鲂鳑鴋鶭龍龐',
	'배':'㔨㗑㚰㟝㠔㤳㮎㯁㰆㶔㶨㶪㻗㾦䋔䋳䒔䔒䣙䪹䫊伓俖俳倍偝啡坏坯培妚嶏徘扒拜拝排掰揹杯柸桮毰湃炋焙牌猅环琣琲白盃碚禙肧背胚荖蓓蓜衃裴裵褙賠赔軰輩輫辈配醅阫陪韛',
	'백':'㓦㡍㼟㼣㿟䞟䳆伯佰兡岶帛柏栢洦湐瓸白百竡粨絔苩覇銆霸魄鮊鲌',
	'뱀':'㖱',
	'번':'㸋㺕䉒䋣䋦䌓䕰䪛䪤䫶䮳僠勫反噃墦奿嬏幡旙旛棥樊橎潘瀪瀿烦煩燔璠畨番磻笲籓緐繁繙羳翻膰蕃薠藩蘩蠜袢襎蹯轓鐇鑁飜鱕鷭磻',
	'벌':'㕹㘺䇅䑔䣹伐傠垡栰橃浌瞂筏罚罰罸藅閥阀',
	'범':'㕨㠶㴀䀀䑺䒦䒮䟪䬚䭵凡凢凣帆忛杋柉梵氾汎泛滼犯盕笵範舤舧范訉諚軓釩钒颿',
	'법':'㳒佱法灋珐琺疺鍅',
	'베':'北裵褙北',
	'벡':'佰',
	'벽':'㘠㨽㱸㵨㷶䌟䑀䤨䧗䮠䴙僻劈噼堛壁孹廦憵挀揊擗擘檗檘湢澼璧甓疈癖皕碧礔礕稫糪綼繴薜蘗襞躃躄辟釽銢鐴闢霹鰏鲾鷿鸊鼊',
	'변':'㛹㝸㣐㦚㭓㲢㳎㵷㺹㻘䉸䐔䒪䛒䟍䪻䮁便匥卞变変峅弁忭扁抃拚昪汳汴炞犿玣甂稨笾籩糄編胼腁苄藊覍變賆跰辡辨辩辫辮辯边辺邉邊釆閞駢騈骈骿鴘便',
	'별':'㔡㢼㿜䇷䋢䌘䏟䘷䟤䠥䤢䥕䨆䭱䳤丿別别嫳彆徶憋批撇暼潎瘪癟瞥莂虌蛂蟞襒覕蹩鐅閉鱉鳖鷩鼈龞',
	'병':'㔙㙃㨀㻂䈂䋑䍈䔊䗒䨻䰃䴵䶄丙並乒併倂偋傡兵垪塀寎屏屛帡帲幈并幷庰怲恲抦捠摒昞昺柄栟棅椪榜氞洴炳琕瓶甁甹病眪秉窉竝竮箳簈絣缾聠艵苪荓蛃蛢誁踫軿輧迸逬邴郱鈵鉼鋲陃鞆頩餅餠饼駢騈鮩鵧',
	'보':'㙅㙛㷛㻄㻉㾟䀯䋠䑰䩉䯙䲕䳈䳰䴐俌保呆埗堡堢報媬宝寚寳寶报普暜椺步歨歩洑湺潽烳煲父珤甫盙簠緥莆菩葆蕔藵蚥补補褓諩譜谱賲踄輔辅鐠镨靌駂鮬鳵鴇鸨黼',
	'복':'㒒㓀㙏㚆㠅㬼㯷㲫䃼䇚䈏䑑䕎䕐䗱䞳䟮䧤䨱䪁䫝䴆䵗伏僕副匐卜垘墣复宓幞復扑撲攴攵服栿棴椱楅樸澓濮獛畐畗癁福稪穙箙絥纀腹茯菐菔葍蔔蕧虙虲蝠蝮袱複襆襥覄覆諨贌踣踾蹼輹輻轐辐醭鍑鍢馥鮲鰒鳆鳪鵩鶝鸔福',
	'본':'㡷㮺㯻㶱䬱呠本楍絊',
	'볼':'乶',
	'봉':'㛔㜂㠮㡝㦀㶻㷨㷭㷯㸼㻱䀱䆇䋽䒠䗦䗬䙜䡫䧏䩬䩼䭰䮾䳞䴶丰仹俸凤唪埄埲塜塳夆奉妦封尨峯峰崶捀捧摓桻棒槰樥汎泛浲淎湗溄漨烽焨熢犎琒琫甭盽竼篈篷綘縫纄缝艂芃莑菶蓬蘕蜂蠭覂賵赗逢鋒鎽鏠鑝锋鞛韸韼髼鬔鳯鳳鴌',
	'부':'㓡㕊㕮㟊㠫㠬㠸㤔㤱㥉㧵㨐㩤㫙㭥㭪㰴㲗㵚㷆㷌㽬㾈䂤䃿䄮䊿䋨䍌䍍䍒䎍䎔䎧䏽䑧䒀䒄䒇䓏䓨䓵䔰䗄䘀䝾䞜䞯䞸䟔䠵䡍䦣䨗䪔䪖䫍䬏䭸䮛䯽䱐䳕䳝䴸䴺䵾不仅仆付伏伕俘俯偩傅冨凫剖副剻勏吥否呋咅咐哹嚩坿垺埠培報夫妇妋姇娐娝婄婦媍孚孵富専尃峊巬巭府廍弣復怀怤懯扶抔抙拊捊捬掊敷斧旉暊枎柎桴棓椨榑殕泭浮涪渓溥滏烰焤父犃玞玸琈璷瓿畉痡砆磗祔禣秿稃竎符筟箁篰簿粰糐紑紨綒緮缶缹缻罘罦肤胕腐腑腝膚艀芙芣苻荴莩萯蔀蚨蚹蛗蜉蝜衭袝裒複褔覆訃詂讣豧負賦賻负赋赙赴趺跗踎踣邞郙郛部郶鄜酜釜釡鈇鉜錇锫阜阝附陚雬頫颫餢駙驸鬴鮒鲋鳧鳬鳺鴀麩麬麱麸麹復﨓',
	'북':'僰北踣鉳',
	'분':'㖹㞣㤋㤓㥹㨧㮥㯣㱵㷊㸮㿎䩿䭻䴅体倴偾僨兝分匪吩喯喷噴坋坌坟墳奔奙奮妢岎帉幩弅忿愤憤扮捹撪昐朆朌枌桳梤棻棼橨歕氛汾泍渀湓濆瀵炃焚燌燓犇獖玢瓫瓰畚盆砏秎竕笨粉粪糞紛纷羒羵翂翉翸聁肦膹芬苯葐蒶蕡蚠蚡衯訜豮豶賁贲躮軬輽轒逩酚鈖錛鐼锛隫雰頒餴饙馚馩魵鱝鲼黂黺鼖鼢',
	'불':'㘬㚕㞸㪄㺻䞞䭮不乀仏佛冹刜咈坲堋岪巿帗弗彿怫払拂昢柫梻氟沸漰炥煘甶祓笰紱紼绂绋翇艴茀鉘韍韨髴鬅鮄黻不',
	'붓':'㖚',
	'붕':'㥊㬟㵯㻚䙖䨜倗傰嘣堋塴崩弸掤朋棚椖漰焩痭硼綳繃绷萠蹦鏰镚鬅鵬鹏',
	'비':'㑭㔈㔗㔻㗠㗺㘘㘩㠲㡙㣁㥱㧙㩌㩺㪏㫵㮰㳪㵒㵺㸢㹃㺽㼰㽡㿙㿫䀝䀟䀣䁹䃾䆏䇑䈈䉾䊌䊧䎵䑄䒈䕁䕗䘡䙍䚜䚰䚹䛍䠊䠋䡟䡶䣥䤏䤵䨽䨾䩀䩁䪐䪟䫁䫌䫠䬠䮆䯱䰁䰦䲹䴽丕仳伾俷俻俾偹備僃剕匕匪卑厞否呸啚啡啤噽嚊嚭圮坒埤壀备夶奜奰妃妣婓婔婢媲嫓嬶屁屄屝岯崥庀庇庳怌悂悱悲惫憊扉批抷斐昲暃曊朇朼枇枈柲棐椑榌榧比毖毗毘毞毴沘沸泌淝淠渄渒濞焷犕狉狒猆琵畀畁疕疪疿痞痱痹痺睤睥砒碑磇祕禆秕秘秠笓箄箆篚篦簲粃粊糒紕緋纰绯罴羆翡聛肥肶脴脾腓腗膍臂舭芘芾苤菲萆萉萞蓖蕜薭蚍蚽蜚蜰蜱螕螷蟦蠯裨裶襣誹諀譬诽豍豼豾貔費贔费赑轡辔邳郫鄙鄪鈈鈚鉟錍鎞鐨钚镄閟阰陫陴隦霏靅非靟鞞鞴飛飝飞餥馡駓騑騛髀髬魮魾鯡鲱鼙鼻泌',
	'빈':'㟗㡦㯽㰋㺍㻞䎙䚔䧬䨈份傧儐嚬娦嫔嬪宾彬摈擯斌朩梹椕槟檳殡殯浜滨濒濱濵瀕牝獱玭瑸璸矉礗穦繽缤膑臏薲蘋蠙豩豳貧賓賔贫邠鑌镔霦頻顮顰频颦馪驞髌髕髩鬂鬓鬢',
	'빙':'㓈㵗䀻䛣仌俜冫冰凭凴娉慿憑氷泵涄淜砯聘靐騁骋',
	'뿐':'兺哛',
	'사':'㐶㓔㕐㕜㕽㖿㙦㚶㛖㜁㝍㟃㠺㠼㡸㩄㭒㱔㱝㲚㴓㴬㴲㵃㵔㵼㸺㸻㹑㹬㺨㺰㽄㾚㾴㾹䀅䄕䇁䇃䉣䎣䏤䓾䔋䔑䔮䛐䞏䠶䣃䣉䣳䤬䥱䥾䦉䩖䫢䬷䭄䯯䲉䴓䵦丝乍亊事亖些仕伺似佀佘使俟倳倽傞傻僿儍儩写冩剚卸厍厙厶叓史司咋咝唆唦啥喳嗄嗣嘥噝四塮士夕奢姒娑娰孠寫寺射屣峫嵖巳师師徙思恖戺挱挲捨揸摣斜斯枱柌柤查柶査桫桬梭楂楒榭榹樝死汜沙泀泗泤泻洍浉涘涻渣溮漇瀃瀉灺灼燍牭犧狮猀猞献猹獅獻瑡痧皶皻砂砟硰碴磃社祀祠禗禠禩私竢笥筛篩簁簑簔籭粆糸紗絲纱缷耍耜肀肂肆舍舎莎莏葸蒒蓑蓰蕬蕼藛虒虵蛇蛳蜡蜤螄蟖蟴衺裟覗訯詐詞誜謝诈词谢貄賒賖賜赊赐赦蹅蹝躧辝辞辤辭逤邪釲釶鈶鈻鉂鉇鉈鉰銯鋖鍦鐁铊閯食飤飼餷饲馇駛駟騇騦驶驷髿魦魳鮻鯊鯋鰤鲨鳾鶳鷥鸶麝鼶齄飼',
	'삭':'㩂㮶䀥䁻䅴䌇䖛削嗍揱搠數朔槊溯溹烁爍獡矟索蒴鎙鑠铄數索',
	'산':'㛽㢫㦃㪔㪚㮼㯆㹌㹪䃟䈀䉈䊲䐮䚲䝜䡲䨷䴮产仐伞傘删刪剷匴厁圸壭姍姗孪孿山嵼摌散杣橵毵毿汕浐滻潵潸澘狦狻珊產産疝痠祘笇筭算簅糤繖舢蒜藖虄訕讪赸跚軕邖酸鏟鏾铲閂閊闩隡霰饊馓',
	'살':'㐊䊛乷摋撒杀榝樧殺煞脎萨蔡蔱薩虄閷',
	'삼':'㡎㣌㧲㭅㰑㵕㺑䀐䅟䊉䊏䥇䦂䫅䫩䫮䵇三仨俕剼叁参參叄嘇幓弎彡曑杉森椮槮檆毝毿涁渗滲犙甧穇穼糁糂糝糣縿罧芟葠蓡蔘薓衫襂贂釤鏒钐閐鬖參',
	'삽':'㒎㚫㛼㩑㪪㰱㴙㵤㽂䈉䔼䙣䛽䝊䬃䬊䮜䮢偛卅唼啃啑喢帹扱挿插揷歃歰涩渋澀澁牐甴箑箿翜翣臿萐譅趿遪鈒鍤鎝钑锸雭霅霎靸颯飒馺',
	'상':'㜀㟄㦂㦼㫾䉘䌮䒙䔗䔪䗮䘮䡦䫙䫪䮣䴂䵰䵼丄上丧仩伤偿傷傸像償儴勨厢向响商喪嗓嘗嚐垧塽墒孀尙尚尝峠嶑常床庠廂徜恦想愓慡慯扄搡晌桑桒桛槡樉樣橡殇殤湘湯滳漡漺潒灀爽牀状狀瑺甞相磉礵祥箱絴緔緗縔绱缃翔葙蔏螪蟐蟓蠰裳褬襐觞觴詳謪详象賞贘赏鋿鎟鏛鏯鐌鑜霜顙颡騻驦骦鬺鮝鯗鱌鱨鱶鲞鲿鷞鸘鹴祥',
	'새':'㗷㘔䈢䚡䰄䵘噻塞壐愢灑玺璽瓕簺賽赛鰓鳃',
	'색':'㣱㥶㩙㮦㱇㾊䂹䉢䊂䞽啬嗇嗦塞愬懎摵擌栜槭歮歵泎洓濇瀒瘷矠穑穡穯索繬色薔賾赜轖銫鎍铯齚齰塞',
	'생':'㗂㽒㽓䚇䲼䴤栍殅泩湦牲珄生甥省眚笙苼貹鉎鼪省﨡',
	'샤':'仒',
	'서':'㐨㓾㘧㛉㜿㠘㢴㣽㥠㭀㯕㵂㵰㷂㽰㾷䇴䈝䉀䋒䋡䍱䑕䓚䤱䦽䧈䧾䱬书俆偦卥叙唑噬圕垿墅壻婿嫬屖屿嶼序庶庻徆徐恓恕悇抒捿揟撕敍敘暑曙書栖棲楈樨氥汿沀湑溆漵潊潻澨濖犀瑞瑹癙硒稰筮簭粞糈糬紓絮緒緖縃纾绪署耡聓聟胥舒舾芧蒣薯藇蜍蝑蠴西觢誓諝谞迉逝遾醑鉏鋤鏣锄閪魣鱪鱮鱰鵨黍鼠鼡',
	'석':'㒪㙽㛫㛭㝜㫺㭊㱤䁺䂖䂙䂞䄷䖨䨛䲽佦冟匇唽夕奭嬕射席惁惜扸昔晰晳析桞棤檡汐沢沯淅潟澙澤炻焟焬皙睗石矽硕碩磶祏穸緆腊舃舄菥蓆蕮蜥螫裼褯襫邜釈释釋釸鉐錫锡鮖鼫',
	'선':'㒨㔯㔵㘣㧥㩊㪇㪨㭠㯀㲔㳬㵛㵪㶍㷽㺼㾌㿅䁢䁣䃠䄠䄳䄽䆄䉳䍻䗠䘰䙋䙲䙴䚚䠣䡪䢭䢾䤼䥧䦅䨘䱇䱧䲂䳦亘仙傓僊僎僐僲先单単善單塇墠墡奾婵嫙嫸嬋嬗宣尟尠屳廯愃扇揎搧敾旋暶檈歚毨氙洗渲漩灗灷烍煽熯狝獮珗琁瑄璇璿癣癬碹磰禅禒禪秈筅箲籼絤綫線縇縼繏繕线缐缮羡羨腺膳舩船苮蔙藓蘚蜁蝉蟬蟮蟺褼襈詵謆譔譱诜赻跣跴跹蹮躚軐选選還鄯酰銑鍌鍹鏇鐥铣镟霰颴饍騸骟鮮鯅鰚鱓鱔鱻鲜鳝',
	'설':'㐥㓭㔎㞕㡜㣯㨝㳿㴮㴽㻡㿱䙝䝟䥹䨮䱑乴亵伳偰僁卨哾囓媟屑抴挈揲揳暬枻楔榍樰泄洩渫焫爇疶碟禼稧糏紲絏絬緤绁膤舌艝蔎薛蛥褉褻設說説设说躠轌辥辪雪鱈鳕齧',
	'섬':'㚒㣣㨛㩥㪎㰇㰊㴸㺤䀹䁡䃱䃸䆎䊱䊹䕭䠾䯭䯹剡嬐孅憸掞掺摻撡攕晱暹棎歼殱殲炶熌燅爓睒繊纎纖纤蟾襳覢譫讝谵贍赡銛铦閃闪陝韱',
	'섭':'㒤㦪㰔㰼㴇㸉㸎㽊䜓䢡䤮䯀䯅嗫囁夑屟屧弽徢慑懾摂摄攝欇涉渉滠灄燮爕疌籋聂聶葉蠂詟讋讘踂踙蹑躞躡銸鍱鑷镊鞢韘顳颞葉',
	'성':'㙚㝭㨘㮐㷣㼩㼳㽮㾪䁞䃏䇈䗌䚖䫆偗垩垶城墭声姓娍宬峸性惺成星晟晠曐殸渻煋狌猩珹瑆皨盛省睲窚筬箵篂絾聖聲胜腥荿觪觲誠謃诚郕醒鋮鍟铖騂骍鮏鯎鯹',
	'세':'㑕㔟㔺㢷㱑㸷䬽䵻世丗亗勢卋岁嵗帨彗挩朑檅歲歳洒洗涗涚祱稅税笹細繐细蔧蛻蜕裞說説貰贳跩軎轊銴齛齥說',
	'소':'㑿㔅㕖㗛㙌㢝㥰㧧㨞㪢㪽㫹㮴㲈㲖㲧㲵㴅㴑㶮㸛㸴㿋䈃䈰䊥䏴䑹䒕䒚䔠䔥䔫䕅䘘䙼䛾䜹䝪䟽䨭䬰䲆䴛佋俏傃关卲召咲哨啸喿嗉嘨嘯囌埽塐塑娋嫊宵小少尕巢巣巶弰彇愫愬慅所扫捎掃掻搔旓昭柖梳榡樔櫯櫹歗毜氉沼泝消涑溞溯溸漅潇潲瀟炤烧焇焼熽燒牊玿琑璅甦疋疎疏痟瘙矂稣穌窼笑笤筱筲筿箫箾篠簘簫素紹綀綤縤繅绍缫翛肖膆艄艘苏莦萧萷蓀蔬蕭蘇蛸螦蟏蟰蠨袑訴謏謖诉踃踈輎逍遡邵鄛酥銷销霄韶颵颾騒騷骚髾魈鮹鯂鯵鰠鰷鰺鱢鲹鳋齭',
	'속':'㑛㔄㬘㯈䅇䌚䔎䔩䞖䥔䲇䴰俗僳属屬憟束梀樕殐洬涑潥簌粟続續续蔌藗藚觫誎謖谡贖赎趚速遬鋉餗',
	'손':'㢲䁚䐣䕖噀孙孫巺巽愻损損搎槂潠狲猻荪蓀蕵薞逊遜顨飡飧飱餐',
	'솔':'㲞䢦乺卛帥摔率甩碿窣蜶蟀',
	'솟':'㕾',
	'송':'㞞㧐㨦㩳㬝㮤㮸㹐䛦䢠䯳倯凇宋庺彸悚愯憽捒松枀枩柗梥楤檧淞竦荣蜙訟誦讼诵送鍶鎹锶頌颂餸駷鬆',
	'솨':'䐝惢曬',
	'솰':'唰',
	'쇄':'㕞㬠䈗䞆䣔䵀刷唢嗩嗮埣惢晒曬殺涮溑灑琐瑣砕碎縰繀誶鎖鎩鎻鏁铩锁殺',
	'쇠':'㲤䪎哸夊殺衰釗钊鞖',
	'수':'㑔㑯㒘㒸㖟㖬㘜㛐㛢㛮㛸㜐㝊㝽㟬㢑㣊㥅㥞㥨㱁㲑㲓㲙㲣㴚㵞㵦㸂㸡㹋㻟㻽㼡㽷䄖䅡䅫䆳䇓䇕䈭䈹䉌䉤䋶䍁䍋䏂䐰䐹䒘䔹䔺䕑䗏䗛䛵䜐䜔䜬䜿䝂䝐䠔䠼䡭䡵䢘䢫䤇䤹䥙䥦䧌䩳䬒䭉䭨䭭䮟䯝䰅䰑䱸䳠俢修倕傁兽凁厜収受叜叟售嗖嗽嚺囚圳垂垨埀壽夀娷媭嫂嬃嬘嬦守宿寿岫峀嶲嶿帅帥幁廀廋彗惥惾愁戍手扌捜授掱搜摉摗擞擻收数數旞晬杸树栦樇樹橾檖櫢欶殊殳水氵氺汓泅洙浽涭溲滖滫漱潄潚澻濉瀡瀭煫燧狩獀獣獸琇琡璓璲璹瓍痩瘦瘶盨睟睡睢瞍祟禭秀税稤穂穗穟竖竪篲籔粋粹糔絒綇綉綏綬繍繡繸繻纗绣绥绶缍羞脩脺脽腄腧膄膸臹艏苬茱荾菙菽蒐蓃蓚蓨蕦薮藪虽螋袖裋襚訹詶誰誶譢讎讐谁谇豎賥軗輸输遀遂邃鄋酧酬醙醻銖銹鎀鎪鏅鏉鏥鏽鐆鐩铢锈锼閖陎陲隋随隧隨雔雖雠需須须颼飕餿饈馊馐首騪髄髓鬚魗鮂鰽',
	'숙':'㑉㑐㓘㜚㝛㩋㪩㳤㴋㴼㶖䃞䃤䎘䏋䑿䨹䱙俶倏倐儴儵叔埱塾夙婌孰宿尗掓摍橚淑潚焂熟玊珟琡璛璹粛肃肅莤菽蓿虪諔跾驌骕鮛鱐鷫鹔',
	'순':'㒐㔼㚝㝄㝇㡄㥧㦏㨚㫬㬀㰬㵌㵮㶷㸪㽦䀢䀵䋸䏛䐇䑞䓐䔚䖲䘩䙉䜦䣨䥎䴄伨侚偱咰奞姰峋巡廵徇循恂憌揗旬杊栒楯榫槆橓殉毥洵浱淳湻滣漘潃犉狥珣畃盹盾眴瞚瞤瞬碷磭笋筍箰簨紃純纯肫脣舜芛荀莼蒓蓴蕣衠詢諄询谆賐輴郇醇醕錞陙順顺馴駨駿驯鬊鯙鶉鹑鹠',
	'술':'㖅㞊㺷㾁䢞䢤䮅䳳噊戌欰沭珬絉荗蒁術袕述鉥銊錰鶐',
	'숭':'㓽㟣㣝䯷崇崧嵩硹菘',
	'쉬':'㳃䘹伜倅晬殳泅淬焠琗',
	'슬':'㺩㻎㻭厀濏瑟璱膝虱蝨鯴鲺',
	'습':'㒊㗩㠄㦻㿇䏉䒁䗑习啃塍嶍慴拾槢湿溼漝濕熠習袭褶襲謵隰霫飁騽鰼鳛',
	'승':'㐼㞼㮱㱡㴍䋲䒏䮪䱆丞乗乘僧冼勝升呏堘塍嵊憴承抍斘昇枡桝椉榺橳氶洆溗焺甸畻竔縄繩绳脀蕂蝇蝿蠅譝阩陞陹騬鬙鱦鵿',
	'시':'㒋㒮㒾㔭㖷㚸㞔㣈㫭㮛㳏㹝㺇㻢䂠䈕䊓䌤䌳䏡䒨䓱䗐䙾䛈䜵䜻䟗䡳䢄䦠䩃䲩䲭乨使侍偲兕兘凘匙卶厮呞咶啻嘶埘塒始媤宩寺尸屍屎崼嵵市廝弑弒徥恃戠揌提揓施时旹是昰時枲枾柴柹柿榯毢毸沶湤溡漦澌犲猜眂眎矢示礻祡禔笶簛絁緦缌罳翄翅翤翨腮膪茬莳葈葹蒔蓍褷襹視视試詩諟諡諰试诗豉豕豺邿酾釃鈰鉃鍉铈顋颸飔飴鰣鲥鳲鸍鸤鼭',
	'식':'㥀㮩㴧㵓䤭䭒喰埴媳寔式息拭栻植殖湜烒煶熄瘜禃篒籂蒠蚀蝕識軾轼遈鄎鉽鎴食飠飾餝饣饰',
	'신':'㐰㑗㚨㛙㛛㜪㢹㫳㭡㰮㳯㶦㶳㾕䅸䆣䊁䒖䚱䛜䛨䝲䢅䢻䣅䪿䭀䯂䰠伩伸侁信兟卂吲呻哂噺囟妽姺娠孞宸屾峷弞愼慎扟抻敒新昚晨曟柛榊氠汛瀋烥烬燊燼珅璶甡申眒眘矤矧砷神祳笉籶籸紳绅肾胂脤腎臣茞荩莀莘薪藎蜃裑訊訙訠訫訷誶讯识賮贐赆身辛辰迅鉮鋠阠頣顖駪鯓鰰鵢鷐麎辰神',
	'실':'㗭㣰㺙䊝䶡失实実室實怸悉榁窸螅蟋鏭飋鰘',
	'심':'㔤㖊㚞㚯㜄㜦㝷㣺㤈㰂㴱㶒㻣㽸䉇䚓䤁伈侺吢吣噚堔婶嬸审宷審寻尋心忄愖憳攳杺枔桪梣樳橬沁沈沉浔淰深渖潯瀋煁燖璕甚瘎瞫芯葚蕈蟳襑覾諗諶讅谂谉谌邥鄩鈊鐔镡鬵魫鱏鱘鲟沈',
	'십':'䦹什兙十卌拾椞瓧竍籵趇辻拾',
	'쌀':'㐘',
	'쌍':'㕠䉶䝄䨇双孇欆艭雙﨎',
	'씨':'氏',
	'씻':'㘒',
	'아':'㚳㝞㢌㢐㦱㧎㧴㰳㿿䃁䄉䄰䅉䋍䋩䋪䍓䖸䢝䪵䳗䳘丫亚亜亞伢俄俹児兒厊吖哑哦唖唲啊啞垭妸妿娅娥娿婀婭孲屙峨峩庌御我挜掗桠椏氩氬涐牙犽猗玡珴疨疴痖痾瘂皒睋砑硪稏笌聣芽莪蕥蚜蛾衙襾覀訝誐讶迓鈳錏錒鐚钶铔锕阿雅餓饿騀鴉鵝鵞鵶鸦鹅齖',
	'악':'㓵㖾㗁㟧㠋㦍㮙㹊䠎䣞䥃䫷乐偓偔僫剭卾咢喔嗌噩垩堊堮岳崿嶽幄恶悪惡愕捳握楃楽樂櫮渥湂琧腛腭萼葯蕚蝁覨諤讍谔遌鄂鍔鑩锷顎颚鰐鱷鳄鶚鸑鹗齶齷龌',
	'안':'㗴㘖㟁㫨㷳㸩䀂䅁䢿䨃䬶䮗䯃䳛侒偐唵喭垵堓妟姲婩安岸峖按晏暥案桉楌殷氨洝犴眼矸荌諺贋贗赝軅銨錌铵閼雁鞌鞍頇顏顔顸颜騴鮟鳫鴈鴳鷃黫',
	'알':'㖕㖖㧉㩵㷎䀑䁊䔾䥟䮸䯉䯵䰲䵝劜咹嘎嘠圠堨屵嶭戛戞按挖捾揠擜斡歹歺濣焥猰穵窫聐胺訐謁讦谒軋轧遏錷钀閼阏頞鴶齃齾﨟',
	'암':'㘙㛺㜝㞄㽢䅖䖗䨄䫡䬓䯥䳺匼唵啱啽埯堷壧媕岩嵒嵓巌巖巗庵揜揞晻暗痷癌盦盫碞礹罯腤菴萻葊蓭裺誝諳谙闇隌雸韽頷颔馣鵪鶕鹌麙麣黤黬黭黯',
	'압':'㔩㕎㛕㳌㷈㾎䆘䑥䑪䜙儑匎匼压唈圔圧壓姶岋庒庘押曱炠狎砐硆鞥鰪鴨鸭',
	'앙':'㒕㟅㭿㹧㼜㿮䀚䄃䇦䒋䒢䘧䩕䬬䭹䭺䱀仰佒傟卬咉坱央姎岇岟怏慃抰昂昻枊殃泱炴盎眏秧紻羻胦詇軮醠鉠雵鞅駚鴦鸯',
	'애':'㕌㗒㘷㝵㣻㤅㦈㱯㶼㾏㿄䅬䔽䕏䝽䨠䬵䶣伌僾厓叆呃哀哎唉唲啀喝嗄嗌嗳嘊噫噯埃堐塧壒娭娾嫒嬡崕崖嵦愛懓懝挨捱敱敳昹暧曖欸毐涯漄濭燰爱猚獃瑷璦皑皚皧睚瞹砹硋硙碍磑礙艾蔼薆藹譪賹銰鎄鑀锿閡阂阨隘霭靄靉餲馤騃鱫鴱',
	'액':'㟯㧖䘸䝈䩹䱮厄呝嗌峉戹扼掖搤涱液砨磀縊缢腋苊蚅詻豟貖軛軶轭鈪阨阸隘頟額额',
	'앳':'厑',
	'앵':'㴄㹙㹚䁝䨉䴍嘤嚶奣嫈桜樱櫻甇甖罂罃罌莺譻鶯鷪鸎鸚鹦',
	'야':'㖡㘃㙒㭨䓉䤳䥺乛也亱倻偌冶吔喏嘢埜壄夜婼惹捓揶擨斜枒椰漜焲爷爺琊瑘祂耶若裸邪野釾鋣鎁铘鵺若',
	'약':'㒢㜰㰛㵸㿑䋤䐞䖃䚥䟑䠯䤀䶳叒哟喲嫋嵶弱攊楉洂渃瀹爚礿禴箬箹篛籥約纅约若药葯蒻薬藞藥蘥跃躍鄀鑰鰙鰯鶸鸙龠掠略',
	'양':'㐮㔦㠤㦹㨾㬕㳱㺊䁑䉴䍩䑆䑋䖆䖹䬗䬺䭐䭥䵮佯养劷勨勷嚷垟壌壤奍嬢孃崵徉忀恙懩懹扬揚攁攘敭旸昜暘杨样楊様樣檨欀氜氧氱洋漾瀁瀼炀烊煬爙獽珜瓖瓤疡痒瘍癢眻礢禓禳穣穰纕羊羏羕蘘蛘蝆襄詳諹譲讓让躟輰酿醸釀鍚鐊鑲钖镶阦阳陽霷颺飏養饟馕驤骧鬤鰑鴹鸉亮兩凉梁糧良諒量',
	'어':'䁩䏸䐳䔡䗨䢩䥏䰻䱷䲣仒唹圄圉峿御扵敔於棜淤渔漁瘀禦秗箊篽籞菸蓹蘌蘓語语醧鋙铻閼飫饇饫馭驭魚鯲鱼鷠齬龉',
	'억':'㫇䖁䗷亿億忆悥憶抑檍澺癔繶肊臆訲餩',
	'언':'㢇㫃㰽䁙䇾䓂䗡䞁䤷偃傿匽唁喭嘕堰墕娮嫣嵃彥彦愝椻漹焉牪琂甗篶萒蔫蝘褗言訁諺讞讠谚谳躽這遃郾鄢隁鰋鶠鼴鼹齞齴',
	'얼':'㙞㜸㮆㴪䡾乻噦孼孽嵲巕枿槷櫱糱糵臬臲蘖蠥鎳镍闑隉',
	'엄':'㚧㛪㢂㢛㤿㭺䄋䉷䕾䛳䣍䲓䶫䶮严俨俺儼剦厂厈厱厳噞嚴奄孍崦嶖巖广掩揜曮欕淹渰硽罨腌覎觃醃閹阉隒顩龑',
	'업':'㗼㡋㡤㪑㱉㸣䁆䌜䎨䤶䧨䱒䲜业俺嶪嶫業殗澲邺鄴餣驜鸈',
	'엇':'旕',
	'엉':'㫈',
	'에':'㤬恚曀殪',
	'엔':'円',
	'여':'㒜㦛㶛㺞㼂㾒䂊䂛䑂与予伃余侞如妤嬩忬悆懙旟桇櫲欤歟汝洳滪澦狳玙璵畬畭畲硢礖礜穥筎籅籹絮肗舁舆與艅茹蓣蕠蕷蘆輿轝邚銣錄録铷雓餘馀鮽鴽鸒勵呂女廬旅濾礪閭驪麗黎',
	'역':'㑊㘁㚜㣂㴁㴒㶠㻛㽣䍞䓈䓪䖌䡛䦴䧕䭞䮙䰥䳬亦伇圛坄垼域埸墿屰峄嶧帟役怿懌戫攊易晹曎棫棭歝淢湙炈燡琙疫痬睪硛緎縌繹绎罭虉蜮訳譯译豛逆醳鈠閾阈駅驛驿魊鯣鶂鶃鷊鹝鹟力曆歷轢',
	'연':'㒄㓴㕣㜣㝚㦓㨎㫟㬫㭇㮒㳂㳄㳙㳭㴊㶜㷑㷼㸐㸶㻆㽭㾓㿵㿼䀽䂩䂴䄗䆓䊙䍾䓴䔳䕼䖄䗎䗺䙇䛇䜩䞂䢥䨊䬇䬼䱲䳣䳿䴏偄兖兗剈唌嘫噮嚥囦埏堧壖妍姢姸娟娫嬊嬽嬿宴延悁愞抁挻捐掾揀揅撋昖曣棩椼椽樮橪橼櫞沇沿涎涓淵渁渆渊渕渷溎演灁烟烻焔焰然煙燃燕狿珚瑌瓀研砚硏硯碝礝筵綖緛緣縁縯繎缘羡羨耎肙肰胭臙莚葕蔅蜎蜒蜵蝝蠕衍裫觾讌豣蹨軟輭轋软郔酀醼鈆鉛鋋铅閼驠鳶鷰鸢鼘鼝年憐戀撚漣煉璉秊練聯輦蓮連鍊',
	'열':'㖶䆕䆢䊦䭇吶呐咽噎恱悅悦揑涅湼潱热熱税蠮說説閱閲阅列劣咽烈裂說',
	'염':'㚩㦔㱘㶄㷋㷔㷺㿕䀋䅧䌪䎃䎦䒣䛁䣸䤡䦲䫇䶲乵偣冄冉厌厣厭厴呥塩壛夵姌媣嬮恹懕懨扊抩敥曕染棪檶檿櫩殓滟灎灔灧灩炎焔焰燄猒珃琰盐稔艳艶艷苒蒅蚦蚺衻袡豓豔酓酽醶釅閆閻闫阎餍饜髥髯魇魘鯰鲶鹽黡黶廉念捻殮簾',
	'엽':'㒯㩎㷸䈎䭎䭟偞僷厭喦嚈囁摂擛擪擫攝晔曄曅曗枼枽殜烨熀燁爗皣瞱瞸葉鐷靥靨饁馌獵',
	'엿':'㖲㖳',
	'영':'㘇㜲㡕㢍㨕㮠㲟㵬㶈㿘䀴䁐䃷䊔䋝䑉䑍䕦䙬䚆䣐䦫䨍䪯䭊䭗䭘偀咏営塋婴媖嬫嬰嬴孆孾嵘嶸巆巊廮影怺愥摬撄攍攖攚映景暎朠柍柡栄栐梬楧楹榮櫿永泳浧渶溁溋潁濙濚濴瀛瀯瀴灜煐營爃狞獰瑛瑩璄璎瓔瘿癭盁盈矃矨碤礯禜穎籝籯緓縈纓绬缨英营萦萾蘡蝧蝾蠑蠳覮詠謍賏贏赢迎郢醟鍈鐛鑍锳霙韺頴颍颕颖鶧令囹寧嶺怜玲瑩羚聆鈴零靈領',
	'예':'㖂㙠㙪㙯㛳㜒㝣㡫㡼㤤㨅㪒㪫㲊㲼㵝㵩㹭䂱䃜䄁䄿䆌䆿䇤䇩䋵䍲䎈䓲䕍䖊䗟䘽䛖䜜䜭䞊䡺䢃䮘䮹乂倪兌兑兿刈勚勩医叡呓呭囈埶堄壡婗嫕嫛寱帠怈悘惢拽捙掜晲曳曵枍枘栧棿槸橤殹汭泄洩淣濊猊獩玴瑿瘗瘞瘱睨睿瞖秇秽穢繄繠羿翳艺芮芸苅蓺蕊蕋薉藝蘂蘃蘙蚋蜹蜺袣裔褹襼觬詍詣誉譽讛诣豫貎跇踅輗郳銳鋭鏏锐霓靾預预饖鯢鲵鷖鹥麑黳齯例禮醴隸',
	'옌':'円',
	'오':'㐅㑨㜜㜩㟼㠂㠗㢪㤇㥿㩠㬳㮧㱬㹳㻍㾲㿰䃖䎸䐿䓊䖚䛩䜑䜒䞛䡧䥝䦋䦜䫓䫨䮏䮯䯠䴈䴠䵅乄乌五仵伍俉俣傲午厫吳吴吾呉呜唔啎嗚嗷嗸噁噢圫圬坞埡塢墺夭奡奥奧娛娪娯娱媪嫯寤岙嵨嶅嶴廒弙忢忤悞悟悪悮惡慠懊扷捂摀摮擙敖於旿晤杇梧歍汙汚污汻洖洿浯溩滶澚澳烏焐熓熬爊牾獒獓玝珸瑦璈痦磝祦窏窹筽繺聱肟脵茣蔜蘁蜈螐螯袄襖誤謷謸误趶迂迃迕逜遨遻郚鄔鋘鎢鏊鏕鏖鐭钨镺隖隞隩驁骜鰞鰲鳌鴮鷔鼇鼯惡',
	'옥':'㓇䑁䞝剭墺媉屋沃澳狱獄玉砡箼莹軉鈺鋈钰阿鳿',
	'온':'㝧㬈㼔䅱䦟䦷䭓塭媼愠慍揾搵昷桽榅榲殟氲氳温溫煴熅瑥瘒瘟稳穏穩緼縕缊蒀蒕蕰蕴薀藴蘊褞豱輼轀辒酝醖醞鎾闦鞰韞韫饂馧鰛鰮鳁',
	'올':'㐏㐚㐳㽾䑢䦍䪲乯兀卼嗢屼扤杌淴瞃矹腽膃阢靰鼿齀兀',
	'옹':'㘢㙲㜉㝘㢕㨣㮬㴩㷏㺋㻾㽫㿈䈵䐥䔨䗸䩺䱵勜喁嗈嗡噰塕壅嵡廱拥擁暡滃澭灉瓮甕痈癕癰瞈禺罋翁聬臃蓊蕹螉邕郺鎓雍雝顒颙饔鰅鶲齆',
	'와':'㘥㛂㧚㹻㼘䂺䆧䠚䨟䰀䵷佤卧吪咓哇唩啝囮婐捰搲攨枙洼涡涹渦溛漥猧瓦畖砙窊窝窩窪臥莴萵蛙蜗蝸訛譌讹迗邷鈋頋鼃',
	'왁':'䢲',
	'완':'㘤㛡㝴㣪㱧㻨㼝䖾䛃䝹䯈䯛刓剜唍啘园垸埦妧婉婠完宛岏嵈帵忨惋抏捖捥梡椀浣涴烷玩琓琬盌睕碗緩缓羱翫脘腕莞萖薍豌貦贃輐関闗關阮頑顽',
	'왈':'䚴嗗曰聉',
	'왕':'㑌㒬㞷㲿㳝㳹㴏䤑䶭仼尢尣尩尪尫彺往徃忹旺暀枉汪瀇王皇蚟迋迬',
	'왜':'㗏㰪䶐倭劸娃娲媧歪矮緺蛙躷騧',
	'외':'㙗㛱㞇㟴㠕䃬䋿䠿䫥偎外峞崴嵔嵬巍廆徻愄懀揋桅椳歪渨溾煨猥畏瘣碨磈聩聵腲葨詴鍡隈隗鮠鰃鳂',
	'욋':'夞',
	'요':'㑃㑱㑸㑾㕭㘭㙘㝔㞁㟱㧒㨱㫏㫐㴭㹓㹛㿢䁏䁘䄏䆗䆙䆞䌁䌊䌛䍃䔄䖴䙅䚺䚻䠛䢣䫜䬙䯚䳩䶧么仸侥偠傜僥凹匋吆喓嗂坳垇垚垰堯墝夭妖姚娆婹媱嫑嬈宎寥尧尭岆峣崾嶢嶤幺徭徺徼愮憿抝拗挠揺搖摇撓擾暚曜杳枖柪柼桡梎楆榚榣樂橈殀浇溔澆烑熎燿狕猺珧瑤瑶矅磘祅穾窅窈窑窔窯窰筄約縟繇繞绕耀腰舀艞芺苭荛葽蓔蕘蘨蛲蟯袎褥襓要覞訞詏謠謡讑谣軪輋遙遥遶邀鎐闄陶隢靿颻飖餆饒饶騕鰩鳐鴁鴢鷂鷕鹞了僚寮尿料樂燎療蓼遼',
	'욕':'㦺嗕媷峪慾昙欲浴溽縟缛蓐褥谷輍辱鄏鋊鵒鹆',
	'용':'㐯㛚㝐㟾㣑㦶㦷㫪㯴㲝㲨㶲㺎㼸䄾䇀䇯䈶䗤䞻䠜䡆䡥䢆䢇䤊䧡䩸佣俑傇傛傭冗勇勈埇塎墉媶嫆嫞宂容嵱庸彮恿悀愑愹慂慵憃搈搑摏桶榕榵槦氄涌湧溶滽熔牅牗瑢用甬癰砽硧穁穃縙耸聳舂苚茸蓉蛹褣踊踴蹖軵鄘鎔鏞镕镛頌髶鯒鰫鱅鲬鳙鴪鷛龍',
	'우':'㒁㒖㕛㕱㘾㙑㙖㚥㚭㝢㝼㡰㤑㥑㥥㦙㪀㬂㱊㲾㳓㷒㺮㻦㼴䁱䄨䆰䉱䊸䋅䌂䌔䍂䒜䚤䟳䢓䣁䣿䥳䦀䦸䦾䨒䨕䨞䩒䩽䴁于亏亴优佑俁偊偶優区區又友右叹吁吘吽喁噢噳嚘圩堣塸媀宇寓尤峟嵎庽忧怄怣惢愚慪憂懮扜扝扰挧旴杅桙楀樞櫌櫙歶汼沋湡澞瀀牛牜犹獶玗瑀疣盂盓盱祐祤禑禹穻竽紆纋纡羽翢耦耰肬腢芋芌苃荢萭蕅藕虞虶衧訏訦訧謣踽迂遇邘邮郵鄅鄾酑釪鍝鏂陓隅雨雩駀骬髃魷鯃鱿鸆麀麌齲齵龋羽',
	'욱':'㤢㦽㮋㰲䉛䜡䤋勖勗喐噢奥奧彧旭旮昱朂栯澳煜燠礇稢稶薁郁頊顼',
	'운':'㚃㛣㜏㟦㩈㻒䆬䇖䉙䚋䞫䢵䨶䩵䫟䲰云喗囩夽妘恽惲愪抎暈枟橒殒殞沄涢溳澐熉眃磒秐筼篔紜縜繧纭耘耺腪芸蒷蕓蝹賱运運郓郧鄆鄖陨隕雲霣韗韵韻餫齳暈',
	'울':'㐛㠨㭗䁌䖇䵥亐尉欎欝灪爩菀蔚鬰鬱黦',
	'웅':'㞲㷱䧺僌熊雄',
	'원':'㐾㝨㟲㟶㠾㤪㥐㥳㨬㷧㹉㽜䅈䈠䏍䑱䓕䕂䖠䖤䗕䘼䛄䛷䡝䥉䩊䩩䪭䬧䲮䲶䳃䳒䴨倇傆傊元冤原厡厵员員圆圎園圓圜垣塬夗夘妴媛媴嫄宛寃怨惌愿援晼朊杬楥楦榞榬沅洹湲源溒爰猨猿獂瑗畹盶眢禐笎箢綩芫苑茒葾蒝蒬薗薳蚖蜿蝯螈衏袁褑褤諢謜诨豲貟贠踠轅辕远逺遠邍邧酛鈨鋺鎱闧阮院隕顐願駌騵魭鴛鵷鶢鶰鸳鹓黿鼋阮',
	'월':'㜧㞽㳉䄴䋐䎳䞲䟠䡇䢁䤦䬂仴刖岄怴戉抈月枂樾泧狘粤粵蚎蚏越跀軏鈅鉞钥钺',
	'위':'㖐㗸㙎㙔㞮㟪㢻㣦㥜㦣㫉㬙㮃㷉㻰䈧䍴䍷䘙䙟䦱䧦䪘䬐䬑䭳䲁䴧为伟伪位倭偉偽僞儰卫危厃叞喂喟喡喴噅噕囗囲围圍墛委威媁媙媦孬寪尉峗崣嶎帏幃徫愇慰暐楲洈涠渭湋潿炜為煒煟熨熭爲犚犩猬玮瑋痿硊緭緯縅纬罻胃苇萎葦葳蒍蔚蔿藯蘤蘶蜲蝛蝟螱蟡衛衞袆褘褽覣諉謂讆讏诿谓贀踒躗躛违逶違鄬鍏闈闱隇霨韋韑韙韚韡韦韪頠颹餧餵骩骪骫魏鰄鳚',
	'유':'㐡㐵㒡㓜㔱㔽㕗㗀㛜㡏㣸㥚㧫㫍㫿㬰㳊㳛㳶㳺㴗㶋㶙㶭㹘㹨㺄㺠㻀㻥㼌㼶㽔㽕㽥㾞䀁䂋䃋䅎䅑䅗䆜䐓䑊䑻䒴䔀䗽䘱䚃䛕䛻䜅䜽䞕䞥䢊䢟䧷䩱䪋䫱䬀䬔䰆䰭䰰䱂䳑䵋丣乳亏亴侑俁俞偊偤儒兪冘匬卣吁呦唀唯喩喻嚅囿堣堬壘壝姷婑婾媃媨媮嬬孧孺宥寙岰峳崳嵎嵛帷幼幽庮庽庾怮悠惟愈愉懦抭揄揉擩攸斔斞斿曘有杅柔柚桵梄楡楢楰楺榆槱櫾歈毹毺油泑洧浟渘渪游湵滺潍濡濰濻瀢煣燸牖牰狖猶猷琟瑈瑜瓇甤由疣痏瘉瘐癒盱眑睮禉禸秞窬窳籲糅綏維緌繆维羐羑羭聈肉脜腬腴臾芕茰荽莠莸萮萸葇蒏蓶蕍蕕蕤薷蚰蚴蜏蜼蝓蝚蝣蝤螤螸裕褎褏褕襦覦觎誘諛諭讉诱谀谕貁貐趡踓踰蹂輏輮輶迶逌逰逾遊遗遺邎鄃酉酭醀醹釉鈾銪鍒鍮鑐铀铕隃鞣韖顬颥騟騥鮋鮪鰇鱬鲉鲔鶔黝鼬龥劉杻柳流溜琉留硫紐類',
	'육':'㣃㥔㻙䋭䘻儥哊唷喅堉宍棛毓淯焴粥肉育蒮蘛蜟袬逳錥六戮陸',
	'윤':'㠈㣧㽙䤞䦞䪳允勻匀奫尹昀橍润潤狁玧胤膶荺蜳蝡論贇赟酳鈗鋆閏閠闰阭馻倫崙淪輪',
	'율':'㐕㐠㯨䋖䢖䫻䮇凓噊欥汩潏燏矞繘聿茟銉驈鱊鴥鴧律慄栗率',
	'융':'㭜䘬娀戎曧毧漋瀜狨絨绒羢肜茙融螎駥隆',
	'윽':'厼',
	'은':'㐆㒚㕶㙬㡥㤙㥯㥼㦩㴈㶏㹜㹞䅰䇵䌥䓄䖐䖜䨸䭡䴦乚听嗯嚚圁圻垠垦垽峎峾嶾恩慇慭憖憗懚摁斦檃檭檼櫽殷泿溵濦煾犾狺猌珢瘾癮磤稳穏蒑蒽蘟言訔訚誾讔鄞銀银隐隠隱齗龂',
	'을':'䎲乙圪釔钇鳦',
	'음':'㕂㖗㞤㱃㸒䕃䚿䜾䤃䨙䨧䪩乑侌吟吽喑噖噾婬岑崟崯廕愔摿淫淾烎瘖癊碒窨苂荫荶蔭訡趛鈝阥阴陰隂霒霠霪音韾飮飲饮鷣',
	'읍':'㘊㱞㴔㵫䇼䉗䓃䔱䭂俋唈悒挹揖歞泣浥湆湇煜裛邑',
	'응':'㒣㣹㶐㶝䧹凝噟应応應疑膺譍軈鷹鹰',
	'의':'㓷㕈㕒㘈㛄㝖㠖㠜㢊㥋㦉㦤㩘㫊㬾㱅㱲㳖㼁㽈㾨㿲䉝䉨䒾䓹䝘䝝䣡䧇䧧䪰䫑䫯䬥䭲䰙䰮䰯䲑䴊义亄仪依倚偯儀儗冝凒劓医吚嬑嬟孴宐宜寲崖嶬嶷庡意懿扆拟撎擬旑旖椅椬檥檹欹毅毉涯漪燱犄狋猗畩疑矣礒祎禕稦竩籎縊羛義艤萓薏薿藙蚁螘螠蟻衣衤觺誼譩議譺议谊豙輢轙逘郼醫醷鈘銥錡鐿铱锜镱顗顡餏饐饻鷾鸃',
	'읫':'夞',
	'이':'㐌㑆㑥㒃㕥㖇㛅㛋㜇㠯㢮㢽㣇㥴㦾㧠㮕㯩㰘㰝㰻㴣㹫㺿㼢䄬䋙䌺䎟䎠䎶䏪䔟䔬䙹䛂䝯䞅䣵䧅䩟䬁䬮䮊䱌乁二以伊伿佁佴侇侕儞刵勩匜厼台咡咦咿嗌圯坨夷姨媐宧寅尒尓尔峏峓崺已巸廙异弍弐弛弬彛彜彝彞怡恞扅攺敡施易暆杝枱柂栭栮桋椸樲歋殔毦洏洟洢洱潩熪爾狏珆珥瓵異痍眙眤眱眲移笖箷簃粫綛羠羡而耳聏肄肔胣胰胹苡苢荋荑薾蛇蛜蛦螔衈衪袘袲袻訑詑詒誀謻诒貤貮貳貽贰贻趰跠輀轜迆迤迩迱迻邇酏鉯鉺铒陑隭隶頉頤頥顊颐飴餌饴饵駬骪骫髵鮞鮧鲕鴯鶍鸸黟利吏履易李梨泥理痢罹裏裡里離',
	'익':'㔴㚤㜋㢞䄩䋚䌻䘝䣧䯆䴬嗌弋杙榏浳瀷熤熼獈益穓翊翌翼膉艗芅蛡謚谥釴隿霬骮鷁鹢黓齸匿溺益',
	'인':'㘻㝙㠴㣼㧈㧢㪦㲽㸾㽼䀔䀕䃌䄄䇙䍰䏖䏰䑒䒡䓰䧣䲟人亻仁仞仭儿凐刃刄印咽囙囜因垔堙夤姻婣寅屻岃廴引忈忍忎戭扨朄朲杒梕欭歅殥氤洇洕湚湮濥煙牣璌禋秂秵筃籾粌紉絪緸纫肕芢茚茵荵蔩蚓螾裀訒認諲认讱躵軔轫釼鈏銦鏔铟闉陻靭靱靷鞇韌韧駰骃魜鮣吝燐璘藺隣鱗麟',
	'일':'㳑䒤䭿䳀一佚佾劮呹囸壱壹夁嬄尼弌日泆浂溢燚皼衵軼轶辷逸釰鈤鎰镒馹驲鴩鷧逸',
	'임':'㤛㶵䄒䇮䋕䏕䚾䛘䭃临乑任壬妊姙恁栠栣棯祍秹稔紝絍纴腍荏菍衽袵賃赁軠鈓銋飪餁饪鵀林淋臨',
	'입':'入卄叺圦廿扖杁込魞鳰立笠粒',
	'잇':'㗡',
	'잉':'㑞㚺㞌㭁㺱䄧䚮䞉䵴仍剩剰媵孕扔礽膡艿芿賸辸陾',
	'자':'㑑㓨㖢㘂㘞㘹㚗㜽㠿㢀㤵㧗㧘㪥㫮㰣㰷㷷㹀㺆㺭㾅㾳䂣䄍䆅䈘䋾䏑䔂䔝䕢䖪䗪䗹䘣䙻䛋䠖䦻䧳䨏䩾䭣䰞䰵䲿䳄䵭仔做兹刺刾吇呰呲咨啙啫嗞垐塖姉姊姕姿嬨子孖字孜孳孶宱嵫庛恣慈扻朿杍柘栥榨樜橴毑泚溂溠滋澬濨炙煑煮熫牸玆玼珁瓷甆疵痄眥眦矷磁礠禌秄秭秶稵積笫籽粢糍紫緕纃者耔胏胔胾自芓茈茊茡茨茲莿蔗薋藉虸蚝蛓螆蟅蠀觜訾訿諮谘貲資赀资赭赼趀趑趦鄑醡鈭鋅鎡锌镃雌頾頿飷飺餈骴髊髭鮓鮺鰦鲊鲝鴜鶿鷀鷓鹚鹧鼒齊齍',
	'작':'㑅㘀㤰㩱㪕㬭㸲㹱䅵䇎䋏䎞䎰䝫䞢䦃䧿䱜䲵仢作剒勺嚼圴妁妰婥岝岞怍扚斫斱昨杓柞汋灼炸烵焯焳熦爑爝爵犳猎皭皵碏禚秨稓穱筰綽繛绰芍苲莋謶趞趵酌酢醋鈼鐯雀靍飵鵲鷟鹊',
	'잔':'㟞㥇㮍㱚㻵䎒䏼䗃䙁䝳䩆䱠䴼僝刬剗孱嶘戋戔拃栈桟棧残殘潹潺琖盏盞糤菚虥虦輚轏醆饊馓驏骣',
	'잘':'乲乽囐',
	'잠':'㔆㞥㟛㣅㺘㻸䁮䃡䅾䍼䐶䗝䗞䘉䟅䣟䣠䤐䫈䭕䰼䲋䳥兂啿喒埁寁岑挦揝撍撏昝暂暫涔潛潜濳熸硶箴篸簪簮臜臢蘸蚕蝅蠶蠺譧賺赚趈蹔鐕',
	'잡':'㧜㬁䕹䙄䞙䨿䪞䵽匝卡咂咔啑喋嘁囃帀币抸拤杂沞煠疀眨砸磼襍譗迊鉔雑雜雥韴',
	'잣':'㗯',
	'장':'㘯㙊㙣㛇㢓㢡㮜㯍㵴㶓㼻㽴㽵䉃䊋䊢䍧䍭䒂䗅䛫䞪䠆䯴䵁丈丬仉仗仧傽兏匞匠匨场場塟塲墇墏墙墻壮壯壵奖奘奨奬妆妝娤嫜嫱嬙将將嶂嶈帐帳幛幥庄廧弉张張慞戕扙掌摪斨暲杖桨桩梉槳樁樟樯檣欌浆漳漿焋爿牂牄牆状狀獎獐璋瓺痮瘬瘴瞕礃章粀粧粻糚罉羘肠脏腸膓臓臟臧艢苌荘莊萇葬蒋蔁蔣蔵蔷薔藏蘠螀螿蟑装裝賍賘賬贓贜账赃蹡躼遧鄣酱醤醬銺鏘鏱鐣鑶锵長镸长障鞝餦駔騿驵髒鱂鱆鳉麞狀',
	'재':'㒲㗍㘽㢤㦲㦳㧳㩟㪰㱰䍉䏁䝴䬩䮨䴭䵧侢傤儎再咦哉喍在夈宰崽才扗捚斋斎材栽梓榟洅渽溨滓災灾烖睵縡纔裁財賫賳賷财赍載载酨釮鉙齋齎齜龇',
	'쟁':'㓌㬹䋫䍵䟫䦛䦶䱢争噌峥崝崡崢挣掁掙棦槍爭狰猙琤瞠碀筝箏諍诤趟錚鎗鏳鏿铮饓鬇',
	'저':'㑏㓳㝉㡳㡹㤖㪆㫂㫝㭬㭽㯉㵭㶆㸖㾻㿾䃊䃴䇡䈌䊰䍆䍕䎝䏣䐗䘄䘢䠧䡤䢸䣌䣷䪶䬡䭖䱉且仾伫伹佇低储儲劯呧咀唨坥坾墸奃她姐媎宁屠岨庅底弤怚抒抯抵拞掋摴杵杼柠柢楮槠樗橥櫡櫧櫫氐沮泞渚滁潴濐瀦牴狙猪疧疷疽眝眡砠禇竚筯箸篨紵纻罝羜羝翥聜苎苧苴茋菧菹葅著蕏藷藸蛆蝫蠩袓袛褚觝詆詛詝诅诋豠豬貯贮趄趆跙躇軧这這邸阺陼雎骶鯳鴡齟龃猪',
	'적':'㒀㠃㢩㣙㭙㯖㰅㹍㺓䁤䊞䊮䚍䚐䟱䢰䣢䤲䨀䨤䮰䯼䰹䳭䴞䵂䵠乇借勣吊唙啇啲嘀嚁墑嫡寂庴廭廸弔戝摘擿敵旳梑樀樍歒浾滴漃灻炙烾熵狄玓瓋甋癪的硳碛磧积積笛篴籊籍籴糴績绩翟耤聻肑芍苖荻菂葃蔋蔐藉藡蠈襀覿觌謫讁谪豴賊贼赤趯跡踖蹟躍躤迪迹逐逖逷適鏑镝靮頔馰鰿鸐炙',
	'전':'㒰㒹㔊㕓㙉㙻㜊㞟㞡㠭㡐㢆㥏㦮㧂㨵㫋㭵㮵㰄㰜㷙㻇㼷䀬䁴䇳䍹䏝䐌䐪䓦䔐䟢䟧䠄䡀䡒䡘䡱䣑䥖䧃䧖䧘䧠䩄䩅䬻䱳䱼䳪专伝传佃佺倎偂傎傳全典前剪剸厘厧叀吮唸唺啭囀堟塡填塼壂壥奠姾婝婰媊嫥孨専專屇展峑嵮巅巓巔帴廛彅恮悛战戦戩戬戰拴捵揃搌搷擶攧敟旃旜晪暷朘栓栴棧椣椫椾榐槇槙樿橏櫤歬殿毡氈氊沺淟湔湹滇澱澶瀍烇煎牋牷猠琠瑐瑑瑔瑱瑼璳甎田电甸畋畑畠痊痶瘨癜癫癲皽盷睓砖硂碊碘磌磚窴竣竱笺筌箋箭篆篯篿籛糋絟緾縓纏纒缠羴羶翦脠腆腞膞膻臇荃葏葥蒃蕇蜔蟤覥觍詮諓諯謭譾诠谫賟趁跈跧蹍蹎躔転輇輾轉转辁辗邅鄟鄽鈿銓銭鋑錢錪鎆鎸鐉鐫钱钿铨镌闐阗隽電靛靦顓顚顛顫颛颠颤飦餞餰饘饯馢駩騚騡鬋鱄鱣鳣鴫鷆鷏鸇鹯齻',
	'절':'㐉㑜㔃㔢㔾㗫㦢㪿㮞㸅㸞䁀䏳䓆䕙䗻䘁䟙䩢䪼䫕䲙切卩卪姪尐岊嶻帙幯截折撧擮晢晣棁棳楶沏浙準疖癤窃窒竊節絕絶绝聺节苆蕝蠘蠞蠽趃镻',
	'점':'㓠㝪㶘㶣㸃㼭䀡䍄䘂䘋䛸䟋䤔䩇佔占厃唸嚸坫垫墊奌岾店惦扂掂渐漸点煔玷痁磹秥笘簟粘胋苫蒧蔪蛅螹袩覘觇誗踮鏩阽霑頕颭飐鮎鲇黏點',
	'접':'㑙㢎䐑䐲䝃䝕䪓慴挕接摺擑曡椄楪楫渫聑艓菨蜨蝶褋襵跕蹀鰈鲽',
	'정':'㓅㘫㝎㡠㡧㣏㣔㫀㫌㱏㲂㴿㵾㷚㹶㼗㽀䁎䂻䄇䅍䆑䆵䆸䇸䈣䊒䋊䋼䗴䞓䟓䦐䦺䩠䩶䯕䰳䱓䵺丁丼井亭仃佂侦侱侹停偵净凈叮呈啨啶圢埕埥埩塣奵妌姃娗婙婧婷媜宑定寊屲嵉嵿帄帧幀庭廷征徎徰忊怔悜情愸打挰挺掟揁揨政整旌旍晶晸朾枨柽柾栕桢桯梃梷棖椗楟楨榳橸檉檙正汀汫汬泟浄浈涏淀淨渟湞濎濪瀞灯炡烶玎珵珽琔町甼疔盯眐睁睈睛睜矴碇碠碵磸祯禎程穽竧竫筳箐精糽綎緽耓耵聇聙聢聤肼脡脭腈腚艇艼莛萣葶薡虰蛏蜓蝊蝏蟶裎訂証誔諪订证貞贞赪赬踭遉邒郑鄭酊酲釘鉦鋌鋥錠鐤钉钲铤锃锭閮阱阷霆靓靖靗靘静靚靜靪鞓頂頲頳顁顶颋飣饤鴊鼎鼑鼮鼱靖精',
	'제':'㐧㑪㖒㗣㝂㣢㨈㨹㫼㴉㸄㼵䀸䂑䃅䄞䄢䄺䅠䇽䍤䎺䏲䐎䐡䑭䑯䔶䖙䚣䛱䜞䠁䢑䧑䨑䨖䩘䩚䪠䪡䪢䪣䬫䬾䭁䮺䰏䱥䱨䱱䶍䶑䶒䶓䶩亝侪俤偍偙傺僀儕制剂剤劑厗呧哜啼嗁嚌埞堤姼娣媂媞帝弟徲怟悌惿慸憏懠折挤提摕擠斉斊晢栬梊梯櫅泲济淛済渧滛漈漽濟焍狾猘珶瑅璾癠睇睼碮碲磾祭禔禵稊穄穧第綈緹绨缇罤脐腣臍艩苐荑荠萕蒢蕛薺虀蛴蝭蠐袃裚製褆諸謕诸趧跻踶蹄蹏躋醍銻鍗鑇锑际除隄際隮霁霽鞮韲題题騠骶鮆鮧鮷鯯鯷鰶鱭鲚鳀鴺鵜鶗鶙鹈麡齊齌齏齐齑諸',
	'조':'㒛㓮㕚㚋㜖㟘㡑㡟㡽㣿㨄㬽㭤㮻㯥㯾㷖㷮㸠㺐䂏䄚䆆䆴䈇䉆䍜䍮䎭䏆䐬䒃䒒䔃䔘䔙䖣䖺䗢䘟䜊䝖䞴䟭䠷䢐䥄䧂䩦䯾䱔䳂䵲伄佻俎傮兆凋刁刟劋助厝召叼唕唣啁啅嘈嘲噪垗奝嬥宨嶆幧庣弔弴彫徂恌慥懆找抓挑措操旐早昭晀晁曌曹曺朓朝条枛枣栆梍條棗槽樢樤殂殦汈沠漕潮澡灶炤照燥燳爪爫爼狣珇琱瑵璪瘹皁皂盄眺瞗瞾碉祖祚祧租稠穒窎窕窱窵竃竈竨笊箌簓粗粜糙糟糶組絛絩縧繰组绦缲罀罩罺羄聎肁肇肈肏胙脁臊艁艚茑荮莇莜葤蒩蓚蓧蓸蔦薻藋藻蚤蛁蜩螩螬褿襙覜訋詔誂調謯謿譟诏调赵趒趙趮跳蹧躁造遭鄵醩釂釕釣鈟銚銱鋚鋽錭錯鎥鎺鏪鐰鑃鑿钌钓铞铫阻阼雕雿靎靻鞗駋駣髞魡鮉鮡鯈鯛鰷鲦鲷鳥鵰鸟麆鼂鼌',
	'족':'㞺㵀哫族瘯簇足踿鏃镞',
	'존':'存尊拵橂燇袸銌',
	'졸':'㐍㐒㰵䂐䘚䚝䯿䱣伜卆卒拙捽椊炪猝稡箤踤',
	'종':'㗰㙡㚇㜡㡖㢔㣫㣭㥖㨑㯶㹣㻜䁓䅊䇗䈦䈺䍟䐫䑸䗥䘴䙂䙕䝋䡮䢨䳷从伀倊倧傱刣喠堫堹妐婃孮宗尰嵏嵕嵷嵸幒従徔徖從徸忪怂悰慒慫昮暰朡枞柊棕椶樅歱汷泈淙潀炂煄熧猔猣琮瑽疭瘇瘲瞛碂磫種稯籦粽糉糭終綜緃緟緵縦縱纵终综翪肿腙腫艐苁葼蓗蔠蝬螽衳誴諥豵賨賩踨踪踵蹤蹱銿錝鍐鍾鐘钟锺騌騣騤骔骙鬃鬉鬷鯮鯼鴤鶎鼨',
	'좌':'㔫㘴㘸㛗㝾㟇㭫䂳䟶佐侳剉咗坐夎屮左座挫痤睉矬脞莝蓌蓙袏趖遳銼锉髽',
	'죄':'㠑㪓嶵檌罪脧辠',
	'주':'㔿㕀㕏㕑㖄㞫㡡㤽㦞㦵㧣㫶㴤㴻㹥㺛㿒㿧䇠䈙䊘䌧䌷䎇䎷䎻䏭䓓䓟䖞䛆䝬䟞䠫䣭䧓䩜䪒䲖䲤䶇丟丢丶主伷住作侏侜俦做儔冑凑厨厾周呪咒咮唒啁喌嗾噣嚋壴奏妵姝婤宔宙尌嵀州帱幬幮廚徟怞懤拄揍斢族昼晝晭朱柱株椆楱樦橱櫉櫥殶注洀洲淍湊澍炷炿烐燽犨犫珘珠畴疇疛疰皗盩矪砫硃祝祩秼稠筹籀籌籒粙紂紬紸絑綢纣绸罜肘胄腠舟菗葄蔟薵蛀蛛蟕蟵袾裯註詋誅調譸诛诪賙赒走赱趎足跓跦踌蹰躊躕軴輈輖輳辀辏逎週遒邾郮酎酒鉒銂銩鋳鑄铥铸霌霔飳馵駐駯駲騆驻鮢鯐鴸鵃鸼麈黈鼄',
	'죽':'俼喌竹粥鬻',
	'준':'㑓㑺㒞㕙㝦㡒㷪㻐㻪㼱䐏䔿䞭䣩䥴䮞俊偆僎僔儁准凖噂埈埻墫壿夋宒寯尊屯峻嶟恂惷懏捘撙晙樽殾浚準濬焌畯皴睃稕竣竴箺純綧繜罇葰蠢訰譐踆踳蹲迿逡遵鎨鐏陖隼雋餕馂駿骏鱒鳟鵔鵕鶽鷷',
	'줄':'㤕乼啐崒崪窋笜茁誶',
	'줏':'㗟',
	'중':'㐺㑖㣡㲴㴢䌬䝦䦿䳯中仲众妕媑狆眾筗舯茽蚛蝩衆衶褈迚重鈡隀',
	'즉':'㑡䐚即卽唧喞崱揤皍荝莭萴蝍鯽鰂鱡鲗鲫',
	'즐':'㘉喞堲擳栉楖櫛瀄騭骘',
	'즘':'怎',
	'즙':'揖楫檝汁湒濈緝葺蕺霵',
	'증':'㣒㷥㽪䇰䉕䎖䒱䕄䗀䙢䡕䥌䥭䰝噌囎塍増增嶒憎拯撜曽曾橙橧潧烝熷璔甑症矰磳竲篜繒缯罾蒸譄證贈赠鄫驓鱛',
	'지':'㕄㞢㞨㞴㡶㢟㨁㩼㫑㫖㯄㱴㲍㲛㴯㸟㽧㽻䂡䄊䅩䇛䏯䑛䓋䓌䓜䓡䓩䘭䙙䜄䝷䞇䟖䟡䠦䡹䣽䤠䥍䧴䪧䱈䲀䲬䳅䵹䶵之俧倁凪劧厎只吱咫哋地址坁坔坘坻埊墀墬娡岻嶳帋底彽志忯恉扺抧抵持指挚搘摯支旨智杫枝枳栺梽椥榰止氏池汥汦沚泜洔淽渍漬潪疻痣知砋砥祇祉祗祬秓秖秪竾筂筫箈篪紙綕纸耆肢胑胝脂至舐舓芝芷蚳蜘衼覟觗訨誌謘識貾質贄贽赿趾踟躓軹輊轵轾迟逇遅遟遲酯鋕阯馶驇鮨鳷鴲鷙鸷鼅識',
	'직':'㞋㮨㹄䐈喞嬂樴溭犆直禝稙稷織织聀职職膱蘵蟙軄',
	'진':'㐱㖘㣀㥲㬐㬜㭄㯸㰉㲀䀆䀌䀼䂦䂧䈯䊶䐜䑐䗯䝩䟴䡩䨯䪾䫃䳲侭侲儘唇嗔嗪嚍堻塡塦填塵壗姫嫀嫃嬧尘尽屒帪弫抮挋振搢搸敐敶昣晉晋枃桭棧榗榛樄樼殄殝津浕溍溱濜獉珍珎珒琎瑧瑨璡甄畛疢疹盡眕眞真眹瞋禛秦稹籈紖紾絼縉縝縥纼缙缜聄胗臸臻蒖蓁蔯薼薽蜄螓螴袗裖診誫謓诊賑赈趁趂軙軫轃轸辰辴进迧進鉁錱鎭鎮镇阵陈陣陳震靕駗鬒黰',
	'질':'㑵㗌㗧㘍㜱㜼㩫㲳㲺䏄䑇䜠䟈䬹䱃佚侄儨劕厔叱呹垤妷姪嫉峌帙庢恎愱戜抶挃昳晊柣桎槉櫍洷潌瓆瓞疾眣眰礩祑秩秷窒紩絰绖翐耊耋胅腟膣臷苵蒺蛭螏螲袟袠詄豑豒貭質质跌迭郅銍鑕铚锧',
	'짐':'㘰㪸㮳㯢㴨㼉䧵䲴斟朕栚酙鴆鸩',
	'집':'㗊㗱㙫㠍㠎㣬㱷㴕䁒䅤䉅䌖䐕䩰䮶亼什偮卙咠執嶯慹戢执汁潗瓡絷緝縶缉艥蓻諿謺輯辑鍓鏶集雦雧什',
	'짓':'嗭',
	'징':'㠞徴徵惩憕懲澂澄瀓癥瞪',
	'차':'㗬㞖㢒㣾㦋㨋㷢㸙㼮㽨㾝䁟䂘䂨䃎䊬䐒䐤䑘䑡䒲䖕䖳䞣䟕䠡䡨䣜䦈䯸䰈䰩䱹䳐䴾䵙䶥且仛佌佽侘借偖偧偨剳劄厏叉咱唓唶嗏嗟嗻奓奲姹嫅岔嵯嵳差徣扠扯挓搓搽撦暛杈栨槎次此汊瑳砗硨磋笡箚紁絘肞舣艖芆茶莗蒫蔖虘蛼衩褨訍譇跐踷蹉車车遮醝釵銟鎈鹺鹾齄齇齜齹茶',
	'착':'㒂㓸㚟㲋䇥䓎䕴䥘䥣丵凿剒娕娖戳捉搾撯擆擉斮斲斵昔浞灂珿着穛窄笮篧簎籱糳縒莡著諑诼躇辵辶逪鋜錯鑡鑿错齪龊',
	'찬':'㛑㜺㠝㣓㦌㬄㸇㸑㹽㺗㻮䂎䉔䉵䌣䞼䟎䡽䬤䬸䰖䱗丳儏儧儹兓劗囋巑撰撺攅攒攛攢櫕欑殩湌澯濽灒灿熶燦爘爨璨瓉瓒瓚禶穳窜竄篡篹簒籑籫粲繤纂纉纘缵羼薒襸讃讚賛贊赞趱趲蹿躜躥躦鄼酂酇鑚鑹鑽镩餐饌饡馔',
	'찰':'㞉㦫㱜㳐㳨䃰䓭䕓䥷䶪乲偺刹剎咱哳嚓囋察巀扎拶擦攃札桚檫櫒獺礤礸糌紥紮耫蚻蠿詧鍘鑔铡镲',
	'참':'㕘㜗㜞㟥㟻㠁㦧㨻㰫㸥㺥㽩㿊䁪䂁䑎䜛䜟䟃䤘䤫䧯䪌䱿䳻䶨傪僣僭儳劖厽叁参參叄叅噆嚵堑塹墋壍嬠嬱崭嵾嶃嶄嶊巉惨惭慘慙慚憯懴懺搀摲攙斩斬旵朁椠槧欃毚毶渗滲漸瀺獑瘆瘮碜磛磣站艬覱詀謲譖譛讒讖谗谮谶趻酁醦錾鏨鑱镵饞馋驂骖魙黪黲',
	'창':'㒉㘟㧿㫤㼽䄝䅛䅮䆫䎫䗉䚎䞎䠀䢢䤌䥊䩨䮖䱽䲝仓仺伥伧倀倉倡傖僘凔刅创刱剏剙創厰呛唱嗆囪囱娼嵢廠彰怅怆悵惐惝愴戗戧抢搶摐摤敞昌昶晿暢枪椙槍氅沧涨淌淐滄漲濸炝焻熗牎牕猖獊玚玱琩瑒瑲畅畼疮瘡磢窓窗窻篬胀脹舱艙苍菖蒼螥裮誯謒賶跄蹌鋹錆錩锖锠閶阊鬯鯧鲳鶬鸧鼚',
	'채':'㥒㦅㳗䃀䌨䌽䐆䐱䘍䞗䠕䣋䰂倸债債囆埰婇寀寨彩採柴棌榸瘥瘵睬砦祭綵縩茝菜蔡虿蠆責踩采釵钗靫',
	'책':'㖽㟙㥽㨲㩍㩞㳻㿭䇿䜺䞰䟄䯔䶦冊册厇唶啧嘖嫧帻幘憡拺措敇柞柵栅皟瞔磔笧策筞箣箦簀籷粣翟舴茦萗蓛蔶虴蚱諎謮責责迮銏鏼頙',
	'처':'㜘䁦䖏凄処刞处妻悽淒狙竌紪緀耝萋處褄覰覷覻觑郪霋鶈',
	'척':'㘮㞝㡿㥻㽚䋇䑾䗩䞠䞶䯜俶倜傶刺剔叺呎坧塉墄墌尺嵴彳徏悐惕惖慼慽戚拓捗掦掷摭擲斥涤滌瘠硩磩粎脊膌蚇蜴褁跖踢踯蹐蹠蹢躑適鏚陟隲隻鶺鹡鼜齣刺',
	'천':'㐪㚈㟫㣤㯌㱛䀒䀖䄹䆤䆥䉦䍎䑶䒶䚶䢬䢴䥀䵐串仟侟俴倩僢儃兛兲冁刋剶千喘嘽囅圌圱圲天夼奷巛川幝忏扦拪揼撰擅曻杄栫梴棈楾櫏歂氚汌汘泉洊洤浅淺湶溅濺瀳灛灥燀牮猭玔珔瑏瓩皘硟祆穿竏篅篟粁綪繟腨臶舛芊茜荈荐莤葲蒇蒨蔳蕆薦蚕譂谸賎賤贱践踐輤輲辿迁遄遷釧釺钎钏閳闎闡阐阡靔靝鞯韀韆韉鰁鳈',
	'철':'㙍㬚㯙䄌䒆䚢䞵䟾䥫䫎䮕凸剟勶叕哲啜啠喆嚞嚽囅埑彻徹悊惙掇掣撤敠敪歠涰澈烲焎爡畷瞮砓綴缀罬聅腏蛈蜇裰諁輟轍辍辙酫醊醛鉄銕鋨錣鐡鐵铁锇飻餮驖',
	'첨':'㐁㑒㔐㖭㙴㚲㜬㡨㤁㤐㦰㬲㮇㵇㶺㾆䄡䄼䇝䋬䏦䑚䞌䠨䦓䪜佥僉冿厃噡婖尖嶦幨忝悿惉掭敁槧檐櫼沗沾添湉瀐瀸灊燂甛甜瞻签簷簽籖籡籤舔舚菾虃裣裧襜襝詹諂讇谄酟鋓鍩鐱鑯锘閚韂餂黇',
	'첩':'㡇㤴㥈㨗㨩㩸㩹㫸㬪㭯㱌㲲㳧䌌䑖䕈䠟䥡䧪䩞䴑䴴䵿倢倿偼叠呫喋堞妾婕媫崨帖怗惵捷曡氎淁牃牒畳疂疉疊睫穕緁耴脻萜蓵褶褺誱諜谍貼贴踕踥輒輙辄迠鉆钻鮿鯜',
	'청':'㕔㵙䝼䞍䨝䴖凊厅厛圊夝庁廰廳掅晴暒氰淸清甠碃聴聼聽菁蜻請请郬鋹錆閶靑青鬯鯖鲭鶄鶬晴',
	'체':'㓹㔸㚄㡗㬱㿃䀙䄟䇧䌡䎮䏅䐭䗖䙗䟷䠠䪆䴘䶏体切剃叇啑嚏嚔墆屉屜崹嵽帖彘懘挮掣揥搋摖摰替杕栘棣楴殢涕滞滯璏疐痸皉矵砌磜祶禘笍綴締缔蒂蔕蕞蝃螮褅諦谛躰軆达迏迖递逓逮遆遞遰釱鉪銐鐟霴靆餟骵體髢髰鬀鬄鷈鷉切',
	'초':'㗹㤘㥮㩰㭂㯧㲬㴥㶤㷅㸈㹦䂃䄪䇌䈾䌃䌭䎄䎐䒑䘯䜈䟁䠂䥚䩌䫸䫿䰫䲃䶰仦仯偢僬僺儊初剿劁劋劭勦吵哨嘮噍妱嫶屌岧岹峭嶕嶣巐帩弨怊悄愀愺憔憷抄招摷撨杪梢椒椘楚樵檚櫵欩潐濋炒焣焦煍燋燞璴瘄癄眧睄瞧硝礁礎祒秒稍綃绡耖肖膲艸艹芀苕茮草荹菬萔蕉蕱藮蟭觘訬誚謅譙诌诮谯貂超趠趭軺轈轺迢酢醋醮釥鈔鉊鍣鍫鍬鐎钞锹陗鞘鞩韒顦騲髫鷦鹪麨鼦齠齼龆',
	'촉':'㔉㙇㯮㻿䃚䇍䌵䎌䕽䙱䛤䟉䟟䠱䪅亍促劚嘱囑孎属屬数斶斸曯欘歜灟烛燭爥瘃瞩矗矚竐脨臅薥蜀蠋蠾襡襩触觸趗趣趨踀躅钃髑鸀',
	'촌':'刌吋寸屗忖村澊籿邨',
	'촐':'伜',
	'총':'㞱㷓㹅䆹䈡䉥䐋䓗䕺䗓䡯䤸䧭䰌丛偬傯冢匆叢囪囱埫塚宠寵忩怱总悤惣愡憁捴揔搃摠棇樬樷欉漎漗潈潨濍灇焧熜燪爜璁篵総緫縂縦縱總繱聡聦聪聰茐葱蓯蔥藂蟌謥銃鍯鏓鏦铳騘驄骢塚',
	'촬':'㔍㭮㵶䆯䵵娺撮攥窡繓襊',
	'쵀':'䦤啐啛祽錊',
	'최':'㜠㝡㝮㵏䊫䔴䘒䙑䧽䴝催凗嗺嘬墔崔慛摧最榱槯樶欼漼熣獕璀皠磪穝紣綷縗缞羧脧膗衰鋷鏙',
	'추':'㑇㑳㔌㖩㗓㗙㛀㠇㥢㨨㩅㩆㩾㭰㮅㮲㰎㵵㷃㷕㻓㼙㾭㾽㿷䀺䅢䅳䆋䆶䇬䋓䋘䋺䎿䐍䐐䐢䑼䔏䜴䝒䝙䠓䣯䦌䨂䨨䪮䮔䱦䲡䳡䵸䶆丑侴僦僽出刍吜啾坠埾墜娵媝媰寉尴尷岀崷帚惆憱抽捶推掫揂揪揫搊搥杻枢棰棷棸椎楸榋槌樞橻殠沝渞湫湬湭溴煪煼犓甀甃瘳皱皺睭瞅矁硾礈秋秌穐箃箒箠篍篘簉籕緅緧縋縐绉缒膇芻菆菷萑萩蒭藲蝵蟗蠤觕諈諏诹貙趋趍趣趥趨追遚邹郰鄒鄹酋醔醜錐錗錘鎚鑆锤锥陬隹雏雛鞦鞧顀駎騅騶驺骓鬌鬏魋鯞鯫鰌鰍鱃鲰鳅鵻鶖鶵鹙麁麄麤黀齱齺龝',
	'축':'㗤㛩㜅㰗㾥䙒䙘䙯䠞䥮䮱丑丒傗嘁嘼噈妯拀敊斣柚柷槭殧滀潚畜祝稸竺笁筑築篫縬縮缩舳茿蓄蓫豖趣踧蹙蹜蹴蹵軸轴逐鄐閦顣鱁鼀',
	'춘':'㖺㫩㿤䞐䞺䡅䦮䲠偆堾媋旾春暙杶杽椿橁櫄湷瑃睶萅萶蝽賰鰆鶞',
	'출':'㑁㔘䘤䟣䢺出岀怵怷朮术樎欪泏炢础秫絀绌莍黜黢',
	'충':'㓍㤝㥙㧤㮔㳘㳞䂌䆔䖝䘪䝑䟲䡴傭充冲嘃忠忡揰沖浺漴爞珫痋盅祌种翀茧茺虫蟲衝衷',
	'췌':'忰悴惴揣疩瘁膵萃贅赘顇',
	'취':'㪜㯔㯜㱖䕜䶴冣取吹嘴噿娶就嶉揣槜橇檇欈毳濢炊璻疩瘁竁翆翠聚脃脆膬臎臭臰觜趣酔酻醉顇驟骤鷲鹫龡',
	'측':'㳁䈟仄侧側則厕厠嘁庂廁恻惻捑昃昗汄测測畟稄',
	'츤':'儭',
	'층':'䁬层層蹭',
	'치':'㛓㢁㢋㣥㥡㨖㮹㯰㰞㱀㴛㶴㺈㿂㿐㿳䀿䅆䅔䆈䇪䉜䊷䊼䌶䎩䏧䐉䕌䚦䚳䝰䞃䞾䟀䣎䦯䧝䮈䰡䶔乿侈俿値值偨偫傂卮卶哆嗤垁垑埴夂妛媸寘峙崰崻嵯差巵帜幟庤廁廌徝徴徵恀恥憄懥懫拸搱旘昃杘栀梔植椔樨歭歯治淄湽滍炽熾瓻甾畤痓痔痴癡眵秲稚稺穉糦紎絺緇緻缁置耆耛耻胵致芖茌茬荎菑葘薙藢蚩袮袳裭褫襧觯觶訵誃誺豸跮跱輜輺辎郗鉹錙鍿锱阤陊雉馳駤騺驰鯔鲻鴙鴟鵄鶅鸱黹齒齝齿',
	'칙':'䳵侙则則勅勑恜慗敕淔趩遫鉓飭饬鶒鷘',
	'친':'䞋䠳䠴亲儬嚫媇寴榇櫬澵瀙藽衬襯親齓齔龀',
	'칠':'㐂㓒㓼㓿㔑㭍㯃䜉䣛七柒桼漆',
	'침':'㑴㓄㓎㕴㝲㪛㴆㴴㶩㾛䆮䈜䑣䒞䘲䚀䚁䜷䤟䥠䪴䫖䫬䭙伈伔侵兓唚埐夦寑寖寝寢嶜忱惨慘抋抌揕枕枮梫椹沈沉浸湛濅琛砧碪祲綅綝莐萙葴誛諃賝踸郴針鈂鋟鍖鍼针锓霃駸骎鮼鱵',
	'칩':'㙷㞏㞚㮑漐蛰蟄釞馽',
	'칭':'㛵䕝偁爯秤称稱穪',
	'카':'㻔佧胩',
	'쾌':'侩儈叏哙噲夬快獪筷',
	'타':'㓃㙐㛆㛊㟎㢉㥩㨊㯐㰐㸰㸱㻧㼠㾃䂝䅜䆛䍫䑨䑮䒳䙃䙤䜏䠤䡐䤩䤪䤻䩔䪑䰿䲊䴱亸他佗刴剁吒咃咑咜咤哚唾嚲垛垜垞埵堕堶墮墯奼妥媠嫷它尮岮崜嶞彵惰憜打扡拕拖挅挆揣撱朵朶柁桗椭椯楕橢毤毻池沱沲涶灹炧炨牠痑砣砤碢秅紽綞舵袉詫诧趓跎跥跺躱躲軃迤酡鍺锗陀陁陏馱駄駘駝駞驮驼鮀鰖鴕鵎鸵鼉鼍鼧',
	'탁':'㔬㤞㧻㪬㹿㺟䐾䓬䮓乇仛伲侂倬凙剢剫劅卓吒啄啅噣坼度庹托拆拓擢斀晫杔柝桌椓槕槖橐汑沰浊涿濁濯琢琸矺硺窧箨籜萚蘀蠗袥襗託讬跅踔踱逴鈬鐲鐸铎镯飥饦馲驝魠鵫度拓',
	'탄':'㖔㛶㧷㨏䋎䘺僤吞呑啴嘆嘽坦弹弾彈怹惮憚憻掸摊撣擹攤暺歎殚殫氽汆湠滩灘炭疃痪瘓瘫癱碳綻绽羰袒誕譠诞騨驒',
	'탈':'㣞䫄侻夺奪捝敓敚梲毲痥稅税脫脱莌鮵鵽',
	'탐':'㤾㴷㵅䏙䏥僋嗿忐探撢沊眈耽貪賧贪赕躭酖醓',
	'탑':'㗳㛥㯓㲩㲮㹺䈳䌈䑜䑽傝嗒嚃塌塔墖搨搭撘榻毾溻漯狧瘩禢耷遢錔鎑鑉闒阘鞜鞳鮙鰨鳎',
	'탕':'㼒䑗䦒偒圵婸宕帑摥汤湯烫燙璗盪砀碭簜糖荡菪蕩薚蘯蝪趤踼逿鐋铴雼糖',
	'태':'㑀㑷㙂㟋㣍㣖㤗㥭㳲䈚䌼䬈䭾傣兊兌兑冭台呆呔囼埭大太夳娧孡忕忲态怠態戻抬捸斄曃殆汰泰溙炱炲燤笞粏紿綐緿绐肽胎脫脱舦苔菭蜕詒跆軩迨逮邰酞鈦銳鋭钛颰颱駄駘駾骀鮐鲐',
	'택':'㡯㭦䕉䕪伬宅択择擇沢泽澤烢礋蠌鸅宅',
	'탱':'㯑幀撐撑樘橕橖牚竀',
	'터':'摅攄',
	'토':'㫦兎兔吐土圡堍套汢芏茔莵討讨釷钍鵵',
	'톤':'䵯啍噋噸瓲畽',
	'톨':'㐋',
	'통':'㣚㪌㳆㷁嗵恫恸慟憅捅桶樋洞熥痌痛筒筩統綂统蓪通洞',
	'퇴':'㕍㞂㞜㢈㥆㨃㱣㷟㾼㿉㿗䀃䇏䊚䏨䜃䨺䫋䭔俀僓垖堆塠尵嵟弚推敦桘槌煺痽磓穨脮腿蓷藬蘈螁褪蹆蹪追退鎚陮隤頧頹頺頽颓骽鴭',
	'투':'㕻㖣㚐㢏㪗䛠䞬䟝䤅偷偸哣套妒妬投敨渝牏秺緰蘣透闘骰鬦鬪鬬鬭',
	'퉁':'佟',
	'특':'㥂㧹忑忒慝特脦蚮蟘貣貸鋱铽鴏',
	'틈':'闖闯',
	'파':'㗞㜑㝿㞎㨇㩯㭛㸭㿬䃻䆉䎬䎱䔤䝛䥯䯲䰾䶕叵吧啵嘙坝坡垻壩夿妑婆尀岜岥嶓巴帊帕弝怕把摆播擺朳杷櫇欛汃汖汴波派潖灞爬爸玻琶疤皅皤破碆笆笸筢箥簸粑紦罢罷羓耙舥芭菠葩蒎蔢蚆蚾袙譒豝趴跁跛鄱鈀鉕錃鎃钯钷靶頗颇駊鲃',
	'판':'㤆判办坂岅昄板汴版瓣瓪畈眅粄舨蝂販贩辦辧鈑钣阪鵥',
	'팔':'㭭仈八叭哵捌朳汃玐釟',
	'팟':'巼',
	'패':'㔥㗗㛝㤄㧩㫲㳈㶚㸬㸽䊃䖰䟺䢙䩗䩻䰽䱝伂伯佩倍呗唄姵孛悖抜拔拨捭敗斾旆昁梖棑沛浿牌牬犻狈狽猈珮珼矲稗笩篺簰粺肺背苝茷蛽覇誖貝贁贝败邶郥鄁鋇钡霈霸馷',
	'팽':'㑟㤣㧸㱶㼞䄘䑫䙀䥋亨伻傍嘭嵭彭憉掽旁梈澎烹甏皏砰硑碰磞祊稝膨蟚蟛軯輣錋閍闏騯',
	'퍅':'愎',
	'편':'㓲㴜㸤㼐㾫䏒䡢䭏便偏匾囨媥平徧惼扁揙楄楩煸片牑犏猵碥箯篇編緶缏编翩艑萹蝙褊覑諞谝貵蹁遍鍽鞭頨騗騙骗魸鯾鯿鳊鶣',
	'폄':'砭窆貶贬',
	'평':'㛁㺸䍬䓑䦕匉呯坪姘岼平怦抨拼枰泙玶硼胓苹萍蓱蚲評评閛駍鮃鲆',
	'폐':'㙄㡀㢢㯇㾱䉬䕠䠘䯗吠嬖幣幤废廃廢弊敝斃杮梐櫠毙狴獘獙癈砩箅肺蔽蕟薜蜌鄨鐾閇閉闭陛髀鼣',
	'포':'㘵㚴㚿㫧㬥㬧㯡㲒㳍䈬䈻䊇䍖䎂䔕䛌䝵䤖䩝䫽䭋䮒䶌佈佨儤刨勹包匍匏咆咘哺圃圑垉埔奅孢宲峬布庖庯忁怉怖悑抛抪抱拋捕晡暴曓曝枹柨泡浦瀑炮炰爮狍瓝疱皰砲礟礮笣胞脬脯舖舗苞菢萢葡蒱蒲虣蚫蜅袌袍裦褒褜襃誧謈跑軳逋酺鈽鉋鋪鑤钸铇铺闁陠靤鞄飽餔饱髱鮑鯆鲍鵏麃麅麭齙龅暴',
	'폭':'䋹䌿幅暴曝瀑爆輻輻',
	'폴':'乶',
	'폿':'喸',
	'퐁':'乓',
	'표':'㘐㟽㠒㧼㬓㯱㯹㲏㵱㶾㹾㼼䁃䁭䅺䏇䔸䕯䙳䞄䮽䱪䴩䶂俵僄儦剽勡嘌墂婊嫖幖彪彯徱慓摽旚杓标標檦殍淲滮漂瀌熛燢爂犥猋瓢瘭皫瞟磦票穮篻縹缥翲脿膘臕莩蔈薸藨螵表裱褾諘謤豹贆醥錶鏢鑣镖镳闝顠颩颷飃飄飆飇飈飊飘飙飚驃驫骉骠髟魒鰾鳔',
	'푸':'䬌',
	'푼':'分',
	'품':'品榀禀稟',
	'풍':'㐽㒥㠦䏎䵄偑僼冯凨凬凮堸寷枫栤楓檒沣沨渢灃煈猦疯瘋砜碸葑蘴諷讽豊豐鄷酆闏霻靊風颪飌风馮麷',
	'피':'㓟㗪㢰㨢㯅㱟䏢䏶䙓佊僻帔彼怶披旇柀氕犤狓疲皮秛紴罷翍耚藣被襬詖诐貏貱跛辟避鈹銔铍陂鞁骳髲鮍鲏',
	'픽':'煏腷',
	'필':'㓖㢶㢸㪤㮿㳼㻫㻶䄶䏘䖩䟆䩛䫾䬛䮡佖佛匹吡咇哔嗶妼弻弼彃必怭払拂榓毕泌滗滭潷熚珌畢疋笔筆筚篳縪罼胇苉苾荜蓽虑袐襅觱跸蹕邲鉍鏎铋鞸韠飶饆馝駜驆魓鮅鴄鵯鷝鹎',
	'핍':'乏偪姂愊逼鴔',
	'하':'㗇㗿㙈㙤㰤㰺㵑䠍䪗䫗丅下丷何假厦呀哧哬嗬嘏嚇圷夏夓岈廈懗抲昰河煆瑕疜瘕睱碋碬緞縀罅芐荷菏蕸虾蝦袔諕谺賀贺赮遐鍜鎼鏬閕閜霞鞐颬騢鰕',
	'학':'㕡㕰㰒㶅㿥䅂䖈䖋䤕䨋䮤䳽嗀嗃嚛嚯壆壑奭学學峃嶨斈涸澩狢疟瘧癋皬矐确硸翯虐蠚觷謔謞谑貈郝雤靏鴬鶮鶴鷽鸖鸴鹤鶴',
	'한':'㒏㛠㡾㢨㪋㯗㲦㵄㸁䁂䂅䈨䉯䍐䍑䎯䏷䓍䓳䕿䗙䛞䥜䦘䦥䮧仠佷傼僩僴兯厂哻垾娨娴嫨嫺嫻寒屽恨悍憪扞捍撊旱晘暵桿橌橺汉汗浫漢澖澣瀚焊狠猂皔瞷罕翰蓒蔊蛝螒覵豻貋邗邯釬銲閈閑閒闬闲限雗韓韩駻骭鶾鷳鷴鷼鹇麲鼾',
	'할':'㔛㔠㝬㪴㮫㿣䕣䕸䦖䦪䫘䶤乤傄割劼嗐害搳瞎硈磍縖舝螛轄辖鎋韔鶷',
	'함':'㓧㖤㘅㘎㘚㛾㟏㟔㤷㨔㮭㯺㰹㴠㶰㺖㺝㼨㽉䈄䎏䐄䓿䕔䖔䘖䘶䟰䣻䤴䥁䧟䨡䩂䫲䱤䲗䶃䶟䶠䶢函凾含咸唅啣喊圅壏娢晗梒槛檻欦浛涵淊澏濫焓琀甉筨糮緘缄臽舰艦莟菡蛿蜬蜭衔衘諴譀谽豃豏輱轞邯醎銜鋡錎闞阚陥陷顄顑餡馅馠鬫魽鰔鹹',
	'합':'㘡㝓㥺㭘㰰䆟䖎䖖䛅䢔䧻䶎佮匌合呷哈嗑峆峇廅敮柙榼欱溘烚熆珨盇盍盒盖秴篕粭翈耠蓋蛤詥郃閤闔阖陕陜頜颌魻鮯鴿鸽',
	'항':'㔰㟟㤚㰠䀪䁰䘕䜶䟘䢽䣈䲳亢伉佭佷吭塂夯姮嫦岲巷恆恒抗斻杭栙桁沆港炕笐缸缿罁肛肮航苀蚢行衖貥跭迒邟酐鈧钪閌闀闂闶降項頏项颃骯鬨魧行降',
	'해':'㒠㗨㙰㚊㜾㞒㤥㧡㰡㰧㰩㱼㾂㾬䀭䇋䉏䚸䠹䠽䡡䦏䪥䯐䱺䲒亥侅偕劾咍咳嗐嗨垓塰夥奚妎姟孩害峐嶰廨慀懈晐楷檞欬氦海澥瀣獬瑎畡痎絯繲胲膎荄薢薤蟹蠏觟解觧該諧该谐豥賅賌赅輆邂郋酼醢陔韰頦颏餀饚駭駴骇骸鮭鲑龤',
	'핵':'䃒劾势栶核翮覈輅',
	'행':'㓑㼬䁄䂔䓷䛭䯒䰢倖哘啈垳堼婞幸悻杏洐涬烆筕絎緈绗胻荇莕行裄鴴鵆鸻﨨',
	'향':'㕿㗽㴡㿝䅨䊑䖮䦭䦳乡享亯向响嚮姠晑曏楿珦稥膷芗萫薌蚃蠁郷鄉鄊鄕銄響飨餉饗饷香鱜麘黁',
	'허':'㞰㠊䔓嘘噓墟憈栩歔浒虗虚虛許许鄦驉魖魼',
	'헌':'㦥䆭䘆䜢䧮仚佡宪巘巚幰憲搟攇櫶瀗献獻軒轩',
	'헐':'歇滊',
	'험':'㷿㸝㿌姭崄嶮忺杴榃猃獫玁硷礆譣险険險騐験驗验',
	'혀':'暳',
	'혁':'㤸㦦㬨㮝㷜㷦䓇䚂䚫䦗䱛䵱伵侐吓嚇奕弈捇殈洫焃焱煂爀盢瞁虩衋覤赥赩赫趘阋革鬩',
	'현':'㘋㡉㢺㧋㧦㫫㬎㭹㹡㻹䀏䍗䏹䗾䚯䛹䝨䝮䥪䧋䧎䩙䮄䲻伣伭俔儇县吅呟咞哯垷埍妶娊娹婱嬛岘峴弦弲怰悬惤懸敻昡显晛梋泫洵灦炫玄现玹現琄痃県眩睍矎礥絃絢縣繯绚缳翾胘臔臤舷苋莧虤蚬蚿蜆蠉衒袨見訮詪詽誢誸譞讂賢贒贙贤鉉鋗鋧鑦铉鞙韅顕顯駽見',
	'혈':'㐖䆝䆷䋉䐼䒸䕵䙽䛎䦑䦧䩤䩧䫼吷坹奊娎孑岤桖泬烕疦穴絜緳茓蝢血裇趐頁页',
	'혐':'㺌㽐㾾䵌嫌馦',
	'협':'㙝㛍㢵㤲㥦㥷㮉㶸㼪㽠㾜㿓䁋䇲䏩䏮䕛䝱䬅䶝侠俠冾劦勰匧协協叶嗋垥埉夹夾峡峽恊悏惬愜愶慊拹挟挾旪梜浃浹熁燲狭狹硖硤祫筴箧篋綊胁脅脇脋脥荚莢蛱蛺鉿鋏铗铪陜陿鞈頬頰颊餄饸',
	'형':'㐩㓝㚾㢠㣜㭢㯏㺾㼆㼛䅽䚘䢛䣆䤯䤰䳙亨侀兄刑哼坓型夐娙嵤形悙擤桁泂泶浻涥滎滢潆瀅瀠灐炯熒營玹珩瑩硎脝荆荊荥荧萤蓥藀蘅蛍蛵螢衡褮詗诇賯迥逈邢郉鉶鋞鎣铏陉陘馨鶑',
	'혜':'㚛㜎㥣㨙㩨㬩㰥㰿㿽䎚䒊䙎䚷䛊䜁䤈䧥䫣䲪偕傒僡儶兮匸嘒嚖嚡寭嵆嵇彗徯忚恵惠慧憓懳暳榽槥橀橞櫘潓璤盻蒵蕙螇蟪謑譓譿豀豯蹊醯鏸鞋鞵韢騱鼷',
	'호':'㕆㗅㙱㚏㚪㚼㝀㞻㠙㣗㦆㦿㨭㩝㬔㬶㯛㵆㸦㾰䇘䉿䊀䊺䋀䋆䎁䐧䒵䕶䗂䚽䜰䝞䝥䠒䤣䧚䧫䨼䩴䪽䭌䭍䯫䰧䴣乊乎乕互傐儫冱冴号吳呉呺呼哠唬喖嗥嘑嘷噑嚎垀壕壶壷壺壼夰好媩嫭嫮岵峼帍弖弧怙恏悎戶户戸戽扈护摢昈昊昦晧暠暤暭曍枑枦椃楜槴歑毫沍沪泘浩淏湖滈滬滸滹澔濠濩瀥灏灝烀煳熩犒狐猢猲獆獋獔琥瑚瓠瓳皐皓皜皞皡皥祜穫箎箶簄籇粐糊綔縞缟聕胡舮芦苸萀葫蒿蔰薃薅藃虍虎虖虝號蝴蠔衚許謼護譹豪軤轷鄗鄠醐鈩錿鍸鎬镐雇雐雽頀顥颢餬鬍魱鯱鰗鰝鳸鶘鶦鹕',
	'혹':'㦯㷤㺉㽇䞱惑或掝熇豰酷鍙閄頶鵠',
	'혼':'㑮㖧㛰㮯㱪䅙䊐䎜䐊䚠䛰䡣䧰䮝䰟䴷倱圂堚婚婫忶惛惽挥掍昆昏昬棍棔殙浑涽混渾溷焜焝珲琿睧睯緷繉觨閽阍餛馄魂鯇鯶鼲',
	'홀':'㖴㧮㧾㨡㳷㺀䁫䓤䝆䨚䩐䬍䴯乥匢匫唿啒囫寣忽惚曶核笏絗芴鍃锪',
	'홍':'㖓㙆㬴㶹䀧䂫䃔䆪䉺䜫䞑䧆䨎䪦䫹䲨仜叿哄唝嗊垬妅娂屸弘晎汞泓洚洪渱潂澒灴烘焢硔篊粠紅红苰荭葒葓蕻虹訌讧谼谾鉷銾閧霐霟鬨魟鴻鸿',
	'화':'㕦㗾㟆㠏㦊㭉㳸㶡䄀䅿䒩䔢䛡伙俰划化华吙吳呉咊和哗啝嘩埖墷夻姀婲嬅崈崋惒摦擭旤杹枠柇桦椛楇槬樺沎澕火灬璍画畫畵盉硴祸禍禾竵糀舙花芲華萂蕐訸話誮譁譮话貨货邩釫鈥鉌錵鏵钬铧靴鞾驊骅髁魤鱯鳠鷨龢',
	'확':'㠛㦜㨯㬑㬦㸕㺢䁨䂄䈅䉟䨥劐嬳廓彉彍彏彟彠戄扩拡挄擴攉攫曤檴爴獲玃瓁矆矍矡矱確碻礭穫篗籆籰耯臒臛艧蒦蠖貜鑊镬雘霩靃鸌鹱廓',
	'환':'㕕㛟㞍㡲㪱㬇㬊㶎㹕㹖㿪䀓䁵䆠䍺䒛䒯䗭䚪䜨䝔䝠䠉䦡䭴䯘䴉䴋䴟丸亘唤喚喛嚾圜奂奐宦寏寰峘幻弮患愌懁懽换換擐攌晥暅桓梙槵欢歓歡汍涣渙湲漶澴烉焕煥犱獾瑍環瓛癏皖眩睅睆瞣笂糫紈絙綄纨羦肒芄荁萈萟藧讙豢貛轘还逭還酄釻鋎鍰鐶锾镮闤阛雈驩鬟鯇鰀鰥鱞鲩鳏鴅鵍鹮',
	'활':'㓉㕲㵈䀨䄆䄑䦢䱻䴳咶奯姡敌活滑濶猾眓磆秮秳萿蛞螖豁越趏闊阔',
	'황':'㠩㠵㡃㡆㡛㣴㤺㨪㬻㵁㶂㾮䀮䁜䄓䅣䊗䊣䌙䍿䐠䐵䑟䞹䪄䮲䳨偟兤况凰喤堭塃墴奛媓宺崲巟幌徨怳恍惶惺愰慌揘晃晄曂朚楻榥櫎況湟滉潢炾煌熿獚瑝璜癀皇皝皩眖礦穔篁簧縨肓艎荒葟蝗蟥衁詤諻謊谎貺贶趪軦遑鎤隍韹餭騜鰉鱑鳇鷬黃黄',
	'홰':'哕噦噧澅翙翽',
	'회':'㑹㒑㜳㞀㞧㠢㣛㧟㨤㱱㷄㷇㻅㾯䕇䖶䛛䜋䝅䝇䢈䤧䩈䫭䭝䴜䵳会佪刽劊匯咴囘回囬壞嬒屷廻廽徊恛恢悔懐懷拻擓敼晦會杤栃桧樑檜櫰洃洄浍淮湏滙澮瀤灰烣烩烸燴狯獪璯痐盔瞺硘禬絵繪绘耲脍膾茴荟薈藱蘹蚘蛔蛕蜖螝褢褱詯詼誨諙诙诲豗賄贿迴逥郐鄶鐬靧頮颒鮰鱠鲙',
	'획':'㓰㖪㗲㦎㩇䐸䦝䪝䬉劃咟嚄嚿婳嫿撶湱獲画畫畵砉窢繣获謋謢讗韄騞',
	'횡':'㢬㶇䍔䎕䫺䬖䬝吰嚝宖峵彋揈撔横橫澋竑紭薨衡谹輷鈜鋐鐄鑅黉黌',
	'효':'㕺㚠㤊㩭㫴㭳㮁㵿㹲㺧䂚䉰䋂䒝䓔䕧䖀䥵䫞䬘侾俲倄傚効呺哓哮啋嗃嘋嘵嚆嚣嚻囂婋孝宯崤庨憢撬效敩斅斆晓暁曉枭枵校梟歊殽毊洨涍淆滧灱灲烋熇爻猇獢痚皛皢硣穘窙笅筊肴胶膮藠虈虓訤詨誟誵郩酵顤餚驍驕骁髇髐鴞鸮﨧',
	'후':'㖃㗋㗜㢿㤧㫗㬋㮢㰭㱙㴟㷞㸸㺅㻈㽳䂉䏏䖉䗔䙈䞀䞧䣱䣴䧁䫛䳧侯候冔厚后吼吽呍喉喣嗅嘔垕堠姁帿後朽洉涸煦犼猤猴珛珝疞瘊睺矦篌糇翭翵芋葔蝴螑詡譃诩豞逅郈鄇酗銗鍭餱骺鮜鯸鱟鲎鲘齁齅',
	'훈':'䌲䗼䙧䠝䵫勋勛勲勳嚑坃埙塤壎壦晕暈曛焄煇熏燻爋獯瞓矄纁臐荤葷蔒薫薰蘍訓训醺鑂馴',
	'훌':'㗵欻歘烼魆',
	'훙':'薨顭',
	'훤':'㓩䁔䚙䚭吅咺喧嚾媗愋昍晅暄暖楦烜煊狟睻禤箮翧萱萲蕿藼蘐蝖諠諼讙谖貆',
	'훨':'䎀',
	'훼':'㑰㩓㷐䂕䃣䛼卉喙檓毀毁毇燬芔虫虺譭顪餯',
	'휘':'㧑㩣㫎㭏㹆㺔䘗媈幑彙彚徽戯戱揮撝晖暉椲楎汇泋瀈灳煇禈翚翬諱讳輝辉鰴麾',
	'휭':'遤',
	'휴':'㔒㥟㩗㩦㱗㳜㵻㹯㽯䏫䝗䮌䰍亏休倠儶咻嘼堕婎孈巂庥携擕攜烋烌瓗畦眭睳茠蘳虧蠵觹觽觿貅貕酅銝鑴隓隳雟飍驨髤髹鮴鵂鸺',
	'휵':'䛙慉搐槒畜',
	'휼':'㤜㳚䎉䘏䢕䬄卹恤憰烅獝瞲肷譎谲賉遹鐍霱鷸鹬',
	'흉':'㐫㓙㕳㕼䠗兇凶匈哅忷恟汹洶胷胸訩詾讻',
	'흑':'㱄潶釛黑黒',
	'흔':'㥵㯊㾙䜣俒俽妡庍很忻惞慁拫掀昕欣炘焮煡琿痕盺脪舋衅訢邤釁鍁锨鞎',
	'흘':'㐹䇄䏌䢀䬣仡吃屹忔扢汔汽疙籺紇纥肐虼訖讫趷迄釳鷸麧齕龁',
	'흠':'㐸䜗噷嬜廞揿撳欠欽歆鑫钦',
	'흡':'㒆㡊㩉㪧㬛㲸㽏䁯䞩䨐䶋吸噏恰歙洽潝熻翕翖闟',
	'흥':'㒷䕟兴匈嬹臖興馫',
	'희':'㑶㙿㚀㚦㜯㝆㠻㩬㬢㰕㰨㱆㶊㷗㷩㸍㹷㺣䂀䊠䐅䖒䖷䛥䨳䮎俙僖凞呬咥唏喜嘻噫嚱囍姫姬嬉屃屓屭巇希忥怬悕愾憘憙戏戯戱戲晞暿曦桸橲欷歖浠烯焁焈煕熂熈熙熹熺燨燹爔牺犔犠犧狶琋睎瞦礂禧稀繥羲莃蟢誒譆诶豨豷釐隵霼餙餼饎饩鯑鱚鵗齂凞',
	'히':'㕧䐖䦙呬忾',
	'힐':'㩪恄撷擷欯犵纈缬翓肸肹襭詰诘頡颉黠'
}
