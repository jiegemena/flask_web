 function httpGet(url, Succ) {
            if (window.XMLHttpRequest) {
                var AjaxXML = new XMLHttpRequest();
            }
            else {
                var AjaxXML = new ActiveXObject("Microsoft.XMLHTTP");
            }
            AjaxXML.open("GET", url, true);
            AjaxXML.send();
            AjaxXML.onreadystatechange = function () {
                if (AjaxXML.readyState == 4) {
                    if (AjaxXML.status == 200) {
                        Succ(AjaxXML.responseText);//成功的时候调用这个方法
                    }
                    else {
                        if (fnfiled) {
                            Field(AjaxXML.status);
                        }
                    }
                }
            };
        }

         function httpPost(url, data, Succ) {
            if (window.XMLHttpRequest) {
                var AjaxXML = new XMLHttpRequest();
            }
            else {
                var AjaxXML = new ActiveXObject("Microsoft.XMLHTTP");
            }
            AjaxXML.open("POST", url);
            AjaxXML.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            AjaxXML.send(data);
            AjaxXML.onreadystatechange = function () {
                if (AjaxXML.readyState == 4) {
                    if (AjaxXML.status == 200) {
                        Succ(AjaxXML.responseText);
                    }
                    else {
                        if (fnfiled) {
                            Field(AjaxXML.status);
                        }
                    }
                }
            };
        }