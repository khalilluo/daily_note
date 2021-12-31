```qml
    TextEdit {
        id: searchText
        text: qsTr("测试")
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.left: parent.left
        anchors.leftMargin: 20
    }

    Button{
        id:btnSennd
        text: "发送"
        anchors.top: searchText.bottom
        anchors.topMargin: 20
        anchors.left: searchText.left
        onClicked: {
            var u="http://localhost:8001/getString"
            var data="inputtext:"+searchText.text
//            post(u, data)
            get(u)
        }
    }

    ScrollView{
        width: 300
        height: 200
        anchors.top: btnSennd.bottom
        anchors.topMargin: 40
        anchors.left: searchText.left
//        verticalScrollBarPolicy:Qt.ScrollBarAlwaysOn
        contentItem:TextEdit {
            id: result
            text: qsTr("result:")
        }
    }


    property var xmlhttp: null

    //get method- asyn请求
    function get(url){
        if(xmlhttp==null){
            xmlhttp = new XMLHttpRequest()
            xmlhttp.onreadystatechange=onResultReady;
        }

        if(xmlhttp.readyState===0){
            result.remove(0, result.length)
            xmlhttp.open("GET", url, true)
            xmlhttp.send()
        }
    }

    //post mothod- asyn请求
    function post(url, data){
        if(xmlhttp==null){
            xmlhttp=new XMLHttpRequest()
            xmlhttp.onreadystatechange=onResultReady;
        }

        if(xmlhttp.readyState===0){
            result.remove(0, result.length)
            xmlhttp.open("POST", url, true)
            xmlhttp.send(data)
        }
    }

    //response,.readyState===4:返回请求结果
    function onResultReady(){
        console.log(xmlhttp.readyState)
        if(xmlhttp.readyState===4){
            if(xmlhttp.responseText!==null){
                result.append("response data: "+ xmlhttp.responseText)
            }
            xmlhttp.abort()
        }
    }

```