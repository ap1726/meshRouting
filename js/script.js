console.log("Загрузка...")


dlinaSoobsheniya=13;
propusknayaSposobnost=512;
vhodniePotoki=5;
kHersta=0.7;

$('input[name=dlinaSoobsheniya]').val(dlinaSoobsheniya);
$('input[name=propusknayaSposobnost]').val(propusknayaSposobnost);
$('input[name=vhodniePotoki]').val(vhodniePotoki);
$('input[name=kHersta]').val(kHersta);

$('#nav1').click(function(){
        $('#content1').show();
        $('#content2').hide();
        $('#content3').hide();
        $('#content4').hide();
        $('.navi').css('background','#888');
        $('#nav1').css('background', '#ccc');
});
$('#nav2').click(function(){
        $('#content1').hide();
        $('#content2').show();
        $('#content3').hide();
        $('#content4').hide();
        $('.navi').css('background','#888');
        $('#nav2').css('background', '#ccc');
        if (count<1){
            $('#areaMatrix').html("<p><h4>Введите узлы, связи, параметры и нажмите расчитать</h4></p>");
        }
        else {
            getMatrix();
        }
});
$('#nav3').click(function(){
        $('#content1').hide();
        $('#content2').hide();
        $('#content3').show();
        $('#content4').hide();
        $('.navi').css('background','#888');
        $('#nav3').css('background', '#ccc');
        if (count<1){
            $('#areaMatrix').html("<p><h4>Введите узлы, связи, параметры и нажмите расчитать</h4></p>");
        }
        else {
            getMatrix();
        }
}); 
$('#nav4').click(function(){
        $('#content1').hide();
        $('#content2').hide();
        $('#content3').hide();
        $('#content4').show();
        $('.navi').css('background','#888');
        $('#nav4').css('background', '#ccc');
        getMatrix();
});

// ============================

var count = 0;
var mode = 0;

function modeSet(input) {
    if (input === 0) {
        mode=0;
        console.log('mode=0');
        $('#button1').css('background','#ccc');
        $('#button2').css('background','#fff');
        $('.nodeMesh').css('cursor','default');
    }
    else {
        mode=1;
        console.log('mode=1');
        $('#button1').css('background','#fff');
        $('#button2').css('background','#ccc');
        $('.nodeMesh').css('cursor','pointer');
    }
}
function reloadCount(){
    $("#count").val(count);
}
$("#areaMeshNet").click(function(e){
    if (count<20) {
        if (mode===0) {
        var xClick = e.pageX - $(this).offset().left;
        var yClick = e.pageY - $(this).offset().top;
        console.log(xClick+"------"+yClick);
        count++;
        reloadCount();
        $('#areaMeshNet').append("<div class=nodeMesh id=node"+count+" style=top:"+yClick+"px;left:"+xClick+"px; onclick=nodeGet("+count+");>"+count+"</div>");
        }
        else{
        }
    }
    else alert("Превышено количество узлов! (20)");
});
var lineX1, lineX2, lineY1, lineY2, clicks=0, adresMatrix=[], widthLineArr=[];
function nodeGet(input) {
    if (clicks === 0) {
        lineX1=$('#node'+input).offset().left - $('#areaMeshNet').offset().left;
        lineY1=$('#node'+input).offset().top - $('#areaMeshNet').offset().top;
        clicks++;
        adresMatrix.push(input-1);
        console.log(input);

    }
    else {
        clicks=0;
        lineX2=$('#node'+input).offset().left - $('#areaMeshNet').offset().left;
        lineY2=$('#node'+input).offset().top - $('#areaMeshNet').offset().top;
        
        var lineWidth=Math.round(Math.sqrt(Math.pow((lineX2-lineX1),2)+Math.pow((lineY2-lineY1),2)));

        $('#areaMeshNet').append("<svg id=line><line x1="+lineX1+" y1="+lineY1+" x2="+lineX2+" y2="+lineY2+"/></svg>");
        adresMatrix.push(input-1);
        widthLineArr.push(lineWidth);

    }
}
function emptyArea() {
    $("#areaMeshNet").empty();
    $("#areaMatrix").empty();
    $("#areaTrafik").empty();

    count=0;
};

function getMatrix() {

    if ($("input").is(".inputMatrix")){
        // $('#areaMatrix').append("<p><h4>Здесь будет матрица весов. Выставите узлы и связи на вкладке \"Схема\"</h4>");
    }
    else {
        reloadMatrix();
    }
};
function reloadMatrix(){
    //Матрица пропускной способности areaMatrix
    $("#areaMatrix").empty();

    $('#areaMatrix').append("<span class=colNumber></span>");
    for(var k=0; k<(count); k++){
        $('#areaMatrix').append("<span class=colNumber>"+(k+1)+"</span>");
    }
    $('#areaMatrix').append("<br />");
    for(var i=0; i<(count); i++){
        $('#areaMatrix').append("<span class=rowNumber>"+(i+1)+"</span>");
        for(var j=0; j<(count); j++){
            $('#areaMatrix').append("<input type=text class=inputMatrix id=input"+i+"_"+j+" name=inputMatrix value=Infinity />");
        }    
        $('#areaMatrix').append("<br/>");
    }
        var mm=0;
        for (var m=0;m<adresMatrix.length;m=m+2){
            var buf=Math.round(Math.random()*(propusknayaSposobnost-propusknayaSposobnost/2)+propusknayaSposobnost/2);
            $("#input"+adresMatrix[m]+"_"+adresMatrix[m+1]).val(buf);//widthLineArr[mm]
            $("#input"+adresMatrix[m+1]+"_"+adresMatrix[m]).val(buf);
            mm++;

        }
    //Матрица потоков areaTrafik
    $("#areaTrafik").empty();

    $('#areaTrafik').append("<span class=colNumber></span>");
    for(var k=0; k<(count); k++){
        $('#areaTrafik').append("<span class=colNumber>"+(k+1)+"</span>");
    }
    $('#areaTrafik').append("<br />");
    for(var i=0; i<(count); i++){
        $('#areaTrafik').append("<span class=rowNumber>"+(i+1)+"</span>");
        for(var j=0; j<(count); j++){
            $('#areaTrafik').append("<input type=text class=inputTrafik id=inputMatrix"+i+"_"+j+" name=inputTrafik value=Infinity />");
        }    
        $('#areaTrafik').append("<br/>");
    }
        $("#inputMatrix0_"+(count-1)).val(Math.round(Math.random()*(vhodniePotoki-vhodniePotoki/2)+vhodniePotoki/2));
        

};

// var G=[];

// function getGraf(input) {
//     for (var i=0; i<count; i++){
//         var buf=[];

//         for (var j=0; j<count; j++){
//             if (isFinite(+$("#input"+i+"_"+j).val())) continue;
//             buf[j]=+$("#input"+i+"_"+j).val();
//         }

//         G.push(buf);
//     }
//     console.log(G);
// };
$('input').change(function(){
    if ($(this).val==None){    
        $(this).val(999999);
    }
    else{
       $(this).val(777777); 
    }
});
modeSet(0);
console.log("Загружено")