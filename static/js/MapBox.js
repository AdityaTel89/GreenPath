
mapboxgl.accessToken = 'pk.eyJ1IjoiYWRpdHlhdGVsc2luZ2UtODkiLCJhIjoiY2xyM2swZmRkMGgzMjJpcjFwMWRqdmVidCJ9.TlLSvaapHIwb6vrUrsXLYg';


const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v10',
    center: [78.9629, 20.5937],
    zoom: 3
});


map.addControl(new mapboxgl.NavigationControl());


const geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl,
    placeholder: 'Search for places',
    marker: {
        color: 'red'
    }
});


map.addControl(geocoder);


geocoder.on('result', function (event) {

    const coordinates = event.result.geometry.coordinates;


    new mapboxgl.Marker()
        .setLngLat(coordinates)
        .setPopup(
            new mapboxgl.Popup({ offset: 25 })
                .setHTML(`<h3>${event.result.text}</h3><p>${event.result.place_name}</p>`) // Set popup content
        )
        .addTo(map);


    map.flyTo({
        center: coordinates,
        zoom: 12
    });
});

async function plotLocation() {

    const location = document.getElementById('location').value;

    if (!location) {
        alert('Please enter a valid location.');
        return;
    }


    const response = await fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(location)}.json?access_token=${mapboxgl.accessToken}`);
    const data = await response.json();

    if (data.features.length === 0) {
        alert('No results found for the specified location.');
        return;
    }


    const coordinates = data.features[0].geometry.coordinates;


    new mapboxgl.Marker()
        .setLngLat(coordinates)
        .setPopup(
            new mapboxgl.Popup({ offset: 25 })
                .setHTML(`<h3>${data.features[0].text}</h3><p>${data.features[0].place_name}</p>`) // Set popup content
        )
        .addTo(map);
    map.flyTo({
        center: coordinates,
        zoom: 12
    });
}