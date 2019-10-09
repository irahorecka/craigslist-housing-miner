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

    function search() {

        const city = city.querySelector('#city-picker').value;
    }

    render();
});
