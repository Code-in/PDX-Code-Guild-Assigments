

let app = new Vue({
    el: '#app',
    data: {
        latitute: '',
        longitude: '',
        weather: null,
        day: null,
        loading: true,
        weather_icon: null,
    },
    methods: {
        loadWeatherData: function () {
            axios({
                method: 'get',
                url: 'https://api.openweathermap.org/data/2.5/onecall',
                params: {
                    lat: this.latitude,
                    lon: this.longitude,
                    exclude: "minute,hourly",
                    appid: api_key,
                    units: "imperial",
                },
            }).then(response => {
                console.log(response.data)
                this.weather = response.data.current
                console.table(response.data)
                this.updateWeatherData()
            })
        },
        convertDateTime: function (dt) {
            let unix_timestamp = dt
            let datetime = new Date(unix_timestamp*1000)
            console.log(datetime) 
            return datetime
        },
        convertToTime: function (dt) {
            let unix_timestamp = dt
            let datetime = new Date(unix_timestamp*1000)
            var localeSpecificTime = datetime.toLocaleTimeString();
            return localeSpecificTime.replace(/:\d+ /, ' ');
        },
        convertInches: function (rain) {
            if(rain > 0) {
                rain = rain.toFixed(2)
                rain = "" + rain + " in"
            } else {
                rain = "0.0 in"
            }
            return rain
        },
        getLocation: function () {
            if (navigator.geolocation) {
                console.log("getCurrentPosition")
                navigator.geolocation.getCurrentPosition(this.getMyPosition, console.log)
                console.log("getCurrentPosition 2")
                
            } else {
                console.log("Geolocation is not supported by this browser.")
            }
        },

        getMyPosition: function (position) {
            console.log("ShowPosition")
            this.latitude = position.coords.latitude.toFixed(6)
            this.longitude = position.coords.longitude.toFixed(6)
            console.log("Lat: " + this.latitude + "  Long: " + this.longitude)
            this.loadWeatherData()
        },

        updateWeatherData: function() {
            this.day = this.weather
            this.day.dt = this.convertDateTime(this.day.dt)
            console.log(this.day.dt )
            this.day.sunrise = this.convertToTime(this.day.sunrise)
            console.log(this.day.sunrise)
            this.day.sunset = this.convertToTime(this.day.sunset)
            console.log(this.day.sunset )
            this.day.rain = this.convertInches(this.day.rain)
            console.log(this.day.weather[0].icon)
            this.weather_icon = "http://openweathermap.org/img/wn/" + this.day.weather[0].icon + "@4x.png"
        }

    },
    created: function () {
        this.getLocation()
    },

    watch: {
        day: function() {
            console.log("Got the data!!!!!")
            this.loading = false
        }
    },

})




