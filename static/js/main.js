window.onload = function() {
  var dataPoints = [];

  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    theme: "light2",
    title: {
      text: "Daily Sales Data"
    },
    axisY: {
      title: "Units",
      titleFontSize: 24
    },
    data: [{
      type: "column",
      yValueFormatString: "#,### Units",
      dataPoints: dataPoints
    }]
  });

  function addData(data) {
    alert('hello');
    for (var i = 0; i < data.x.length; i++) {
      dataPoints.push({
        x: data.x[i],
        y: data.y[i]
      });
      alert(dataPoints);
    }
    chart.render();
  }

  $.getJSON("data.json", addData);
};

$(function() {
  $('select').change(function() {
    var result = $('.insights-result');
    var value = $(".insights-class option:selected").val();
    result.text(value);
  });
});