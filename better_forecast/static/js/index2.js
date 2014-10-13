$(document).ready(function() {
//    $('#cont').css('visibility', 'hidden');
    $('#finder').on('click', function() {
       $('#cont').attr('style', 'visibility:visible')
    });
//    if ($('#cont').hasClass('hide')){$(this).css('visibility', 'hidden')}

//    $('#thediv1').on('mouseover', function () {
//        $('#map_canvas').css('visibility', 'visible')
//    });
//    $('#thediv1').on('mouseout', function () {
//        $('#map_canvas').css('visibility', 'hidden')
//    });
//    $('#map_canvas').on('mouseover', function () {
//        $('#map_canvas').css('visibility', 'visible')
//    });
//    $('#map_canvas').on('mouseout', function () {
//        $('#map_canvas').css('visibility', 'hidden')
//    });
//    $("#popover").popover({ trigger: "hover" });

//    // Calculates the space between each label
//margin = ($('#thermometer').width() + (parseFloat($('#labels').css('font-size')) / 2));
//margin -= parseFloat($('#labels').css('font-size'));
//    // Calculates the position of the thermometer
//$('#thermometer').width(0.9 * $(this).height());
//$('#thermometer').css('bottom', (($('#thermometer').height() - $('#thermometer').height()) / 2) + 'px');
//$('#thermometer').css('left', ($(this).width() - $('#wrapper').width()) / -2);
    $.ajax({
        url: 'http://api.wunderground.com/api/bf018b5365de19f5/forecast10day/q/GA/College_Park.json',
        type: 'GET',
        dataType: 'jsonp',
        success: function(response) {
            $('#popoverData1').popover({ placement : 'left'});
$('#popoverData2').popover({ placement : 'top', title : response.forecast.simpleforecast.forecastday[1].date.weekday});
$('#popoverData3').popover({ placement : 'top', title : response.forecast.simpleforecast.forecastday[2].date.weekday});
$('#popoverData4').popover({ placement : 'top', title : response.forecast.simpleforecast.forecastday[3].date.weekday});
$('#popoverData5').popover({ placement : 'top', title : response.forecast.simpleforecast.forecastday[4].date.weekday});
$('#popoverData6').popover({ placement : 'top', title : response.forecast.simpleforecast.forecastday[5].date.weekday});
$('#popoverData7').popover({ placement : 'top', title : response.forecast.simpleforecast.forecastday[6].date.weekday});
$('#popoverOption').popover({ trigger: "hover" });
            var i = 0;
            console.log(response.forecast.simpleforecast.forecastday);
//            if (response.forecast.simpleforecast.forecastday[0].conditions == 'Clear' || response.forecast.simpleforecast.forecastday[0].conditions == 'Very Hot')
//            {
////                    html{
////	background: url({% static 'background_images/sunny_day.jpeg' %}) no-repeat center center fixed;
////    -webkit-background-size: cover;
////    -moz-background-size: cover;
////    -o-background-size: cover;
////    background-size: cover;
//                var theurl = 'url({% static "background_images/sunny_day.jpeg" %})';
//                $('html').css('background', 'url({% static "background_images/sunny_day.jpeg" %}) no-repeat center center fixed' );
//                $('html').css('-webkit-background-size', 'cover' );
//                $('html').css('-o-background-size', 'cover' );
//                $('html').css('background-size', 'cover' );

//            }
                var good;
                var d = new Date();
                var n = d.getHours();
            console.log(n);
                if (response.forecast.simpleforecast.forecastday[0].conditions == 'Rain'  && 6 > n > 18) {
                    good = $('html').data('rainynight');
                    $('#finder').css('background', $('#finder').data('rain'));
                    $('span').css('color', 'lightskyblue')

                }
                else if (response.forecast.simpleforecast.forecastday[0].conditions == 'Overcast' ) {
                    good = $('html').data('overcast');
                    $('#finder').css('background', $('#finder').data('over'));
                     $('span').css('color', 'darkgrey')
                }
                else if (response.forecast.simpleforecast.forecastday[0].conditions == 'Partly Cloudy' || response.forecast.simpleforecast.forecastday[0].conditions == 'Mostly Cloudy' ) {
                    good = $('html').data('partlycloudy');
                                        $('#finder').css('background', $('#finder').data('rain'));
                    $('span').css('color', 'lightskyblue')

                }
                else if (response.forecast.simpleforecast.forecastday[0].conditions == 'Clear' && 6 < n < 18) {
                    good = $('html').data('sunnyday');
                    $('#finder').css('background', $('#finder').data('sun'));
                    $('span').css('color', 'red')

                }
                else if (response.forecast.simpleforecast.forecastday[0].conditions == 'Rain' && 6 < n < 18) {
                    good = $('html').data('rainyday');
                    $('#finder').css('background', $('#finder').data('rain'))
                    $('span').css('color', 'lightskyblue')
                }
                else if (response.forecast.simpleforecast.forecastday[0].conditions == 'Thunderstorm' || response.forecast.simpleforecast.forecastday[0].conditions == 'Chance of a Thunderstorm'  && 6 < n < 18) {
                    good = $('html').data('stormyday');
                                        $('#finder').css('background', $('#finder').data('storm'))
                    $('span').css('color', 'lightblue')

                }

                else if (response.forecast.simpleforecast.forecastday[0].conditions == 'Clear' && 6 > n > 18) {
                    good = $('html').data('normalnight');
                }


                $('html').css('background', good);
                $('html').css('background-size', 'cover');
            var condition;
            var image;
            while (i < response.forecast.simpleforecast.forecastday.length ) {
                if (response.forecast.simpleforecast.forecastday[i].conditions == 'Clear'){$('#thesun'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Rain'){$('#therain'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Thunderstorm'){$('#therain'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Partly Cloudy'){$('#thesun'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Overcast'){$('#thesun'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Mostly Cloudy'){$('#thesun'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Snow'){$('#thesnow'+ i).show()}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Ice Pellets'){$('#thep'+ i).append('Stay indoors')}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Chace of Ice Pellets'){$('#thep'+ i).append('Stay indoors')}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Blizzard'){$('#thep'+ i).append('Stay indoors')}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Very Cold'){$('#thep'+ i).append('You should probably put on a jacket')}
                else if (response.forecast.simpleforecast.forecastday[i].conditions == 'Very Hot'){$('#thep'+ i).append('Head to the beach')}
                else {$('#thep'+ i).append('Chill with friends');
                     $('#thep'+ i).css('color', 'lightblue');
                     $('#thep'+ i).css('font-family', 'Verdana');
                     $('#thep'+ i).css('font-size', '16px')}


                if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/tstorms.gif' || response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/chancetstorms.gif') {

                  image = '../static/background_images/thunder.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/mostlycloudy.gif') {
                    image = '../static/background_images/mostlycloudy.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/rain.gif') {
                    image = '../static/background_images/rain.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/partlycloudy.gif') {
                    image = '../static/background_images/partycloudy.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/clear.gif') {
                    image = '../static/background_images/sun.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/snow.gif') {
                    image = '../static/background_images/snow.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/icepellets.gif') {
                    image = '../static/background_images/hail.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/chanceicepellets.gif') {
                    image = '../static/background_images/hail.png'
                }
                else if (response.forecast.simpleforecast.forecastday[i].icon_url == 'http://icons.wxug.com/i/c/k/cloudy.gif') {
                    image = '../static/background_images/overcast1.png'
                }
                else {
                    image = response.forecast.simpleforecast.forecastday[i].icon_url;}
                condition = response.forecast.simpleforecast.forecastday[i].conditions;
                var weekday = response.forecast.simpleforecast.forecastday[i].date.weekday;
                var day = response.forecast.simpleforecast.forecastday[i].date.day;
                var month = response.forecast.simpleforecast.forecastday[i].date.monthname;

                $('#thediv'+i).prepend("<p style='font-size: 20px'>"+weekday+
                    "</p><p>"+""+ month +"</p><p>"+
                    day+"</p>" +
                    "<img class='img"+i+"' src='"+image+"'><p>"+condition+"</p>");

                $('html').fadeIn('slow');
                $('#thediv0').fadeIn('slow');
                $('.divies').css('display', 'none');

                    $('.divies').fadeIn(1000);
//                $('.divies').css('display', 'inline-block');
                i++
            }
        }

    });
//});

$.ajax({
        url: 'http://api.wunderground.com/api/bf018b5365de19f5/conditions/q/CA/San_Francisco.json',
        type: 'GET',
        dataType: 'jsonp',
        success: function(response) {
            var i = 0;
            console.log(response);
//            while (i < response.forecast.simpleforecast.forecastday.length ) {
//                $('#thediv'+i).append("<p>Its going to be "+response.forecast.simpleforecast.forecastday[i].conditions+" on "+response.forecast.simpleforecast.forecastday[i].date.weekday+", the "+response.forecast.simpleforecast.forecastday[i].date.day+"</p><img src='"+response.forecast.simpleforecast.forecastday[i].icon_url+"'>");
//                $('#thediv'+i).fadeIn('slow');
//                i++
//            }
        }
    });
});