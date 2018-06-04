   // 交通信息
  var carBar = echarts.init(document.getElementById("c-car-bar"));
  function updateCarBar(val) {
    var min = 500, max = 2000;
    if (val === '全部车辆') {
      min = 6000;
      max = 12000;
    }
    carBar.setOption(mockSingleChartOption(undefined, min, max));
  }
  updateCarBar();
  charts.push({ name: '车辆', chart: carBar });
  template = Handlebars.compile($('#selectOptions').html());
  $("#carSelect").html(template({ data: mockNos('Car').concat({ id: '全部车辆' }).reverse() }));
  $("#carSelect option:first").attr("selected", "selected");
  $('#selector-car').selectFilter({
    callBack: function (val) {
      updateCarBar(val)
    }
  });
  updateSelectChart("#carSelect", "#selector-car", updateCarBar, 3000);
  
  // 响应式图表调整
  window.onresize = function () {
    charts.forEach(function (c) {
      if (c && c.chart) {
        c.chart.resize();
      }
    })
  }