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
      $('#chartContainer').html('<img class="size" src="/static/img/category.png">')
    }
    if (value === '2') {
      $('#chartContainer').html('<img class="size" src="/static/img/city3.png">')
    }
    if (value === '3') {
      $('#chartContainer').html('<img class="size" src="/static/img/heatmap.png">')
    }
    if (value === '4') {
      $('#chartContainer').html('<img class="size" src="/static/img/hour_trans1.png">')
    }
    if (value === '5') {
      $('#chartContainer').html('<img class="size" src="/static/img/month.png">')
    }
    if (value === '6') {
      $('#chartContainer').html('<img class="size" src="/static/img/month_trend.png">')
    }
    if (value === '7') {
      $('#chartContainer').html('<img class="size" src="/static/img/month_trend_sub.png">')
    }
    if (value === '8') {
      $('#chartContainer').html('<img class="size" src="/static/img/product.png">')
    }
  }).change();
});