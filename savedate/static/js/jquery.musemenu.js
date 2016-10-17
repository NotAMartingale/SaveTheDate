/*
 ADOBE CONFIDENTIAL
 ___________________

 Copyright 2011 Adobe Systems Incorporated
 All Rights Reserved.

 NOTICE:  All information contained herein is, and remains
 the property of Adobe Systems Incorporated and its suppliers,
 if any.  The intellectual and technical concepts contained
 herein are proprietary to Adobe Systems Incorporated and its
 suppliers and may be covered by U.S. and Foreign Patents,
 patents in process, and are protected by trade secret or copyright law.
 Dissemination of this information or reproduction of this material
 is strictly forbidden unless prior written permission is obtained
 from Adobe Systems Incorporated.
*/
(function(a){a.fn.museMenu=function(){return this.each(function(){var b=a(this),c="absolute",d,f,g,l,h,i;if(b.css("position")=="fixed"){c="fixed";i=b;var j=Muse.Utils.getStyleSheetRuleById(Muse.Utils.getPageStyleSheet(),this.id);d=j?Muse.Utils.getRuleProperty(j,"top"):b.css("top");f=j?Muse.Utils.getRuleProperty(j,"left"):b.css("left");g=j?Muse.Utils.getRuleProperty(j,"right"):b.css("right");l=j?Muse.Utils.getRuleProperty(j,"bottom"):b.css("bottom");h=parseInt(b.css("margin-left"))}else for(j=b.parent();j.length>
0&&j.attr("id")!="page";){if(j.css("position")=="fixed"){c="fixed";i=j;var k=j.offset(),m=b.offset(),o=Muse.Utils.getStyleSheetRuleById(Muse.Utils.getPageStyleSheet(),j.attr("id")),q=o?Muse.Utils.getRuleProperty(o,"top"):j.css("top"),p=o?Muse.Utils.getRuleProperty(o,"left"):j.css("left"),n=o?Muse.Utils.getRuleProperty(o,"right"):j.css("right"),o=o?Muse.Utils.getRuleProperty(o,"bottom"):j.css("bottom");d=q&&q!="auto"?parseInt(q)+(m.top-k.top):q;f=p&&p!="auto"&&p.indexOf("%")==-1?parseInt(p)+(m.left-
k.left):p;g=n&&n!="auto"&&n.indexOf("%")==-1?parseInt(n)+(k.left+j.width())-(m.left+b.width()):n;l=o&&o!="auto"?parseInt(o)+(k.top+j.height())-(m.top+b.height()):o;h=parseInt(j.css("margin-left"))+(p&&p.indexOf("%")!=-1?m.left-k.left:0);break}j=j.parent()}var s=a(),t=!1,v=b.find(".MenuItemContainer"),j=b.find(".MenuItem"),k=b.find(".SubMenu").add(j),w;k.on("mouseover",function(){t=!0});k.on("mouseleave",function(){t=!1;setTimeout(function(){t===!1&&(v.each(function(){a(this).data("hideSubmenu")()}),
s=a())},300)});v.on("mouseleave",function(b){var c=a(b.target),d=c.closest(".SubMenu");w&&clearTimeout(w);d.length>0&&(w=setTimeout(function(){d.find(".MenuItemContainer").each(function(){a(this).data("hideSubmenu")()});s=c.closest(".MenuItemContainer").data("$parentMenuItemContainer")},300))});v.on("mouseenter",function(){clearTimeout(w)});j.each(function(){var j=a(this),k=j.siblings(".SubMenu"),m=j.closest(".MenuItemContainer"),n=m.parentsUntil(".MenuBar").filter(".MenuItemContainer").length===
0,o;if(n&&k.length>0)j.data("offsetContainerRaw",a("<div style='position:"+c+"' class='MenuBar popup_element'></div>").hide().appendTo("body")),k.show(),o=k.position().top,k.hide();m.data("$parentMenuItemContainer",m.parent().closest(".MenuItemContainer")).data("showSubmenuOnly",function(){if(n&&k.length>0){var a=j.data("offsetContainer"),p="undefined"!=typeof a,a=a||j.data("offsetContainerRaw");if(c!="fixed")p=m.offset(),a.css({left:p.left,top:p.top});else if(!p){var p=m.position(),q=0,s=0;g&&g!=
"auto"&&(q=b.outerWidth()-p.left);l&&l!="auto"&&(s=o);a.css({left:f,top:d,right:g,bottom:l,marginLeft:h+p.left,marginRight:q,marginTop:p.top,marginBottom:s})}a.append(k).show();j.data("offsetContainer",a);i&&a&&i.data("hasScrollEffect")===!0&&a.cloneScrollEffectsFrom(i)}k.show();k.find(".SubMenu").hide()}).data("hideSubmenu",function(){var a=j.data("offsetContainer");a&&a.data("hasScrollEffect")===!0&&a.clearScrollEffects();k.hide()}).data("isDescendentOf",function(a){for(var b=m.data("$parentMenuItemContainer");b.length>
0;){if(a.index(b)>=0)return!0;b=b.data("$parentMenuItemContainer")}return!1});var p=function(){var b=s;b.length==0?m.data("showSubmenuOnly")():m.data("$parentMenuItemContainer").index(b)>=0?m.data("showSubmenuOnly")():m.siblings().index(b)>=0?(b.data("hideSubmenu")(),m.data("showSubmenuOnly")()):b.data("isDescendentOf")(m)?m.data("showSubmenuOnly")():b.data("isDescendentOf")(m.siblings(".MenuItemContainer"))?(m.siblings(".MenuItemContainer").each(function(){a(this).data("hideSubmenu")()}),m.data("showSubmenuOnly")()):
b.get(0)==m.get(0)&&m.data("showSubmenuOnly")();s=m},q=null;j.on("mouseenter",function(){j.data("mouseEntered",!0);q=setTimeout(function(){p()},200);j.one("mouseleave",function(){clearTimeout(q);j.data("mouseEntered",!1)})});k.length&&(j.attr("aria-haspopup",!0),Muse.Browser.Features.Touch&&(j.click(function(){return k.is(":visible")}),a(document.documentElement).on(Muse.Browser.Features.Touch.End,Muse.Browser.Features.Touch.Listener(function(b){!k.is(":visible")&&a(b.target).closest(m).length>0?
(b.stopPropagation(),Muse.Utils.redirectCancelled=!0,setTimeout(function(){Muse.Utils.redirectCancelled=!1},16),j.data("mouseEntered")&&setTimeout(function(){m.data("showSubmenuOnly")()},200)):k.is(":visible")&&a(b.target).closest(k).length==0&&a(b.target).closest(m).length==0&&m.data("hideSubmenu")()}))))});j.filter(".MuseMenuActive").each(function(){for(var b=a(this).closest(".MenuItemContainer").data("$parentMenuItemContainer");b&&b.length>0;)b.children(".MenuItem").addClass("MuseMenuActive"),
b=b.data("$parentMenuItemContainer")})})}})(jQuery);
;(function(){if(!("undefined"==typeof Muse||"undefined"==typeof Muse.assets)){var a=function(a,b){for(var c=0,d=a.length;c<d;c++)if(a[c]==b)return c;return-1}(Muse.assets.required,"jquery.musemenu.js");if(-1!=a){Muse.assets.required.splice(a,1);for(var a=document.getElementsByTagName("meta"),b=0,c=a.length;b<c;b++){var d=a[b];if("generator"==d.getAttribute("name")){"2014.3.1.295"!=d.getAttribute("content")&&Muse.assets.outOfDate.push("jquery.musemenu.js");break}}}}})();