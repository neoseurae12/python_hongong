# urllib 모듈

# 모듈 읽어들이기
from urllib import request

# urlopen() 함수 => 구글의 메인 페이지 읽기
target = request.urlopen("https://google.com")
output = target.read()

# 출력
print(output)


'''
b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; 
charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" 
itemprop="image"><title>Google</title><script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){window.google={kEI:\'fizRYqG1D4WI-AaN9oeoAg\',
kEXPI:\'0,1302536,56873,6058,207,4804,2316,383,246,5,1354,4013,1123753,1197732,380759,16114,17444,11240,17572,4858,1362,9290,3021,17588,
4020,978,13227,3848,10622,14762,7979,5081,885,708,1279,2451,291,149,1103,840,1986,4311,3514,606,2023,2299,6340,8328,3227,2845,7,17450,16320,
1851,2614,3901,9241,3,346,230,6460,148,13975,4,1528,2304,7039,25073,2658,4163,3192,13660,4437,16786,5800,2557,4097,4049,3,3541,1,42154,2,
14022,14116,11623,5679,1021,2380,2719,18260,2,6,7755,4567,6259,23418,830,422,5835,12137,2831,4332,19,6071,1394,445,2,2,1,6959,3831,13836,
2006,8155,6582,799,3043,858,10779,2162,5179,2651,11806,5,1922,4740,966,3463,610,23,5416,1449,1278,1663,1,2585,3309,1495,4560,1942,702,
6040,859,4832,37,1282,3523,1111,158,431,17,298,1078,284,367,511,731,2913,283,2148,308,278,273,978,6,123,415,285,4,1,2,2,2,2,1385,1491,
2523,73,482,878,15,82,924,18,1808,290,76,467,1089,3522,2415,137,585,2,1588,10,4,581,56,10,212,3,701,2,98,130,71,493,252,755,1056,313,
1288,75,322,3,208,6,2290,349,5386947,150,9,8799633,3311,141,795,19735,1,1,346,427,3,2,259,1,3,2,2,2,1,3,4,1,8,2,2,1,3,56,56,2,23949645,
4042142,1964,2935,159,1358,965,11256,3405,5477,1382288\',kBL:\'ecaJ\'};google.sn=\'webhp\';google.kHL=\'ko\';})();(function(){\nvar 
f=this||self;var h,k=[];function l(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||h}
function m(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}\nfunction n(a,b,c,d,g)
{var e="";c||-1!==b.search("&ei=")||(e="&ei="+l(d),-1===b.search("&lei=")&&(d=m(d))&&(e+="&lei="+d));d="";!c&&f._cshid&&-1===b.search("&cshid=")
&&"slh"!==a&&(d="&cshid="+f._cshid);c=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+"&zx="+Date.now()+d;/^http:/i.test(c)&&"https:"===
window.location.protocol&&(google.ml&&google.ml(Error("a"),!1,{src:c,glmm:1}),c="");return c};h=google.kEI;google.getEI=l;google.getLEI=m;
google.ml=function(){return null};google.log=function(a,b,c,d,g){if(c=n(a,b,c,d,g)){a=new Image;var e=k.length;k[e]=a;a.onerror=a.onload=
a.onabort=function(){delete k[e]};a.src=c}};google.logUrl=n;}).call(this);(function(){\ngoogle.y={};google.sy=[];google.x=function(a,b)
{if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.sx=function(a){google.sy.push(a)};google.lm=
[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.
loadAll=function(a,b){google.lq.push([a,b])};google.bx=!1;google.lx=function(){};}).call(this);google.f={};(function(){\ndocument.
documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"===c||"q"===
c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",
function(b){var a;a:{for(a=b.target;a&&a!==document.documentElement;a=a.parentElement)if("A"===a.tagName){a="1"===a.getAttribute("data-nohref");
break a}a=!1}a&&b.preventDefault()},!0);}).call(this);</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}
#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;
# top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline 
# !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,
# .h{font-family:&#44404;&#47548;,&#46027;&#50880;,arial,sans-serif}.ko{font-size:9pt}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}
# td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#1558d6}em{font-weight:bold;font-style:normal}.lst
# {height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;
# margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#4b11a8;text-decoration:none}a:hover,
# a:active{text-decoration:underline}.fl a{color:#1558d6}a:visited{color:#4b11a8}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;
# margin-left:13px;font-size:11px}.lsbb{background:#f8f9fa;border:solid 1px;border-color:#dadce0 #70757a #70757a #dadce0;height:30px}.
# lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;
# color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#dadce0}.lst:
# focus{outline:none}.tiah{width:458px}</style><script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){window.google.erd={jsr:1,bv:1616,de:true};
# \nvar f=this||self;var g,h=null!=(g=f.mei)?g:1,m,n=null!=(m=f.sdo)?m:!0,p=0,q,r=google.erd,u=r.jsr;google.ml=function(a,b,d,k,c)
# {c=void 0===c?2:c;b&&(q=a&&a.message);if(google.dl)return google.dl(a,c,d),null;if(0>u){window.console&&console.error(a,d);if(-2===u)throw a;
# b=!1}else b=!a||!a.message||"Error loading script"===a.message||p>=h&&!k?!1:!0;if(!b)return null;p++;d=d||{};var e=c;c=encodeURIComponent;b="/
# gen_204?atyp=i&ei="+c(google.kEI);google.kEXPI&&(b+="&jexpid="+c(google.kEXPI));b+="&srcpg="+c(google.sn)+"&jsr="+c(r.jsr)+"&bver="+c(r.bv)+
# ("&jsel="+e);e=a.lineNumber;void 0!==e&&(b+="&line="+\ne);var l=a.fileName;l&&(b+="&script="+c(l),e&&l===window.location.href&&(e=document.
# documentElement.outerHTML.split("\\n")[e],b+="&cad="+c(e?e.substring(0,300):"No script found.")));for(var t in d)b+="&",b+=c(t),b+="=",b+=c(d[t]);
# b=b+"&emsg="+c(a.name+": "+a.message);b=b+"&jsst="+c(a.stack||"N/A");12288<=b.length&&(b=b.substr(0,12288));a=b;k||google.log(0,"",a);return a};
# window.onerror=function(a,b,d,k,c){q!==a&&(a=c instanceof Error?c:Error(a),void 0===d||"lineNumber"in a||(a.lineNumber=d),void 0===b||
# "fileName"in a||(a.fileName=b),google.ml(a,!1,void 0,!1,"SyntaxError"===a.name||"SyntaxError"===a.message.substring(0,11)||0<a.message.
# indexOf("Script error")?2:0));q=null;n&&p>=h&&(window.onerror=null)};})();</script></head><body bgcolor="#fff"><script nonce="gdiVx2wPqPP-
# JGhbn1s68g">(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();
# if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();
# </script><div id="mngb"><div id=gbar><nobr><b class=gb1>&#44160;&#49353;</b> <a class=gb1 href="https://www.google.co.kr/imghp?hl=ko&tab=wi">
# &#51060;&#48120;&#51648;</a> <a class=gb1 href="https://maps.google.co.kr/maps?hl=ko&tab=wl">&#51648;&#46020;</a> <a class=gb1 
# href="https://play.google.com/?hl=ko&tab=w8">Play</a> <a class=gb1 href="https://www.youtube.com/?gl=KR&tab=w1">YouTube</a> <a class=gb1 
# href="https://news.google.com/?tab=wn">&#45684;&#49828;</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> 
# <a class=gb1 href="https://drive.google.com/?tab=wo">&#46300;&#46972;&#51060;&#48652;</a> <a class=gb1 style="text-decoration:none" 
# href="https://www.google.co.kr/intl/ko/about/products?tab=wh"><u>&#45908;&#48372;&#44592;</u> &raquo;</a></nobr></div><div id=guser 
# width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a 
# href="http://www.google.co.kr/history/optout?hl=ko" class=gb4>&#50937; &#44592;&#47197;</a> | <a  href="/preferences?hl=ko" 
# class=gb4>&#49444;&#51221;</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=ko&passive=true&continue=https://
# www.google.com/&ec=GAZAAQ" class=gb4>&#47196;&#44536;&#51064;</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0>
# </div></div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" 
# src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo">
# <br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td 
# align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="ko" name="hl" type="hidden"><input name="source" 
# type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0">
# <div style="position:relative;zoom:1"><input class="lst tiah" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000;padding-right
# :38px" autocomplete="off" value="" title="Google &#44160;&#49353;" maxlength="2048" name="q" size="57"><img src="/textinputassistant/tia.png" 
# style="position:absolute;cursor:pointer;right:5px;top:4px;z-index:300" data-script-url="/textinputassistant/11/ko_tia.js" id="tsuid1" alt="" 
# height="23" width="27"><script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){var id=\'tsuid1\';document.getElementById(id).onclick = function()
# {var s = document.createElement(\'script\');s.src = this.getAttribute(\'data-script-url\');(document.getElementById(\'xjsc\')||
# document.body).appendChild(s);};})();</script></div></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" 
# value="Google &#44160;&#49353;" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid2" 
# value="I&#8217;m Feeling Lucky" name="btnI" type="submit"><script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){var id=\'tsuid2\';document.
# getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}\nelse 
# top.location=\'/doodles/\';};})();</script><input value="AJiK0e8AAAAAYtE6jkIWu39jq0_f_b2do6MbEp-0FU4G" name="iflsig" type="hidden"></span>
# </span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=ko&amp;authuser=0">
&#44256;&#44553;&#44160;&#49353;</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="gdiVx2wPqPP-JGhbn1s68g">
(function(){\nvar a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject)
{var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="WqQANb"><a href="/intl/ko/ads/">&#44305;&#44256; &#54532;&#47196;&#44536;&#47016;</a><a href="http://www.google.co.kr/intl/ko/services/">&#48708;&#51592;&#45768;&#49828; &#49556;&#47336;&#49496;</a><a href="/intl/ko/about.html">Google &#51221;&#48372;</a><a href="https://www.google.com/setprefdomain?prefdom=KR&amp;prev=https://www.google.co.kr/&amp;sig=K_-X98ZoOyV0cxP7D7TRZjUjtRqHY%3D">Google.co.kr</a></div></div><p style="font-size:8pt;color:#70757a">&copy; 2022 - <a href="/intl/ko/policies/privacy/">&#44060;&#51064;&#51221;&#48372;&#52376;&#47532;&#48169;&#52840;</a> - <a href="/intl/ko/policies/terms/">&#50557;&#44288;</a></p></span></center><script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){window.google.cdo={height:757,width:1440};(function(){\nvar a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();</script> <script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){google.xjs={ck:\'xjs.hp.0ZdZ9Q3uqrw.L.X.O\',cs:\'ACT90oHy4Z_9pyHHelHHDTNWhYMuP6DgJw\',excm:[]};})();</script>  <script nonce="gdiVx2wPqPP-JGhbn1s68g">(function(){var u=\'/xjs/_/js/k\\x3dxjs.hp.en.Ob9ZD00ZUx4.O/am\\x3dAMATAIAEQAI/d\\x3d1/ed\\x3d1/rs\\x3dACT90oE4myh1DULgKPtdN-NWkiN-VjDJsQ/m\\x3dsb_he,d\';\nvar d=this||self,e=function(a){return a};var g;var l=function(a,b){this.g=b===h?a:""};l.prototype.toString=function(){return this.g+""};var h={};\nfunction n(){var a=u;google.lx=function(){p(a);google.lx=function(){}};google.bx||google.lx()}\nfunction p(a){google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");var b=document;var c="SCRIPT";"application/xhtml+xml"===b.contentType&&(c=c.toLowerCase());c=b.createElement(c);if(void 0===g){b=null;var k=d.trustedTypes;if(k&&k.createPolicy){try{b=k.createPolicy("goog#html",{createHTML:e,createScript:e,createScriptURL:e})}catch(q){d.console&&d.console.error(q.message)}g=b}else g=b}a=(b=g)?b.createScriptURL(a):a;a=new l(a,h);c.src=a instanceof l&&a.constructor===l?a.g:"type_error:TrustedResourceUrl";var f,m;(f=(a=null==(m=(f=(c.ownerDocument&&c.ownerDocument.defaultView||window).document).querySelector)?void 0:m.call(f,"script[nonce]"))?a.nonce||a.getAttribute("nonce")||"":"")&&c.setAttribute("nonce",f);document.body.appendChild(c);google.psa=!0};google.xjsu=u;setTimeout(function(){n()},0);})();function _DumpException(e){throw e;}\nfunction _F_installCss(c){}\n(function(){google.jl={attn:false,blt:\'none\',chnk:0,dw:false,dwu:true,emtn:0,end:0,ine:false,injs:\'none\',injt:0,injth:0,injv2:false,lls:\'default\',pdt:0,rep:0,snet:true,strt:0,ubm:false,uwp:true};})();(function(){var pmc=\'{\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:true,\\x22cgen\\x22:true,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22dhqt\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22ffql\\x22:\\x22ko\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22isbh\\x22:28,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22&#44160;&#49353;&#50612; &#51648;&#50864;&#44592;\\x22,\\x22dym\\x22:\\x22&#51060;&#44163;&#51012; &#52286;&#51004;&#49512;&#45208;&#50836;?\\x22,\\x22lcky\\x22:\\x22I&#8217;m Feeling Lucky\\x22,\\x22lml\\x22:\\x22&#51088;&#49464;&#55176; &#50508;&#50500;&#48372;&#44592;\\x22,\\x22oskt\\x22:\\x22&#51077;&#47141; &#46020;&#44396;\\x22,\\x22psrc\\x22:\\x22&#44160;&#49353;&#50612;&#44032; \\\\u003Ca href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003E&#50937; &#44592;&#47197;\\\\u003C/a\\\\u003E&#50640;&#49436; &#49325;&#51228;&#46104;&#50632;&#49845;&#45768;&#45796;.\\x22,\\x22psrl\\x22:\\x22&#49325;&#51228;\\x22,\\x22sbit\\x22:\\x22&#51060;&#48120;&#51648;&#47196; &#44160;&#49353;\\x22,\\x22srch\\x22:\\x22Google &#44160;&#49353;\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22refpd\\x22:true,\\x22rfs\\x22:[],\\x22sbas\\x22:\\x220 3px 8px 0 rgba(0,0,0,0.2),0 0 0 1px rgba(0,0,0,0.08)\\x22,\\x22sbpl\\x22:16,\\x22sbpr\\x22:16,\\x22scd\\x22:10,\\x22stok\\x22:\\x22CCWoMjCeIEKly0L6-IVDsPZqHpQ\\x22,\\x22uhde\\x22:false}}\';google.pmc=JSON.parse(pmc);})();</script>        </body></html>'
'''