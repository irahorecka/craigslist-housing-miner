document.addEventListener('DOMContentLoaded', () => {

    // state
    let draw = false; // for keeping track of mouse down

    // elements
    let points = [];
    let lines = [];
    let svg = null;

    function render() {

        document.querySelector('#_submit').onclick = () => {
            for (let i = 0; i < points.length; i++)
                points[i].remove();
            for (let i = 0; i < lines.length; i++)
                lines[i].remove();
            points = [];
            lines = [];
        }

    }

    function search {

        const color = city.querySelector('#city-picker').value;
        const thickness = document.querySelector('#thickness-picker').value;

        if (connect) { // if we should connect the line to the prior point
            const last_point = points[points.length - 1];
            const line = svg.append('line')
                            .attr('x1', last_point.attr('cx'))
                            .attr('y1', last_point.attr('cy')) // start line at last point
                            .attr('x2', x)
                            .attr('y2', y) // end our new point 
                            .attr('stroke-width', thickness * 2)
                            .style('stroke', color);
            lines.push(line); // add that line to the array of lines
        }

        const point = svg.append('circle')
                         .attr('cx', x)
                         .attr('cy', y)
                         .attr('r', thickness)
                         .style('fill', color);
        points.push(point); // define point styling
    }

    render();
});
