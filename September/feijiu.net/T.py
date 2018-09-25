# import os
#
# from lxml import etree
# #
# # page = """
# #
# # <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
# # <html xmlns="http://www.w3.org/1999/xhtml">
# #
# # <head>
# #     <title>浙江回收废纸,纸回收浙江_绍兴市柯桥区安昌镇富宝废旧物资回收站-中国Feijiu网商家</title>
# # <META NAME="keywords" CONTENT="浙江回收废纸,纸回收浙江">
# # <META NAME="description" CONTENT="长期回收废纸、生活用纸、工业用纸、纺织化纤红绿纸管、宝塔纸管">
# #
# #
# #     <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
# #     <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
# #     <link type="text/css" rel="stylesheet" href="http://style.feijiu.net/css/shop/base.css" />
# #     <script type="text/javascript" src="http://style.feijiu.net/js/index/jquery-1.8.2.min.js"></script>
# #     <link type="text/css" rel="stylesheet" href="http://style.feijiu.net/css/shop/shop01/index.css"/>
# #     <link rel="stylesheet" href="http://style.feijiu.net/css/shop/style.css"/>
# #     <script type="text/javascript" src="http://style.feijiu.net/js/Comm_sp.js"></script>
# #     <script type="text/javascript" src="http://style.feijiu.net/js/GetShopLink.js"></script>
# #     <script type="text/javascript" src="http://style.feijiu.net/js/shoptop.js"></script>
# #     <script type="text/javascript" src="http://style.feijiu.net/js/promptbox.js"></script>
# #     <script type="text/javascript" src="http://style.feijiu.net/js/qiehuan.js"></script>
# #     <script language="javascript" src="http://style.feijiu.net/js/ads400.js"></script>
# #
# #     <script>
# #         // 搜索函数
# #         //全站搜索
# #         function doSearch1() {
# #             var keyword = document.getElementById('shuru1').value;
# #             var goUrl = '/allptsrdcaxk.html'
# #
# #             if (keyword == '请输入产品名称') { keyword = ''; document.getElementById('shuru1').focus(); return false; }
# #             else {
# #                 //window.open("http://www.feijiu.net/search.aspx?GoUrl=" + goUrl + "&key=" + escape(keyword));
# #                 window.open("http://www.feijiu.net/searchGo.aspx?GoUrl=http://www.feijiu.net/gq/s/k/&key=" + escape(keyword));
# #             }
# #         }
# #         //本店铺搜索
# #         function doSearchMe1() {
# #             var keyword = document.getElementById('shuru1').value;
# #             if (keyword == '请输入产品名称')
# #             { keyword = ''; document.getElementById('shuru1').focus(); return false; }
# #             else {
# #                 window.location = "http://www.feijiu.net/shop/shop_new/search.aspx?GoUrl=http://wym1666.feijiu.net/&key=" + escape(keyword);
# #             }
# #
# #         }
# #     </script>
# #
# # </head>
# # <body>
# #     <form name="aspnetForm" method="post" action="contactusnews.aspx" id="aspnetForm">
# # <div>
# # <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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T25Nb3VzZU92ZXI9InBsYXllcignc3VibmF2X3p6Jyk7IiBvbk1vdXNlT3V0PSJjbG9jZXIoJ3N1Ym5hdl96eicpOyI+DQoJCSAgPHA+PC9wPg0KCQkgIDx1bD4NCgkJICAgIDxsaT48YSBocmVmPSJodHRwOi8vd3ltMTY2Ni5mZWlqaXUubmV0L3p6cnkuYXNweCI+5LyB5Lia6K6k6K+B5L+h5oGvPC9hPjwvbGk+DQoJCQk8bGk+PGEgaHJlZj0iaHR0cDovL3d5bTE2NjYuZmVpaml1Lm5ldC9ob25vcl96cy5hc3B4Ij7kvIHkuJrojaPoqonor4HkuaY8L2E+PC9saT4NCiAgICAgICAgICAgIDxsaSBjbGFzcz0ibGFzdCI+PGEgaHJlZj0iaHR0cDovL3d5bTE2NjYuZmVpaml1Lm5ldC9FeHBvbmVudC5hc3B4Ij7lvrfkv53mjIfmlbA8L2E+PC9saT4NCgkJCTxsaSBjbGFzcz0ibGFzdCI+PGEgaHJlZj0iaHR0cDovL3d5bTE2NjYuZmVpaml1Lm5ldC9ldmFsdWF0ZS5hc3B4Ij7llYblj4vor4Tku7c8L2E+PC9saT4NCgkJICA8L3VsPg0KCQk8L2Rpdj4NCgkgIDwvbGk+ZAIEDxYCHwAFiwMgPGxpID48YSBocmVmPSJodHRwOi8vd3ltMTY2Ni5mZWlqaXUubmV0L2Nhc2UuYXNweCIgT25Nb3VzZU92ZXI9InBsYXllcignc3VibmF2X2h6Jyk7IiBvbk1vdXNlT3V0PSJjbG9jZXIoJ3N1Ym5hdl9oeicpOyI+5ZCI5L2c5qGI5L6LPC9hPg0KCSAgICA8ZGl2IGlkPSJzdWJuYXZfaHoiIGNsYXNzPSJzdWJuYXYiICBPbk1vdXNlT3Zlcj0icGxheWVyKCdzdWJuYXZfaHonKTsiIG9uTW91c2VPdXQ9ImNsb2Nlcignc3VibmF2X2h6Jyk7Ij4NCgkJICA8cD48L3A+DQoJCSAgPHVsPg0KCQkJPGxpIGNsYXNzPSJsYXN0Ij48YSBocmVmPSJodHRwOi8vd3ltMTY2Ni5mZWlqaXUubmV0L2NvbW5ld3MuYXNweCI+5LyB5Lia5Yqo5oCBPC9hPjwvbGk+DQoJCSAgPC91bD4NCgkJPC9kaXY+DQoJICA8L2xpPmQCBQ8WAh8ABUg8bGkgPjxhIGhyZWY9Imh0dHA6Ly93eW0xNjY2LmZlaWppdS5uZXQvTWVzcy5hc3B4Ij7nu5nmiJHnlZnoqIA8L2E+PC9saT5kAgoPFgIfAAWXCTxkaXYgY2xhc3M9ImNweWluZm8iPjxkaXYgY2xhc3M9ImNvbHVtbl90aXRsZSBjbGVhcmZsb2F0Ij48aDI+5YWs5Y+45L+h5oGvPC9oMj48L2Rpdj48ZGl2IGNsYXNzPSJjcHlpbmZvX2NvbiI+PGRpdiBjbGFzcz0iamliaWUiIHRpdGxlPSLmoIflh4bkvJrlkZgiPjxzcGFuPjxpbWcgc3JjPSJodHRwOi8vc3R5bGUuZmVpaml1Lm5ldC9pbWFnZXMvZ3FpbmZvbGlzdC9iaWFvemh1bl90Yi5wbmciPjwvc3Bhbj48c3Ryb25nPuesrDHlubQ8L3N0cm9uZz48L2Rpdj48ZGl2IGNsYXNzPSJxci1jb2RlIj48aW1nIHNyYz0iaHR0cDovL2ltZzIuZmVpaml1Lm5ldC9SZW5aaGVuZy8yMDE3LzEyLzkvMTc0MjQ5My5qcGciIC8+PHNwYW4+W+aJq+aPj+S6jOe7tOeggSDlhbPms6jmnKzllYbpk7pdPC9zcGFuPjwvZGl2PjxoMj7nu43lhbTluILmn6/moaXljLrlronmmIzplYflr4zlrp3lup/ml6fnianotYTlm57mlLbnq5k8L2gyID48dWw+PGxpPuaJgOWxnuihjOS4mu+8muW6n+e6uDwvbGk+PGxpPue7j+iQpeaooeW8j++8muWbnuaUtuWFrOWPuDwvbGk+PGxpPuWFrOWPuOS4u+iQpe+8muW6n+e6uCznlJ/mtLvnlKjnurgs5bel5Lia55So57q4LOe6uue7h+WMlue6pOe6oue7v+e6uOeuoSzlrp3loZTnurjnrqE8L2xpPjxsaT7miYDlnKjlnLDljLrvvJrmtZnmsZ/nnIHnu43lhbTluILmn6/moaXljLrlronmmIzplYflr4zlrp3lup/ml6fnianotYTlm57mlLbnq5k8L2xpPjxsaT7kvpvmsYLkv6Hmga/mlbDph4/vvJozMOadoTwvbGk+PC91bD48ZGl2IGNsYXNzPSJyZW56aGVuZyI+PGRsPjxkdD7lvrfkv53otYTotKjorqTor4HvvJo8L2R0PjxkZD48aW1nIHNyYz0iaHR0cDovL3N0eWxlLmZlaWppdS5uZXQvaW1hZ2VzL3Nob3AvZGItc2FtbGwuZ2lmIiAvPjxhIGhyZWY9Imh0dHA6Ly93eW0xNjY2LmZlaWppdS5uZXQvenpyeS5hc3B4IiAgdGFyZ2V0PSJfYmxhbmsiPuW3suiupOivgTwvYT48L2RkPjwvZGw+PGRsPjxkdD7kvIHkuJrlrp7lnLDorqTor4HvvJo8L2R0PjxkZD48aW1nIHNyYz0iaHR0cDovL3N0eWxlLmZlaWppdS5uZXQvaW1hZ2VzL3Nob3Avcnpfc2RfaC5wbmciIC8+PGEgaHJlZj0iaHR0cDovL3d3dy5mZWlqaXUubmV0L3podWFudGkvcmVuemhlbmdfc2QvIiAgdGFyZ2V0PSJfYmxhbmsiPuacquiupOivgTwvYT48L2RkPjwvZGw+PC9kaXY+PC9kaXY+PC9kaXY+ZAIMDxYCHwAFiwc8ZGl2IGNsYXNzPSJzaWRlX2NvbHVtbiI+PGRpdiBjbGFzcz0iY29sdW1uX3RpdGxlIGNsZWFyZmxvYXQiPjxoMj7kv6Hmga/liIbnsbs8L2gyPjwvZGl2PjxkaXYgY2xhc3M9InNpZGVfY29uIj4gPGRsPjxkdD48c3Ryb25nPuS+m+W6lOS/oeaBr+exu+WIqzo8L3N0cm9uZz48L2R0PjxkZD48YSBocmVmPSJodHRwOi8vd3ltMTY2Ni5mZWlqaXUubmV0L2dsaXN0LmFzcHg/Y2w9MTAuNjA0Ni42MDU2Ij7nrrHmnb/nurg8L2E+PC9kZD48ZGQ+PGEgaHJlZj0iaHR0cDovL3d5bTE2NjYuZmVpaml1Lm5ldC9nbGlzdC5hc3B4P2NsPTEwLjYwNTIiPuW6n+e6uOeusTwvYT48L2RkPjwvZGw+PGRsPjxkdD48c3Ryb25nPuaxgui0reS/oeaBr+exu+WIqzo8L3N0cm9uZz48L2R0PjxkZD48YSBocmVmPSJodHRwOi8vd3ltMTY2Ni5mZWlqaXUubmV0L3FsaXN0LmFzcHg/Y2w9MTAuNjA0OSI+5Yqe5YWs44CB5paH5YyW55So57q4PC9hPjwvZGQ+PGRkPjxhIGhyZWY9Imh0dHA6Ly93eW0xNjY2LmZlaWppdS5uZXQvcWxpc3QuYXNweD9jbD0xMC42MDUyIj7lup/nurjnrrE8L2E+PC9kZD48ZGQ+PGEgaHJlZj0iaHR0cDovL3d5bTE2NjYuZmVpaml1Lm5ldC9xbGlzdC5hc3B4P2NsPTMuMjU4Ij7pgKDnurjorr7lpIc8L2E+PC9kZD48ZGQ+PGEgaHJlZj0iaHR0cDovL3d5bTE2NjYuZmVpaml1Lm5ldC9xbGlzdC5hc3B4P2NsPTEwLjk0ODkiPuW6n+e6uOi+uTwvYT48L2RkPjxkZD48YSBocmVmPSJodHRwOi8vd3ltMTY2Ni5mZWlqaXUubmV0L3FsaXN0LmFzcHg/Y2w9MTAuNjA1MCI+55Sf5rS755So57q4PC9hPjwvZGQ+PGRkPjxhIGhyZWY9Imh0dHA6Ly93eW0xNjY2LmZlaWppdS5uZXQvcWxpc3QuYXNweD9jbD0xMC42MDQ2LjYwNzQiPuWFtuWug+WMheijheeUqOe6uDwvYT48L2RkPjwvZGw+PC9kaXY+PC9kaXY+ZAIODxYCHgdWaXNpYmxlZ2QCEw9kFgRmDxYCHwAFuAg8ZGl2PjxoMj7nu43lhbTluILmn6/moaXljLrlronmmIzplYflr4zlrp3lup/ml6fnianotYTlm57mlLbnq5k8L2gyPg0KICAgICAgICAgICAgICAgICAgICAgICAgPHA+6IGUIOezuyDkurrvvJo8c3Bhbj7prY/lhYjnlJ88L3NwYW4+77yI5oC757uP55CG77yJPC9wPg0KICAgICAgICAgICAgICAgICAgICAgICAgPHA+PGEgaHJlZj0iYWJvdXR1c05ld3MuYXNweCIgdGFyZ2V0PSJfYmxhbmsiPuafpeeci+WFrOWPuOS7i+e7jTwvYT48YSBocmVmPSJ6enJ5LmFzcHgiIHRhcmdldD0iX2JsYW5rIj7mn6XnnIvotYTotKjorqTor4E8L2E+PC9wPg0KICAgICAgICAgICAgICAgICAgICAgICAgPHVsPg0KICAgICAgICAgICAgICAgICAgICAgICAgPGxpPuenu+WKqOeUteivne+8mjxpbWcgc3JjPSJodHRwOi8vd3d3LmZlaWppdS5uZXQvdHh0dG9waWMuYXNweD9mc2l6ZT0xMiZ0ZWxwaWM9Y3A0dlJoVmhvTVdSSU1nQWdjTmtQdz09IiBzdHlsZT0idmVydGljYWwtYWxpZ246IG1pZGRsZTsiPjwvbGk+DQogICAgICAgICAgICAgICAgICAgICAgICA8bGk+55S144CA44CA6K+d77yaPGltZyBzcmM9Imh0dHA6Ly93d3cuZmVpaml1Lm5ldC90eHR0b3BpYy5hc3B4P2ZzaXplPTEyJnRlbHBpYz1pVndnS0QzZitncFRENDN2S2w4YTdnPT0iIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjogbWlkZGxlOyI+PC9saT4NCiAgICAgICAgICAgICAgICAgICAgICAgIDxsaT7kvKDjgIDjgIDnnJ/vvJo8L2xpPg0KICAgICAgICAgICAgICAgICAgICAgICAgPGxpPuWFrOWPuOWcsOWdgO+8mua1meaxn+ecgee7jeWFtOW4guafr+ahpeWMuuWuieaYjOmVh+WvjOWuneW6n+aXp+eJqei1hOWbnuaUtuermTwvbGk+DQogICAgICAgICAgICAgICAgICAgICAgICA8bGk+6YKu5pS/57yW56CB77yaPC9saT4NCiAgICAgICAgICAgICAgICAgICAgICAgIDxsaT7nlLXlrZDpgq7nrrHvvJo8L2xpPg0KICAgICAgICAgICAgICAgICAgICAgICAgPGxpPuWFrOWPuOS4u+mhte+8mmh0dHA6Ly93eW0xNjY2LmZlaWppdS5uZXQvPC9saT4NCiAgICAgICAgICAgICAgICAgICAgICAgIDwvdWw+DQogICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj5kAgEPFgIeBXN0eWxlBQhkaXNwbGF5OmRkQHNGJJ/EShLDRo2t45Wggl8FHbGS6Fg6zbHrIMtDtTI=" />
# # </div>
# #
# # <div>
# #
# # 	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAYxOLYCk+BrT5KjlLmVQWg0w+6ufgM7lr8shDkhOk+wSMESY6bgfcjxwvdprzfKLymaDDCaYY/nW8f6V+k22SRAYnYc6KMBoR//QfZ0klLyM3Tb9ZH5+aOMz4Fk3fAZbEbozIOSE2Jr+tcPBSjX4lqLsz74AMqaDtteEegd6x3WQg==" />
# # </div>
# #     <div>
# #         <div id="ctl00_s_top">
# #             <div class="s_header">
# #                 <!--搜索开始-->
# #                 <p>
# #                     <input name="shuru" id="shuru1" maxlength="100" type="text" value="请输入产品名称" onfocus="javascript:if(this.value=='请输入产品名称')this.value='';"
# #                         onblur="javascript:if(this.value=='')this.value='请输入产品名称';" onkeyup="if(event.keyCode==13)doSearchMe1();" />
# #                     <span class="btn1"><a href="javascript:void(0);" onclick=" return doSearch1();">搜全站</a></span>
# #                     <span class="btn2"><a href="javascript:void(0);" onclick=" return doSearchMe1();">搜索店铺</a></span>
# #                 </p>
# #                 <!--搜索结束-->
# #                 <!--登录开始-->
# #                 <strong><a href="http://www.feijiu.net" target="_blank"></a></strong>
# #                 <div id="topbar_UserLogin1">
# #                     <span>您好，欢迎来到<span><a href="http://www.feijiu.net/" target="_blank">Feijiu网!</a></span>[<a
# #                         href="http://www.feijiu.net/login.aspx" target="_blank" rel="nofollow">请登录</a>] [<a href="http://www.feijiu.net/reg.aspx"
# #                             target="_blank" rel="nofollow">免费注册</a>]</span></div>
# #
# #                 <script type="text/javascript">
# #                     function LoginUser() {
# #                         var userName = getUserName();
# #                         if (userName != "") {
# #
# #                             document.getElementById("topbar_UserLogin1").innerHTML = "<span>您好<em><a href=\"http://user.feijiu.net/\" target=\"_blank\" title=\"点击进入我的废旧\">" + userName + "</a></em>，欢迎来到<span><a href=\"http://www.feijiu.net/\" target=\"_blank\">Feijiu网!</a></span> <a href=\"http://user.feijiu.net/\" target=\"_blank\">我的Feijiu</a></span> ";
# #                         }
# #                         else {
# #                             document.getElementById("topbar_UserLogin1").innerHTML = "<span>您好，欢迎来到<span><a href=\"http://www.feijiu.net/\" target=\"_blank\">Feijiu网!</a></span>[<a href=\"http://www.feijiu.net/login.aspx\" target=\"_blank\">请登录</a>] [<a href=\"http://www.feijiu.net/reg.aspx\" target=\"_blank\">免费注册</a>]</span>";
# #                         }
# #                     }
# #                     LoginUser();
# #                     setInterval(LoginUser, 3000);
# #
# #                 </script>
# #
# #                 <!--登录结束-->
# #             </div>
# #         </div>
# #     </div>
# #
# #
# #     <input name="ctl00$userurl" type="hidden" id="ctl00_userurl" value="http://wym1666.feijiu.net/" />
# #     <div id="wrapwrap">
# #         <div id="wrap">
# #             <div id="banner"><h2>绍兴市柯桥区安昌镇富宝废旧物资回收站</h2> <div id="vip"><img src="http://style.feijiu.net/images/shop/n_logo_bzhy.png" style='width:148px;height:100px;'/></div></div>
# #             <div id="ctl00_nav1">
# #                 <div id="nav">
# #                     <ul>
# #                         <li ><a href="http://wym1666.feijiu.net/">商铺首页</a></li>
# #                         <li  ><a href="http://wym1666.feijiu.net/qlist.aspx" onmouseover="player('subnav_qg');" onmouseout="clocer('subnav_qg');">求购信息</a>
# # 	     <div id="subnav_qg" class="subnav"  onmouseover="player('subnav_qg');" onmouseout="clocer('subnav_qg');">
# # 		  <p></p><ul><li><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6049">办公、文化用纸</a></li><li><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6052">废纸箱</a></li><li><a href="http://wym1666.feijiu.net/qlist.aspx?cl=3.258">造纸设备</a></li><li><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.9489">废纸边</a></li><li><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6050">生活用纸</a></li></ul></div></li>
# #                         <li  ><a href="http://wym1666.feijiu.net/glist.aspx" onmouseover="player('subnav_gy');" onmouseout="clocer('subnav_gy');">供应信息</a>
# # 	     <div id="subnav_gy" class="subnav"  onmouseover="player('subnav_gy');" onmouseout="clocer('subnav_gy');">
# # 		  <p></p><ul><li><a href="http://wym1666.feijiu.net/glist.aspx?cl=10.6046.6056">箱板纸</a></li><li><a href="http://wym1666.feijiu.net/glist.aspx?cl=10.6052">废纸箱</a></li></ul></div></li>
# #                         <li ><a href="http://wym1666.feijiu.net/products.aspx" onmouseover="player('subnav_zt');"
# #                             onmouseout="clocer('subnav_zt');">产品展厅</a>
# #                             <div id="subnav_zt" class="subnav" onmouseover="player('subnav_zt');" onmouseout="clocer('subnav_zt');">
# #                                 <p>
# #                                 </p>
# #                                 <ul>
# #
# #                                             <li><a href="http://wym1666.feijiu.net/products.aspx?cl=10.6049">
# #                                                 办公、文化用纸</a></li>
# #
# #                                             <li><a href="http://wym1666.feijiu.net/products.aspx?cl=10.6052">
# #                                                 废纸箱</a></li>
# #
# #                                             <li><a href="http://wym1666.feijiu.net/products.aspx?cl=3.258">
# #                                                 造纸设备</a></li>
# #
# #                                             <li><a href="http://wym1666.feijiu.net/products.aspx?cl=10.9489">
# #                                                 废纸边</a></li>
# #
# #                                             <li><a href="http://wym1666.feijiu.net/products.aspx?cl=10.6050">
# #                                                 生活用纸</a></li>
# #
# #                                 </ul>
# #                             </div>
# #                         </li>
# #                         <li ><a href="http://wym1666.feijiu.net/aboutusNews.aspx">公司简介</a></li>
# #                         <li  ><a href="http://wym1666.feijiu.net/zzry.aspx" OnMouseOver="player('subnav_zz');" onMouseOut="clocer('subnav_zz');">资质认证</a>
# # 	     <div id="subnav_zz" class="subnav"  OnMouseOver="player('subnav_zz');" onMouseOut="clocer('subnav_zz');">
# # 		  <p></p>
# # 		  <ul>
# # 		    <li><a href="http://wym1666.feijiu.net/zzry.aspx">企业认证信息</a></li>
# # 			<li><a href="http://wym1666.feijiu.net/honor_zs.aspx">企业荣誉证书</a></li>
# #             <li class="last"><a href="http://wym1666.feijiu.net/Exponent.aspx">德保指数</a></li>
# # 			<li class="last"><a href="http://wym1666.feijiu.net/evaluate.aspx">商友评价</a></li>
# # 		  </ul>
# # 		</div>
# # 	  </li>
# #                          <li ><a href="http://wym1666.feijiu.net/case.aspx" OnMouseOver="player('subnav_hz');" onMouseOut="clocer('subnav_hz');">合作案例</a>
# # 	    <div id="subnav_hz" class="subnav"  OnMouseOver="player('subnav_hz');" onMouseOut="clocer('subnav_hz');">
# # 		  <p></p>
# # 		  <ul>
# # 			<li class="last"><a href="http://wym1666.feijiu.net/comnews.aspx">企业动态</a></li>
# # 		  </ul>
# # 		</div>
# # 	  </li>
# #                         <li ><a href="http://wym1666.feijiu.net/Mess.aspx">给我留言</a></li>
# #                         <li class="cur"><a href="http://wym1666.feijiu.net/contactusNews.aspx">联系我们</a></li>
# #
# #                     </ul>
# #                 </div>
# #             </div>
# #
# #
# #
# #             <div id="content" class="clearfloat">
# #
# #
# #                 <!--侧栏-->
# #
# #                 <script>
# #                     function addfavorite() {
# #                         if (document.all) {
# #                             window.external.addFavorite('http://wym1666.feijiu.net/Shop/shop_new/contactusnews.aspx', '收藏夹');
# #                         }
# #                         else if (window.sidebar) {
# #                             window.sidebar.addPanel('绍兴市柯桥区安昌镇富宝废旧物资回收站', 'http://wym1666.feijiu.net/Shop/shop_new/contactusnews.aspx', "");
# #                         }
# #                         else {
# #                             alert("收藏失败！请尝试Ctrl+D");
# #                         }
# #                     }
# #                 </script>
# #
# #                 <div class="side">
# #                     <!--公司介绍开始-->
# #                     <div class="cpyinfo"><div class="column_title clearfloat"><h2>公司信息</h2></div><div class="cpyinfo_con"><div class="jibie" title="标准会员"><span><img src="http://style.feijiu.net/images/gqinfolist/biaozhun_tb.png"></span><strong>第1年</strong></div><div class="qr-code"><img src="http://img2.feijiu.net/RenZheng/2017/12/9/1742493.jpg" /><span>[扫描二维码 关注本商铺]</span></div><h2>绍兴市柯桥区安昌镇富宝废旧物资回收站</h2 ><ul><li>所属行业：废纸</li><li>经营模式：回收公司</li><li>公司主营：废纸,生活用纸,工业用纸,纺织化纤红绿纸管,宝塔纸管</li><li>所在地区：浙江省绍兴市柯桥区安昌镇富宝废旧物资回收站</li><li>供求信息数量：30条</li></ul><div class="renzheng"><dl><dt>德保资质认证：</dt><dd><img src="http://style.feijiu.net/images/shop/db-samll.gif" /><a href="http://wym1666.feijiu.net/zzry.aspx"  target="_blank">已认证</a></dd></dl><dl><dt>企业实地认证：</dt><dd><img src="http://style.feijiu.net/images/shop/rz_sd_h.png" /><a href="http://www.feijiu.net/zhuanti/renzheng_sd/"  target="_blank">未认证</a></dd></dl></div></div></div>
# #                     <!--公司介绍结束-->
# #                     <!--联系方式开始-->
# #
# #                     <!--联系方式结束-->
# #                     <!--信息分类开始-->
# #                     <div class="side_column"><div class="column_title clearfloat"><h2>信息分类</h2></div><div class="side_con"> <dl><dt><strong>供应信息类别:</strong></dt><dd><a href="http://wym1666.feijiu.net/glist.aspx?cl=10.6046.6056">箱板纸</a></dd><dd><a href="http://wym1666.feijiu.net/glist.aspx?cl=10.6052">废纸箱</a></dd></dl><dl><dt><strong>求购信息类别:</strong></dt><dd><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6049">办公、文化用纸</a></dd><dd><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6052">废纸箱</a></dd><dd><a href="http://wym1666.feijiu.net/qlist.aspx?cl=3.258">造纸设备</a></dd><dd><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.9489">废纸边</a></dd><dd><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6050">生活用纸</a></dd><dd><a href="http://wym1666.feijiu.net/qlist.aspx?cl=10.6046.6074">其它包装用纸</a></dd></dl></div></div>
# #                     <!--信息分类结束-->
# #                     <!--点此留言开始-->
# #
# #                     <!--点此留言结束-->
# #                     <!--收藏本店铺开始-->
# #                     <div id="ctl00_scshop" class="side_fav">
# #                         <a href="javascript:void(0);" onclick="addfavorite();"></a>
# #                     </div>
# #                     <!--收藏本店铺结束-->
# #
# #
# #                     <!--点此留言开始-->
# #
# #                     <!--点此留言结束-->
# #                     <!--收藏本店铺开始-->
# #
# #                     <!--收藏本店铺结束-->
# #                 </div>
# #
# #
# #
# #         <script type="text/javascript" src="http://api.map.baidu.com/api?v=1.5&ak=t1IZIWZEdV98SlZScZ5Qa6Rc"></script>
# # <div class="main">
# #
# # 	  <div class="column_title clearfloat"><h2>联系方式</h2></div>
# # 	  <div class="contact">
# # 	    <div><h2>绍兴市柯桥区安昌镇富宝废旧物资回收站</h2>
# #                         <p>联 系 人：<span>魏先生</span>（总经理）</p>
# #                         <p><a href="aboutusNews.aspx" target="_blank">查看公司介绍</a><a href="zzry.aspx" target="_blank">查看资质认证</a></p>
# #                         <ul>
# #                         <li>移动电话：<img src="http://www.feijiu.net/txttopic.aspx?fsize=12&telpic=cp4vRhVhoMWRIMgAgcNkPw==" style="vertical-align: middle;"></li>
# #                         <li>电　　话：<img src="http://www.feijiu.net/txttopic.aspx?fsize=12&telpic=iVwgKD3f+gpTD43vKl8a7g==" style="vertical-align: middle;"></li>
# #                         <li>传　　真：</li>
# #                         <li>公司地址：浙江省绍兴市柯桥区安昌镇富宝废旧物资回收站</li>
# #                         <li>邮政编码：</li>
# #                         <li>电子邮箱：</li>
# #                         <li>公司主页：http://wym1666.feijiu.net/</li>
# #                         </ul>
# #                         </div>
# # 	    <div id="ctl00_ContentPlaceHolder1_isShowMap" style="display:">
# # 	    <div id="allmap" style="width:700px;height:400px;"></div>
# # 	    </div>
# # 	  </div>
# # 	</div>
# # <script type="text/javascript">
# # window.onload=function indexFox(){
# # if(document.getElementById("ctl00_ContentPlaceHolder1_isloadMap").value=="1"){
# #     var map = new BMap.Map("allmap");            // 创建Map实例
# #     var point = new BMap.Point(document.getElementById("ctl00_ContentPlaceHolder1_altX").value,document.getElementById("ctl00_ContentPlaceHolder1_altY").value);    // 创建点坐标
# #     map.centerAndZoom(point,12);                     // 初始化地图,设置中心点坐标和地图级别。
# #     map.enableScrollWheelZoom();                            //启用滚轮放大缩小
# #     var marker = new BMap.Marker(point);  // 创建标注
# #     map.addOverlay(marker);              // 将标注添加到地图中
# #
# #     var infoWindow = new BMap.InfoWindow(document.getElementById("ctl00_ContentPlaceHolder1_altName").value);  // 创建信息窗口对象
# #     map.openInfoWindow(infoWindow,point); //开启信息窗口
# #
# #     marker.addEventListener("click", function(){this.openInfoWindow(infoWindow);});
# #     }
# # }
# # </script>
# # <input name="ctl00$ContentPlaceHolder1$altX" type="hidden" id="ctl00_ContentPlaceHolder1_altX" value="114.501084" />
# # <input name="ctl00$ContentPlaceHolder1$altY" type="hidden" id="ctl00_ContentPlaceHolder1_altY" value="38.055933" />
# # <input name="ctl00$ContentPlaceHolder1$altName" type="hidden" id="ctl00_ContentPlaceHolder1_altName" value="浙江省绍兴市柯桥区安昌镇富宝废旧物资回收站" />
# # <input name="ctl00$ContentPlaceHolder1$isloadMap" type="hidden" id="ctl00_ContentPlaceHolder1_isloadMap" value="1" />
# #
# #             </div>
# #         </div>
# #
# #         <div id="footer">
# #             绍兴市柯桥区安昌镇富宝废旧物资回收站&nbsp;&nbsp;&nbsp;&nbsp;地址：浙江省绍兴市柯桥区安昌镇富宝废旧物资回收站<br />
# #             技术支持：<a href="http://www.feijiu.net" target="_blank">Feijiu网</a>(原中国废旧物资网) <a href="http://user.feijiu.net"
# #                 target="_blank" rel="nofollow">商铺管理入口</a> | <a href="http://www.feijiu.net/help/aboutus/layer.aspx"
# #                     target="_blank" rel="nofollow">免责声明</a> | 客服中心 400-811-6831</div>
# #     </div>
# #     <div id="r-dbicon" onmouseover="this.style.cursor='pointer'" onclick="document.location='http://wym1666.feijiu.net/zzry.aspx';"></div>
# #     <div id="divPop"></div>
# #
# #     <script type="text/javascript">
# #         document.write("<img width=0 src=\"http://www.feijiu.net/_Control/tongji.aspx?lPg=" + document.referrer.replace(/&/g, "@") + "\" />");
# #     </script>
# #
# #     <div style="display: none;">
# #
# #         <script src="http://s6.cnzz.com/stat.php?id=1489646&web_id=1489646&show=pic" language="JavaScript"
# #             charset="gb2312"></script>
# #
# #         <script type="text/javascript">
# #             var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
# #             document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F28375d9dc4927c62b3e61e3bfcd2332a' type='text/javascript'%3E%3C/script%3E"));
# #         </script>
# #         <script>
# #             (function () {
# #                 var bp = document.createElement('script');
# #                 var curProtocol = window.location.protocol.split(':')[0];
# #                 if (curProtocol === 'https') {
# #                     bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
# #                 }
# #                 else {
# #                     bp.src = 'http://push.zhanzhang.baidu.com/push.js';
# #                 }
# #                 var s = document.getElementsByTagName("script")[0];
# #                 s.parentNode.insertBefore(bp, s);
# #             })();
# # </script>
# #
# #     </div>
# #     </form>
# # </body>
# # </html>
# # """
# #
# # html = etree.HTML(page)
# #
# # info = html.xpath('//*[@class="contact"]//text()')
# #
# # contact_info_picture_url = html.xpath('//*[@class="contact"]/div/ul/li/img/@src')
# #
# # print(info, '\n', contact_info_picture_url)
#
# l1 = ['\r\n                ', '深圳海隆达贸易有限公司', '\r\n                        ', '联 系 人：', '吴志兵', '（）', '\r\n                        ', '\r\n                        \r\n                        ', '移动电话：', '\r\n                        ', '电\u3000\u3000话：86-0755', '\r\n                        ', '传\u3000\u3000真：', '\r\n                        ', '公司地址：广东省深圳市\t\t\t\t\t\t \t\t\t\t\t\t红岭中路法制报社后楼', '\r\n                        ', '邮政编码：', '\r\n                        ', '电子邮箱：', '\r\n                        ', '公司主页：http://w437254191.feijiu.net', '\r\n                        \r\n                        \r\n                ', '\r\n                    ', '\r\n                ', '\r\n                ', '\r\n            ']
# l2 = ['\r\n\t    ', '康晟造纸设备调剂经营部', '\r\n                        ', '联 系 人：', '马永康', '（）', '\r\n                        ', '查看公司介绍', '查看资质认证', '\r\n                        ', '\r\n                        ', '移动电话：', '\r\n                        ', '电\u3000\u3000话：', '\r\n                        ', '传\u3000\u3000真：', '\r\n                        ', '公司地址：', '\r\n                        ', '邮政编码：', '\r\n                        ', '电子邮箱：', '\r\n                        ', '公司主页：http://ma15716361000.feijiu.net/', '\r\n                        ', '\r\n                        ', '\r\n\t    ', '\r\n\t    ', '\r\n\t    ', '\r\n\t  ']
# l3 = ['\r\n                ', '项城市蝾螈再生资源回收有限公司', '\r\n                        ', '联 系 人：', '王先生龚先生', '（经理）', '\r\n                        ', '\r\n                        \r\n                        ', '移动电话：', '\r\n                        ', '电\u3000\u3000话：', '\r\n                        ', '传\u3000\u3000真：', '\r\n                        ', '公司地址：河南省周口市项城市', '\r\n                        ', '邮政编码：', '\r\n                        ', '电子邮箱：', '\r\n                        ', '公司主页：http://wpm7199.feijiu.net', '\r\n                        \r\n                        \r\n                ', '\r\n                    ', '\r\n                ', '\r\n                ', '\r\n            ']
# l4 = ['\r\n\t    ', '绍兴市柯桥区安昌镇富宝废旧物资回收站', '\r\n                        ', '联 系 人：', '魏先生', '（总经理）', '\r\n                        ', '查看公司介绍', '查看资质认证', '\r\n                        ', '\r\n                        ', '移动电话：', '\r\n                        ', '电\u3000\u3000话：', '\r\n                        ', '传\u3000\u3000真：', '\r\n                        ', '公司地址：浙江省绍兴市柯桥区安昌镇富宝废旧物资回收站', '\r\n                        ', '邮政编码：', '\r\n                        ', '电子邮箱：', '\r\n                        ', '公司主页：http://wym1666.feijiu.net/', '\r\n                        ', '\r\n                        ', '\r\n\t    ', '\r\n\t    ', '\r\n\t    ', '\r\n\t  ']
#
# astr = """深圳海隆达贸易有限公司
# 联 系 人：吴志兵（）
# 移动电话：
# 电　　话：86-0755
# 传　　真：
# 公司地址：广东省深圳市 红岭中路法制报社后楼
# 邮政编码：
# 电子邮箱：
# 公司主页：http://w437254191.feijiu.net"""
#
# li = astr.split('\n')
# for i in l2:
#     j = i.replace('\r\n', '').replace(' ', '').replace('\u3000\u3000', '').replace('\r\n\t    ', '')\
#         .replace('\t\t\t\t\t\t', '').replace('\r\n                        ', ' ')\
#         .replace('\t', '').replace('（）', '')
#     if j != '':
#         li.append(j)
#
# items = []
# for i in li:
#     j = i.split('：')
#     if len(j) > 1:
#         for k in j:
#             if k != '':
#                 items.append(k)
#     else:
#         items.append(j[0])
#
# contact_index = items.index('联系人')
# address_index = items.index('公司地址')
#
# company = li[0]
# contact = items[contact_index+1]
# address = items[address_index+1]
# print(company, contact, '\n', address)

# import sys
#
# sys.path.append('../')
# from ProxyPool import IPool
#
# proxies = {
#             "http": "http://" + IPool().get_proxy(),
#         }
#
# print(proxies)

#
# headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Connection": "keep-alive",
#         "Host": "ouyanglingfeng.feijiu.net",
#         "Referer": "http://ouyanglingfeng.feijiu.net/",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": ""
#         }
#
# url = "http://ouyanglingfeng.feijiu.net/contactusNews.aspx"
# items = url.split('/')
# del items[3]
# host = items[2]
# items[1] = "//"
# refer = items[0] + items[1] + items[2]
#
# print(host, '\n', refer)


# li = ['http://w437254191.feijiu.net//contactusNews.aspx', 'http://ma1571636.feijiu.net//contactusNews.aspx', 'http://wpm7199.feijiu.net//contactusNews.aspx', 'http://feijiu0153.feijiu.net//contactusNews.aspx', 'http://wym1666.feijiu.net//contactusNews.aspx', 'http://dupeng6269.feijiu.net//contactusNews.aspx', 'http://wenhao1153.feijiu.net//contactusNews.aspx', 'http://pudong.feijiu.net//contactusNews.aspx', 'http://qingdaochuanqi.feijiu.net//contactusNews.aspx', 'http://feibao960.feijiu.net//contactusNews.aspx', 'http://13991169731.feijiu.net//contactusNews.aspx', 'http://qaz123456zxc.feijiu.net//contactusNews.aspx', 'http://as615948147.feijiu.net//contactusNews.aspx', 'http://13832290787.feijiu.net//contactusNews.aspx', 'http://15918630755.feijiu.net//contactusNews.aspx', 'http://feilongfeijiu.feijiu.net//contactusNews.aspx', 'http://xiu886520.feijiu.net//contactusNews.aspx', 'http://ruihezhiye.feijiu.net//contactusNews.aspx', 'http://jixieshebei678.feijiu.net//contactusNews.aspx', 'http://zzq69.feijiu.net//contactusNews.aspx', 'http://wwchache.feijiu.net//contactusNews.aspx', 'http://wang15527569644.feijiu.net//contactusNews.aspx', 'http://tcxwz.feijiu.net//contactusNews.aspx', 'http://yuanqinfang1.feijiu.net//contactusNews.aspx', 'http://fuyingjixie.feijiu.net//contactusNews.aspx']
# for i in li:
#     print(i)
#
# import xlsxwriter
#
#
# workbook = xlsxwriter.Workbook('t.xlsx')
# worksheet = workbook.add_worksheet()
#
#
# print(worksheet)
#
# import xlsxwriter
#
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet('test')
# worksheet.write('A1', 'Hello, world')
# workbook.close()
#
# print(worksheet)
# A = """连衣裙,毛呢大衣,针织衫,羽绒,马甲,卫衣,打底衫,短外套,长袖连衣裙,连衣裙套装,针织连衣裙,蕾丝连衣裙,背带裙,雪纺连衣裙,一字肩连衣裙,针织开衫套头衫,高领毛衣,宽松毛衣,中长款羊毛衫,羊绒衫,打底衫,长袖衬衫,长袖T恤,长袖打底衫,蕾丝打底衫,加绒打底衫,加绒衬衫,毛呢大衣,轻薄羽绒服,牛仔外套,毛衣外套,中长款风衣,西装外套,PU皮衣"""
# # #
# # # B = A.split(',')
# # # print(B)

