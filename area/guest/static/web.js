
$('.form-require').blur(function () {
    $(this).next("span").remove();
});

function checkform() {
    onDown = 0
    $('.form-require').each(function () {
        if ($(this).val().length < 1) {
            onDown = onDown + 1;
            $(this).after('<span class="require-alert">** 不能为空</span>');
        }
    });
    if (onDown == 0) {
        return true;
    } else
        return false;
}

function GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}

function activeMenu(path) {
    urlpath = window.location.pathname;
    urlpath = urlpath.replace(path, '');
    urlpaths = urlpath.split('/')
    $("#menu-nav").find('a').each(function () {
      thisPath = $(this).attr('href');
      thisPath = thisPath.replace(path, '');
      thisPaths = thisPath.split('/');
      if (thisPaths[2] == urlpaths[2]) {
        $(this).parent('li').addClass('active');
      }
    });
  }

  function loginout(){
    delCookie('jgcloudd');
    delCookie('username');
    location.href = '/ui/index';
}