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
<div id="Vue_index">
    <el-container>
        <%--<el-header>--%>
        <%--&lt;%&ndash;顶部容器&ndash;%&gt;这里是Header-desu--%>
        <%--</el-header>--%>

        <header>
            <%--标题--%>
            <h1 style="font-size:64px;letter-spacing: 10px">
                I KNOW BIRDS
            </h1>
        </header>

        <el-main>
            <main>
                <%--存放主体内容： 照片上传、识别结果--%>
                <div>
                    <%--左边，上传照片--%>
                    <el-card class="box-card">
                        <el-upload
                                class="upload-demo"
                                ref="upload"
                                action="https://jsonplaceholder.typicode.com/posts/"
                                :on-preview="handlePreview"
                                :on-remove="handleRemove"
                                :file-list="fileList"
                                :auto-upload="false">
                            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                            <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">
                                上传到服务器
                            </el-button>
                            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
                        </el-upload>
                    </el-card>
                </div>

                <div>
                    <%--右边，识别结果--%>
                    <%--<el-card class="box-card" style="display: flex;align-items: center;justify-content: center;">--%>
                    <el-card class="box-card card-position">

                    </el-card>
                </div>
            </main>
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
    var Vue_index = new Vue({
        el: '#Vue_index',
        data: {
            site_name: "I Know Birds 鸟类识别平台",
            github_url: "https://github.com/MakeItPossible-MJT/Birds_Identification",
            fileList: [{
                name: 'food.jpeg',
                url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'
            }, {
                name: 'food2.jpeg',
                url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'
            }]
        },
        methods: {
            details: function () {
                return this.site_name + " - 软件工程第五小组";
            },
            submitUpload() {
                this.$refs.upload.submit();
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {
                console.log(file);
            }
        }
    })

</script>

</html>
