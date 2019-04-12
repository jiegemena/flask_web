

UserData = {
    /**
     * 查询渠道商
     * @param {*} id 
     * @param {*} pageindex 
     * @param {*} pagesize 
     * @param {*} state 
     * @param {*} roleid 
     * @param {*} username 
     * @param {*} web_name 
     * @param {*} bak 
     */
    getUserSearch:function(id='',pageindex=1,pagesize=20,state='',roleid='',username='',web_name='',bak){
        $.ajax({
            type: "POST",
            dataType: "html",
            url: '/api/user/query',
            data: 'pageindex='+ pageindex +'&pagesize='+ pagesize +'&state='+ state +'&roleid='+ roleid +'&username='+username+'&web_name='+ web_name +'&id=' + id,
            success: function (result) {
                data = $.parseJSON(result);
                console.log(data)
                bak(data)
            },
            error: function (data) {
                alert("error:" + data.responseText);
            }

        });
    },
    /**
     * 编辑用户
     * @param {*} id 
     * @param {*} username 
     * @param {*} password 
     * @param {*} web_name 
     * @param {*} email 
     * @param {*} phone 
     * @param {*} address 
     * @param {*} bak 
     */
    editUser:function(id,username,password,web_name,email,phone,address,bak){
        $.ajax({
            type: "POST",
            dataType: "html",
            url: '/api/user/edit',
            data: 'username='+ username +'&password='+ password + '&web_name=' + web_name +'&email='+ email +'&phone='+ phone +'&address='+ address +'&id=' + id,
            success: function (result) {
                data = $.parseJSON(result);
                console.log(data)
                bak(data)
            },
            error: function (data) {
                alert("error:" + data.responseText);
            }

        });
    },
    addUser:function(postarr='username=&password=&web_name=&email=&phone=&address=',bak){
        $.ajax({
            type: "POST",
            dataType: "html",
            url: '/api/user/add',
            data: postarr,
            success: function (result) {
                data = $.parseJSON(result);
                console.log(data)
                bak(data)
            },
            error: function (data) {
                alert("error:" + data.responseText);
            }

        });
    },
    get_login_user:function(bak){
        $.ajax({
            type: "POST",
            dataType: "html",
            url: '/api/user/get_login_user',
            data: 'a=b',
            success: function (result) {
                data = $.parseJSON(result);
                console.log(data)
                bak(data)
            },
            error: function (data) {
                alert("error:" + data.responseText);
            }

        });
    }
};