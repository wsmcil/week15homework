function init() {
    var data = [{
        values: [19, 26, 55, 88],
        labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
        type: "pie"
    }];

    var layout = {
      height: 500,
      width: 500
    };

    addSelector();

    Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
    var PIE = document.getElementById("pie");
    Plotly.restyle(PIE, "values", [newdata]);
}

function getData(dataset) {
    var data = [];
    switch (dataset) {
        case "dataset1":
            data = [1, 2, 3, 38];
        break;
        case "dataset2":
            data = [10, 20, 30, 37];
        break;
        case "dataset3":
            data = [100, 200, 300, 23];
        break;
        default:
            data = [30, 30, 30, 11];
    }
    updatePlotly(data);
}

function addSelector(){
    $.ajax({
        url:("names/"),
        dataType:'text',
        type: 'get',
        success:function(response){
            var list = response;
            var mylist = list;
 //             ** If yout API returns something, you're going to proccess the data here.
        }
    });
    var elem = document.getElementById('selDataset');
    elem.options.add( new Option("Ukraine","dataset4") );
    
}

init();