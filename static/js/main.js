function displayChart(d1, d2, chartType, chartTitle, y) {
  var dataPoints = [];
  var chart = new CanvasJS.Chart('chartContainer', {
    animationEnabled: true,
    theme: 'light2',
    title: {
      text: chartTitle
    },
    axisY: {
      title: y,
      titleFontSize: 24
    },
    data: [{
      type: chartType,
      yValueFormatString: '#,### Units',
      dataPoints: dataPoints
    }]
  });

  for (var i = 0; i < d1.length; i++) {
    dataPoints.push({
      x: d1[i],
      y: d2[i]
    });
  }
  chart.render();
}

$(function() {
  if (window.location.pathname === '/admin') {
    $('.admin').show();
    $('.user').hide();
    $('.home').hide();
  }
  else if (window.location.pathname === '/user') {
    $('.admin').hide();
    $('.user').show();
    $('.home').hide();
  }
  else {
    $('.home').show();
    $('.admin').hide();
    $('.user').hide();
  }

  $('select').change(function() {
    var result = $('.insights-result');
    var value = $('.insights-class option:selected').val();
    if (value === '1') {
      var d1 = [1120112, 1120224, 1120560, 1120336, 1120672, 1120784, 1120448];
      var d2 = [4877866, 2647335, 854047, 732380, 300091, 250875, 16385];
      displayChart(d1,d2, 'column', 'City having highest transactions', 'Transactions');
    }
    if (value === '2') {
      $('#chartContainer').html('<img class="size" src="/static/img/category.png">')
    }
    if (value === '3') {
      $('#chartContainer').html('<img class="size" src="/static/img/city3.png">')
    }
    if (value === '4') {
      $('#chartContainer').html('<img class="size" src="/static/img/heatmap.png">')
    }
    if (value === '5') {
      $('#chartContainer').html('<img class="size" src="/static/img/hour_trans1.png">')
    }
    if (value === '6') {
      $('#chartContainer').html('<img class="size" src="/static/img/month.png">')
    }
    if (value === '7') {
      $('#chartContainer').html('<img class="size" src="/static/img/month_trend.png">')
    }
    if (value === '8') {
      $('#chartContainer').html('<img class="size" src="/static/img/month_trend_sub.png">')
    }
    if (value === '9') {
      $('#chartContainer').html('<img class="size" src="/static/img/product.png">')
    }
  }).change();
});