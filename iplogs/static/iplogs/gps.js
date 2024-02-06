function getLocation() {
    return new Promise((resolve, reject) => {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                console.log("Latitude is :", lat);
                console.log("Longitude is :", lon);

                // Send 'lat' and 'lon' to your server
                fetch('/store_location/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')  // Assuming you have a function to get the CSRF token
                    },
                    body: JSON.stringify({latitude: lat, longitude: lon})
                }).then((response) => {
                    if (response.ok) {
                        resolve();
                    } else {
                        // If the request failed, retry after 1 second
                        setTimeout(() => getLocation().then(resolve).catch(reject), 1000);
                    }
                }).catch((error) => {
                    // If there was an error, retry after 1 second
                    setTimeout(() => getLocation().then(resolve).catch(reject), 1000);
                });
            });
        } else {
            reject('Geolocation not available');
        }
    });
}

async function main() {
    try {
        await getLocation();
        // The location has been fetched and stored, you can proceed with the rest of your code here
    } catch (error) {
        console.error(error);
    }
}

main();

function getCookie(name) {
    var cookieArr = document.cookie.split(";");
    
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        
        if(name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    return null;
}