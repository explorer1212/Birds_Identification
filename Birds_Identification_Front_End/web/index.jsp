<%--
  Created by IntelliJ IDEA.
  User: LeoK
  Date: 2020/11/21
  Time: 9:42
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>

<head>
    <meta charset="UTF-8">
    <%--引入Element--%>
    <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
    <%--<link rel="stylesheet" href="element-ui/lib/theme-chalk/index.css">--%>
    <%--CSS样式文件--%>
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <title>I Know Birds - 鸟类识别系统</title>
</head>
<body>
<div id="Vue_DIV">
    <el-container height="100%">
        <el-header>
            <%--顶部容器--%>
        </el-header>

        <el-main>


        </el-main>


        <el-footer>
            <%--底部容器--%>
            ©CopyRight 2020 {{details()}}
        </el-footer>


    </el-container>
</div>
</body>
<%--引入Vue.min 即Vue完成版生产环境 非开发版--%>
<%--<script src="js/vue.min.js"></script>--%>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.min.js"></script>
<%--引入Element组件库--%>
<%--<script src="element-ui/lib/index.js"></script>--%>
<script src="https://unpkg.com/element-ui/lib/index.js"></script>
<script>
    //注册使用vue
    var Vue = window.Vue;
    var Vue_DIV = new Vue({
        el: '#Vue_DIV',
        data: {
            site_name: "I Know Birds 鸟类识别平台",
            github_url: "https://github.com/MakeItPossible-MJT/Birds_Identification",
        },
        methods: {
            details: function () {
                return this.site_name + " - 软件工程第五小组";
            }
        }
    })
</script>

</html>
