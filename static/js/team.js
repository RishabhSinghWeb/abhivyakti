var mediaQueryList = window.matchMedia('(max-width: 600px)');


if (mediaQueryList.matches) {
    /* the viewport is 600 pixels wide or less */
    function openSide() {
        document.getElementById("mySidenav").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        document.getElementById("main-10").style.left = "250px";
        document.getElementById("close").style.display = "inline";
        document.getElementById("open").style.display = "none";

    }
}
else {
    function openSide() {
        document.getElementById("mySidenav").style.width = "350px";
        document.getElementById("main").style.marginLeft = "350px";
        document.getElementById("main-10").style.left = "350px";
        document.getElementById("close").style.display = "inline";
        document.getElementById("open").style.display = "none";

    }
}






/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeSide() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("main-10").style.left = "0"
    document.getElementById("close").style.display = "none";
    document.getElementById("open").style.display = "inline";

}



$('#coordinators').click(function () {
    $('.links-10').toggle(500);

})

$('#choreo-links').click(function () {
    $('.choreo-links').toggle(700);

})
$('#euphony-links').click(function () {
    $('.euphony-links').toggle(700);

})
$('#draco-links').click(function () {
    $('.draco-links').toggle(700);

})
$('#rit-links').click(function () {
    $('.rit-links').toggle(700);

})
$('#photo-links').click(function () {
    $('.photo-links').toggle(700);

})
$('#media-links').click(function () {
    $('.media-links').toggle(700);

})
$('#compare-links').click(function () {
    $('.compare-links').toggle(700);

})
$('#deco-links').click(function () {
    $('.deco-links').toggle(700);

})
$('#ccc-links').click(function () {
    $('.ccc-links').toggle(700);

})
$('#info-links').click(function () {
    $('.info-links').toggle(700);

})
$('#lit-links').click(function () {
    $('.lit-links').toggle(700);

})
$('#npc-links').click(function () {
    $('.npc-links').toggle(700);

})
$('#sec-links').click(function () {
    $('.sec-links').toggle(700);

})
$('#contro-links').click(function () {
    $('.contro-links').toggle(700);

})
$('#epc-links').click(function () {
    $('.epc-links').toggle(700);

})
$('#ipc-links').click(function () {
    $('.ipc-links').toggle(700);

})

$(".list1").click(function () {
    $('.span1').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span6, .span7, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main1').toggle(700)
    $('.main2, .main3, .main4, .main5, .main6, .main7, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var r = document.querySelector(':root');
    r.style.setProperty('--cyan', 'yellow');
})
$(".list2").click(function () {
    $('.span2').toggleClass('span-rotate')
    $('.span1, .span3, .span4, .span5, .span6, .span7, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main2').toggle(700)
    $('.main1, .main3, .main4, .main5, .main6, .main7, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'cyan');

})
$(".list3").click(function () {
    $('.span3').toggleClass('span-rotate')
    $('.span2, .span1, .span4, .span5, .span6, .span7, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main3').toggle(700)
    $('.main2, .main1, .main4, .main5, .main6, .main7, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'rgb(0, 255, 55)');
})
$(".list4").click(function () {
    $('.span4').toggleClass('span-rotate')
    $('.span2, .span3, .span1, .span5, .span6, .span7, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main4').toggle(700)
    $('.main2, .main3, .main1, .main5, .main6, .main7, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'orange');
})
$(".list5").click(function () {
    $('.span5').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span1, .span6, .span7, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main5').toggle(700)
    $('.main2, .main3, .main4, .main1, .main6, .main7, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'yellow');
})
$(".list6").click(function () {
    $('.span6').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span1, .span7, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main6').toggle(700)
    $('.main2, .main3, .main4, .main5, .main1, .main7, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'rgb(0, 255, 55)');
})
$(".list7").click(function () {
    $('.span7').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span6, .span1, .span8, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main7').toggle(700)
    $('.main2, .main3, .main4, .main5, .main6, .main1, .main8, .main9, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'orange');
})
$(".list8").click(function () {
    $('.span8').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span6, .span7, .span1, .span9, .span10, .span11').removeClass('span-rotate')
    $('.main8').toggle(700)
    $('.main2, .main3, .main4, .main5, .main6, .main7, .main1, .main9, .main10, .main11').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'cyan');
})
$(".list9").click(function () {
    $('.span9').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span6, .span7, .span8, .span1, .span10, .span11').removeClass('span-rotate')
    $('.main9').toggle(700)
    $('.main2, .main3, .main4, .main5, .main6, .main7, .main8, .main1, .main10, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'yellow');
})
$(".list10").click(function () {
    $('.span10').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span6, .span7, .span8, .span9, .span1, .span11').removeClass('span-rotate')
    $('.main10').toggle(700)
    $('.main2, .main3, .main4, .main5, .main6, .main7, .main8, .main9, .main1, .main11, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'rgb(0, 255, 55)');
})
$(".list11").click(function () {
    $('.span11').toggleClass('span-rotate')
    $('.span2, .span3, .span4, .span5, .span6, .span7, .span8, .span9, .span10, .span1').removeClass('span-rotate')
    $('.main11').toggle(700)
    $('.main2, .main3, .main4, .main5, .main6, .main7, .main8, .main9, .main10, .main1, .links-10').hide(700)
    var m = document.querySelector(':root');
    m.style.setProperty('--cyan', 'orange');
})



$(".li1").click(function () {
    $('.sp1').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell1').toggle(700)
    $('.cord1, .acord1').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)

})
$(".li2").click(function () {
    $('.sp2').toggleClass('span-rotate')
    $('.sp3, .sp1, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.draco-links, .choreo-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell2').toggle(700)
    $('.cord2, .acord2').hide(700)
    $('.cell3, .cell1, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)

})
$(".li3").click(function () {
    $('.sp3').toggleClass('span-rotate')
    $('.sp2, .sp1, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .choreo-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell3').toggle(700)
    $('.cord3, .acord3').hide(700)
    $('.cell2, .cell1, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li4").click(function () {
    $('.sp4').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp1, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .choreo-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell4').toggle(700)
    $('.cord4, .acord4').hide(700)
    $('.cell2, .cell3, .cell1, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li5").click(function () {
    $('.sp5').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp1, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .choreo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell5').toggle(700)
    $('.cord5, .acord5').hide(700)
    $('.cell2, .cell3, .cell4, .cell1, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li6").click(function () {
    $('.sp6').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp1, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .choreo-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell6').toggle(700)
    $('.cord6, .acord6').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell1, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li7").click(function () {
    $('.sp7').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp1, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .choreo-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell7').toggle(700)
    $('.cord7, .acord7').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell1, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li8").click(function () {
    $('.sp8').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp1, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .choreo-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell8').toggle(700)
    $('.cord8, .acord8').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell1, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li9").click(function () {
    $('.sp9').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp1, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .choreo-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell9').toggle(700)
    $('.cord9, .acord9').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell1, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li10").click(function () {
    $('.sp10').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp1, .sp11, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .choreo-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell10').toggle(700)
    $('.cord10, .acord10').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell1, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li11").click(function () {
    $('.sp11').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp1, .sp12, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .choreo-links, .npc-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell11').toggle(700)
    $('.cord11, .acord11').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li12").click(function () {
    $('.sp12').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp1, .sp13, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .choreo-links, .sec-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell12').toggle(700)
    $('.cord12, .acord12').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell1, .cell13, .cell14, .cell15, .cell16').hide(700)
})
$(".li13").click(function () {
    $('.sp13').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp1, .sp14, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .choreo-links, .contro-links, .epc-links, .ipc-links').hide(700)
    $('.cell13').toggle(700)
    $('.cord13, .acord13').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell1, .cell14, .cell15, .cell16').hide(700)
})
$(".li14").click(function () {
    $('.sp14').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp1, .sp15, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .choreo-links, .epc-links, .ipc-links').hide(700)
    $('.cell14').toggle(700)
    $('.cord14, .acord14').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell1, .cell15, .cell16').hide(700)
})
$(".li15").click(function () {
    $('.sp15').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp1, .sp16').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .choreo-links, .ipc-links').hide(700)
    $('.cell15').toggle(700)
    $('.cord15, .acord15').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell1, .cell16').hide(700)
})
$(".li16").click(function () {
    $('.sp16').toggleClass('span-rotate')
    $('.sp2, .sp3, .sp4, .sp5, .sp6, .sp7, .sp8, .sp9, .sp10, .sp11, .sp12, .sp13, .sp14, .sp15, .sp1').removeClass('span-rotate')
    $('.euphony-links, .draco-links, .rit-links, .photo-links, .media-links, .compare-links, .deco-links, .ccc-links, .info-links, .lit-links, .npc-links, .sec-links, .contro-links, .epc-links, .choreo-links').hide(700)
    $('.cell16').toggle(700)
    $('.cord16, .acord16').hide(700)
    $('.cell2, .cell3, .cell4, .cell5, .cell6, .cell7, .cell8, .cell9, .cell10, .cell11, .cell12, .cell13, .cell14, .cell15, .cell1').hide(700)
})


$('.cord-1').click(function () {
    $('.cord1').toggle(700)
    $('.acord1').hide(700)
})
$('.acord-1').click(function () {
    $('.acord1').toggle(700)
    $('.cord1').hide(700)
})
$('.cord-2').click(function () {
    $('.cord2').toggle(700)
    $('.acord2').hide(700)
})
$('.acord-2').click(function () {
    $('.cord2').hide(700)
    $('.acord2').toggle(700)
})
$('.cord-3').click(function () {
    $('.cord3').toggle(700)
    $('.acord3').hide(700)
})
$('.acord-3').click(function () {
    $('.cord3').hide(700)
    $('.acord3').toggle(700)
})
$('.cord-4').click(function () {
    $('.cord4').toggle(700)
    $('.acord4').hide(700)
})
$('.acord-4').click(function () {
    $('.cord4').hide(700)
    $('.acord4').toggle(700)
})
$('.cord-5').click(function () {
    $('.cord5').toggle(700)
    $('.acord5').hide(700)
})
$('.acord-5').click(function () {
    $('.cord5').hide(700)
    $('.acord5').toggle(700)
})
$('.cord-6').click(function () {
    $('.cord6').toggle(700)
    $('.acord6').hide(700)
})
$('.acord-6').click(function () {
    $('.cord6').hide(700)
    $('.acord6').toggle(700)
})
$('.cord-7').click(function () {
    $('.cord7').toggle(700)
    $('.acord7').hide(700)
})
$('.acord-7').click(function () {
    $('.cord7').hide(700)
    $('.acord7').toggle(700)
})
$('.cord-8').click(function () {
    $('.cord8').toggle(700)
    $('.acord8').hide(700)
})
$('.acord-8').click(function () {
    $('.cord8').hide(700)
    $('.acord8').toggle(700)
})
$('.cord-9').click(function () {
    $('.cord9').toggle(700)
    $('.acord2').hide(700)
})
$('.acord-9').click(function () {
    $('.cord9').hide(700)
    $('.acord9').toggle(700)
})
$('.cord-10').click(function () {
    $('.cord10').toggle(700)
    $('.acord10').hide(700)
})
$('.acord-10').click(function () {
    $('.cord10').hide(700)
    $('.acord10').toggle(700)
})
$('.cord-11').click(function () {
    $('.cord11').toggle(700)
    $('.acord11').hide(700)
})
$('.acord-11').click(function () {
    $('.cord11').hide(700)
    $('.acord11').toggle(700)
})
$('.cord-12').click(function () {
    $('.cord12').toggle(700)
    $('.acord12').hide(700)
})
$('.acord-12').click(function () {
    $('.cord12').hide(700)
    $('.acord12').toggle(700)
})
$('.cord-13').click(function () {
    $('.cord13').toggle(700)
    $('.acord13').hide(700)
})
$('.acord-13').click(function () {
    $('.cord13').hide(700)
    $('.acord13').toggle(700)
})
$('.cord-14').click(function () {
    $('.cord14').toggle(700)
    $('.acord14').hide(700)
})
$('.acord-14').click(function () {
    $('.cord14').hide(700)
    $('.acord14').toggle(700)
})
$('.cord-15').click(function () {
    $('.cord15').toggle(700)
    $('.acord15').hide(700)
})
$('.acord-15').click(function () {
    $('.cord15').hide(700)
    $('.acord15').toggle(700)
})
$('.cord-16').click(function () {
    $('.cord16').toggle(700)
    $('.acord16').hide(700)
})
$('.acord-16').click(function () {
    $('.cord16').hide(700)
    $('.acord16').toggle(700)
})
