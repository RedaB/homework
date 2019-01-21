// jshint esversion: 6


//Building the MeatData
function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Using `d3.json` to fetch the metadata for a sample
    d3.json(`/metadata/${sample}`).then(metaData => {
      
      // Using d3 to select the panel with id of `#sample-metadata`
      let PANEL = d3.select('sample-metadata');
      
      // Using `.html("")` to clear any existing metadata
      PANEL.html("");
      
       // Using `Object.entries` to add each key and value pair to the panel
      Object.entries(metaData).forEach(([key, value]) => {
        
        // Using d3 to append new ags for each key-value in the metadata
        PANEL.append('h6').text(`${key}: ${value}`);
      });

      // Building the Gauge Chart
      buildGauge(data.WFREQ);
    });
  
}


//Building Buble Chart
// function buildCharts(sample) {

//   // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(`/samples/${sample}`).then(sampleData => {
    let sampleValues = sampleData.sample_values;
    let otuIds = sampleData.otu_ids;
    let otuLabels = sampleData.otu_labels;

  });

    // @TODO: Build a Bubble Chart using the sample data
    let trace1 = {
      x: otuIds,
      y: sampleValues,
      mode: 'markers',
      marker: {
        color: otuIds,
        size: sampleValues,
        colorscale: 'Earth'
      }
    };


    let data = [trace1];
    
    let layout = {
      title: 'OTU IDs vs Sample Values',
    };

    Plotly.newPlot('bubble', data, layout);

  }

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
// 
    //  let allLabels = otu_ids;

    // let allValues = sample_values;

    // let data = [{
    //   values: sample_values,
    //   labels: otu_ids,
    //   type: 'pie',
    //   name: 'Top 10 Samples',
    //   marker: {
    //     colors: ultimateColors
    //   },
    //   domain: {
    //     row: 0,
    //     column: 0
    //   },
    //   hoverinfo: 'label+percent+name',
    //   textinfo: 'none'
    // }];

    // let layout = {
    //   height: 400,
    //   width: 500,
    //   grid: {rows: 2, columns: 2}
    // };

    // Plotly.newPlot('myDiv', data, layout);

//

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
