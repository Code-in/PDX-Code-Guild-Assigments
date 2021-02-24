let app = new Vue({
    el: '#app',
    data: {
        startstop: 'Start',
        timerType: null,
        displayTime: '',
        timerInterval: null,
        minute: 0,
        second: 0,
        millisecond: 0,
    },
    methods: {
        currentTime: function(state) {
            this.toggleMethod(this.currentTime, state, this.setCurrentTimeMethod)
            console.log("Current Time: " + this.startstop)
        },
        stopWatch: function(state) {
            this.toggleMethod(this.stopWatch, state, this.setStopWatchMethod)
            console.log("Stop Watch: " + this.startstop)
        },
        countDownTimer: function(state) {
            this.toggleMethod(this.countDownTimer, state, null)
            console.log("Count Down Timer: " + this.startstop)
        },


        toggleMethod: function(selectedTimerType, state, timermethod) {
            if (this.timerType === null) {
                this.timerType = selectedTimerType
                timermethod()
                this.startstop = 'Stop'
            } else {
                if (selectedTimerType === this.timerType) {
                    this.toggle(state)
                }
            }
        },
        toggleTimer: function(state) {
            this.timerType = null
            this.startstop = 'Start'
            console.log("Toggle Timer")
            clearInterval(this.timerInterval);
        },
        toggle: function(state) {
            if (state === 'Start') {
                this.startstop = 'Stop'
            } else {
                this.startstop = 'Start'
                console.log("Getting called!!!")
                clearInterval(this.timerInterval);
            }
        },
        setCurrentTimeMethod: function() {
            this.timerInterval = setInterval(function() {
                console.log("Setting setCurrentTimeMethod")
                let date = new Date();
                let hours = date.getHours();
                let minutes = "0" + date.getMinutes();
                let seconds = "0" + date.getSeconds();
                console.log("Time:" + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2))
                console.log("Timer Type: " + this.timerType)
                console.log("Interval: " + this.timerInterval)
                app.displayTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2)
            }, 1000);
        },
        setStopWatchMethod: function() {
            this.timerInterval = setInterval(function() {
                app.millisecond++;
                if (app.millisecond == 100) {
                    app.millisecond = 0
                    app.second++
                    if (app.second == 60) {
                        app.second = 0
                        app.minute++
                        if(app.minute == 60) {
                            app.minute = 0
                            app.hour++
                        }
                    }
                }
                app.displayTime = app.minute.toString().padStart(2, '0') + ':' + app.second.toString().padStart(2, '0') + ':' + app.millisecond.toString().padStart(2, '0')
            }, 10);
        },
    }
})