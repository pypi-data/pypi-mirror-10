/*global jQuery */

(function(window, $) {
  'use strict';

  $(function() {
    var barChartNonTimeSeries = function(data, metricTitle, graphElement, graphColours) {
      var chart = nv.models.multiBarChart();

      var margin = {top: 10, right: 80, bottom: 150, left: 60},
          height = ($(window).height() - 500) > 500 ? ($(window).height() - 500) : 500,
          width = parseInt($(graphElement).css('width').replace('px', ''));

      if (navigator.userAgent.indexOf('PhantomJS') !== -1) {
        width *= $(graphElement).parent().parent().hasClass('col-sm-12') ? 1.5 : 0.7;
      }

      chart.margin(margin)
           .height(height)
           .width(width);

      chart.x(function(d) {
          return d.title;
        });

      chart.y(function(d) {
          return d.value;
        });

      chart.yAxis.tickFormat(d3.format(','));

      chart.tooltips(true)
           .stacked(true)
           .duration(350);

      if (graphColours) {
        chart.color(graphColours);
      }

      var dataMap = {};
      var newData = [];
      var el = null;

      for (var i = 0; i < data.filtered.length; i++) {
        el = data.filtered[i];

        if (typeof el.dimension === 'undefined' || !el.dimension) {
          el.dimension = metricTitle;
        }

        if (!(el.dimension in dataMap)) {
          dataMap[el.dimension] = [];
        }

        dataMap[el.dimension].push({
          'title': el.title,
          'value': el.value
        });
      }

      $.each(dataMap, function(k, v) {
        newData.push({'key': k, 'values': v});
      });

      var svg = d3.select(graphElement).append("svg");

      svg.datum(newData)
          .transition()
          .duration(500)
          .call(chart)
          .style({'height': height + 'px', 'width': width + 'px'});

      // Line up x-axis labels to be centred on each bar / line in the chart.
      // Thanks to:
      // http://stackoverflow.com/a/13472375/2066849
      var xTicks = svg.select('.nv-x.nv-axis > g').selectAll('g');
      xTicks
          .selectAll('text')
          .attr('transform', function(d,i,j) {return 'translate (-12, 70)  rotate(-90 0,0)';});

      nv.utils.windowResize(chart.update);

      return chart;
    }

    var draw = function(data, graphWrapperElement, metricTitle, displayMode) {
      $(graphWrapperElement).append('<section class="graph"></section>');

      var graphElement = graphWrapperElement + ' > .graph';
      var graphColours = null;

      data['isPrint'] = navigator.userAgent.indexOf('PhantomJS') !== -1;

      switch (displayMode) {
        case 'bar-chart-non-time-series':
          nv.addGraph(function() {
            barChartNonTimeSeries(data, metricTitle, graphElement, graphColours);
          });
          return;
      }
    };

    if (typeof graphData !== 'undefined' && graphData.length) {
      $.each(graphData, function(i, gd) {
        draw(gd.data,
             gd.graphWrapperElement,
             gd.metricTitle,
             gd.displayMode);
      });
    }
  });
})(window, jQuery);
