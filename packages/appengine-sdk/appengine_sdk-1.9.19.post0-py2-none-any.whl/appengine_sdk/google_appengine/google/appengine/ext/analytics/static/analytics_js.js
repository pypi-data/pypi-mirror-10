/* Copyright 2008-9 Google Inc. All Rights Reserved. */ (function(){var l,m=this,n=function(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b},p=function(a){return"string"==typeof a},r=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}},aa=Date.now||function(){return+new Date},u=function(a,b){var c=a.split("."),d=m;c[0]in d||!d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)c.length||void 0===b?d=d[e]?d[e]:d[e]={}:d[e]=b},v=function(a,b){function c(){}
c.prototype=b.prototype;a.p=b.prototype;a.prototype=new c;a.s=function(a,c,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[c].apply(a,g)}};var w=function(a){if(Error.captureStackTrace)Error.captureStackTrace(this,w);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))};v(w,Error);var ba=function(a,b){for(var c=a.split("%s"),d="",e=Array.prototype.slice.call(arguments,1);e.length&&1<c.length;)d+=c.shift()+e.shift();return d+c.join("%s")},x=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,"")},y=function(a){a=String(a);var b=a.indexOf(".");-1==b&&(b=a.length);b=Math.max(0,2-b);return Array(b+1).join("0")+a},z=function(a,b){return a<b?-1:a>b?1:0};var A=function(a,b){b.unshift(a);w.call(this,ba.apply(null,b));b.shift()};v(A,w);var B=function(a,b,c){if(!a){var d="Assertion failed";if(b)var d=d+(": "+b),e=Array.prototype.slice.call(arguments,2);throw new A(""+d,e||[]);}};var D=Array.prototype,E=D.indexOf?function(a,b,c){B(null!=a.length);return D.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;if(p(a))return p(b)&&1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},ca=D.forEach?function(a,b,c){B(null!=a.length);D.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=p(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},da=D.filter?function(a,b,c){B(null!=a.length);return D.filter.call(a,b,
c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g=p(a)?a.split(""):a,h=0;h<d;h++)if(h in g){var t=g[h];b.call(c,t,h,a)&&(e[f++]=t)}return e},ea=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]},F=function(a,b,c){B(null!=a.length);return 2>=arguments.length?D.slice.call(a,b):D.slice.call(a,b,c)};var G=function(a){var b=arguments.length;if(1==b&&"array"==n(arguments[0]))return G.apply(null,arguments[0]);for(var c={},d=0;d<b;d++)c[arguments[d]]=!0;return c};G("area base br col command embed hr img input keygen link meta param source track wbr".split(" "));var H;a:{var I=m.navigator;if(I){var fa=I.userAgent;if(fa){H=fa;break a}}H=""};var J=function(){return-1!=H.indexOf("Edge")};var ga=-1!=H.indexOf("Opera")||-1!=H.indexOf("OPR"),K=-1!=H.indexOf("Edge")||-1!=H.indexOf("Trident")||-1!=H.indexOf("MSIE"),L=-1!=H.indexOf("Gecko")&&!(-1!=H.toLowerCase().indexOf("webkit")&&!J())&&!(-1!=H.indexOf("Trident")||-1!=H.indexOf("MSIE"))&&!J(),M=-1!=H.toLowerCase().indexOf("webkit")&&!J(),ha=function(){var a=H;if(L)return/rv\:([^\);]+)(\)|;)/.exec(a);if(K&&J())return/Edge\/([\d\.]+)/.exec(a);if(K)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(M)return/WebKit\/(\S+)/.exec(a)},ia=function(){var a=
m.document;return a?a.documentMode:void 0},ja=function(){if(ga&&m.opera){var a=m.opera.version;return"function"==n(a)?a():a}var a="",b=ha();b&&(a=b?b[1]:"");return K&&!J()&&(b=ia(),b>parseFloat(a))?String(b):a}(),ka={},N=function(a){var b;if(!(b=ka[a])){b=0;for(var c=x(String(ja)).split("."),d=x(String(a)).split("."),e=Math.max(c.length,d.length),f=0;0==b&&f<e;f++){var g=c[f]||"",h=d[f]||"",t=RegExp("(\\d*)(\\D*)","g"),q=RegExp("(\\d*)(\\D*)","g");do{var k=t.exec(g)||["","",""],C=q.exec(h)||["","",
""];if(0==k[0].length&&0==C[0].length)break;b=z(0==k[1].length?0:parseInt(k[1],10),0==C[1].length?0:parseInt(C[1],10))||z(0==k[2].length,0==C[2].length)||z(k[2],C[2])}while(0==b)}b=ka[a]=0<=b}return b},la=m.document,ma=ia(),na=!la||!K||!ma&&J()?void 0:ma||("CSS1Compat"==la.compatMode?parseInt(ja,10):5);!L&&!K||K&&K&&(J()||9<=na)||L&&N("1.9.1");K&&N("9");var O=function(a,b,c){var d=document;c=c||d;var e=a&&"*"!=a?a.toUpperCase():"";if(c.querySelectorAll&&c.querySelector&&(e||b))return c.querySelectorAll(e+(b?"."+b:""));if(b&&c.getElementsByClassName){a=c.getElementsByClassName(b);if(e){c={};for(var f=d=0,g;g=a[f];f++)e==g.nodeName&&(c[d++]=g);c.length=d;return c}return a}a=c.getElementsByTagName(e||"*");if(b){c={};for(f=d=0;g=a[f];f++){var e=g.className,h;if(h="function"==typeof e.split)h=0<=E(e.split(/\s+/),b);h&&(c[d++]=g)}c.length=d;return c}return a};var oa=function(a){a=a.className;return p(a)&&a.match(/\S+/g)||[]},pa=function(a,b){for(var c=oa(a),d=F(arguments,1),e=c,f=0;f<d.length;f++)0<=E(e,d[f])||e.push(d[f]);c=c.join(" ");a.className=c},ra=function(a,b){var c=oa(a),d=F(arguments,1),c=qa(c,d).join(" ");a.className=c},qa=function(a,b){return da(a,function(a){return!(0<=E(b,a))})};var P=function(a){P[" "](a);return a};P[" "]=function(){};var sa=!K||K&&(J()||9<=na),ta=K&&!N("9");!M||N("528");L&&N("1.9b")||K&&N("8")||ga&&N("9.5")||M&&N("528");L&&!N("8")||K&&N("9");var Q=function(a,b){this.type=a;this.currentTarget=this.target=b;this.defaultPrevented=this.l=!1};Q.prototype.preventDefault=function(){this.defaultPrevented=!0};var R=function(a,b){Q.call(this,a?a.type:"");this.relatedTarget=this.currentTarget=this.target=null;this.charCode=this.keyCode=this.button=this.screenY=this.screenX=this.clientY=this.clientX=this.offsetY=this.offsetX=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.j=this.state=null;if(a){var c=this.type=a.type;this.target=a.target||a.srcElement;this.currentTarget=b;var d=a.relatedTarget;if(d){if(L){var e;a:{try{P(d.nodeName);e=!0;break a}catch(f){}e=!1}e||(d=null)}}else"mouseover"==
c?d=a.fromElement:"mouseout"==c&&(d=a.toElement);this.relatedTarget=d;this.offsetX=M||void 0!==a.offsetX?a.offsetX:a.layerX;this.offsetY=M||void 0!==a.offsetY?a.offsetY:a.layerY;this.clientX=void 0!==a.clientX?a.clientX:a.pageX;this.clientY=void 0!==a.clientY?a.clientY:a.pageY;this.screenX=a.screenX||0;this.screenY=a.screenY||0;this.button=a.button;this.keyCode=a.keyCode||0;this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=
a.metaKey;this.state=a.state;this.j=a;a.defaultPrevented&&this.preventDefault()}};v(R,Q);R.prototype.preventDefault=function(){R.p.preventDefault.call(this);var a=this.j;if(a.preventDefault)a.preventDefault();else if(a.returnValue=!1,ta)try{if(a.ctrlKey||112<=a.keyCode&&123>=a.keyCode)a.keyCode=-1}catch(b){}};var ua="closure_listenable_"+(1E6*Math.random()|0),va=0;var wa=function(a,b,c,d,e){this.c=a;this.e=null;this.src=b;this.type=c;this.g=!!d;this.h=e;this.key=++va;this.d=this.f=!1},xa=function(a){a.d=!0;a.c=null;a.e=null;a.src=null;a.h=null};var S=function(a){this.src=a;this.b={};this.i=0};S.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.b[f];a||(a=this.b[f]=[],this.i++);var g;a:{for(g=0;g<a.length;++g){var h=a[g];if(!h.d&&h.c==b&&h.g==!!d&&h.h==e)break a}g=-1}-1<g?(b=a[g],c||(b.f=!1)):(b=new wa(b,this.src,f,!!d,e),b.f=c,a.push(b));return b};var ya=function(a,b){var c=b.type;if(c in a.b){var d=a.b[c],e=E(d,b),f;if(f=0<=e)B(null!=d.length),D.splice.call(d,e,1);f&&(xa(b),0==a.b[c].length&&(delete a.b[c],a.i--))}};var T="closure_lm_"+(1E6*Math.random()|0),U={},za=0,Ba=function(){var a=Aa,b=sa?function(c){return a.call(b.src,b.c,c)}:function(c){c=a.call(b.src,b.c,c);if(!c)return c};return b},Ca=function(a,b,c,d,e){if("array"==n(b))for(var f=0;f<b.length;f++)Ca(a,b[f],c,d,e);else if(c=Da(c),a&&a[ua])a.u(b,c,d,e);else{if(!b)throw Error("Invalid event type");var f=!!d,g=V(a);g||(a[T]=g=new S(a));c=g.add(b,c,!0,d,e);c.e||(d=Ba(),c.e=d,d.src=a,d.c=c,a.addEventListener?a.addEventListener(b.toString(),d,f):a.attachEvent(Ea(b.toString()),
d),za++)}},Ea=function(a){return a in U?U[a]:U[a]="on"+a},Ga=function(a,b,c,d){var e=!0;if(a=V(a))if(b=a.b[b.toString()])for(b=b.concat(),a=0;a<b.length;a++){var f=b[a];f&&f.g==c&&!f.d&&(f=Fa(f,d),e=e&&!1!==f)}return e},Fa=function(a,b){var c=a.c,d=a.h||a.src;if(a.f&&"number"!=typeof a&&a&&!a.d){var e=a.src;if(e&&e[ua])ya(e.t,a);else{var f=a.type,g=a.e;e.removeEventListener?e.removeEventListener(f,g,a.g):e.detachEvent&&e.detachEvent(Ea(f),g);za--;(f=V(e))?(ya(f,a),0==f.i&&(f.src=null,e[T]=null)):
xa(a)}}return c.call(d,b)},Aa=function(a,b){if(a.d)return!0;if(!sa){var c;if(!(c=b))a:{c=["window","event"];for(var d=m,e;e=c.shift();)if(null!=d[e])d=d[e];else{c=null;break a}c=d}e=c;c=new R(e,this);d=!0;if(!(0>e.keyCode||void 0!=e.returnValue)){a:{var f=!1;if(0==e.keyCode)try{e.keyCode=-1;break a}catch(g){f=!0}if(f||void 0==e.returnValue)e.returnValue=!0}e=[];for(f=c.currentTarget;f;f=f.parentNode)e.push(f);for(var f=a.type,h=e.length-1;!c.l&&0<=h;h--){c.currentTarget=e[h];var t=Ga(e[h],f,!0,c),
d=d&&t}for(h=0;!c.l&&h<e.length;h++)c.currentTarget=e[h],t=Ga(e[h],f,!1,c),d=d&&t}return d}return Fa(a,new R(b,this))},V=function(a){a=a[T];return a instanceof S?a:null},W="__closure_events_fn_"+(1E9*Math.random()>>>0),Da=function(a){B(a,"Listener can not be null.");if("function"==n(a))return a;B(a.handleEvent,"An object listener must have handleEvent method.");a[W]||(a[W]=function(b){return a.handleEvent(b)});return a[W]};var Y=function(a,b,c){"number"==typeof a?(this.a=Ha(a,b||0,c||1),X(this,c||1)):(b=typeof a,"object"==b&&null!=a||"function"==b?(this.a=Ha(a.getFullYear(),a.getMonth(),a.getDate()),X(this,a.getDate())):(this.a=new Date(aa()),this.a.setHours(0),this.a.setMinutes(0),this.a.setSeconds(0),this.a.setMilliseconds(0)))},Ha=function(a,b,c){b=new Date(a,b,c);0<=a&&100>a&&b.setFullYear(b.getFullYear()-1900);return b};l=Y.prototype;l.getFullYear=function(){return this.a.getFullYear()};l.getYear=function(){return this.getFullYear()};
l.getMonth=function(){return this.a.getMonth()};l.getDate=function(){return this.a.getDate()};l.getTime=function(){return this.a.getTime()};l.getUTCHours=function(){return this.a.getUTCHours()};l.setFullYear=function(a){this.a.setFullYear(a)};l.setMonth=function(a){this.a.setMonth(a)};l.setDate=function(a){this.a.setDate(a)};
l.add=function(a){if(a.r||a.o){var b=this.getMonth()+a.o+12*a.r,c=this.getYear()+Math.floor(b/12),b=b%12;0>b&&(b+=12);var d;a:{switch(b){case 1:d=0!=c%4||0==c%100&&0!=c%400?28:29;break a;case 5:case 8:case 10:case 3:d=30;break a}d=31}d=Math.min(d,this.getDate());this.setDate(1);this.setFullYear(c);this.setMonth(b);this.setDate(d)}a.m&&(b=new Date(this.getYear(),this.getMonth(),this.getDate(),12),a=new Date(b.getTime()+864E5*a.m),this.setDate(1),this.setFullYear(a.getFullYear()),this.setMonth(a.getMonth()),
this.setDate(a.getDate()),X(this,a.getDate()))};l.q=function(){return[this.getFullYear(),y(this.getMonth()+1),y(this.getDate())].join("")+""};l.toString=function(){return this.q()};var X=function(a,b){if(a.getDate()!=b){var c=a.getDate()<b?1:-1;a.a.setUTCHours(a.a.getUTCHours()+c)}};Y.prototype.valueOf=function(){return this.a.valueOf()};var Z=function(){};Z.k=function(){Z.n||(Z.n=new Z)};Z.k();new Y(0,0,1);new Y(9999,11,31);K||M&&N("525");Z.k();u("ae.init",function(){Ia();Ja();Ca(window,"load",function(){});Ka()});
var Ia=function(){var a;if(a=p("ae-content")?document.getElementById("ae-content"):"ae-content"){a=O("table","ae-table-striped",a);for(var b=0,c;c=a[b];b++){c=O("tbody",null,c);for(var d=0,e;e=c[d];d++){e=O("tr",null,e);for(var f=0,g;g=e[f];f++)f%2&&pa(g,"ae-even")}}}},Ja=function(){var a=O(null,"ae-noscript",void 0);ca(ea(a),function(a){ra(a,"ae-noscript")})},Ka=function(){m._gaq=m._gaq||[];m._gaq.push(function(){m._gaq._createAsyncTracker("UA-3739047-3","ae")._trackPageview()});(function(){var a=
document.createElement("script");a.src=("https:"==document.location.protocol?"https://ssl":"http://www")+".google-analytics.com/ga.js";a.setAttribute("async","true");document.documentElement.firstChild.appendChild(a)})()};u("ae.trackPageView",function(){m._gaq&&m._gaq._getAsyncTracker("ae")._trackPageview()});var Ma=function(a){if(void 0==a||null==a||0==a.length)return 0;a=Math.max.apply(Math,a);return La(a)},La=function(a){var b=5;2>b&&(b=2);--b;return Math.ceil(a/b)*b},Na=function(a,b,c){a=a.getSelection();1==a.length&&(a=a[0],null!=a.row&&(null!=b.starttime&&(c+="&starttime="+b.starttime),null!=b.endtime&&(c+="&endtime="+b.endtime),null!=b.latency_lower&&(c+="&latency_lower="+b.latency_lower),null!=b.latency_upper&&(c+="&latency_upper="+b.latency_upper),b=c+"&detail="+a.row,window.location.href=b))},
Oa=function(a,b,c,d,e){var f=new google.visualization.DataTable;f.addColumn("string","");f.addColumn("number","");f.addColumn({type:"string",role:"tooltip"});for(var g=0;g<b.length;g++)f.addRow(["",b[g],c[g]]);c=Math.max(10*b.length,200);b=Ma(b);a=new google.visualization.ColumnChart(document.getElementById("rpctime-"+a));a.draw(f,{height:100,width:c,legend:"none",chartArea:{left:40},fontSize:11,vAxis:{minValue:0,maxValue:b,gridlines:{count:5}}});google.visualization.events.addListener(a,"select",
r(Na,a,d,e))};u("ae.Charts.latencyHistogram",function(a,b,c){var d=new google.visualization.DataTable;d.addColumn("string","");d.addColumn("number","");for(var e=0;e<b.length;e++)d.addRow([""+a[e],b[e]]);for(e=b.length;e<a.length;e++)d.addRow([""+a[e],0]);b=Ma(b);(new google.visualization.ColumnChart(document.getElementById("latency-"+c))).draw(d,{legend:"none",width:20*a.length,height:200,vAxis:{maxValue:b,gridlines:{count:5}}})});
u("ae.Charts.latencyTimestampScatter",function(a,b,c,d,e){var f=new google.visualization.DataTable;f.addColumn("number","Time (seconds from start)");f.addColumn("number","Latency");for(var g=0;g<a.length;g++){var h=Math.round(a[g]-c);f.addRow([h,b[g]])}a=d.starttime?d.starttime:0;b=new google.visualization.ScatterChart(document.getElementById("LatencyVsTimestamp"));b.draw(f,{hAxis:{title:"Time (seconds from start of recording)",minValue:a},vAxis:{title:"Request Latency (milliseconds)",minValue:0},
tooltip:{trigger:"none"},legend:"none"});google.visualization.events.addListener(b,"select",r(Na,b,d,e))});
u("ae.Charts.entityCountBarChart",function(a,b,c,d){var e=new google.visualization.DataTable;e.addColumn("string","");e.addColumn("number","Reads");e.addColumn({type:"string",role:"tooltip"});e.addColumn("number","Misses");e.addColumn({type:"string",role:"tooltip"});e.addColumn("number","Writes");e.addColumn({type:"string",role:"tooltip"});var f=50;f>b.length&&(f=b.length);for(var g=0;g<f;g++)e.addRow(["",b[g][1]-b[g][3],b[g][0],b[g][3],b[g][0],b[g][2],b[g][0]]);b=20*f;f=b+130;a=new google.visualization.ColumnChart(document.getElementById(d+
"-"+a));c=La(c);a.draw(e,{height:100,width:f,chartArea:{width:b},fontSize:10,isStacked:!0,vAxis:{minValue:0,maxValue:c,gridlines:{count:5}}})});
u("ae.Charts.rpcVariationCandlestick",function(a){var b=new google.visualization.DataTable;b.addColumn("string","");b.addColumn("number","");b.addColumn("number","");b.addColumn("number","");b.addColumn("number","");b.addRows(a);(new google.visualization.CandlestickChart(document.getElementById("rpcvariation"))).draw(b,{vAxis:{title:"RPC Latency variation (milliseconds)"},hAxis:{textPosition:"out",slantedText:!0,slantedTextAngle:45,textStyle:{fontSize:13}},height:250,chartArea:{top:10,height:100},
legend:"none",tooltip:{trigger:"none"}})});u("ae.Charts.totalTimeBarChart",function(a,b,c,d){for(var e=[],f=0;f<b.length;f++)e[f]=b[f]+" milliseconds";Oa(a,b,e,c,d)});u("ae.Charts.rpcTimeBarChart",function(a,b,c,d,e){var f=[],g=[],h=c.indices,t=c.times;c=c.stats;for(var q=0;q<b;q++)f[q]=0,g[q]=null;for(q=0;q<h.length;q++){f[h[q]]=t[q];b=c[q];var k="Calls: "+b[0];if(0<b[1]||0<b[2]||0<b[3])k+=" Entities";0<b[1]&&(k+=" R:"+b[1]);0<b[2]&&(k+=" W:"+b[2]);0<b[3]&&(k+=" M:"+b[3]);g[h[q]]=k}Oa(a,f,g,d,e)});})();
